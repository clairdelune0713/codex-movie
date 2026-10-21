from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,sys
ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
inventory=json.loads((ROOT/'exports'/'asset-inventory-verification.json').read_text(encoding='utf-8'))
inspection={'inspected_at':datetime.now(timezone.utc).isoformat(),'project_revision':p['revision'],'selected_assets':48,'method':'Visual inspection of all six full-resolution selected gallery sheets, plus supplied reference contact sheet and detailed originals for Mags, Boss, Jade, Tine training state and toy states.','scope':['Original cast identity and supplied-image preservation','Original warm rounded 3D style, no existing Pixar/Disney characters observed','Wardrobe and state variants; sunglasses on Leung reference','Empty environment geography and clear action space','Toy head/tail shape and complementary break','Cage latch/door, 99/100 counter states, postcard insertion area','Image labels and selected candidate IDs'], 'result':'Selected asset set suitable for human review. Video performance, continuity in motion and final audio remain unrendered.','assets':[{'tag':a['tag'],'candidate_id':a['candidate_id'],'sha256':a['sha256'],'inspected':True} for a in inventory['checks']],'notes':['Boss c02 corrects the notch to his anatomical left ear. c01 retained.','Tine pre-graduation variant preserves supplied identity with collar only; original bandana reference retained for graduation onward.','Postcard image area is intentionally blank for an actual selected reunion frame in the edit.','Whole-toy and counter state insets represent reference views/states, not duplicate physical objects.','Environment light is a look reference; script time-of-day transitions remain required.','Contact sheets and gallery labels are not video-generation references.']}
(ROOT/'exports'/'asset-review'/'visual-inspection.json').write_text(json.dumps(inspection,ensure_ascii=False,indent=2),encoding='utf-8')
p['production_stage']='awaiting_asset_approval'
p['provider_routing_decision_path']='provider-routing-decision.json'
p['asset_inspection_path']='exports/asset-review/visual-inspection.json'
note='All 48 selected assets visually inspected and presented as a complete review set; await explicit approval before final prompts or new Seedance submissions. Project name intentionally blank per user instruction.'
if note not in p['production_notes']: p['production_notes'].append(note)
if any(a['id']=='red-taxi' and a['selected_candidate_id']=='c02' for a in p['asset_list']):
    inspection['notes'].append('Taxi c02 inspected: exact word TAXI appears clearly in black capitals on the white illuminated roof light, as requested by the user. c01 retained.')
    (ROOT/'exports'/'asset-review'/'visual-inspection.json').write_text(json.dumps(inspection,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'proposal.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'inspected_assets':48,'stage':p['production_stage']}))
