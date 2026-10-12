"""Authorized BytePlus direct route. Four named settings, memory-only secrets."""
import sys
sys.dont_write_bytecode = True
import base64
import hashlib
import hmac
import json
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
import prepare

ROOT=Path(__file__).resolve().parent
ENV=ROOT.parents[2]/'aifx-studio'/'.env'
NAMES=('VOLC_ACCESS_KEY','VOLC_SECRET_KEY_RAW','VOLC_PROJECT_NAME','VOLC_ENDPOINT_SEEDANCE_25')
MANAGEMENT='ark.ap-southeast-1.byteplusapi.com'
TASKS='https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks'

def settings():
    found={}
    for line in ENV.read_text(encoding='utf-8-sig').splitlines():
        match=re.match(r'^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)\s*$',line)
        if not match or match[1] not in NAMES: continue
        value=match[2].strip()
        if value[:1] in ('"',"'"):
            quote=value[0]
            end=value.rfind(quote)
            if end<1: raise RuntimeError('Malformed quoted named setting')
            value=value[1:end]
        else:
            value=re.split(r'\s+#',value,maxsplit=1)[0].strip()
        found[match[1]]=value
    if not all(found.get(n) for n in NAMES):
        raise RuntimeError('Missing named settings: '+','.join(n for n in NAMES if not found.get(n)))
    return found

class ProviderError(RuntimeError):
    def __init__(self,status,code,message):
        self.status,self.code,self.message=status,code,message
        super().__init__(f'Provider HTTP {status}: {code}: {message}')

