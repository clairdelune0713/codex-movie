from pathlib import Path
import base64
import hashlib
import json
import mimetypes
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

from seedance_client import ROOT, WORKSPACE, TASK_BASE, load_settings, authenticated_headers, json_request, atomic_json, now, ProviderError

HELPER = Path('C:/Users/Admin 3/.codex/skills/movi2/scripts/project.py')
USAGE = HELPER.with_name('usage.py')
SESSION = 'session_41fc80be622d4ff88cfe8e96eedd92d1'
ATTEMPT = 'attempt_01'
TAKE = 'take_01'
FOLDER = ROOT / 'chapters/chapter_01/takes'
JOURNAL = ROOT / 'exports/submission-attempt_01.json'
JOB = ROOT / 'exports/usage-attempt_01.json'

def helper(*args):
    result = subprocess.run([sys.executable, str(HELPER), *map(str,args)], capture_output=True, text=True, encoding='utf-8')
    if result.returncode:
        raise RuntimeError('Movi2 helper failed: ' + result.stdout[-1600:] + result.stderr[-300:])
    return json.loads(result.stdout)

def load_project():
    return json.loads((ROOT / 'project.json').read_text(encoding='utf-8'))

def record_usage(entry):
    atomic_json(JOB, entry)
    result = subprocess.run([sys.executable, str(USAGE), 'record', str(ROOT), '--session', SESSION, '--from', str(JOB)], capture_output=True, text=True, encoding='utf-8')
    if result.returncode:
        raise RuntimeError('Usage recording failed: ' + result.stderr[-300:] + result.stdout[-500:])

def update_take(changes, reason):
    project = load_project()
    chapter = project['chapters'][0]
    take = next((t for t in chapter['takes'] if t['id'] == TAKE), None)
    if take is None:
        chapter['takes'].append(changes)
    else:
        take.update(changes)
    proposal = ROOT / ('proposal-take-' + str(project['revision']) + '.json')
    atomic_json(proposal, project)
    helper('check', ROOT, '--from', proposal)
    helper('commit', ROOT, '--from', proposal, '--reason', reason)

