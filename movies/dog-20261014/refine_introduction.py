"""Use approved collar/lead state for the indoor bond, before active guide work."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as h
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=json.loads(json.dumps(p))
c=next(c for c in q['chapters'] if c['id']=='s02_c03')
oldrole=c['reference_roles']['@TartWorking']
newrole='ONE cream Labrador Tart in an indoor bonding/familiarisation session, brown collar with separate brown collar lead held loosely by Ah Ming. Four paws on the ROOM FLOOR beside his knee, never on a chair. No working harness during this first familiarisation; active guide work is in later scenes.'
c['tagged_assets']=['@TartOffDuty' if x=='@TartWorking' else x for x in c['tagged_assets']]
c['linked_asset_ids']=['asset_tart_off_duty' if x=='asset_tart_working' else x for x in c['linked_asset_ids']]
c['reference_roles'].pop('@TartWorking');c['reference_roles']['@TartOffDuty']=newrole
c['prompt']=c['initial_prompt'].replace('@TartWorking','@TartOffDuty').replace(oldrole,newrole)
oldfirst=c['first_frame']
c['first_frame']='Ah Ming sits in the blue chair, hand lowered beside his LEFT knee. Tart stands with all FOUR PAWS ON THE FLOOR at his left knee, cream dog head below seated man chest height. Brown collar and loosely held brown collar lead only; no guide harness. The chair beside him is empty.'
c['prompt']=c['prompt'].replace(oldfirst,c['first_frame'])
lock='''INDOOR FAMILIARISATION — BEFORE ACTIVE GUIDE WORK
First half: only cream Tart and Ah Ming. The dog stands on the floor at knee height; Ah Ming is seated above him, never seated level with a dog on a chair. Collar and brown lead are the approved indoor familiarisation state. A later short indoor heel-training insert shows them taking a few side-by-side steps on a clear straight familiar practice-room floor under staff supervision; this is bonding, not public guide navigation. No guide harness in this introduction. Second half after the clean cut: only May and brown Tine, orange lead held by May; Tine briefly tries the lap then returns to floor and rests chin on knee. Keep source actions and identities, never switch dogs or handlers.
'''
c['prompt']=c['prompt'].replace('ACTIVE REFERENCES\n',lock+'\nACTIVE REFERENCES\n',1)
c['location_map']+=' First greeting is a collar/lead indoor familiarisation before active guide work; dog stays on floor.'
c.setdefault('prompt_refinements',[]).append({'reason':'Two generated training introductions added an extra lead to harness. The source does not require the working harness during first indoor bonding, so use existing approved collar/lead state and explicit floor height; public guide scenes retain harness-only controls.'})
q.setdefault('script_changes',[]).append({'scene':2,'scope':'Minor visual production adaptation only','change':'First indoor handler familiarisation uses approved collar-and-lead Tart, without working harness. The short supervised shared-pace insert remains indoors. Original actions/dialogue/timing unchanged; all public guide work still uses rigid harness handle without collar lead.'})
for future in q['chapters']:
    if future['chapter_index']<14 or '@TartWorking' not in future['tagged_assets']:continue
    grip='''VISIBLE GUIDE-HANDLE CONTACT
Whenever the working pair travels, Ah Ming LEFT hand visibly wraps the brown horizontal cross-grip of the rigid SILVER TWO-ARM GUIDE FRAME attached to Tart body harness. The collar D-ring is empty while the harness is ON. During stationary phone/recording/rest the rigid bar may rest; there is no flexible line emerging from his hand or dog collar. Flexible brown collar lead stays packed until the explicitly timed harness-OFF reunion transition, when the separate brown lead is correctly clipped on. This is literal solid-metal-to-hand contact, not a loop or thin cord.
'''
    future['prompt']=future['prompt'].replace('ACTIVE REFERENCES\n',grip+'\nACTIVE REFERENCES\n',1)
print(h.save(ROOT,p,q,'Keep first indoor bond in approved collar state and specify public guide-handle contact'))