class Client:
    def __init__(self):
        self.config=settings()
        self.token=None
        self.token_time=0
        self.endpoint=None

    def safe_message(self,text):
        for val in list(self.config.values())+[self.token or '']:
            if val: text=text.replace(val,'[redacted]')
        return re.sub(r'https?://\S+','[provider URL]',text)[:800]

    def request(self,url,method='GET',body=None,headers=None,timeout=180):
        request=urllib.request.Request(url,data=body,headers=headers or {},method=method)
        try:
            with urllib.request.urlopen(request,timeout=timeout) as response:
                return json.loads(response.read())
        except urllib.error.HTTPError as error:
            try:
                data=json.loads(error.read())
                item=data.get('error') or data.get('ResponseMetadata',{}).get('Error') or data
                code=item.get('code') or item.get('Code') or 'unknown'
                message=item.get('message') or item.get('Message') or 'Provider rejected request'
            except (ValueError,AttributeError):
                code,message='unknown','Provider rejected request'
            raise ProviderError(error.code,code,self.safe_message(str(message))) from None

    def management(self,action,payload):
        body=json.dumps(payload,separators=(',',':'),ensure_ascii=False).encode()
        query=urllib.parse.urlencode(sorted({'Action':action,'Version':'2024-01-01'}.items()),quote_via=urllib.parse.quote)
        now=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
        body_hash=hashlib.sha256(body).hexdigest()
        canonical_headers=f'content-type:application/json\nhost:{MANAGEMENT}\nx-content-sha256:{body_hash}\nx-date:{now}\n'
        signed='content-type;host;x-content-sha256;x-date'
        canonical='\n'.join(['POST','/',query,canonical_headers,signed,body_hash])
        scope=f'{now[:8]}/ap-southeast-1/ark/request'
        to_sign='\n'.join(['HMAC-SHA256',now,scope,hashlib.sha256(canonical.encode()).hexdigest()])
        key=self.config['VOLC_SECRET_KEY_RAW'].encode()
        for part in [now[:8],'ap-southeast-1','ark','request']:
            key=hmac.new(key,part.encode(),hashlib.sha256).digest()
        signature=hmac.new(key,to_sign.encode(),hashlib.sha256).hexdigest()
        headers={'Content-Type':'application/json','Host':MANAGEMENT,'X-Content-Sha256':body_hash,'X-Date':now,'Authorization':f'HMAC-SHA256 Credential={self.config["VOLC_ACCESS_KEY"]}/{scope}, SignedHeaders={signed}, Signature={signature}'}
        return self.request(f'https://{MANAGEMENT}/?{query}','POST',body,headers)

    def resolve(self):
        items=[]
        page=1
        while True:
            result=self.management('ListEndpoints',{'ProjectName':self.config['VOLC_PROJECT_NAME'],'PageNumber':page,'PageSize':100}).get('Result',{})
            rows=result.get('Items',[])
            items+=rows
            if len(items)>=result.get('TotalCount',len(items)) or not rows: break
            page+=1
        def suitable(row):
            model=json.dumps(row.get('ModelReference',{})).lower()
            return str(row.get('Status','')).lower() in ('running','ready') and bool(re.search(r'seedance[-_ ]?2[-_. ]?5',model))
        matches=[row for row in items if suitable(row)]
        configured=self.config['VOLC_ENDPOINT_SEEDANCE_25']
        chosen=next((row for row in matches if row.get('Id')==configured),None)
        if chosen is None:
            if len(matches)!=1: raise RuntimeError(f'Expected one accessible running Seedance 2.5 endpoint; found {len(matches)}')
            chosen=matches[0]
        self.endpoint=chosen['Id']
        resolution={'endpoint':self.endpoint,'model_reference':chosen.get('ModelReference'),'verified_at':datetime.now(timezone.utc).isoformat(),'configured_endpoint_matched':self.endpoint==configured,'reason':'Resolved against running Seedance 2.5 endpoints in the authorized project','documentation':['https://docs.byteplus.com/en/docs/ModelArk/seedance-2-5','https://docs.byteplus.com/ja/docs/modelark/create-video-generation-task-api'],'settings_source':'User-authorized sibling environment file; only four named settings read; credentials retained in memory.'}
        prepare.write_json(ROOT/'exports'/'endpoint-resolution.json',resolution)
        return {'matching_running_endpoints':len(matches),'configured_endpoint_matched':self.endpoint==configured}

    def authenticate(self):
        if not self.endpoint:
            saved=ROOT/'exports'/'endpoint-resolution.json'
            if saved.is_file(): self.endpoint=prepare.helper.read(saved)['endpoint']
            else: self.resolve()
        result=self.management('GetApiKey',{'DurationSeconds':3600,'ResourceType':'endpoint','ResourceIds':[self.endpoint]})
        self.token=(result.get('Result') or {}).get('ApiKey') or result.get('ApiKey')
        if not self.token: raise RuntimeError('Temporary token was not returned')
        self.token_time=time.monotonic()

    def task(self,suffix='',method='GET',payload=None):
        if not self.token or time.monotonic()-self.token_time>2800: self.authenticate()
        headers={'Authorization':'Bearer '+self.token,'Content-Type':'application/json','X-Project-Name':self.config['VOLC_PROJECT_NAME']}
        body=None if payload is None else json.dumps(payload,separators=(',',':'),ensure_ascii=False).encode()
        return self.request(TASKS+suffix,method,body,headers)

    def download(self,url,destination):
        destination.parent.mkdir(parents=True,exist_ok=True)
        partial=destination.with_suffix(destination.suffix+'.partial')
        with urllib.request.urlopen(url,timeout=240) as response, partial.open('wb') as out:
            while True:
                block=response.read(1024*1024)
                if not block: break
                out.write(block)
        partial.replace(destination)

def bind(project,chapter):
    assets=prepare.helper.active_assets(project,chapter)
    bindings=[]
    mapping={}
    content=[]
    for i,asset in enumerate(assets,1):
        candidate=prepare.helper.selected_media(asset)
        path=ROOT/candidate['path']
        data=path.read_bytes()
        if len(data)>30*1024*1024: raise RuntimeError('Reference exceeds image-size limit')
        provider_tag=f'@Image{i}'
        mapping[asset['tag'].casefold()]=provider_tag
        bindings.append({'asset_id':asset['id'],'tag':asset['tag'],'provider_tag':provider_tag,'candidate_id':candidate['id'],'path':candidate['path'],'role':'reference_image','sha256':hashlib.sha256(data).hexdigest()})
        mime='image/png' if path.suffix.lower()=='.png' else 'image/jpeg'
        content.append({'type':'image_url','image_url':{'url':f'data:{mime};base64,'+base64.b64encode(data).decode()},'role':'reference_image'})
    prompt=prepare.helper.TAG.sub(lambda m:mapping[m[0].casefold()],chapter['prompt'])
    return prompt,bindings,[{'type':'text','text':prompt}]+content

