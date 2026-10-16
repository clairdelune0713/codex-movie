"""Refine only the observed bad working-gear takes; no selected image changes."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as h
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=json.loads(json.dumps(p))
for c in q['chapters']:
    if c['id'] not in ('s02_c03','s03_c03','s03_c04'):continue
    lock='''OBSERVED ERROR REPAIR — RIGID HANDLE AND HAND OWNERSHIP
The cream dog is a working GUIDE dog. His brown collar has an EMPTY D-ring. The ONLY connection used for guiding is the two-arm SILVER METAL GUIDE HANDLE fixed to the brown body harness. A hand grips the brown horizontal crossbar on that rigid metal frame. Draw and animate that visible solid contact literally. No thin flexible line, loop or cord connects handler hand to the cream dog's collar; no flexible line dangles from the hand. All flexible walking leads are packed inside the CLOSED navy bag in cream-dog scenes. Only brown Tine, when explicitly present in his own part, has an orange flexible collar lead held by May. Gear never transfers across cuts.
'''
    if c['id']=='s03_c03':
        lock+='The recess is a clear patch of public pavement inland of the kerb. No takeaway cup, drink, glass, loose lead or object is on the ground. Right hand holds the compact recorder. Left hand lightly rests on the top of the harness beside the solid guide bar during stationary recording, then closes around its brown cross-grip after the recorder is packed.\n'
    if c['id']=='s03_c04':
        lock+='At frame zero left hand rests on the solid guide-handle brown cross-grip; right hand takes phone only while stationary. Phone goes back inside bag before turning for onward travel. At the cafe both hands are free of flexible lines; Tart collar ring remains empty.\n'
    if c['id']=='s02_c03':
        lock+='First nine seconds only cream Tart and Ah Ming, no brown dog, no orange object/line. Seated greeting then walking insert with left hand around the solid guide bar. After the clean cut, second nine seconds only May and brown Tine, orange collar lead belonging to this brown dog only.\n'
    c['prompt']=c['prompt'].replace('ACTIVE REFERENCES\n',lock+'\nACTIVE REFERENCES\n',1)
    c.setdefault('prompt_refinements',[]).append({'reason':'Visible collar-lead error in actual first take; explicit solid-handle grip and packed flexible leads.','replaces_take':'take_01'})
print(h.save(ROOT,p,q,'Repair observed flexible leads on three working Tart takes'))
