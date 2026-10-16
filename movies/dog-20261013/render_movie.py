"""Journaled native 1080p Seedance rendering; no secrets, base64 or signed URLs saved."""
import argparse
import base64
import hashlib
import json
import mimetypes
import os
import re
import subprocess
import sys
import time
import uuid
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

from seedance_transport import Client, ApiFailure
ROOT=Path(__file__).resolve().parent
SKILL=Path('C:/Users/Admin 3/.codex/skills/movi2/scripts')
sys.path.insert(0,str(SKILL))
import project as helper
sys.path.insert(0,str(ROOT/'tools/python-deps'))
import imageio_ffmpeg
FF=Path(imageio_ffmpeg.get_ffmpeg_exe())
JOURNAL=ROOT/'exports/task-journal.json'

def now():return datetime.now(timezone.utc).isoformat()
def read(f):return json.loads(f.read_text(encoding='utf-8-sig'))
def save(f,v):
    f.parent.mkdir(parents=True,exist_ok=True)
    tmp=f.with_suffix(f.suffix+'.'+uuid.uuid4().hex+'.partial')
    tmp.write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf-8')
    os.replace(tmp,f)
def journal():return read(JOURNAL) if JOURNAL.exists() else {'project_id':read(ROOT/'project.json')['id'],'takes':{}}
def preflight(cid):
    result=subprocess.run([sys.executable,'-X','utf8',str(SKILL/'project.py'),'render-ready',str(ROOT),'--chapter',cid],capture_output=True,text=True,encoding='utf-8')
    if result.returncode:raise RuntimeError('render-ready rejected '+cid+': '+result.stdout)
def record(t):
    ledger=read(ROOT/'usage.json')
    session=next(s['id'] for s in ledger['sessions'] if not s.get('ended_at'))
    cost={'kind':'unknown','basis':'Awaiting provider generation outcome and usage/billing evidence'}
    tokens=t.get('provider_usage',{}).get('completion_tokens')
    if t['status']=='succeeded' and isinstance(tokens,(int,float)):
        cost={'kind':'estimated','currency':'USD','amount':str(Decimal(str(tokens))*Decimal('11.7')/Decimal('1000000')),
            'basis':'Measured provider usage.completion_tokens x published Seedance 2.5 1080p image-only list rate USD 11.7/M tokens; BytePlus https://docs.byteplus.com/id/docs/modelark/model-pricing?redirect=1 checked 2026-10-13. Actual account discounts/tax/payment not verified.'}
    record={'attempt_id':t['attempt_id'],'chapter_id':t['chapter_id'],'take_id':t['id'],
        'state':t.get('submission_state') if t.get('submission_state') in ('submitting','uncertain','rejected') else t['status'],
        'model':'dreamina-seedance-2-5-260628','resolution':'1080p','duration_seconds':t['duration'],
        'reference_video_seconds':0,'usage':t.get('provider_usage',{}),'cost':cost}
    if t.get('task_id'):record['task_id']=t['task_id']
    target=ROOT/'exports/usage-records'/f"{t['attempt_id']}.json";save(target,record)
    result=subprocess.run([sys.executable,'-X','utf8',str(SKILL/'usage.py'),'record',str(ROOT),'--session',session,'--from',str(target)],capture_output=True,text=True,encoding='utf-8')
    if result.returncode:raise RuntimeError('Usage ledger write failed: '+result.stdout+' '+result.stderr)