def register_take(chapter_id,take):
    current=prepare.helper.read(ROOT/'project.json')
    proposal=json.loads(json.dumps(current))
    chapter=next(c for c in proposal['chapters'] if c['id']==chapter_id)
    old=next((t for t in chapter['takes'] if t['id']==take['id']),None)
    if old: old.update(take)
    else: chapter['takes'].append(take)
    proposal['production_stage']='rendering'
    prepare.helper.save(ROOT,current,proposal,f'Record {chapter_id} take status {take["status"]}')

def submit(client,chapter_ids=None,retry=False):
    client.resolve()
    client.authenticate()
    for chapter_id in (chapter_ids or [c['id'] for c in prepare.helper.read(ROOT/'project.json')['chapters']]):
        project=prepare.helper.read(ROOT/'project.json')
        chapter=next(c for c in project['chapters'] if c['id']==chapter_id)
        if retry and any(t['status'] in ('pending','processing') for t in chapter['takes']):
            raise RuntimeError(f'{chapter_id} still has an accepted job in progress. Do not duplicate.')
        number=max([t.get('take_number',0) for t in chapter['takes']]+[0])+1 if retry else 1
        take_id=f'take_{number:02d}'
        journal=ROOT/'chapters'/chapter_id/'takes'/f'{take_id}-journal.json'
        if journal.exists():
            recorded=prepare.helper.read(journal)
            if recorded.get('submission_state') in ('accepted','downloaded','failed'):
                print(json.dumps({'chapter':chapter_id,'submission':'already_recorded'}),flush=True)
                continue
            raise RuntimeError(f'{chapter_id} has an uncertain submission. Reconcile before any new POST.')
        ready=subprocess.run([sys.executable,str(prepare.HELPER),'render-ready',str(ROOT)],capture_output=True,text=True)
        if ready.returncode: raise RuntimeError('Asset/render preflight failed: '+ready.stdout[:700])
        prompt,bindings,content=bind(project,chapter)
        payload={'model':client.endpoint,'content':content,'duration':chapter['duration'],'ratio':'21:9','resolution':'720p','generate_audio':True,'watermark':False,'return_last_frame':True,'output_format':'mp4','omni_reference_task_type':'reference','seed':261009+chapter['chapter_index']+1000*(number-1)}
        serialized=json.dumps(payload,separators=(',',':'),ensure_ascii=False).encode()
        if len(serialized)>64*1024*1024: raise RuntimeError('Serialized request exceeds 64 MB')
        take={'id':take_id,'take_number':number,'status':'pending','prompt':chapter['prompt'],'submitted_prompt':prompt,'bindings':bindings,'duration':chapter['duration'],'resolution':'720p','ratio':'21:9','model':client.endpoint,'source_revision':project['revision'],'dependency_fingerprint':prepare.helper.chapter_fingerprint(ROOT,project,chapter),'created_at':datetime.now(timezone.utc).isoformat(),'settings':{k:v for k,v in payload.items() if k not in ('content','model')},'request_bytes':len(serialized)}
        record={'submission_state':'submitting','chapter_id':chapter_id,'take':take}
        prepare.write_json(journal,record)
        register_take(chapter_id,take)
        try:
            result=client.task(method='POST',payload=payload)
        except ProviderError as error:
            record.update(submission_state='rejected',error={'status':error.status,'code':error.code,'message':error.message})
            prepare.write_json(journal,record)
            take.update(status='failed',error=error.message)
            register_take(chapter_id,take)
            raise
        except Exception:
            record['submission_state']='uncertain'
            prepare.write_json(journal,record)
            raise RuntimeError(f'{chapter_id} submission uncertain; do not duplicate') from None
        if not result.get('id'):
            record['submission_state']='uncertain'
            prepare.write_json(journal,record)
            raise RuntimeError('Provider returned no task ID; do not duplicate')
        take['task_id']=result['id']
        record.update(submission_state='accepted',task_id=result['id'],take=take)
        prepare.write_json(journal,record)
        register_take(chapter_id,take)
        print(json.dumps({'chapter':chapter_id,'submission':'accepted','duration':chapter['duration'],'references':len(bindings),'request_mb':round(len(serialized)/1024/1024,2)}),flush=True)

