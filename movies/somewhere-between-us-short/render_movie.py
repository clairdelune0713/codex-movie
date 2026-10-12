"""New-movie Seedance renderer. Approved text + individual assets, no storyboard.

User authorized the four existing base settings on 2026-10-09 in this chat.
The older adapter is imported only as a read-only authentication transport.
All state, submissions and outputs belong exclusively to this new movie.
"""
import argparse, base64, copy, hashlib, hmac, importlib.util, json, mimetypes, re, subprocess, sys, urllib.parse
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parent
HELPER=Path('C:/Users/admina/.codex/skills/movi2/scripts/project.py')
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
h=module('movi2',HELPER)
api=module('transport',ROOT.parent/'tart-and-tine/exports/seedance_render.py')
JOURNAL=ROOT/'exports/seedance-journal.json'

def manage(client,action,body):
    raw=json.dumps(body,ensure_ascii=False,separators=(',',':')).encode()
    digest=hashlib.sha256(raw).hexdigest();stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');date=stamp[:8]
    query=urllib.parse.urlencode({'Action':action,'Version':'2024-01-01'},quote_via=urllib.parse.quote)
    signed='content-type;host;x-content-sha256;x-date'
    headers=f'content-type:application/json\nhost:{api.HOST}\nx-content-sha256:{digest}\nx-date:{stamp}\n'
    scope=f'{date}/ap-southeast-1/ark/request'
    canonical='\n'.join(['POST','/',query,headers,signed,digest])
    sign='\n'.join(['HMAC-SHA256',stamp,scope,hashlib.sha256(canonical.encode()).hexdigest()])
    key=client.settings['VOLC_SECRET_KEY_RAW'].encode()
    for part in (date,'ap-southeast-1','ark','request'):key=hmac.new(key,part.encode(),hashlib.sha256).digest()
    signature=hmac.new(key,sign.encode(),hashlib.sha256).hexdigest()
    authorization=f"HMAC-SHA256 Credential={client.settings['VOLC_ACCESS_KEY']}/{scope}, SignedHeaders={signed}, Signature={signature}"
    return client.request(f'https://{api.HOST}/?{query}','POST',body,{'Content-Type':'application/json','Host':api.HOST,'X-Date':stamp,'X-Content-Sha256':digest,'Authorization':authorization})

def connect(verify=False):
    values=api.read_credentials();client=api.Client(values)
    file=ROOT/'exports/endpoint-verification.json'
    if verify:
        items=[];page=1
        while True:
            result=manage(client,'ListEndpoints',{'ProjectName':values['VOLC_PROJECT_NAME'],'PageNumber':page,'PageSize':100}).get('Result',{})
            batch=result.get('Items',[]);items+=batch
            if len(items)>=result.get('TotalCount',len(items)) or not batch:break
            page+=1
        eligible=[e for e in items if str(e.get('Status','')).lower() in ('running','1') and re.search(r'seedance.*2[._ -]?5',json.dumps(e.get('ModelReference',{})),re.I)]
        selected=next((e for e in eligible if e['Id']==values['VOLC_ENDPOINT_SEEDANCE_25']),None)
        if selected is None:
            if len(eligible)!=1:raise RuntimeError('Cannot unambiguously resolve a running Seedance 2.5 endpoint in the authorized project')
            selected=eligible[0]
        record={'verified_at':api.now(),'configured_endpoint':values['VOLC_ENDPOINT_SEEDANCE_25'],'resolved_endpoint':selected['Id'],'model_reference':selected.get('ModelReference'),'status':selected.get('Status'),'credentials_changed':False,'credential_values_persisted':False}
        h.atomic_write(file,record)
    else:
        if not file.exists():raise RuntimeError('Probe the new movie endpoint before polling')
        record=h.read(file)
        if record['configured_endpoint']!=values['VOLC_ENDPOINT_SEEDANCE_25']:raise RuntimeError('Configuration changed; reverify endpoint')
    values['VOLC_ENDPOINT_SEEDANCE_25']=record['resolved_endpoint'];client=api.Client(values)
    client.authenticate()
    return values,client

