"""Record verified delivery via the Movi2 revision helper."""
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
HELPER=Path('C:/Users/admina/.codex/skills/movi2/scripts/project.py')
def load(path): return json.loads(path.read_text(encoding='utf-8-sig'))
def write(path,value): path.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')

p=load(ROOT/'project.json')
v=load(ROOT/'exports/video-verification.json')
j=load(ROOT/'exports/task-journal.json')['tasks']
assert len(j)==24 and len({t['task_id'] for t in j.values()})==24
assert all(t['status']=='succeeded' and (ROOT/t['path']).is_file() for t in j.values())
assert all(c['active_take_id'] and len(c['screenshots'])==3 for c in p['chapters'])
assert v['decode_ok'] and v['decoded_frames']==11700 and v['duration']==390
assert (v['width'],v['height'],v['fps'])==(1470,630,30)
p['production_stage']='delivered'
p['final_video_path']=v['path']
p['delivery']={'verification':v,'verification_path':'exports/video-verification.json',
               'assembly_manifest_path':'exports/assembly-manifest.json',
               'visual_review':{'chapters_sampled':24,'samples_per_chapter':3,
                 'review_scope':'Identity, style, costume states, blocking, and obvious visual defects in sampled frames',
                 'limitations':'Sampled frame inspection; dialogue transcription and frame-by-frame animation audit not performed'},
               'provider_jobs':24,'duplicate_jobs':0}
proposal=ROOT/'delivery-proposal.json'
write(proposal,p)
for args in [('check','--from',str(proposal)),('commit','--from',str(proposal),'--reason','Deliver fully rendered and verified 6 minute 30 second movie')]:
    proc=subprocess.run([sys.executable,str(HELPER),args[0],str(ROOT),*args[1:]],capture_output=True,text=True,encoding='utf-8')
    if proc.returncode: raise ValueError(proc.stdout+proc.stderr)
    print(proc.stdout)
proc=subprocess.run([sys.executable,str(HELPER),'status',str(ROOT)],capture_output=True,text=True,encoding='utf-8')
report=json.loads(proc.stdout)
write(ROOT/'exports/final-project-check.json',report)
assert not report['errors'] and not report['warnings']
assert all(a['freshness']=='current' for a in report['artifacts'] if a['kind']=='takes')
print(json.dumps({'delivered':v['path'],'duration':v['duration'],'resolution':[v['width'],v['height']],
                  'fps':v['fps'],'decoded_frames':v['decoded_frames'],'project_errors':report['errors']}))