def submit():
    if JOURNAL.exists() or (ROOT / 'exports/submission-attempt_01.lock').exists():
        raise RuntimeError('A single generation has already been journaled; poll/reconcile it instead of submitting again')
    project = load_project()
    if project['generation_constraints']['generation_requests'] != 1 or len(project['chapters']) != 1:
        raise RuntimeError('Single-generation project constraint failed')
    chapter = project['chapters'][0]
    if chapter['duration'] != 30 or project['aspect_ratio'] != '16:9':
        raise RuntimeError('Requested output settings changed')
    route = json.loads((ROOT / 'exports/endpoint-resolution.json').read_text(encoding='utf-8'))
    settings = load_settings()
    headers = authenticated_headers(settings, route)
    fingerprint = helper('fingerprint', ROOT, '--chapter', 'chapter_01')['dependency_fingerprint']
    bindings = []
    images = []
    tags = {}
    for asset in project['asset_list']:
        if asset['id'] not in chapter['linked_asset_ids']:
            continue
        candidate = next(c for c in asset['candidates'] if c['id'] == asset['selected_candidate_id'])
        path = ROOT / candidate['path']
        raw = path.read_bytes()
        if len(raw) > 30*1024*1024:
            raise RuntimeError('Reference exceeds supported size')
        mime = mimetypes.guess_type(path.name)[0]
        reference = '@Image' + str(len(bindings)+1)
        tags[asset['tag']] = reference
        bindings.append({'asset_id':asset['id'], 'tag':asset['tag'], 'reference':reference, 'role':'reference_image', 'candidate_id':candidate['id'], 'path':candidate['path'], 'sha256':hashlib.sha256(raw).hexdigest(), 'mime_type':mime})
        images.append({'type':'image_url','image_url':{'url':'data:' + mime + ';base64,' + base64.b64encode(raw).decode('ascii')},'role':'reference_image'})
    pattern = '|'.join(re.escape(k) for k in sorted(tags,key=len,reverse=True))
    compiled = re.sub('(?:' + pattern + r')(?![\w-])',lambda m:tags[m.group(0)],chapter['prompt'])
    if len(bindings) != 5 or 'mall_c02' in str(bindings):
        raise RuntimeError('Expected the five approved references including FIRST mall only')
    body = {'model':route['endpoint'],'content':[{'type':'text','text':compiled}]+images,'duration':30,'ratio':'16:9','resolution':'720p','generate_audio':True,'watermark':False,'return_last_frame':True,'output_format':'mp4','omni_reference_task_type':'reference','seed':20261022}
    serialized = json.dumps(body,ensure_ascii=False,separators=(',',':')).encode('utf-8')
    if len(serialized) > 64*1024*1024:
        raise RuntimeError('Serialized request exceeds provider limit')
    lock = ROOT / 'exports/submission-attempt_01.lock'
    fd = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL)
    os.write(fd,b'Exactly one generation attempt is reserved. Do not resubmit.\n')
    os.close(fd)
    submitted_at = now()
    entry = {'attempt_id':ATTEMPT,'chapter_id':'chapter_01','take_id':TAKE,'state':'submitting','model':route['model_reference']['FoundationModel']['Name'] + '-' + route['model_reference']['FoundationModel']['ModelVersion'],'resolution':'720p','duration_seconds':30,'reference_video_seconds':0,'cost':{'kind':'unknown','basis':'Awaiting provider task usage/billing; no charge assumed from render selection'}}
    journal = {'attempt_id':ATTEMPT,'session_id':SESSION,'chapter_id':'chapter_01','take_id':TAKE,'state':'prepared','created_at':submitted_at,'source_revision':project['revision'],'dependency_fingerprint':fingerprint,'bindings':bindings,'settings':{k:v for k,v in body.items() if k not in ('content','model')},'request_bytes':len(serialized),'request_sha256':hashlib.sha256(serialized).hexdigest(),'compiled_prompt':'exports/submitted-prompt-attempt_01.txt'}
    atomic_json(JOURNAL,journal)
    (ROOT/'exports/submitted-prompt-attempt_01.txt').write_text(compiled,encoding='utf-8')
    atomic_json(ROOT/'exports/reference-bindings-attempt_01.json',bindings)
    record_usage(entry)
    update_take({'id':TAKE,'take_number':1,'status':'pending','prompt':chapter['prompt'],'submitted_prompt':compiled,'bindings':bindings,'duration':30,'resolution':'720p','model':entry['model'],'source_revision':project['revision'],'dependency_fingerprint':fingerprint,'created_at':submitted_at},'Journal sole 30-second generation before submission')
    helper('render-ready',ROOT,'--chapter','chapter_01')
    journal.update({'state':'submitting','submitted_at':now()})
    atomic_json(JOURNAL,journal)
    try:
        response = json_request(TASK_BASE,body,headers,timeout=120)
    except ProviderError as error:
        journal.update({'state':'rejected','error_code':error.code,'http_status':error.status,'completed_at':now()})
        atomic_json(JOURNAL,journal)
        entry.update({'state':'failed','error_code':error.code})
        record_usage(entry)
        update_take({'id':TAKE,'status':'failed','error':{'code':error.code,'http_status':error.status}},'Retain rejected sole generation attempt')
        raise
    except (urllib.error.URLError, TimeoutError, OSError):
        journal.update({'state':'uncertain','last_updated_at':now(),'error':'Submission transport interrupted; reconcile before any resubmission'})
        atomic_json(JOURNAL,journal)
        entry['state']='uncertain'
        record_usage(entry)
        raise
    task_id = response.get('id')
    if not task_id:
        journal.update({'state':'uncertain','response_keys':list(response),'last_updated_at':now()})
        atomic_json(JOURNAL,journal)
        raise RuntimeError('Submission returned no task ID; do not resubmit')
    journal.update({'state':'accepted','task_id':task_id,'accepted_at':now()})
    atomic_json(JOURNAL,journal)
    entry.update({'task_id':task_id,'state':'queued'})
    record_usage(entry)
    update_take({'id':TAKE,'task_id':task_id,'status':'processing'},'Record accepted single-generation task')
    print(json.dumps({'state':'accepted','task_id':task_id,'generation_requests':1,'duration':30,'ratio':'16:9','resolution':'720p','reference_count':len(bindings),'request_bytes':len(serialized)}),flush=True)