def poll(client):
    for chapter in prepare.helper.read(ROOT/'project.json')['chapters']:
      for journal in sorted((ROOT/'chapters'/chapter['id']/'takes').glob('take_*-journal.json')):
        if not journal.is_file(): continue
        record=prepare.helper.read(journal)
        if record.get('submission_state')=='downloaded': continue
        if record.get('submission_state')!='accepted': continue
        result=client.task('/'+urllib.parse.quote(record['task_id'],safe=''))
        status=result.get('status')
        take=record['take']
        if status=='succeeded':
            destination=journal.parent/f'{take["id"]}.mp4'
            if not destination.is_file(): client.download(result['content']['video_url'],destination)
            take.update(status='succeeded',path=destination.relative_to(ROOT).as_posix())
            if result['content'].get('last_frame_url'):
                frame=journal.parent/f'{take["id"]}-last-frame.jpg'
                if not frame.is_file(): client.download(result['content']['last_frame_url'],frame)
                take['last_frame_path']=frame.relative_to(ROOT).as_posix()
            take['provider_metadata']={k:result[k] for k in ('duration','framespersecond','resolution','ratio','seed','generate_audio','usage','created_at','updated_at') if k in result}
            record.update(submission_state='downloaded',take=take,provider_status=status)
            prepare.write_json(journal,record)
            register_take(chapter['id'],take)
            print(json.dumps({'chapter':chapter['id'],'status':'downloaded','bytes':destination.stat().st_size}),flush=True)
        elif status in ('failed','cancelled','expired'):
            error=result.get('error') or {}
            take.update(status='failed',error=client.safe_message(str(error.get('message','Provider task '+status))))
            record.update(submission_state='failed',take=take,provider_status=status)
            prepare.write_json(journal,record)
            register_take(chapter['id'],take)
            print(json.dumps({'chapter':chapter['id'],'status':status,'error':take['error']}),flush=True)
        elif record.get('provider_status')!=status:
            record['provider_status']=status
            take['status']='processing' if status=='running' else 'pending'
            record['take']=take
            prepare.write_json(journal,record)
            register_take(chapter['id'],take)
            print(json.dumps({'chapter':chapter['id'],'status':status}),flush=True)
    project=prepare.helper.read(ROOT/'project.json')
    counts={s:0 for s in ('pending','processing','succeeded','failed')}
    for ch in project['chapters']:
        if ch['takes']: counts[ch['takes'][-1]['status']]+=1
    if getattr(client,'last_counts',None)!=counts:
        print(json.dumps({'counts':counts}),flush=True)
        client.last_counts=counts.copy()
    return counts

if __name__=='__main__':
    try:
        client=Client()
        if sys.argv[1]=='diagnose':
            facts=client.resolve()
            client.authenticate()
            print(json.dumps({'named_settings_present':True,'temporary_authentication':'success',**facts}),flush=True)
        elif sys.argv[1]=='submit': submit(client)
        elif sys.argv[1]=='retry': submit(client,sys.argv[2:],retry=True)
        elif sys.argv[1]=='poll': poll(client)
        elif sys.argv[1]=='watch':
            deadline=time.monotonic()+40*60
            while time.monotonic()<deadline:
                counts=poll(client)
                if counts['succeeded']+counts['failed']==8: break
                time.sleep(30)
            else:
                print(json.dumps({'watch':'timed_out','note':'Accepted jobs remain recorded; no duplicate submissions.'}),flush=True)
    except Exception as error:
        message=client.safe_message(str(error)) if 'client' in globals() else str(error)
        print(json.dumps({'error_type':type(error).__name__,'message':message}),flush=True)
        sys.exit(1)