def payload(p,c,endpoint):
    bindings=[];images=[]
    library_path=ROOT/'exports/provider-asset-bindings.json'
    library=read(library_path) if library_path.exists() else {}
    for a in helper.active_assets(p,c):
        selected=helper.selected_media(a);f=ROOT/selected['path'];raw=f.read_bytes()
        if len(raw)>=30*1024*1024:raise ValueError('Oversize reference '+a['id'])
        token='@Image'+str(len(bindings)+1)
        bindings.append({'tag':a['tag'],'provider_tag':token,'asset_id':a['id'],'candidate_id':selected['id'],
            'path':selected['path'],'role':'reference_image','sha256':hashlib.sha256(raw).hexdigest()})
        mime=mimetypes.guess_type(f.name)[0] or 'image/png'
        private=library.get(a['id'])
        if private:
            if (private.get('status')!='Active' or not private.get('verified_at') or
                    private.get('source_sha256')!=bindings[-1]['sha256'] or
                    not re.fullmatch(r'asset-[A-Za-z0-9-]+',private.get('provider_asset_id',''))):
                raise RuntimeError('Private asset must be verified Active and match unchanged source: '+a['id'])
            uri='asset://'+private['provider_asset_id']
            bindings[-1].update(provider_input='private_asset_library',provider_asset_id=private['provider_asset_id'])
        else:
            uri='data:'+mime+';base64,'+base64.b64encode(raw).decode()
        images.append({'type':'image_url','image_url':{'url':uri},'role':'reference_image'})
    mapping={b['tag'].casefold():b['provider_tag'] for b in bindings}
    pattern=re.compile(r'@[^\W\s][\w-]*',re.UNICODE)
    text=pattern.sub(lambda m:mapping[m[0].casefold()],c['prompt'])
    for ref in c.get('continuity_references',[]):
        if ref.get('media_type')!='Image' or ref.get('role')!='reference_image':
            raise RuntimeError('This renderer supports one omni image continuity input only')
        raw=(ROOT/ref['path']).read_bytes();mime=mimetypes.guess_type(ref['path'])[0] or 'image/jpeg'
        token='@Image'+str(len(images)+1)
        images.append({'type':'image_url','image_url':{'url':'data:'+mime+';base64,'+base64.b64encode(raw).decode()},'role':'reference_image'})
        bindings.append({'continuity_reference_id':ref['id'],'provider_tag':token,'path':ref['path'],
            'role':'reference_image','sha256':hashlib.sha256(raw).hexdigest(),
            'source_chapter_id':ref['source_chapter_id'],'source_take_id':ref['source_take_id'],'source_sha256':ref['source_sha256']})
        text+='\nINSPECTED CONTINUITY FRAME\n'+token+'：'+ref['reason']+' 只參照此理由明確指定的視覺特徵；不是新增人物或整段重播。新動作、時序及对白完全按本章TIMELINE，不承接前章音訊。'
    assert 1<=len(images)<=30
    body={'model':endpoint,'content':[{'type':'text','text':text}]+images,
        'duration':c['duration'],'ratio':'16:9','resolution':'1080p','generate_audio':True,
        'watermark':False,'return_last_frame':True,'output_format':'mp4',
        'omni_reference_task_type':'reference','seed':2026101300+c['chapter_index']}
    size=len(json.dumps(body,ensure_ascii=False,separators=(',',':')).encode('utf-8'))
    if size>64*1024*1024:raise ValueError('Payload exceeds 64MB')
    return body,bindings,text,size

def download(url,target):
    target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():return
    temp=target.with_suffix(target.suffix+'.partial')
    try:
        with urlopen(url,timeout=180) as src,temp.open('wb') as dest:
            while True:
                chunk=src.read(1024*1024)
                if not chunk:break
                dest.write(chunk)
        os.replace(temp,target)
    except Exception:
        raise RuntimeError('Provider media download interrupted; poll same accepted task again') from None

def probe(file):
    result=subprocess.run([str(FF),'-hide_banner','-i',str(file)],capture_output=True,text=True,encoding='utf-8',errors='replace')
    text=result.stderr
    match=re.search(r'Duration: (\d+):(\d+):(\d+\.\d+)',text)
    video=re.search(r'Video: ([^,]+),.*?(\d{2,5})x(\d{2,5})[^\n]*?(\d+(?:\.\d+)?) fps',text)
    audio=re.search(r'Audio: ([^,]+), (\d+) Hz, ([^,\n]+)',text)
    if not match or not video:raise RuntimeError('Cannot probe local video '+file.name)
    return {'duration':sum(float(x)*factor for x,factor in zip(match.groups(),(3600,60,1))),
        'video_codec':video[1],'width':int(video[2]),'height':int(video[3]),'fps':float(video[4]),
        'audio':{'codec':audio[1],'sample_rate':int(audio[2]),'channels':audio[3]} if audio else None}

def inspect_technical(file,t):
    info=probe(file)
    if (info['width'],info['height'])!=(1920,1080):raise RuntimeError('Native resolution mismatch; no batch expansion')
    if not info['audio']:raise RuntimeError('Generated take missing requested audio')
    if info['duration']<t['duration']-0.25:raise RuntimeError('Generated take materially shorter than planned')
    result=subprocess.run([str(FF),'-v','error','-threads','2','-i',str(file),'-f','null','-'],capture_output=True,text=True,encoding='utf-8',errors='replace')
    if result.returncode or result.stderr.strip():raise RuntimeError('Decode errors in '+file.name)
    info.update(decode_verified=True,native_1080p=True)
    return info

