from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

root = Path(__file__).resolve().parent
source = Path('C:/Users/Admin 3/.codex/generated_images/01a1622d-9b0a-7443-8f67-be2f3a4ecde8/exec-711253f8-743d-412b-8e7f-1fc6fe6f6e1d.png')
relative = 'assets/hk_christmas_mall/mall_c02.png'
destination = root / relative
if destination.exists():
    raise RuntimeError('Immutable candidate already exists')
shutil.copy2(source, destination)
if hashlib.sha256(source.read_bytes()).digest() != hashlib.sha256(destination.read_bytes()).digest():
    raise RuntimeError('Reference copy mismatch')
project = json.loads((root / 'project.json').read_text(encoding='utf-8'))
edit = json.loads((root / 'mall-revision-v02.json').read_text(encoding='utf-8'))
asset = next(a for a in project['asset_list'] if a['id'] == 'hk_christmas_mall')
if project['revision'] != 3 or asset['description'] != edit['description']:
    raise RuntimeError('Unexpected source state')
fingerprint = '4c14b5198343c7a3ef67e1f3449c1ae1ccfa50a12062d59af13bc6990e8e87df'
created_at = datetime.now(timezone.utc).isoformat()
candidate = {
    'id': 'mall_c02', 'path': relative, 'prompt': edit['prompt'],
    'source_revision': 3, 'dependency_fingerprint': fingerprint,
    'created_at': created_at, 'input_reference_paths': [edit['edit_target']],
    'generation_method': 'built-in imagegen edit',
    'sha256': hashlib.sha256(destination.read_bytes()).hexdigest(),
    'inspection': 'Clear compact vertical Hong Kong retail atrium, layered storefronts, Traditional Chinese/English signs, bakery, cafe, escalator banks, festive tree and empty clear ground-floor route. No visible people or animals.'
}
try:
    from PIL import Image
    with Image.open(destination) as im:
        candidate['actual_dimensions'] = list(im.size)
except ImportError:
    pass
asset['candidates'].append(candidate)
asset['selected_candidate_id'] = candidate['id']
project['creative_decisions'].append('Mall revised to a compact vertical Hong Kong shopping environment with Traditional Chinese/English retail signage, bakery/cafe set dressing and crisscross escalators.')
(root / 'assets' / 'hk_christmas_mall' / 'mall_c02-metadata.json').write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(root / 'proposal-mall-v02-selection.json').write_text(json.dumps(project, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
manifest = []
for a in project['asset_list']:
    selected = next(c for c in a['candidates'] if c['id'] == a['selected_candidate_id'])
    manifest.append({'tag': a['tag'], 'candidate_id': selected['id'], 'path': selected['path'], 'sha256': hashlib.sha256((root / selected['path']).read_bytes()).hexdigest()})
(root / 'asset-manifest-v02.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'candidate': candidate['id'], 'path': str(destination), 'actual_dimensions': candidate.get('actual_dimensions')}, indent=2))
