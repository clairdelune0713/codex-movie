import importlib.util
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
helper = Path('C:/Users/admina/.codex/skills/movi2/scripts/project.py')
spec = importlib.util.spec_from_file_location('movi2_project', helper)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
project = json.loads((root / 'project.json').read_text(encoding='utf-8'))
references = [str(root / a['candidates'][0]['path']) for a in project['asset_list']]
records = []
for chapter in project['chapters']:
    panels = [s['action'] + ' Framing: ' + s['camera'] for s in chapter['shots']]
    panels.append(chapter['shots'][-1]['end_state'] + ' Final beat of the chapter; emotional eye acting, same geography and props.')
    prompt = f"Use case: illustration-story. Asset type: cinematic chapter storyboard for a 60-second movie, {chapter['title']}, movie seconds {chapter['movie_start']}-{chapter['movie_end']}. Primary request: Generate one 2x2 storyboard canvas, four equal wide rectangular cinematic panels touching seamlessly, read left-to-right then top-to-bottom. Overall canvas near 16:9; each panel cinematic and wide. NO outer frame, gutters, divider lines, text, captions, panel numbers, subtitles, speech bubbles or watermarks.\nInput images: Image 1 supplies ONLY Tart identity and orange training vest, beige puppy. Image 2 supplies ONLY Tine identity and orange vest, brown puppy with pale heart-shaped patch on right rear haunch. Each sheet is three views of ONE dog; never put multiple copies of one dog into a scene. Image 3 is the environment geometry and lighting reference: same low wooden bridge, dry gravel bed, near ramp left, far ramp right, daisies beside far ramp, rounded oak farther right. Image 4 supplies ONLY the small sky-blue ball with its single cream stripe; keep it small relative to puppies, approximately paw-sized, not gigantic.\nStyle: Warm whimsical feature-film CGI like Up, rounded shapes, charming expressive eyes, soft tactile fur, colorful teal foliage and honey light. Match the supplied dog designs. Orange gray-edged training vests with blue round patches remain; do not add narrative text. Same late-afternoon sun from upper left, same yard, no weather or time changes.\nStarting geography: {chapter['handoff']['entry']}\n" + '\n'.join(f"Panel {i}: {description}" for i, description in enumerate(panels, 1)) + "\nContinuity: exactly one beige Tart and one brown Tine whenever both are visible; a close-up may show only the named subject. Four paws per dog, anatomically plausible motion, no morphing, no floating objects. Travel left to right except Tine's motivated return right to left. No water or dangerous height beneath bridge. Warm emotional visual storytelling, no anthropomorphic hands, no franchise characters. The @tags above are metadata and must NOT appear as text in the raster."
    records.append({'chapter_id': chapter['id'], 'id': chapter['id'] + '_sb01', 'grid': '2x2', 'panel_descriptions': panels, 'prompt': prompt, 'reference_paths': [str(Path(p).relative_to(root)).replace('\\', '/') for p in references], 'source_revision': project['revision'], 'dependency_fingerprint': module.chapter_fingerprint(root, project, chapter)})
(root / 'exports/storyboard-submissions-r000002.json').write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'records': records, 'absolute_references': references}, ensure_ascii=False))
