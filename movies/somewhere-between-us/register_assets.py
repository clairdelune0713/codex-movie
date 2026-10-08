import json,shutil,importlib.util
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('movi2','C:/Users/admina/.codex/skills/movi2/scripts/project.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
p=h.read(ROOT/'project.json');proposal=json.loads(json.dumps(p));manifest=h.read(ROOT/'exports/asset-generation.json')+h.read(ROOT/'exports/asset-generation-locations.json');changed=[]
if (ROOT/'exports/asset-generation-humans-v02.json').exists():manifest+=h.read(ROOT/'exports/asset-generation-humans-v02.json')
for entry in manifest:
    a=next(a for a in proposal['asset_list'] if a['id']=='asset_'+entry['id'])
    cid=entry.get('candidate_id',entry['id']+'_c01')
    if any(c['id']==cid for c in a['candidates']):continue
    target=ROOT/'assets'/a['id']/(cid+'.png');target.parent.mkdir(parents=True,exist_ok=True)
    if not target.exists():shutil.copy2(entry['generated_file'],target)
    with Image.open(target) as im:im.load();dims=list(im.size)
    a['candidates'].append({'id':cid,'path':target.relative_to(ROOT).as_posix(),'prompt':entry['prompt'],'created_at':entry['created_at'],'dimensions':dims,'tool':'built-in image_gen','dependency_note':'Created from the user brief and recorded exact prompt; no retroactive dependency fingerprint assigned.'})
    a['selected_candidate_id']=cid;changed.append(entry['id'])
if changed:
    result=h.save(ROOT,p,proposal,'Select generated supporting character and environment identity references')
    print('Committed revision',result['revision'],'selected',changed,'remaining reference warnings',len(result['warnings']))
else:print('No new candidates')
