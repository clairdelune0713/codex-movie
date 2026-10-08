"""Write a truthful delivery specification and verify existing raster artifacts."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[1]
project = json.loads((root / 'project.json').read_text(encoding='utf-8'))
shots = []
for chapter in project['chapters']:
    for index, shot in enumerate(chapter['shots'], 1):
        start = chapter['movie_start'] + shot['start']
        end = chapter['movie_start'] + shot['end']
        shots.append({'chapter_id': chapter['id'], 'shot_index': index, 'movie_start_seconds': start, 'movie_end_seconds': end, 'start_frame': start*30, 'end_frame_exclusive': end*30, 'action': shot['action'], 'camera': shot['camera'], 'audio_direction': shot['audio'], 'end_state': shot['end_state']})
assert shots[0]['start_frame'] == 0 and shots[-1]['end_frame_exclusive'] == 1800
assert all(a['end_frame_exclusive'] == b['start_frame'] for a, b in zip(shots, shots[1:]))
rasters = []
for filename in sorted(root.rglob('*.png')):
    with Image.open(filename) as image:
        image.load()
        dimensions = list(image.size)
        mode = image.mode
    rasters.append({'path': filename.relative_to(root).as_posix(), 'dimensions': dimensions, 'mode': mode, 'decoded': True, 'sha256': hashlib.sha256(filename.read_bytes()).hexdigest()})
spec = {'project_name': project['project_name'], 'source_revision': project['revision'], 'status': 'prepared_awaiting_video_renderer', 'desired_output_filename': 'tart-and-tine-60s.mp4', 'output_goals': {'duration_seconds': 60.0, 'resolution': [1920, 1080], 'aspect_ratio': '16:9', 'fps': 30, 'frame_count': 1800, 'audio_channels': 2, 'audio_sample_rate': 48000, 'transitions': 'Hard cuts, no runtime-changing crossfades'}, 'actual_video': None, 'generated_video_takes': 0, 'generated_audio_tracks': 0, 'storyboard_note': 'Static concept images with four panels per chapter; not animated video and not a verified first/last frame. Source sheets remain the canonical character identity anchors.', 'pending_stages': project['render_state']['pending_stages'], 'shot_ledger': shots, 'continuity_review': ['Single enclosed garden and one consistent late-afternoon light state throughout', 'Near bridge ramp screen-left; far ramp screen-right; daisies immediately far-side; oak beyond', 'The blue ball rolls visibly, then stays at far-side daisies during Tine’s return and the shared bridge crossing', 'Tine returns right-to-left before both puppies cross left-to-right; camera remains on one side of action axis', 'Tart remains beige; Tine remains brown with pale right rear heart patch; vests consistent', 'Reference sheet duplicate views must not become extra on-screen dogs', 'Six times 10 seconds; every chapter has consecutive 3, 3, 4-second shots', 'No dialogue; original score and scene Foley remain directions pending audio production'], 'raster_verification': rasters, 'verified_at': datetime.now(timezone.utc).isoformat(), 'verification_scope': 'Planned timeline, file existence, raster decoding and hashes. No video duration, motion, audio or decode verification is possible before rendering.'}
spec['status'] = project['render_state']['status']
spec['output_goals'].update(project.get('output_profile', {}))
(root / 'exports/delivery-specification.json').write_text(json.dumps(spec, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'planned_seconds': 60, 'planned_frames': 1800, 'shots': len(shots), 'rasters_decoded': len(rasters), 'actual_video': None}))
