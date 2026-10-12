"""Project-local Seedance adapter. Credentials are read only at runtime and never saved."""
import argparse
import base64
import hashlib
import hmac
import importlib.util
import json
import os
import re
import ssl
import subprocess
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
HELPER = Path('C:/Users/admina/.codex/skills/movi2/scripts/project.py')
ENV_FILE = Path('C:/Users/admina/Downloads/project/aifx-studio/.env')
SETTINGS = ('VOLC_ACCESS_KEY','VOLC_SECRET_KEY_RAW','VOLC_PROJECT_NAME','VOLC_ENDPOINT_SEEDANCE_25')
HOST = 'ark.ap-southeast-1.byteplusapi.com'
BASE = 'https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks'
JOURNAL = ROOT / 'exports' / 'task-journal.json'
LOCK = threading.RLock()

def now():
    return datetime.now(timezone.utc).isoformat()

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def atomic_json(path, value):
    path.parent.mkdir(parents=True,exist_ok=True)
    temp = path.with_suffix(path.suffix+'.'+uuid.uuid4().hex+'.partial')
    temp.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
    os.replace(temp,path)

def settings():
    # Parse only the four explicitly authorized settings. Never load sibling variables.
    found = {}
    for line in ENV_FILE.read_text(encoding='utf-8-sig').splitlines():
        match = re.match(r'^\s*(?:export\s+)?([A-Z0-9_]+)\s*=\s*(.*)$',line)
        if not match or match[1] not in SETTINGS:
            continue
        value = match[2].strip()
        if value[:1] in ('"',"'"):
            mark = value[0]
            end = value.find(mark,1)
            if end == -1:
                raise ValueError('Invalid quoting in an authorized setting')
            value = value[1:end]
        else:
            value = re.split(r'\s+#',value,1)[0].strip()
        found[match[1]] = value
    missing = [key for key in SETTINGS if not found.get(key)]
    if missing:
        raise ValueError('Missing authorized settings: '+', '.join(missing))
    return found

class ApiFailure(Exception):
    def __init__(self, status, code):
        self.status, self.code = status, str(code)
        super().__init__(f'Provider request rejected: HTTP {status}, code {self.code}')

def response(request, timeout=120):
    try:
        with urlopen(request,timeout=timeout) as result:
            data = json.loads(result.read())
    except HTTPError as error:
        try:
            data = json.loads(error.read())
            info = data.get('error') or data.get('Error') or data.get('ResponseMetadata',{}).get('Error') or {}
            code = info.get('code') or info.get('Code') or 'HTTPError'
        except Exception:
            code = 'HTTPError'
        raise ApiFailure(error.code,code) from None
    error = data.get('Error') or data.get('ResponseMetadata',{}).get('Error')
    if error:
        raise ApiFailure(200,error.get('Code','ApiError'))
    return data

