"""Commit a narrow director correction after inspecting scene37 take02."""
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=json.loads(json.dumps(p))
lock='Adult dogs in the harbour stay on the PAVED GROUND at all times: all four paws on pavement when standing, haunches on pavement when seated. The wooden bench seat is for humans and the removed harness only. Tart sits ON THE GROUND beside Leung\'s left shoe, never on the bench, never climbing onto furniture. Preserve one ordinary curved guide-harness handle; no extra ring handles or added leashes while working.'
for c in q['chapters']:
    if c['source_scene_number']>49:continue
    if lock not in c['prompt']:c['prompt']+='\nFLOOR-LEVEL STAGING LOCK\n'+lock+'\n'
    if c['source_scene_number']==37:
        c['prompt']=c['prompt'].replace('Tart at left knee.','Tart seated on the PAVED GROUND at Leung\'s left shoe, below the bench seat.')
q['stage']='chapter_director';q['render_status']='rendering'
print(helper.save(ROOT,p,q,'Correct inspected harbour dog placement: dogs stay on pavement beside the human bench'))
j=json.loads((ROOT/'exports/task-journal.json').read_text(encoding='utf-8'));t=j['takes']['scene_37'];src=ROOT/t['path']
reviews={'scene_37':{'take_id':t['id'],'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'inspected':True,'requires_repair':True,'notes':'All sampled shots inspected. Warm original animation, human sunglasses and held leads present, captain/passengers appear as small ferry figures. At 13-16s Tart is incorrectly seated on bench; retake with explicit pavement staging. Audio stream verified technically; dialogue not independently transcribed.'}}
(ROOT/'exports/visual-reviews.json').write_text(json.dumps(reviews,indent=2),encoding='utf-8')
