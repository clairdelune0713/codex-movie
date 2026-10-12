"""Submit once, journal acceptance, poll accepted tasks, retain immutable takes."""
import argparse
import base64
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from seedance_client import Client, ProviderError, ROOT, write_json

HELPER=Path(r'C:\Users\admina\.codex\skills\movi2\scripts\project.py')
spec=importlib.util.spec_from_file_location('movi_project_helper',HELPER)
helper=importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
JOURNAL=ROOT/'exports'/'render-journal.json'

def now():
    return datetime.now(timezone.utc).isoformat()

def project():
    return json.loads((ROOT/'project.json').read_text(encoding='utf-8'))

def check_ready():
    result=subprocess.run([sys.executable,str(HELPER),'render-ready',str(ROOT)],capture_output=True,text=True)
    if result.returncode:
        raise RuntimeError('Render-ready rejected current state: '+result.stdout)

def commit(p,reason):
    proposal=ROOT/'proposal-render-state.json'
    write_json(proposal,p)
    r=subprocess.run([sys.executable,str(HELPER),'commit',str(ROOT),'--from',str(proposal),'--reason',reason],capture_output=True,text=True)
    if r.returncode:
        raise RuntimeError('Project commit failed: '+r.stdout+r.stderr)

def save_take(entry,status,path=None):
    p=project()
    c=next(c for c in p['chapters'] if c['id']==entry['chapter_id'])
    take=next((t for t in c['takes'] if t['id']==entry['take_id']),None)
    if take is None:
        take={'id':entry['take_id'],'take_number':entry['take_number'],'status':'pending','prompt':entry['canonical_prompt'],'submitted_prompt':entry['submitted_prompt'],'bindings':entry['bindings'],'duration':c['duration'],'resolution':'720p','model':entry['model'],'source_revision':entry['source_revision'],'dependency_fingerprint':entry['dependency_fingerprint'],'created_at':entry['created_at']}
        c['takes'].append(take)
    take['status']=status
    take['generate_audio']=entry['settings'].get('generate_audio',True)
    if entry.get('task_id'):
        take['task_id']=entry['task_id']
    if path:
        take['path']=str(Path(path).relative_to(ROOT)).replace('\\','/')
    if entry.get('last_frame_path'):
        take['last_frame_path']=entry['last_frame_path']
    if status=='failed':
        take['error']=entry.get('error','Provider failure')
    # Selection follows actual technical/visual inspection, not mere provider success.
    commit(p,f"Record {entry['chapter_id']} {entry['take_id']} as {status}")

