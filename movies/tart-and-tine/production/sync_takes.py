"""Commit actual journaled Seedance task states through the Movi2 helper."""
import argparse
import importlib.util
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
helper_path=Path('C:/Users/admina/.codex/skills/movi2/scripts/project.py')
spec=importlib.util.spec_from_file_location('movi2_helper',helper_path)
helper=importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
parser=argparse.ArgumentParser()
parser.add_argument('--select-verified',action='store_true')
args=parser.parse_args()
current=helper.read(root/'project.json')
project=json.loads(json.dumps(current))
journal=helper.read(root/'exports/seedance-journal.json')
verifications={}
if args.select_verified:
    verifications={v['take_id']:v for v in helper.read(root/'exports/take-verification.json')}
for chapter in project['chapters']:
    item=journal['takes'].get(chapter['id'])
    if not item:
        continue
    take=dict(item,id=item['take_id'])
    if take['id'] in verifications:
        take['verification']=verifications[take['id']]
    index=next((i for i,t in enumerate(chapter['takes']) if t['id']==take['id']),None)
    if index is None:
        chapter['takes'].append(take)
    else:
        chapter['takes'][index]=take
    if args.select_verified and take['status']=='succeeded' and take['id'] in verifications:
        chapter['active_take_id']=take['id']
        chapter['screenshots']=[{'id':take['id']+f'_sample{i+1:02d}','path':path,'timestamp':timestamp,'source_take_id':take['id']} for i,(path,timestamp) in enumerate(zip(verifications[take['id']]['samples'],[0.25,3.25,6.25,9.5]))]
state=project['render_state']
state.update(status='rendering',integration='Direct Seedance 2.5 with verified base-project endpoint resolution',endpoint_resolution_path='exports/seedance-endpoint-resolution.json',generation_jobs_submitted=len(journal['takes']),video_takes_generated=sum(t['status']=='succeeded' for t in journal['takes'].values()),pending_stages=['Complete submitted Seedance tasks','Inspect actual clips and native audio','Assemble and verify 60-second 480p movie'])
if args.select_verified:
    state.update(status='takes_verified_awaiting_assembly',pending_stages=['Assemble and verify final movie'])
if (root/'exports/video-verification.json').exists():
    result=helper.read(root/'exports/video-verification.json')
    state.update(status='complete',actual_video_runtime_seconds=result['duration_seconds'],final_video_path=result['path'],verification_path='exports/video-verification.json',pending_stages=[])
project['source_text']+='\nRendering update: resolved the endpoint mismatch using the existing Seedance 2.5 endpoint in the named base credentials project; credential values unchanged.' if not any(t.get('task_id') for c in current['chapters'] for t in c['takes']) else ''
print(json.dumps(helper.save(root,current,project,'Record actual Seedance task states and selected verified media'),indent=2))
