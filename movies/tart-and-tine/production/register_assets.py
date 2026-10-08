import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[1]
project = json.loads((root / 'project.json').read_text(encoding='utf-8'))
records = json.loads((root / 'exports/asset-generation-r000001.json').read_text(encoding='utf-8'))
for record in records:
    name = record['name']
    asset = next(a for a in project['asset_list'] if a['id'] == 'asset_' + name)
    target = root / 'assets' / asset['id'] / (name + '_c01.png')
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise RuntimeError('Candidate already exists; register a new version instead.')
    shutil.copy2(record['generated_source'], target)
    with Image.open(target) as img:
        img.load()
        dimensions = list(img.size)
    candidate = {'id': name + '_c01', 'path': target.relative_to(root).as_posix(), 'prompt': record['prompt'], 'source_revision': record['source_revision'], 'dependency_fingerprint': record['dependency_fingerprint'], 'created_at': datetime.now(timezone.utc).isoformat(), 'dimensions': dimensions, 'tool': 'built-in image_gen', 'inspection': 'Decoded and visually inspected. Garden: empty, bridge/daisies/oak readable, dry bed, warm light. Ball: one blue sphere, cream stripe, neutral background.'}
    asset['candidates'].append(candidate)
    asset['selected_candidate_id'] = candidate['id']
    print(name, dimensions, candidate['path'])
(root / 'proposal-r000002.json').write_text(json.dumps(project, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
