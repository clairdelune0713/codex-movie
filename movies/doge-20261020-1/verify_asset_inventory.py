from pathlib import Path
from PIL import Image
import hashlib,json
ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
source=json.loads((ROOT/'source'/'manifest.json').read_text(encoding='utf-8'))
checks=[]
for item in source:
    archived=ROOT/'source'/item['path']
    original=ROOT.parents[1]/'doge-material'/item['path']
    assert hashlib.sha256(archived.read_bytes()).hexdigest()==item['sha256']
    assert hashlib.sha256(original.read_bytes()).hexdigest()==item['sha256']
known={a['id'] for a in p['asset_list']}; used=set()
for a in p['asset_list']:
    c=next(c for c in a['candidates'] if c['id']==a['selected_candidate_id'])
    path=ROOT/c['path']
    with Image.open(path) as im:
        dimensions=list(im.size);format=im.format; im.verify()
    checks.append({'tag':a['tag'],'candidate_id':c['id'],'path':c['path'],'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'dimensions':dimensions,'format':format,'decodable':True})
for c in p['chapters']:
    assert set(c['rough_asset_ids']) <= known
    used.update(c['rough_asset_ids'])
    assert c['source_shots'][0]['start']==0
    assert c['source_shots'][-1]['end']==c['duration']
    assert all(a['end']==b['start'] for a,b in zip(c['source_shots'],c['source_shots'][1:]))
assert used<=known
j=json.loads((ROOT/'exports/task-journal.json').read_text(encoding='utf-8')) if (ROOT/'exports/task-journal.json').exists() else {'takes':{}}
report={'project_revision':p['revision'],'source_files_unchanged':len(source),'selected_assets':len(checks),'source_design_definitions':sum(a['source']=='user-supplied' for a in p['asset_list']),'generated_asset_definitions':sum(a['source']=='generated' for a in p['asset_list']),'active_scene_count':len(p['chapters']),'source_shot_count':sum(len(c['source_shots']) for c in p['chapters']),'runtime_seconds':sum(c['duration'] for c in p['chapters']),'optimized_video_prompts':sum(bool(c['prompt']) for c in p['chapters']),'accepted_video_tasks':sum(bool(t.get('task_id')) for t in j['takes'].values()),'checks':checks}
(ROOT/'exports'/'asset-inventory-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},indent=2))
