"""After explicit approval, permit one genuinely changed compliant animation request.

This is not provider clearance. Normal provider filtering remains enabled.
"""
from pathlib import Path
import json,sys,hashlib
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
if not helper.review_state(ROOT,p).get('ready'):raise RuntimeError('Revised actual image set must have explicit human approval first')
j=json.loads((ROOT/'exports/task-journal.json').read_text(encoding='utf-8'))
t=j['takes']['scene_37']
if t.get('task_id') or t.get('error',{}).get('code')!='InputImageSensitiveContentDetected.PrivacyInformation':raise RuntimeError('Resolution applies only to the recorded rejected image-input request')
jobs=json.loads((ROOT/'toon-revision-jobs.json').read_text(encoding='utf-8'));asset_ids=[x['id'] for x in jobs]
assets={a['id']:a for a in p['asset_list']}
changed=[b['asset_id'] for b in t['bindings'] if b.get('asset_id') in asset_ids and hashlib.sha256((ROOT/helper.selected_media(assets[b['asset_id']])['path']).read_bytes()).hexdigest()!=b['sha256']]
if not changed:raise RuntimeError('Refuse identical resubmission; no reviewed image bytes changed')
q=json.loads(json.dumps(p));q['provider_review_required']=False
q['input_rejection_resolution']={'kind':'compliant_animation_reference_revision','covered_prior_attempt_ids':[t['attempt_id']],'revised_asset_ids':asset_ids,'approved_review_id':p['asset_review']['id'],'provider_clearance_claimed':False,'normal_provider_filtering_enabled':True,'reason':'Genuinely revised, visibly stylized fictional animation references were reviewed and explicitly approved. Submit a new changed request through the same public API; do not disable filtering or use private assets.'}
q['production_stage']='ready_for_new_animation_input_request'
print(helper.save(ROOT,p,q,'Resume only after human approval of genuinely changed original animation references; provider filtering remains enabled'))