def build_entry(p,c,client,take_number):
    active=helper.active_assets(p,c)
    priorities={tag.casefold():i for i,tag in enumerate(c.get('reference_priority',[]))}
    active=sorted(active,key=lambda a:priorities.get(a['tag'].casefold(),len(priorities)))
    bindings=[]
    for i,a in enumerate(active,1):
        selected=helper.selected_media(a)
        path=ROOT/selected['path']
        if not path.is_file():
            raise RuntimeError('Unexpected missing or extraneous reference input.')
        bindings.append({'tag':a['tag'],'provider_tag':f'@Image{i}','asset_id':a['id'],'candidate_id':selected['id'],'path':selected['path'],'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'role':'reference_image','mime_type':'image/jpeg' if path.suffix.lower() in ('.jpg','.jpeg') else 'image/png'})
    mapping={b['tag'].casefold():b['provider_tag'] for b in bindings}
    translated=re.sub(r'@[\w-]+',lambda m:mapping[m.group().casefold()],c['prompt'])
    entry={'chapter_id':c['id'],'take_id':f"{c['id']}_take_{take_number:02d}",'take_number':take_number,'status':'prepared','created_at':now(),'source_revision':p['revision'],'dependency_fingerprint':helper.chapter_fingerprint(ROOT,p,c),'model':client.endpoint,'canonical_prompt':c['prompt'],'submitted_prompt':translated,'bindings':bindings,'settings':{'duration':c['duration'],'ratio':'16:9','resolution':'720p','generate_audio':True,'watermark':False,'return_last_frame':True,'output_format':'mp4','omni_reference_task_type':'reference','seed':41009+int(c['chapter_index'])*37}}
    if c.get('generation_seed') is not None:
        entry['settings']['seed']=c['generation_seed']
    entry['settings']['generate_audio']=c.get('generate_audio',True)
    payload={'model':client.endpoint,'content':[{'type':'text','text':translated}],**entry['settings']}
    for binding in bindings:
        raw=(ROOT/binding['path']).read_bytes()
        if len(raw)>30*1024*1024:
            raise RuntimeError('Reference exceeds per-image limit.')
        payload['content'].append({'type':'image_url','image_url':{'url':'data:'+binding['mime_type']+';base64,'+base64.b64encode(raw).decode()},'role':'reference_image'})
    size=len(json.dumps(payload,ensure_ascii=False,separators=(',',':')).encode())
    if size>64*1024*1024:
        raise RuntimeError('Serialized request exceeds 64 MB.')
    entry['serialized_request_bytes']=size
    entry['reference_count']=len(bindings)
    return entry,payload

def submit_chapters(client,journal,chapters,replace_reviewed=False):
    for chapter_id in chapters:
        previous=[e for e in journal['tasks'] if e['chapter_id']==chapter_id]
        unresolved=[e for e in previous if e['status'] in ('submitting','uncertain','accepted','queued','running','succeeded','downloaded')]
        if unresolved and not (replace_reviewed and all(e['status']=='downloaded' for e in unresolved)):
            print(json.dumps({'chapter':chapter_id,'submission_skipped':True,'existing_status':unresolved[-1]['status']}),flush=True)
            continue
        check_ready()
        p=project()
        c=next(c for c in p['chapters'] if c['id']==chapter_id)
        entry,payload=build_entry(p,c,client,len(previous)+1)
        entry['status']='submitting'
        entry['submitted_at']=now()
        journal['tasks'].append(entry)
        write_json(JOURNAL,journal)
        save_take(entry,'pending')
        # Recheck gate immediately before this individual paid POST.
        check_ready()
        try:
            response=client.submit(payload)
        except ProviderError as error:
            entry.update(status='rejected',error=client.safe(error))
            write_json(JOURNAL,journal)
            save_take(entry,'failed')
            print(json.dumps({'chapter':chapter_id,'status':'rejected','error':entry['error']}),flush=True)
            raise
        except Exception as error:
            entry.update(status='uncertain',error=client.safe(error))
            write_json(JOURNAL,journal)
            print(json.dumps({'chapter':chapter_id,'status':'uncertain','error':entry['error']}),flush=True)
            raise RuntimeError('Submission outcome uncertain; do not retry automatically.') from None
        task_id=response.get('id')
        if not task_id:
            entry.update(status='uncertain',error='Accepted response lacked task ID')
            write_json(JOURNAL,journal)
            raise RuntimeError('Submission returned no task ID; reconciliation required.')
        entry.update(task_id=task_id,status='accepted',accepted_at=now())
        write_json(JOURNAL,journal)
        save_take(entry,'processing')
        take_dir=ROOT/'chapters'/chapter_id/'takes'
        write_json(take_dir/(entry['take_id']+'-submission.json'),{k:v for k,v in entry.items() if k!='error'})
        print(json.dumps({'chapter':chapter_id,'status':'accepted','task_id':task_id,'duration':c['duration'],'reference_count':entry['reference_count']}),flush=True)

def poll_once(client,journal):
    pending=[e for e in journal['tasks'] if e.get('task_id') and e['status'] not in ('downloaded','failed','cancelled','expired','rejected')]
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures={pool.submit(client.poll,e['task_id']):e for e in pending}
        for future in as_completed(futures):
            entry=futures[future]
            try:
                response=future.result()
            except Exception as error:
                print(json.dumps({'chapter':entry['chapter_id'],'poll_error':client.safe(error)}),flush=True)
                continue
            state=response.get('status','unknown')
            if state!=entry['status']:
                print(json.dumps({'chapter':entry['chapter_id'],'status':state}),flush=True)
            entry['status']=state
            entry['last_polled_at']=now()
            write_json(JOURNAL,journal)
            if state=='succeeded':
                content=response.get('content',{})
                url=content.get('video_url')
                if not url:
                    raise RuntimeError('Succeeded task has no video URL.')
                take_dir=ROOT/'chapters'/entry['chapter_id']/'takes'
                path=take_dir/(entry['take_id']+'.mp4')
                if not path.exists():
                    client.download(url,path)
                if content.get('last_frame_url'):
                    frame=take_dir/(entry['take_id']+'-last-frame.jpg')
                    if not frame.exists():
                        client.download(content['last_frame_url'],frame)
                    entry['last_frame_path']=frame.relative_to(ROOT).as_posix()
                entry.update(status='downloaded',path=path.relative_to(ROOT).as_posix(),completed_at=now(),provider_metadata={k:response.get(k) for k in ('duration','ratio','resolution','framespersecond','usage','seed') if k in response})
                write_json(JOURNAL,journal)
                save_take(entry,'succeeded',path)
                print(json.dumps({'chapter':entry['chapter_id'],'status':'downloaded','bytes':path.stat().st_size}),flush=True)
            elif state in ('failed','cancelled','expired'):
                err=response.get('error',{})
                entry['error']=client.safe(json.dumps(err))
                write_json(JOURNAL,journal)
                save_take(entry,'failed')
                print(json.dumps({'chapter':entry['chapter_id'],'status':state,'error':entry['error']}),flush=True)
    counts={s:sum(e['status']==s for e in journal['tasks']) for s in set(e['status'] for e in journal['tasks'])}
    print(json.dumps({'summary':counts,'updated_at':now()}),flush=True)
    return any(e.get('task_id') and e['status'] not in ('downloaded','failed','cancelled','expired','rejected') for e in journal['tasks'])

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['submit','poll','watch','retry-failed'])
    parser.add_argument('--chapters',nargs='*')
    args=parser.parse_args()
    client=Client()
    print(json.dumps({'endpoint_resolution':client.resolve_endpoint()}),flush=True)
    client.authenticate()
    journal=json.loads(JOURNAL.read_text(encoding='utf-8')) if JOURNAL.exists() else {'project':'golden-star-five-friends','created_at':now(),'tasks':[]}
    if args.mode in ('submit','retry-failed'):
        if args.mode=='retry-failed' and not args.chapters:
            raise RuntimeError('Explicit chapter IDs required for confirmed failed retry.')
        wanted=args.chapters or [c['id'] for c in project()['chapters']]
        submit_chapters(client,journal,wanted,replace_reviewed=args.mode=='retry-failed')
    if args.mode in ('poll','watch'):
        while True:
            more=poll_once(client,journal)
            if args.mode=='poll' or not more:
                break
            time.sleep(30)

if __name__=='__main__':
    main()
