from pathlib import Path
import json
from PIL import Image
ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
rough=json.loads((ROOT/'rough-scene-asset-plan.json').read_text(encoding='utf-8'))
for job in json.loads((ROOT/'state-asset-jobs.json').read_text(encoding='utf-8')):
    if not any(a['id']==job['id'] for a in p['asset_list']):
        p['asset_list'].append({'id':job['id'],'tag':'@'+job['id'],'name':job['name'],'category':job['category'],'description':job['description'],'source':'generated','media_type':'Image','reference_paths':job['reference_paths'],'candidates':[],'selected_candidate_id':None,'image_generation_prompt':job['prompt']})
rough['scene_11']=['adult-tine-training' if x=='adult-tine' else x for x in rough['scene_11']]
if 'adult-tine-training' not in rough['scene_13']: rough['scene_13'].append('adult-tine-training')
(ROOT/'rough-scene-asset-plan.json').write_text(json.dumps(rough,indent=2),encoding='utf-8')
for a in p['asset_list']:
    for meta in sorted((ROOT/'assets'/a['id']).glob('c*.json')):
        c=json.loads(meta.read_text(encoding='utf-8'))
        c['id']=meta.stem
        with Image.open(ROOT/c['path']) as im:
            c['actual_dimensions']=list(im.size)
        if not any(x['id']==c['id'] for x in a['candidates']): a['candidates'].append(c)
        a['selected_candidate_id']=c['id']
    if a['id'] in ['sir-squeaks-head','sir-squeaks-tail'] and (ROOT/'assets'/'sir-squeaks-whole'/'c01.png').exists():
        a['reference_paths']=['assets/sir-squeaks-whole/c01.png']
for c in p['chapters']:
    c['rough_asset_ids']=rough[c['id']]
p['production_stage']='asset_atelier'
(ROOT/'proposal.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
selected=sum(bool(a.get('selected_candidate_id')) for a in p['asset_list'])
print(json.dumps({'selected':selected,'total':len(p['asset_list']),'missing':[a['tag'] for a in p['asset_list'] if not a.get('selected_candidate_id')]}))
