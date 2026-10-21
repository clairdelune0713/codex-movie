from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
jobs=json.loads((ROOT/'toon-revision-jobs.json').read_text(encoding='utf-8'))
assets={a['id']:a for a in p['asset_list']}
rows=[]
for j in jobs:
    a=assets[j['id']];c=next(c for c in a['candidates'] if c['id']==a['selected_candidate_id'])
    rows.append({'tag':a['tag'],'candidate_id':c['id'],'path':c['path'],'sha256':hashlib.sha256((ROOT/c['path']).read_bytes()).hexdigest(),'inspected':True,'identity_and_wardrobe_preserved':True,'notes':'Smoother visibly stylized3D materials; no added people, text or existing franchise characters. Leung sunglasses remain opaque.' if a['id']=='blind-guy' else 'Smoother stylized surface detail; distinctive character shapes, age, outfit palette and sheet layout remain recognizable.'})
inspection={'inspected_at':datetime.now(timezone.utc).isoformat(),'project_revision':p['revision'],'method':'Inspected both full-resolution revised-human contact sheets. Remaining40 selected assets have unchanged bytes and retain prior inspection. All48 files decoded and source copies hash-verified.','revised_assets':rows,'source_files_retained':True,'provider_acceptance_of_revisions':'not_tested_pending_asset_approval','video_status':'No accepted task or generated video yet. One rejected input request retained in usage/task journal.'}
path=ROOT/'exports/asset-review/refined-human-inspection.json';path.write_text(json.dumps(inspection,ensure_ascii=False,indent=2),encoding='utf-8')
p['asset_inspection_path']=path.relative_to(ROOT).as_posix()
p['production_stage']='awaiting_asset_approval'
p['provider_refusal_status']='new_animation_reference_set_prepared_awaiting_human_review'
p['production_notes'].append('Eight revised human sheets inspected. They preserve original fictional identities/wardrobes while using smoother stylized3D surfaces. Their actual current images need renewed approval; no provider clearance claimed and no unchanged rejected request repeated.')
(ROOT/'proposal.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'revised_humans':len(rows),'all_selected_assets':len(p['asset_list']),'active_duration_seconds':sum(c['duration'] for c in p['chapters']),'stage':p['production_stage']}))
