import importlib.util
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / 'generated-image-manifest.json').read_text(encoding='utf-8'))
fingerprints = json.loads((ROOT / 'asset-generation-fingerprints.json').read_text(encoding='utf-8'))
p = json.loads((ROOT / 'project.json').read_text(encoding='utf-8'))
changed = []
for a in p['asset_list']:
    if a['source'] != 'generated' or a['id'] not in manifest:
        continue
    info = manifest[a['id']]
    cid = info.get('candidate_id', a['id']+'_c01')
    if any(c['id'] == cid for c in a['candidates']):
        continue
    src = Path(info['source_path'])
    if not src.is_file():
        raise FileNotFoundError(src)
    folder = ROOT / 'assets' / a['id']
    folder.mkdir(parents=True, exist_ok=True)
    dest = folder / (cid + '.png')
    if dest.exists():
        raise FileExistsError(dest)
    shutil.copy2(src, dest)
    with Image.open(dest) as im:
        im.verify()
    with Image.open(dest) as im:
        width, height = im.size
    a['candidates'].append({'id':cid, 'path':dest.relative_to(ROOT).as_posix(),
                            'prompt':info.get('prompt',a['generation_prompt']),
                            'reference_paths':info.get('reference_paths',a['reference_paths']),
                            'source_revision':info.get('source_revision',fingerprints[a['id']]['source_revision']),
                            'dependency_fingerprint':fingerprints[a['id']]['fingerprint'],
                            'created_at':datetime.now(timezone.utc).isoformat(),
                            'width':width,'height':height,'generator':'built-in image_gen'})
    a['selected_candidate_id'] = cid
    changed.append(a['id'])
p['production_stage'] = 'asset_visual_quality_check'
p['prompt_library_consulted'] = ['README.md','TEMPLATE.md','TAGS.md','INDEX.md',
    'shots/scene-01/15_a-man-and-a-woman-sit-facing-each-other-at-a-table.md',
    'shots/scene-01/23_a-woman-sits-at-a-table-in-a-small-apartment-holdi.md',
    'sections/09_dialogue.md']
p['chapters'][7]['scene_summary'] = p['chapters'][7]['scene_summary'].replace('开心','開心')
p['chapters'][18]['pacing_reason'] = '短句粵語對白留自然停頓；名字只在聲音中出現，不加文字。'
p['chapters'][-1]['scene_summary'] = p['chapters'][-1]['scene_summary'].replace('两犬','兩犬')
p['master_prompt_raw'] = p['master_prompt_raw'].replace('此阶段','此階段')
(ROOT / 'proposal.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'new_candidates':changed,'selected_generated':sum(bool(a['selected_candidate_id']) for a in p['asset_list'] if a['source']=='generated')},ensure_ascii=False))
