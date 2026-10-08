"""Direct Seedance client. Text + selected assets only; never a storyboard.

The four base settings were expressly authorized by the user in the earlier
Tart/Tine chat. Values stay in process memory. Existing adapter is used only
as a credential-safe API/signing library, never for its old payload builder.
"""
import argparse, base64, hashlib, hmac, importlib.util, json, mimetypes, re, sys
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
api=module('seedance_transport',ROOT.parent/'tart-and-tine/exports/seedance_render.py')
h=module('movi2',Path('C:/Users/admina/.codex/skills/movi2/scripts/project.py'))
JOURNAL=ROOT/'exports/seedance-journal.json'

def manage(client,action,body):
    host=api.HOST
    raw=json.dumps(body,ensure_ascii=False,separators=(',',':')).encode()
    digest=hashlib.sha256(raw).hexdigest()
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');date=stamp[:8]
    query=urllib.parse.urlencode({'Action':action,'Version':'2024-01-01'},quote_via=urllib.parse.quote)
    signed='content-type;host;x-content-sha256;x-date'
    headers=f'content-type:application/json\nhost:{host}\nx-content-sha256:{digest}\nx-date:{stamp}\n'
    canonical='\n'.join(['POST','/',query,headers,signed,digest])
    scope=f'{date}/ap-southeast-1/ark/request'
    sign='\n'.join(['HMAC-SHA256',stamp,scope,hashlib.sha256(canonical.encode()).hexdigest()])
    key=client.settings['VOLC_SECRET_KEY_RAW'].encode()
    for s in (date,'ap-southeast-1','ark','request'):key=hmac.new(key,s.encode(),hashlib.sha256).digest()
    sig=hmac.new(key,sign.encode(),hashlib.sha256).hexdigest()
    auth=f"HMAC-SHA256 Credential={client.settings['VOLC_ACCESS_KEY']}/{scope}, SignedHeaders={signed}, Signature={sig}"
    return client.request(f'https://{host}/?{query}','POST',body,{'Content-Type':'application/json','Host':host,'X-Date':stamp,'X-Content-Sha256':digest,'Authorization':auth})

def settings(verify=False):
    values=api.read_credentials()
    resolved=api.resolved_settings(values)
    client=api.Client(resolved)
    if verify:
        result=manage(client,'ListEndpoints',{'ProjectName':values['VOLC_PROJECT_NAME'],'PageNumber':1,'PageSize':100})
        items=result.get('Result',{}).get('Items',[])
        selected=next((e for e in items if e.get('Id')==resolved['VOLC_ENDPOINT_SEEDANCE_25']),None)
        if not selected:raise RuntimeError('Previously resolved endpoint is absent in current base project. No jobs submitted.')
        model=json.dumps(selected.get('ModelReference',{}))
        if not re.search(r'seedance.*2[._ -]?5',model,re.I):raise RuntimeError('Resolved endpoint model is not verified as Seedance 2.5.')
        state=str(selected.get('Status','')).lower()
        if state not in ['running','1']:raise RuntimeError('Resolved endpoint is not running: '+state)
        api.save(ROOT/'exports/endpoint-verification.json',{'verified_at':api.now(),'configured_endpoint':values['VOLC_ENDPOINT_SEEDANCE_25'],'resolved_endpoint':resolved['VOLC_ENDPOINT_SEEDANCE_25'],'model_reference':selected.get('ModelReference'),'status':selected.get('Status'),'credential_values_persisted':False})
        client.authenticate()
    return resolved,client

