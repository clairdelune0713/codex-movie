"""Register inspected generated storyboard files as a new current-base proposal."""
import json
import hashlib
import shutil
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[1]
project = json.loads((root / 'project.json').read_text(encoding='utf-8'))
records = json.loads((root / 'exports/storyboard-results-r000002.json').read_text(encoding='utf-8'))
for record in records:
    chapter = next(c for c in project['chapters'] if c['id'] == record['chapter_id'])
    target = root / 'chapters' / chapter['id'] / 'storyboards' / (record['id'] + '.png')
    target.parent.mkdir(parents=True, exist_ok=True)
    if any(item['id'] == record['id'] for item in chapter['storyboards']):
        raise RuntimeError('Candidate ID already registered; use a new candidate ID.')
    if target.exists():
        if hashlib.sha256(target.read_bytes()).digest() != hashlib.sha256(Path(record['generated_source']).read_bytes()).digest():
            raise RuntimeError('Existing candidate differs; never overwrite media.')
    else:
        shutil.copy2(record['generated_source'], target)
    with Image.open(target) as img:
        img.load()
        dimensions = list(img.size)
    item = {key: value for key, value in record.items() if key not in ('generated_source', 'chapter_id')}
    item.update(path=target.relative_to(root).as_posix(), created_at=datetime.now(timezone.utc).isoformat(), dimensions=dimensions, tool='built-in image_gen')
    chapter['storyboards'].append(item)
    chapter['selected_storyboard_id'] = item['id']
    print(chapter['id'], dimensions, item['path'])
project['render_state']['completed_preparation'] = ['60-second timed screenplay', 'Both original puppy identity references', 'Generated empty garden reference', 'Generated ball reference', 'Six chapter storyboard candidates', 'Shot-level camera, sound and continuity directions']
project['render_state']['pending_stages'] = ['Video rendering', 'Original soundtrack generation or composition', 'Assembly and actual video verification']
(root / 'proposal-r000003.json').write_text(json.dumps(project, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