def submit(client,p,c,j,new_take=False,retry_failed=False):
    # Preflight and payload must use exactly the same latest committed state.
    p=read(ROOT/'project.json')
    c=next(current for current in p['chapters'] if current['id']==c['id'])
    old=j['takes'].get(c['id'])
    prior=[];take_number=1
    if old:
        if old.get('submission_state') in ('submitting','uncertain'):
            raise RuntimeError('Uncertain existing submission; reconcile before replacement')
        replace=(new_take and old['status']=='succeeded') or (retry_failed and old['status']=='failed')
        if not replace:
            print(c['id'],'already journaled; no duplicate POST',flush=True);return
        current_fp=helper.chapter_fingerprint(ROOT,p,c)
        if old.get('error',{}).get('code')=='InputImageSensitiveContentDetected.PrivacyInformation':
            mapping=read(ROOT/'exports/provider-asset-bindings.json') if (ROOT/'exports/provider-asset-bindings.json').exists() else {}
            if not mapping.get('asset_009',{}).get('provider_asset_id'):
                raise RuntimeError('Rejected Chan reference requires supported private-library asset binding before retry')
        elif current_fp==old['dependency_fingerprint']:
            raise RuntimeError('Replacement has no changed prompt or dependencies; no identical retry')
        take_number=old['take_number']+1
        prior=old.get('prior_takes',[])+[{k:v for k,v in old.items() if k!='prior_takes'}]
    preflight(c['id'])
    body,bindings,text,size=payload(p,c,client.endpoint)
    if take_number>1:body['seed']+=10000*(take_number-1)
    t={'id':f'take_{take_number:02}','chapter_id':c['id'],'take_number':take_number,'attempt_id':'attempt_'+uuid.uuid4().hex,
        'status':'pending','submission_state':'submitting','created_at':now(),'duration':c['duration'],
        'resolution':'1080p','aspect_ratio':'16:9','model':'dreamina-seedance-2-5-260628',
        'source_revision':p['revision'],'dependency_fingerprint':helper.chapter_fingerprint(ROOT,p,c),
        'prompt':c['prompt'],'submitted_prompt':text,'bindings':bindings,'request_bytes':size}
    if prior:t['prior_takes']=prior
    folder=ROOT/'chapters'/c['id']
    (folder/'submitted-prompt.txt').write_text(text,encoding='utf-8')
    save(folder/'submission-spec.json',{k:v for k,v in t.items() if k not in ('prompt','submitted_prompt')})
    j['takes'][c['id']]=t;save(JOURNAL,j);record(t)
    try:result=client.task(payload=body)
    except ApiFailure as e:
        t.update(status='failed',submission_state='rejected',error={'http_status':e.status,'code':e.code})
        save(JOURNAL,j);record(t);raise
    except Exception as e:
        t.update(submission_state='uncertain',error={'type':type(e).__name__,'reason':'No task ID received; reconcile before any retry'})
        save(JOURNAL,j);record(t);raise RuntimeError('Submission outcome uncertain; no automatic resubmit') from None
    if not result.get('id'):
        t['submission_state']='uncertain';save(JOURNAL,j);record(t);raise RuntimeError('No provider task ID; reconcile before retry')
    t.update(task_id=result['id'],submission_state='accepted',submitted_at=now())
    save(JOURNAL,j);record(t)
    print(c['id'],'accepted',c['duration'],'s, 1080p 16:9,',len(bindings),'references',flush=True)

def poll(client,j):
    changed=False
    for cid,t in j['takes'].items():
        if not t.get('task_id') or t['status'] in ('succeeded','failed'):continue
        try:result=client.task(task_id=t['task_id'])
        except (URLError,TimeoutError):
            print(cid,'status lookup interrupted; job remains accepted',flush=True);continue
        state=result.get('status');old=t.get('provider_status')
        t.update(provider_status=state,checked_at=now())
        if state=='succeeded':
            # Keep URLs in memory only; never persist expiring tokens.
            content=result.get('content',{})
            if not content.get('video_url'):raise RuntimeError('Successful task missing video')
            target=ROOT/'chapters'/cid/'takes'/(t['id']+'.mp4')
            download(content['video_url'],target)
            verification=inspect_technical(target,t)
            if content.get('last_frame_url'):
                last=target.with_name(t['id']+'_last.jpg');download(content['last_frame_url'],last)
                t['last_frame_path']=last.relative_to(ROOT).as_posix()
            t.update(status='succeeded',completed_at=now(),path=target.relative_to(ROOT).as_posix(),
                provider_usage=result.get('usage',{}),verification=verification,
                provider_metadata={k:result[k] for k in ('duration','resolution','ratio','framespersecond','seed') if k in result})
            print(cid,'downloaded and decoded native 1920x1080 with audio;',verification['duration'],'s',flush=True)
        elif state in ('failed','cancelled','expired'):
            error=result.get('error') or {}
            t.update(status='failed',error={'code':error.get('code','ProviderFailure'),'reason':'Provider task failed; see bounded diagnostic if needed'},provider_usage=result.get('usage',{}))
        else:t['status']='processing' if state=='running' else 'pending'
        save(JOURNAL,j);record(t)
        if old!=state:print(cid,state,flush=True);changed=True
    return changed