def download(url,path):
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():
        return
    temporary=path.with_suffix(path.suffix+'.partial')
    with urllib.request.urlopen(url,timeout=120) as response, temporary.open('wb') as output:
        while chunk:=response.read(1024*1024):
            output.write(chunk)
    temporary.replace(path)

def poll():
    journal=json.loads(JOURNAL.read_text(encoding='utf-8'))
    if not journal.get('task_id'):
        raise RuntimeError('No accepted task ID; reconcile uncertain submission')
    if journal['state']=='downloaded':
        print(json.dumps({'state':'downloaded','path':str(FOLDER/(TAKE+'.mp4')),'usage':journal.get('usage',{})}))
        return
    route=json.loads((ROOT/'exports/endpoint-resolution.json').read_text(encoding='utf-8'))
    headers=authenticated_headers(load_settings(),route)
    response=json_request(TASK_BASE+'/'+journal['task_id'],headers=headers)
    status=response.get('status','unknown')
    safe={k:response[k] for k in ('id','status','model','created_at','updated_at','resolution','duration','ratio','framespersecond','seed','usage','service_tier','generate_audio') if k in response}
    if response.get('error'):
        safe['error']={k:v for k,v in response['error'].items() if k in ('code','message')}
    safe['checked_at']=now()
    atomic_json(ROOT/'exports/task-status-attempt_01.json',safe)
    entry=json.loads(JOB.read_text(encoding='utf-8'))
    entry.update({'state':status,'usage':response.get('usage',entry.get('usage',{}))})
    record_usage(entry)
    journal.update({'state':status,'last_polled_at':now(),'usage':response.get('usage',journal.get('usage',{}))})
    atomic_json(JOURNAL,journal)
    if status=='succeeded':
        content=response.get('content',{})
        if not content.get('video_url'):
            raise RuntimeError('Successful task has no downloadable video')
        video=FOLDER/(TAKE+'.mp4')
        download(content['video_url'],video)
        last_frame=content.get('last_frame_url')
        if last_frame:
            download(last_frame,FOLDER/(TAKE+'-last-frame.jpg'))
        changes={'id':TAKE,'status':'succeeded','path':video.relative_to(ROOT).as_posix(),'provider_result':safe}
        if last_frame:
            changes['last_frame_path']=(FOLDER/(TAKE+'-last-frame.jpg')).relative_to(ROOT).as_posix()
        update_take(changes,'Retain successful 30-second source take for inspection')
        journal.update({'state':'downloaded','downloaded_at':now(),'video_sha256':hashlib.sha256(video.read_bytes()).hexdigest(),'video_bytes':video.stat().st_size})
        atomic_json(JOURNAL,journal)
        print(json.dumps({'state':'downloaded','path':str(video),'bytes':video.stat().st_size,'usage':response.get('usage',{})}),flush=True)
    elif status in ('failed','cancelled','expired'):
        update_take({'id':TAKE,'status':'failed','error':safe.get('error',{'code':status})},'Retain terminal unsuccessful single generation')
        print(json.dumps({'state':status,'error':safe.get('error',{}),'usage':response.get('usage',{})}),flush=True)
    else:
        print(json.dumps({'state':status,'task_id':journal['task_id'],'checked_at':safe['checked_at']}),flush=True)

if __name__=='__main__':
    try:
        if sys.argv[1:] == ['submit']:
            submit()
        elif sys.argv[1:] == ['poll']:
            poll()
        else:
            raise RuntimeError('Use submit once or poll')
    except (RuntimeError, urllib.error.URLError, OSError, TimeoutError) as error:
        print(json.dumps({'error_type':type(error).__name__,'error':str(error)[:500]}),flush=True)
        sys.exit(1)