def prepare(p,c,values):
    images=[];bindings=[]
    for asset in h.active_assets(p,c):
        selected=h.selected_media(asset);file=ROOT/selected['path'];data=file.read_bytes()
        mime=mimetypes.guess_type(file.name)[0] or 'image/png'
        if len(data)>30*1024*1024:raise ValueError('Reference image exceeds provider limit')
        token='@Image'+str(len(bindings)+1)
        bindings.append({'tag':asset['tag'],'candidate_id':selected['id'],'reference_token':token,'path':selected['path'],'sha256':hashlib.sha256(data).hexdigest(),'role':'reference_image'})
        images.append({'type':'image_url','image_url':{'url':'data:'+mime+';base64,'+base64.b64encode(data).decode()},'role':'reference_image'})
    text=c['prompt']
    for b in sorted(bindings,key=lambda b:-len(b['tag'])):text=re.sub(re.escape(b['tag'])+r'(?![\w-])',b['reference_token'],text,flags=re.I)
    if re.search(r'@(?!Image\d+\b)[\w-]+',text):raise ValueError('Unbound tag in submission prompt')
    text+='\nREFERENCE MODE: individual identity, wardrobe, prop shape and empty setting references only. One multi-view dog or human sheet means ONE individual. No first-frame input, no storyboard input, no contact-sheet input. Generate full-screen genuine character animation. Night harbour plate supplies geography only for morning chapters; use the chapter lighting. No text, titles, captions, signatures or credits at any timestamp.'
    local_audio=c.get('audio_mode')=='local_original_ambience'
    body={'model':values.get('VOLC_ENDPOINT_SEEDANCE_25','<resolved-endpoint>'),'content':[{'type':'text','text':text}]+images,'duration':c['duration'],'ratio':'21:9','resolution':'720p','generate_audio':not local_audio,'watermark':False,'return_last_frame':True,'output_format':'mp4','omni_reference_task_type':'reference','seed':910900+c['chapter_index']}
    size=len(json.dumps(body,ensure_ascii=False,separators=(',',':')).encode())
    if size>=64*1024*1024 or not 1<=len(images)<=30:raise ValueError('Provider payload limit exceeded')
    take={'id':c['id']+'_take01','chapter_id':c['id'],'take_number':1,'status':'pending','submission_state':'not_submitted','created_at':api.now(),'source_revision':p['revision'],'dependency_fingerprint':h.chapter_fingerprint(ROOT,p,c),'prompt':c['prompt'],'submitted_prompt':text,'bindings':bindings,'duration':c['duration'],'resolution':'720p','aspect_ratio':'21:9','model':'Seedance 2.5','settings':{k:v for k,v in body.items() if k not in ['content','model']},'request_bytes':size}
    if local_audio:take['audio_source']='Locally synthesized original wind and soft paw sounds; provider audio disabled, no recordings or melody'
    return body,take

def sync():
    p=h.read(ROOT/'project.json');q=copy.deepcopy(p);j=h.read(JOURNAL)
    for c in q['chapters']:
        t=j['takes'].get(c['id'])
        if not t:continue
        c['takes']=t.get('prior_takes',[])+[{k:v for k,v in t.items() if k!='prior_takes'}]
        if t['status']=='succeeded' and t.get('verification',{}).get('decode_verified'):c['active_take_id']=t['id']
    done=sum(t['status']=='succeeded' for t in j['takes'].values())
    accepted=sum(bool(t.get('task_id'))+sum(bool(previous.get('task_id')) for previous in t.get('prior_takes',[])) for t in j['takes'].values())
    q['render_state'].update(status='awaiting_assembly' if done==len(p['chapters']) else 'rendering',video_generation='complete' if done==len(p['chapters']) else 'rendering',video_takes_generated=done,generation_jobs_submitted=accepted)
    return h.save(ROOT,p,q,'Register this new movie’s journaled generation tasks and verified take selections')