def sync(j):
    p=read(ROOT/'project.json');proposal=json.loads(json.dumps(p))
    for c in proposal['chapters']:
        if c['id'] not in j['takes']:continue
        t=j['takes'][c['id']]
        c['takes']=t.get('prior_takes',[])+[{k:v for k,v in t.items() if k!='prior_takes'}]
        edits=[]
        for meta in sorted((ROOT/'exports/local-edits').glob(c['id']+'_*.json')):
            edit=read(meta)
            if (edit.get('source_video_take_id')==t['id'] and
                edit.get('dependency_fingerprint')==helper.chapter_fingerprint(ROOT,p,c) and
                all(hashlib.sha256((ROOT/edit['source_'+media+'_path']).read_bytes()).hexdigest()==edit['source_'+media+'_sha256'] for media in ('video','audio'))):
                edits.append(edit)
        c['takes']+=edits
        if (t['status']=='succeeded' and t.get('visual_review',{}).get('inspected') and
            not t['visual_review'].get('requires_repair') and t['dependency_fingerprint']==helper.chapter_fingerprint(ROOT,p,c)):
            c['active_take_id']=t['id']
        else:c['active_take_id']=None
        if edits and edits[-1].get('visual_review',{}).get('inspected') and not edits[-1]['visual_review'].get('requires_repair'):
            c['active_take_id']=edits[-1]['id']
    proposal['render_status']='awaiting_assembly' if len(j['takes'])==55 and all(t['status']=='succeeded' for t in j['takes'].values()) else 'rendering'
    proposal['tool_availability']['jobs_submitted']=sum(bool(t.get('task_id')) for t in j['takes'].values())
    return helper.save(ROOT,p,proposal,'Synchronize journaled Seedance attempts and only inspected selections')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['prepare','submit','poll','sync','run','probe','status'])
    parser.add_argument('--chapters',default='all');parser.add_argument('--inflight',type=int,default=6)
    parser.add_argument('--new-take',action='store_true');parser.add_argument('--retry-failed',action='store_true')
    args=parser.parse_args();p=read(ROOT/'project.json');j=journal()
    if args.command=='status':
        print(json.dumps({s:sum(t['status']==s for t in j['takes'].values()) for s in ('succeeded','processing','pending','failed')},ensure_ascii=False));return
    if args.command=='sync':print(sync(j));return
    if args.command=='prepare':
        plan=[]
        for c in p['chapters']:
            _,bindings,text,size=payload(p,c,'<verified-endpoint>')
            plan.append({'chapter_id':c['id'],'duration':c['duration'],'resolution':'1080p','aspect_ratio':'16:9','bindings':bindings,'request_bytes':size})
        save(ROOT/'exports/submission-plan.json',{'status':'prepared','source_revision':p['revision'],'chapters':plan})
        print('Prepared',len(plan),'payloads. Largest bytes:',max(x['request_bytes'] for x in plan));return
    client=Client();print(client.resolve(),flush=True)
    if args.command=='probe':return
    chosen=p['chapters'] if args.chapters=='all' else [p['chapters'][int(x)-1] for x in args.chapters.split(',')]
    if args.command=='submit':
        for c in chosen:submit(client,p,c,j,args.new_take,args.retry_failed)
    elif args.command=='poll':poll(client,j);print(sync(j))
    elif args.command=='run':
        # Serial ledger and journal writes; provider jobs execute asynchronously.
        chosen_ids={c['id'] for c in chosen}
        queue=[c for c in chosen if c['id'] not in j['takes'] or
            (args.new_take and j['takes'][c['id']]['status']=='succeeded' and
             j['takes'][c['id']]['dependency_fingerprint']!=helper.chapter_fingerprint(ROOT,p,c)) or
            (args.retry_failed and j['takes'][c['id']]['status']=='failed')]
        while True:
            poll(client,j)
            queued_ids={c['id'] for c in queue}
            failed=[t for cid,t in j['takes'].items() if cid in chosen_ids and cid not in queued_ids and t['status']=='failed']
            uncertain=[t for cid,t in j['takes'].items() if cid in chosen_ids and t.get('submission_state')=='uncertain']
            if failed or uncertain:
                sync(j);raise RuntimeError('Batch paused on failed/uncertain job; no blind retry')
            active=sum(t['status'] in ('pending','processing') for t in j['takes'].values())
            while queue and active<args.inflight:
                c=queue.pop(0)
                submit(client,p,c,j,args.new_take,args.retry_failed);active+=1
            if not queue and all(c['id'] in j['takes'] and j['takes'][c['id']]['status']=='succeeded' for c in chosen):
                print(sync(j));print('Requested batch completed',flush=True);break
            time.sleep(30)
    print(json.dumps({s:sum(t['status']==s for t in j['takes'].values()) for s in ('succeeded','processing','pending','failed')}),flush=True)

if __name__=='__main__':
    try:main()
    except Exception as e:
        if isinstance(e,ApiFailure):print(str(e),file=sys.stderr)
        else:print(type(e).__name__+': '+str(e),file=sys.stderr)
        sys.exit(1)
