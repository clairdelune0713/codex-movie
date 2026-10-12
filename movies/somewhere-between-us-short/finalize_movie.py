"""Register only the fully assembled and reviewed separate movie."""
import copy, hashlib, importlib.util, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('h', 'C:/Users/admina/.codex/skills/movi2/scripts/project.py')
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)

p = h.read(ROOT / 'project.json')
j = h.read(ROOT / 'exports/seedance-journal.json')
v = h.read(ROOT / 'exports/video-verification.json')
review = h.read(ROOT / 'exports/visual-review/review-notes.json')
manifest = h.read(ROOT / 'exports/assembly-manifest.json')
assert v['passes'] and v['frame_count'] == 10560
assert v['resolution'] == [1680, 720] and v['duration_seconds'] == 352.0
assert h.review_state(ROOT, p)['ready']
assert j['project_id'] == p['id']
assert len(manifest['inputs']) == len(p['chapters']) == 30
for c, item in zip(p['chapters'], manifest['inputs']):
    t = j['takes'][c['id']]
    assert c['active_take_id'] == t['id'] == item['take_id']
    assert t['status'] == 'succeeded' and t['verification']['decode_verified']
    assert review['takes'][t['id']]['reviewed']
    assert not c.get('storyboards') and not c.get('selected_storyboard_id')
old = ROOT.parent / 'somewhere-between-us'
original = h.read(old / 'history/revision-000014.json')
current = h.read(old / 'project.json')
assert p['id'] != current['id']
for key in ('asset_list', 'chapters', 'render_state', 'detailed_script', 'output_profile'):
    assert original[key] == current[key], 'Original project changed: ' + key
final = ROOT / manifest['output']
assert final.is_file()
delivery = {
    'project_id': p['id'], 'path': manifest['output'],
    'sha256': hashlib.sha256(final.read_bytes()).hexdigest(),
    'duration_seconds': 352, 'resolution': [1680, 720], 'aspect_ratio': '21:9',
    'fps': 30, 'frame_count': 10560, 'audio': 'Stereo AAC, 48000 Hz',
    'original_project_preserved': True, 'titles': False, 'credits': False,
    'verification': 'Complete video/audio decode, frame count, duration, dimensions, motion samples, audio signal and loudness; visual sample review of all selected takes.',
    'limitation': 'Audio was technically inspected; listening and independent transcription were unavailable, so spoken Cantonese accuracy and musical continuity were not independently verified.'
}
h.atomic_write(ROOT / 'exports/delivery.json', delivery)
q = copy.deepcopy(p)
q['render_state'].update(status='complete', video_generation='complete', delivery='rendered',
    final_video_path=manifest['output'], video_takes_generated=30,
    generation_jobs_submitted=sum(bool(t.get('task_id')) + sum(bool(a.get('task_id')) for a in t.get('prior_takes', [])) for t in j['takes'].values()),
    verification_path='exports/video-verification.json', review_path='exports/visual-review/review-notes.json',
    audio_semantics_verified=False)
result = h.save(ROOT, p, q, 'Deliver separately rendered, visually reviewed 352-second movie; verify original project preservation')
print(json.dumps({'saved': result, 'delivery': delivery}, ensure_ascii=False))