class Client:
    def __init__(self):
        self.config = settings()
        self.endpoint = None
        self.token = None
        self.token_time = 0
        self.token_lock = threading.Lock()

    def management(self, action, body):
        raw = json.dumps(body,separators=(',',':'),ensure_ascii=False).encode('utf-8')
        query = urlencode(sorted({'Action':action,'Version':'2024-01-01'}.items()),quote_via=quote)
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
        day = stamp[:8]
        sha = hashlib.sha256(raw).hexdigest()
        headers = 'content-type:application/json\nhost:'+HOST+'\nx-content-sha256:'+sha+'\nx-date:'+stamp+'\n'
        signed = 'content-type;host;x-content-sha256;x-date'
        canonical = '\n'.join(['POST','/',query,headers,signed,sha])
        scope = day+'/ap-southeast-1/ark/request'
        string = '\n'.join(['HMAC-SHA256',stamp,scope,hashlib.sha256(canonical.encode()).hexdigest()])
        key = self.config['VOLC_SECRET_KEY_RAW'].encode()
        for word in [day,'ap-southeast-1','ark','request']:
            key = hmac.new(key,word.encode(),hashlib.sha256).digest()
        signature = hmac.new(key,string.encode(),hashlib.sha256).hexdigest()
        authorization = 'HMAC-SHA256 Credential='+self.config['VOLC_ACCESS_KEY']+'/'+scope+', SignedHeaders='+signed+', Signature='+signature
        request = Request('https://'+HOST+'/?'+query,data=raw,method='POST',headers={
            'Content-Type':'application/json','Host':HOST,'X-Date':stamp,
            'X-Content-Sha256':sha,'Authorization':authorization})
        return response(request)

    def resolve(self):
        items, page = [], 1
        while True:
            data = self.management('ListEndpoints',{'ProjectName':self.config['VOLC_PROJECT_NAME'],'PageNumber':page,'PageSize':100})
            result = data.get('Result',data)
            batch = result.get('Items',[])
            items.extend(batch)
            if len(items)>=result.get('TotalCount',len(items)) or not batch:
                break
            page += 1
        candidates = []
        for item in items:
            desc = json.dumps(item.get('ModelReference',{})).lower()
            desc += ' '+str(item.get('Name','')).lower()
            status = str(item.get('Status','')).lower()
            if re.search(r'seedance[-_. ]2[-_. ]5',desc) and status in ('running','active','ready'):
                candidates.append(item)
        configured = self.config['VOLC_ENDPOINT_SEEDANCE_25']
        exact = [item for item in candidates if item.get('Id')==configured]
        if exact:
            chosen = exact[0]
        elif len(candidates)==1:
            chosen = candidates[0]
        else:
            raise ValueError('No unique running Seedance 2.5 endpoint in the authorized project; matching count='+str(len(candidates)))
        self.endpoint = chosen['Id']
        # Operational endpoint ID is not a credential; do not persist AK/SK/project/token values.
        atomic_json(ROOT/'exports/endpoint-resolution.json',{
            'verified_at':now(),'model_family':'Seedance 2.5',
            'configured_endpoint_matches':self.endpoint==configured,
            'running_matching_endpoint_count':len(candidates),
            'resolved_endpoint_id':self.endpoint,
            'reason':'Configured endpoint verified' if self.endpoint==configured else 'Unambiguous running Seedance 2.5 endpoint in authorized project'})
        self.get_token()
        return {'model_family':'Seedance 2.5','configured_endpoint_matches':self.endpoint==configured,
                'running_matching_endpoint_count':len(candidates),'authentication':'verified'}

    def get_token(self):
        with self.token_lock:
            if self.token and time.monotonic()-self.token_time<2900:
                return self.token
            data = self.management('GetApiKey',{'DurationSeconds':3600,'ResourceType':'endpoint','ResourceIds':[self.endpoint]})
            self.token = data.get('Result',{}).get('ApiKey') or data.get('ApiKey')
            if not self.token:
                raise ValueError('Provider did not return a temporary API key')
            self.token_time = time.monotonic()
            return self.token

    def task(self, task_id=None, payload=None):
        headers = {'Authorization':'Bearer '+self.get_token(),'Content-Type':'application/json',
                   'X-Project-Name':self.config['VOLC_PROJECT_NAME']}
        url = BASE if task_id is None else BASE+'/'+quote(task_id,safe='')
        raw = None if payload is None else json.dumps(payload,separators=(',',':'),ensure_ascii=False).encode()
        return response(Request(url,data=raw,headers=headers,method='POST' if payload is not None else 'GET'))

def preflight():
    proc = subprocess.run([os.sys.executable,str(HELPER),'render-ready',str(ROOT)],capture_output=True,text=True,encoding='utf-8')
    if proc.returncode:
        raise ValueError('Movi2 render-ready rejected current state: '+proc.stdout.strip())
    return read_json(ROOT/'project.json')