def prepare(p,c,values):
    bindings=[];images=[]
    for a in h.active_assets(p,c):
        selected=h.selected_media(a)
        if not selected:raise ValueError('Missing selected reference '+a['tag'])
        f=ROOT/selected['path'];mime=mimetypes.guess_type(f.name)[0] or 'image/png'
        token='@Image'+str(len(bindings)+1)
        bindings.append({'tag':a['tag'],'reference_token':token,'path':selected['path'],'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'role':'reference_image'})
        images.append({'type':'image_url','image_url':{'url':'data:'+mime+';base64,'+base64.b64encode(f.read_bytes()).decode()},'role':'reference_image'})
    text=c['prompt']
    for b in sorted(bindings,key=lambda x:-len(x['tag'])):
        text=re.sub(re.escape(b['tag'])+r'(?![\w-])',b['reference_token'],text,flags=re.I)
    if re.search(r'@(?!Image\d+\b)[\w-]+',text):raise ValueError('Unbound tag in translated prompt')
    text+='\nREFERENCE MODE: These images ground individual identity, costume and empty setting only. The images are NOT exact first frames or storyboards. Generate genuine full-screen character motion. Night harbour plate controls geometry; the chapter lighting overrides plate time of day for morning scenes. No reference-grid reproduction. Human character-sheet front/back/portrait is ONE individual, not three.'
    body={'model':values.get('VOLC_ENDPOINT_SEEDANCE_25','<resolved-endpoint>'),'content':[{'type':'text','text':text}]+images,'duration':20,'ratio':'21:9','resolution':'720p','generate_audio':True,'watermark':False,'return_last_frame':True,'output_format':'mp4','omni_reference_task_type':'reference','seed':814100+c['chapter_index']}
    size=len(json.dumps(body,ensure_ascii=False,separators=(',',':')).encode())
    if size>=64*1024*1024:raise ValueError('Payload exceeds 64MB')
    take={'id':c['id']+'_take01','take_id':c['id']+'_take01','chapter_id':c['id'],'take_number':1,'status':'pending','submission_state':'not_submitted','created_at':api.now(),'source_revision':p['revision'],'dependency_fingerprint':h.chapter_fingerprint(ROOT,p,c),'prompt':c['prompt'],'submitted_prompt':text,'bindings':bindings,'duration':20,'resolution':'720p','aspect_ratio':'21:9','model':'Seedance 2.5','settings':{k:v for k,v in body.items() if k not in ['content','model']},'request_bytes':size}
    return body,take

def sync():
    p=h.read(ROOT/'project.json');proposal=json.loads(json.dumps(p));j=api.load(JOURNAL)
    for c in proposal['chapters']:
        t=j['takes'].get(c['id'])
        if not t:continue
        c['takes']=t.get('prior_takes',[])+[{k:v for k,v in t.items() if k!='prior_takes'}]
        if t['status']=='succeeded' and t.get('verification',{}).get('decode_verified'):c['active_take_id']=t['id']
    done=sum(t['status']=='succeeded' for t in j['takes'].values())
    accepted=sum(bool(t.get('task_id')) for t in j['takes'].values())+sum(bool(prior.get('task_id')) for t in j['takes'].values() for prior in t.get('prior_takes',[]))
    proposal['render_state'].update(status='rendering' if done<30 else 'awaiting_assembly',video_takes_generated=done,generation_jobs_submitted=accepted)
    return h.save(ROOT,p,proposal,'Synchronize journaled Seedance tasks and inspected take selections')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['probe','prepare','submit','poll','sync']);parser.add_argument('--chapters',default='all');parser.add_argument('--replace-rejected',action='store_true');parser.add_argument('--replace-failed',action='store_true');parser.add_argument('--new-take',action='store_true');a=parser.parse_args()
    if a.command=='sync':print(json.dumps(sync()));return
    p=h.read(ROOT/'project.json');chapters=p['chapters'] if a.chapters=='all' else [p['chapters'][int(i)-1] for i in a.chapters.split(',')]
    if a.command=='prepare':
        export=[]
        for c in chapters:
            _,take=prepare(p,c,{})
            api.save(ROOT/'chapters'/c['id']/'submission-plan.json',take);export.append(take)
        api.save(ROOT/'exports/submission-plan.json',{'project_id':p['id'],'revision':p['revision'],'status':'prepared_not_submitted','takes':export})
        print('Prepared',len(export),'text-plus-asset payloads; no secrets or base64 stored.');return
    values,client=settings(verify=a.command in ['probe','submit'])
    if a.command=='probe':print('Base project endpoint verified live; temporary token obtained in memory. No generation jobs submitted.');return
    journal=api.load(JOURNAL) if JOURNAL.exists() else {'project_id':p['id'],'credential_source':'../aifx-studio/.env; four expressly authorized base settings only','takes':{}}
    for c in chapters:
        t=journal['takes'].get(c['id'])
        if a.command=='submit':
            prior=[]
            if t:
                confirmed_success=t['status']=='succeeded' and t.get('provider_status')=='succeeded' and t.get('path') and (ROOT/t['path']).is_file()
                if (a.replace_rejected and t['submission_state']=='rejected' and t['status']=='failed') or (a.replace_failed and t['status']=='failed' and t.get('provider_status')=='failed') or (a.new_take and confirmed_success):
                    prior=t.get('prior_takes',[])+[{k:v for k,v in t.items() if k!='prior_takes'}]
                    if t['dependency_fingerprint']==h.chapter_fingerprint(ROOT,p,c):raise RuntimeError('Request has unchanged dependencies; no identical retry.')
                else:
                    print(c['id'],'already journaled:',t['submission_state'],'no duplicate POST',flush=True);continue
            body,t=prepare(p,c,values)
            if prior:t.update(prior_takes=prior,id=c['id']+'_take'+str(len(prior)+1).zfill(2),take_id=c['id']+'_take'+str(len(prior)+1).zfill(2),take_number=len(prior)+1)
            t['submission_state']='submitting';journal['takes'][c['id']]=t;api.save(JOURNAL,journal)
            try:result=client.ark('POST',body=body)
            except Exception as e:
                t.update(submission_state='rejected' if str(e).startswith('HTTP ') else 'uncertain',error=client.clean(e))
                if t['submission_state']=='rejected':t['status']='failed'
                api.save(JOURNAL,journal);raise
            task=result.get('id')
            if not task:
                t['submission_state']='uncertain';api.save(JOURNAL,journal);raise RuntimeError('Accepted response has no task ID; reconcile before retry.')
            t.update(task_id=task,submission_state='accepted',submitted_at=api.now());api.save(JOURNAL,journal)
            print(c['id'],'accepted; 20s, API 720p profile, 21:9, audio',flush=True)
        elif a.command=='poll':
            if not t or not t.get('task_id'):continue
            if t['status']=='succeeded' and t.get('path') and (ROOT/t['path']).exists():continue
            result=client.ark('GET','/'+urllib.parse.quote(t['task_id'],safe=''));state=result.get('status');old=t.get('provider_status')
            t.update(provider_status=state,checked_at=api.now())
            if state=='succeeded':
                content=result.get('content',{});target=ROOT/'chapters'/c['id']/'takes'/(t['id']+'.mp4')
                if not content.get('video_url'):raise RuntimeError('Succeeded task missing video URL')
                api.download(content['video_url'],target);t['path']=target.relative_to(ROOT).as_posix()
                if content.get('last_frame_url'):
                    last=target.with_name(t['id']+'_last.jpg');api.download(content['last_frame_url'],last);t['last_frame_path']=last.relative_to(ROOT).as_posix()
                t.update(status='succeeded',completed_at=api.now(),provider_metadata={k:result[k] for k in ['duration','resolution','ratio','framespersecond','usage'] if k in result})
            elif state in ['failed','cancelled','expired']:t.update(status='failed',error=client.clean(result.get('error',state)))
            else:t['status']='processing' if state=='running' else 'pending'
            api.save(JOURNAL,journal)
            if state!=old:print(c['id'],state,flush=True)
    if a.command=='poll':print('Summary:',json.dumps({s:sum(t['status']==s for t in journal['takes'].values()) for s in ['succeeded','processing','pending','failed']}),flush=True)

if __name__=='__main__':
    try:main()
    except Exception as e:print(type(e).__name__+': '+str(e),file=sys.stderr);sys.exit(1)