def preflight():
    result=subprocess.run([sys.executable,str(HELPER),'render-ready',str(ROOT)],capture_output=True,text=True,encoding='utf-8')
    if result.returncode:raise RuntimeError('render-ready rejected submission: '+result.stderr)
    return json.loads(result.stdout)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['probe','prepare','submit','poll','sync']);ap.add_argument('--chapters',default='all');ap.add_argument('--replacement',action='store_true');a=ap.parse_args()
    if a.command=='sync':print(json.dumps(sync()));return
    p=h.read(ROOT/'project.json');chapters=p['chapters'] if a.chapters=='all' else [p['chapters'][int(i)-1] for i in a.chapters.split(',')]
    if a.command=='prepare':
        plans=[]
        for c in chapters:
            _,t=prepare(p,c,{})
            h.atomic_write(ROOT/'chapters'/c['id']/'submission-plan-v01.json',t);plans.append(t)
        h.atomic_write(ROOT/'exports/submission-plan.json',{'project_id':p['id'],'revision':p['revision'],'status':'prepared_not_submitted','takes':plans})
        print('Prepared',len(plans),'distinct-duration text-plus-assets payloads. No base64 or credentials persisted.');return
    values,client=connect(a.command in ('probe','submit'))
    if a.command=='probe':print('Live running Seedance 2.5 endpoint verified in the authorized base project; token stays in memory. No generation submitted.');return
    j=h.read(JOURNAL) if JOURNAL.exists() else {'project_id':p['id'],'credential_source':'Four base settings expressly authorized in this chat on 2026-10-09','takes':{}}
    assert j['project_id']==p['id']
    for c in chapters:
        t=j['takes'].get(c['id'])
        if a.command=='submit':
            prior=[]
            if t:
                if a.replacement and t['status'] in ('failed','succeeded') and t['submission_state'] in ('accepted','rejected'):
                    if t['dependency_fingerprint']==h.chapter_fingerprint(ROOT,p,c):raise RuntimeError('Replacement needs changed prompt dependencies, not an identical paid retry')
                    prior=t.get('prior_takes',[])+[{k:v for k,v in t.items() if k!='prior_takes'}]
                else:print(c['id'],'already journaled; no duplicate POST',flush=True);continue
            gate=preflight();body,t=prepare(p,c,values)
            t['preflight_revision']=gate['source_revision']
            if prior:t.update(id=c['id']+'_take'+str(len(prior)+1).zfill(2),take_number=len(prior)+1,prior_takes=prior)
            t['submission_state']='submitting';j['takes'][c['id']]=t;h.atomic_write(JOURNAL,j)
            try:result=client.ark('POST',body=body)
            except Exception as error:
                t.update(submission_state='rejected' if str(error).startswith('HTTP ') else 'uncertain',error=client.clean(error))
                if t['submission_state']=='rejected':t['status']='failed'
                h.atomic_write(JOURNAL,j);raise
            if not result.get('id'):
                t['submission_state']='uncertain';h.atomic_write(JOURNAL,j);raise RuntimeError('No task ID received; reconcile before any retry')
            t.update(task_id=result['id'],submission_state='accepted',submitted_at=api.now());h.atomic_write(JOURNAL,j)
            print(c['id'],'accepted;',c['duration'],'seconds, 720p, 21:9;', 'provider audio' if body['generate_audio'] else 'video only with local original ambience',flush=True)
        else:
            if not t or not t.get('task_id') or t['status']=='failed':continue
            if t['status']=='succeeded' and (ROOT/t['path']).is_file():continue
            result=client.ark('GET','/'+urllib.parse.quote(t['task_id'],safe=''));state=result.get('status');old=t.get('provider_status')
            t.update(provider_status=state,checked_at=api.now())
            if state=='succeeded':
                content=result.get('content',{});file=ROOT/'chapters'/c['id']/'takes'/(t['id']+'.mp4')
                if not content.get('video_url'):raise RuntimeError('Succeeded task missing video URL')
                if t['settings'].get('generate_audio') is False:
                    original=file.with_name(file.stem+'_provider-silent.mp4')
                    api.download(content['video_url'],original)
                    module('original_ambience',ROOT/'local_ambience.py').mux(original,file,c['duration'])
                    t['provider_original_path']=original.relative_to(ROOT).as_posix()
                else:api.download(content['video_url'],file)
                t['path']=file.relative_to(ROOT).as_posix()
                if content.get('last_frame_url'):
                    last=file.with_name(t['id']+'_last.jpg');api.download(content['last_frame_url'],last);t['last_frame_path']=last.relative_to(ROOT).as_posix()
                t.update(status='succeeded',completed_at=api.now(),provider_metadata={k:result[k] for k in ['duration','resolution','ratio','framespersecond','usage'] if k in result})
            elif state in ('failed','cancelled','expired'):t.update(status='failed',error=client.clean(result.get('error',state)))
            else:t['status']='processing' if state=='running' else 'pending'
            h.atomic_write(JOURNAL,j)
            if state!=old:print(c['id'],state,flush=True)
    if a.command=='poll':print('Summary',json.dumps({s:sum(t['status']==s for t in j['takes'].values()) for s in ['succeeded','processing','pending','failed']}),flush=True)

if __name__=='__main__':
    try:main()
    except Exception as error:print(type(error).__name__+': '+str(error),file=sys.stderr);sys.exit(1)