def compile_payload(project, chapter, endpoint):
    spec = importlib.util.spec_from_file_location('project_helper',HELPER)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    active = helper.active_assets(project,chapter)
    bindings = []
    content = []
    prompt = chapter['prompt']
    for index, asset in enumerate(active,1):
        candidate = helper.selected_media(asset)
        path = ROOT/candidate['path']
        raw = path.read_bytes()
        if len(raw)>=30*1024*1024:
            raise ValueError('Reference image too large: '+asset['tag'])
        bindings.append({'tag':asset['tag'],'provider_tag':'@Image'+str(index),
                         'asset_id':asset['id'],'candidate_id':candidate['id'],
                         'path':candidate['path'],'role':'reference_image',
                         'sha256':hashlib.sha256(raw).hexdigest()})
        content.append({'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode(raw).decode()},'role':'reference_image'})
    # Whole-token replacement prevents aliases such as @Tart-rest capturing @Tart-puppy.
    mapping = {b['tag']:b['provider_tag'] for b in bindings}
    pattern = re.compile(r'@[^\W\s][\w-]*',re.UNICODE)
    prompt = pattern.sub(lambda m:mapping.get(m[0],m[0]),prompt)
    content.insert(0,{'type':'text','text':prompt})
    payload = {'model':endpoint,'content':content,'duration':chapter['duration'],
               'ratio':'21:9','resolution':'720p','generate_audio':True,'watermark':False,
               'return_last_frame':True,'output_format':'mp4','omni_reference_task_type':'reference',
               'seed':20261009+chapter['chapter_index']}
    count = len(json.dumps(payload,ensure_ascii=False,separators=(',',':')).encode())
    if count>64*1024*1024:
        raise ValueError('Reference payload exceeds provider request limit')
    return payload,bindings,prompt,helper.chapter_fingerprint(ROOT,project,chapter),count

def export_submission(chapter, bindings, prompt, payload_bytes, fingerprint, revision):
    folder = ROOT/'chapters'/chapter['id']
    folder.mkdir(parents=True,exist_ok=True)
    (folder/'submitted-prompt.txt').write_text(prompt,encoding='utf-8')
    atomic_json(folder/'submission-spec.json',{'duration':chapter['duration'],'ratio':'21:9','resolution':'720p',
        'generate_audio':True,'watermark':False,'return_last_frame':True,'output_format':'mp4',
        'omni_reference_task_type':'reference','bindings':bindings,'serialized_request_bytes':payload_bytes,
        'dependency_fingerprint':fingerprint,'source_revision':revision})

def journal_update(cid, **changes):
    with LOCK:
        # Also protect independent resumed clients, not only threads in this process.
        import msvcrt
        lock_path=JOURNAL.with_suffix('.lock')
        lock_path.parent.mkdir(parents=True,exist_ok=True)
        with lock_path.open('a+b') as handle:
            handle.seek(0,2)
            if not handle.tell(): handle.write(b'0'); handle.flush()
            handle.seek(0)
            msvcrt.locking(handle.fileno(),msvcrt.LK_LOCK,1)
            try:
                journal = read_json(JOURNAL) if JOURNAL.exists() else {'project':'doge-20261009','tasks':{}}
                record = journal['tasks'].setdefault(cid,{'chapter_id':cid})
                record.update(changes)
                journal['updated_at'] = now()
                atomic_json(JOURNAL,journal)
                return dict(record)
            finally:
                handle.seek(0)
                msvcrt.locking(handle.fileno(),msvcrt.LK_UNLCK,1)

def download(url, destination):
    destination.parent.mkdir(parents=True,exist_ok=True)
    partial = destination.with_suffix(destination.suffix+'.partial')
    try:
        with urlopen(Request(url),timeout=120) as incoming, partial.open('wb') as output:
            while True:
                chunk=incoming.read(1024*1024)
                if not chunk: break
                output.write(chunk)
        if partial.stat().st_size==0:
            raise ValueError('Empty provider download')
        os.replace(partial,destination)
    except Exception:
        # Keep partial for diagnostics. No signed URL is written to disk or stdout.
        raise RuntimeError('Provider media download did not complete') from None

def render_one(client, chapter, submit_delay=0):
    cid=chapter['id']
    record = read_json(JOURNAL).get('tasks',{}).get(cid,{}) if JOURNAL.exists() else {}
    if record.get('submission_state') in ('submitting','uncertain') and not record.get('task_id'):
        raise ValueError(cid+': uncertain earlier submission requires reconciliation')
    if record.get('status')=='succeeded' and record.get('path') and (ROOT/record['path']).is_file():
        print(json.dumps({'chapter':cid,'status':'already_downloaded'}),flush=True)
        return record
    if record.get('status') in ('failed','cancelled','expired','rejected'):
        print(json.dumps({'chapter':cid,'status':record['status'],'action':'no automatic paid retry'}),flush=True)
        return record
    if not record.get('task_id'):
        if submit_delay: time.sleep(submit_delay)
        project=preflight()
        current=next(c for c in project['chapters'] if c['id']==cid)
        payload,bindings,prompt,fingerprint,count=compile_payload(project,current,client.endpoint)
        export_submission(current,bindings,prompt,count,fingerprint,project['revision'])
        journal_update(cid,submission_state='submitting',status='pending',submitted_at=now(),
                       take_id='take_01',source_revision=project['revision'],dependency_fingerprint=fingerprint,
                       duration=current['duration'],bindings=bindings)
        try:
            data=client.task(payload=payload)
        except ApiFailure as error:
            journal_update(cid,submission_state='rejected',status='rejected',error_code=error.code,http_status=error.status)
            raise
        except Exception:
            journal_update(cid,submission_state='uncertain',status='pending')
            raise RuntimeError(cid+': submission outcome uncertain; no resubmission') from None
        task_id=data.get('id')
        if not task_id:
            journal_update(cid,submission_state='uncertain',status='pending')
            raise RuntimeError(cid+': response omitted task ID; no resubmission')
        record=journal_update(cid,submission_state='accepted',task_id=task_id,status='queued')
        print(json.dumps({'chapter':cid,'status':'accepted','reference_count':len(bindings),'duration':chapter['duration']}),flush=True)
    prior=None
    while True:
        try:
            data=client.task(task_id=record['task_id'])
        except (URLError,TimeoutError):
            print(json.dumps({'chapter':cid,'status':'poll_temporarily_unavailable'}),flush=True)
            time.sleep(30)
            continue
        status=data.get('status','unknown')
        if status!=prior:
            journal_update(cid,status=status,last_polled_at=now())
            print(json.dumps({'chapter':cid,'status':status}),flush=True)
            prior=status
        if status=='succeeded':
            content=data.get('content',{})
            video_url=content.get('video_url')
            if not video_url: raise ValueError(cid+': succeeded job missing video')
            video=ROOT/'chapters'/cid/'takes'/'take_01.mp4'
            download(video_url,video)
            fields={'status':'succeeded','path':video.relative_to(ROOT).as_posix(),
                    'provider_duration':data.get('duration'),'provider_resolution':data.get('resolution'),
                    'provider_ratio':data.get('ratio'),'provider_usage':data.get('usage'),
                    'completed_at':now()}
            if content.get('last_frame_url'):
                frame=ROOT/'chapters'/cid/'takes'/'take_01-last-frame.jpg'
                download(content['last_frame_url'],frame)
                fields['last_frame_path']=frame.relative_to(ROOT).as_posix()
            result=journal_update(cid,**fields)
            print(json.dumps({'chapter':cid,'status':'downloaded','bytes':video.stat().st_size}),flush=True)
            return result
        if status in ('failed','cancelled','expired'):
            error=data.get('error',{})
            code=error.get('code','GenerationFailed') if isinstance(error,dict) else 'GenerationFailed'
            journal_update(cid,status=status,error_code=code,completed_at=now())
            print(json.dumps({'chapter':cid,'status':status,'error_code':code}),flush=True)
            return read_json(JOURNAL)['tasks'][cid]
        time.sleep(30)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('command',choices=['probe','prepare','render'])
    parser.add_argument('--chapters',nargs='*')
    parser.add_argument('--workers',type=int,default=3)
    args=parser.parse_args()
    if args.command=='prepare':
        project=preflight()
        for chapter in project['chapters']:
            payload,bindings,prompt,fingerprint,count=compile_payload(project,chapter,'endpoint-resolved-at-runtime')
            export_submission(chapter,bindings,prompt,count,fingerprint,project['revision'])
        print(json.dumps({'prepared_chapters':len(project['chapters']),'duration':sum(c['duration'] for c in project['chapters'])}))
        return
    client=Client()
    print(json.dumps(client.resolve()),flush=True)
    if args.command=='probe': return
    project=preflight()
    chapters=[c for c in project['chapters'] if not args.chapters or c['id'] in args.chapters]
    failures=[]
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures={pool.submit(render_one,client,chapter,(i%args.workers)*5):chapter['id'] for i,chapter in enumerate(chapters)}
        for future in as_completed(futures):
            cid=futures[future]
            try:
                result=future.result()
                if result.get('status')!='succeeded': failures.append(cid)
            except Exception as error:
                # Exceptions are deliberately sanitized; do not log network headers/responses.
                print(json.dumps({'chapter':cid,'error':str(error)}),flush=True)
                failures.append(cid)
    print(json.dumps({'finished':len(chapters),'failed_or_pending':failures}),flush=True)
    if failures: raise SystemExit(1)

if __name__=='__main__':
    main()
