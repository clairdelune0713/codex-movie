from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parent.parent
prep = json.loads((ROOT / 'asset-preparation.json').read_text(encoding='utf-8'))
project = json.loads((ROOT / 'project.json').read_text(encoding='utf-8'))
now = datetime.now(timezone.utc).isoformat()
source = '''use [$movi2](<C:\\Users\\Admin 3\\.codex\\skills\\movi2\\SKILL.md>) to generate a 30s 16:9 video. it should be a single generation of 30s, instead of merging multiple ones.
project name: xmas-01 (do not reference other projects)
existing character assets are in xmas-material/ (no need to generate any other characters)
the high level idea is:

ccbug-xmas , kooloo-xmas and louis-xmas are shopping in hong kong mall for preparing a Christmas party.
make it a adventurous journey and fun.

style: Minions 3D cartoon animation [do not include any existing ip in the video]
note:  kooloo-xmas is half the height of the louis-xmas and the ccbug-xmas is 1/3 size of kooloo-xmas
make the clip fun, fast-pacing, hilarious,'''
(ROOT / 'source').mkdir(exist_ok=True)
(ROOT / 'source' / 'user-request.txt').write_text(source, encoding='utf-8')

definitions = [
    ('louis_xmas', '@louis-xmas', 'louis-xmas', 'character', WORKSPACE / 'xmas-material' / 'louis-xmas.jpeg', 'louis_xmas_supplied01', 'Supplied original Louis: tall pointed-eared character, slick black hair with one antenna, thick eyebrows, pink gold-rim glasses, red/green knitted Christmas sweater with black cat motif, black boots. Preserve supplied identity and costume. Overall height 6 scale units. Sweater cat graphic stays a flat motif, never another character.', None),
    ('kooloo_xmas', '@kooloo-xmas', 'kooloo-xmas', 'character', WORKSPACE / 'xmas-material' / 'kooloo-xmas.jpeg', 'kooloo_xmas_supplied01', 'Supplied original charcoal cat with yellow eyes, glowing orange forehead mark, brown reindeer antler headband, brown collar with gold bells and red-tipped tail. Preserve cat anatomy and supplied appearance. Overall standing height including antlers 3 scale units, exactly half Louis.', None),
    ('ccbug_xmas', '@ccbug-xmas', 'ccbug-xmas', 'character', WORKSPACE / 'xmas-material' / 'ccbug-xmas.jpeg', 'ccbug_xmas_supplied01', 'Use only the CENTER RED character in the supplied three-variant reference: one living tiny translucent red glitter ornament creature with black dot eyes, curled feelers, small rounded feet, a green/gold wavy decorative band and rose-gold cap/loop. The pink side variants are alternatives and MUST NOT appear. Overall height 1 scale unit: one third Kooloo and one sixth Louis. No new humanoid arms, fingers or face redesign.', None),
    ('hk_christmas_mall', '@hk-christmas-mall', 'Hong Kong Christmas mall', 'environment', Path(prep['mall_source']), 'mall_c01', 'Empty multilevel Hong Kong luxury mall at Christmas: rounded balconies, glass balustrades, wide flat cream terrazzo concourse, tree at far end, escalators at right, harbour skyline through rear window, warm golden lights and red/green garlands. Reference guides layout and illumination; render the final setting in playful rounded 3D animation. No added people, animals or character mascots.', prep['mall_prompt']),
    ('party_trolley', '@party-trolley', 'Christmas shopping trolley and party supplies', 'prop', Path(prep['trolley_source']), 'trolley_c01', 'One chrome shopping trolley with red handle and four black caster wheels, low rear axle bar, loaded red/green wrapped party supplies, broad red ribbon spool with trailing end and one oversized gold five-point tree-topper star. Preserve trolley construction and ribbon/star states through action. In movie scale the trolley handle is at Louis waist; supplied studio image supplies design rather than absolute scale.', prep['trolley_prompt']),
]
assets = []
manifest = []
for asset_id, tag, name, category, src, candidate_id, description, prompt in definitions:
    folder = ROOT / 'assets' / asset_id
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / (candidate_id + src.suffix.lower())
    if not destination.exists():
        shutil.copy2(src, destination)
    if hashlib.sha256(src.read_bytes()).digest() != hashlib.sha256(destination.read_bytes()).digest():
        raise RuntimeError('Copy mismatch: ' + asset_id)
    relative = destination.relative_to(ROOT).as_posix()
    generated = prompt is not None
    candidate = {'id': candidate_id, 'path': relative, 'prompt': prompt or 'Unmodified user-supplied reference; no image generation.', 'source_revision': project['revision'], 'created_at': now}
    provenance = {'source': 'built-in imagegen' if generated else 'user-supplied xmas-material', 'original_filename': src.name, 'sha256': hashlib.sha256(destination.read_bytes()).hexdigest(), 'prompt': candidate['prompt'], 'input_reference_paths': [], 'requested_style': 'Original glossy playful rounded 3D feature animation; no existing entertainment IP', 'source_revision': project['revision']}
    try:
        from PIL import Image
        with Image.open(destination) as im:
            provenance['actual_dimensions'] = list(im.size)
            candidate['actual_dimensions'] = list(im.size)
    except ImportError:
        pass
    (folder / (candidate_id + '-metadata.json')).write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    assets.append({'id': asset_id, 'tag': tag, 'name': name, 'category': category, 'description': description, 'source': 'generated' if generated else 'supplied', 'media_type': 'Image', 'reference_paths': [], 'status_variants': [], 'candidates': [candidate], 'selected_candidate_id': candidate_id})
    manifest.append({'tag': tag, 'candidate_id': candidate_id, 'path': relative, 'sha256': provenance['sha256']})

idea = 'Three differently sized original Christmas friends shop for party supplies in a Hong Kong mall; a runaway trolley turns shopping into a fast, hilarious miniature adventure, ending in teamwork and an enormous accidental ribbon bow.'
rough_script = '''ROUGH STORY PLAN FOR ASSET REVIEW — final director prompt waits for approval.
0-4s: Clear same-ground-plane group reveal establishes Louis : Kooloo : ccbug = 6 : 3 : 1. Louis pushes the party trolley; Kooloo trots beside him; ccbug rides the basket rim.
4-9s: Kooloo bats the dangling ribbon, springing the trolley forward; Louis lunges after it and lands with one boot on the low rear bar. The party-supply shopping trip becomes a chaotic ride.
9-17s: Brisk ground-floor trolley chase with close calls around gift displays. Louis scrambles at the handle, Kooloo runs alongside with jingling bells, ccbug bobs on the basket rim. All three stay recognizable and correctly scaled.
17-24s: Teamwork: Louis pulls the handle to steer while Kooloo plants paws against the low trolley frame. A tight comic skid brings the trolley safely to rest beside the mall Christmas tree; the loose ribbon spool unwinds around Louis.
24-30s: Reveal Louis gift-wrapped in a giant red bow, still deadpan behind pink glasses. Kooloo gives one smug bell-jingle; ccbug bounces proudly beside the rescued gold star. An original festive musical sting and shared delighted reactions close the joke.
Entire movie is ONE provider generation with duration=30 and ratio=16:9; no generated segment concatenation, no video extension and no second render without renewed instruction. Fast normal-speed physical action, no slow motion. Nonverbal squeaks, gasps, laughter, Foley and original festive comic music; no spoken dialogue required. No title cards, captions, credits or watermarks. Only the three supplied original character identities appear.'''
project.update({
    'source_text': source,
    'input_mode': 'idea',
    'language': 'English',
    'high_level_idea': idea,
    'detailed_script': rough_script,
    'master_prompt_raw': 'Preproduction only: one 30-second generation, Hong Kong mall trolley adventure, supplied cast, original glossy 3D comedy. Final reference-grounded cinematic prompt pending visual asset approval.',
    'style': {
        'medium': 'Original glossy rounded 3D feature animation with exaggerated slapstick acting, elastic poses, tactile knit and glass materials, big readable expressions and brisk comic timing',
        'palette': 'Festive red, evergreen, gold, warm cream and pink accents from the supplied characters',
        'lighting': 'Warm golden mall Christmas illumination, soft cinematic key/fill/rim and reflections',
        'constraints': ['Only supplied original characters; no existing entertainment IP or franchise likenesses', 'Fast pacing and normal-speed action; no slow motion', 'Height ratio Louis:Kooloo:ccbug = 6:3:1 throughout, accounting for camera depth', 'Preserve identity, costume, ornament surface and cat anatomy', 'Only center RED ccbug reference variant appears; no duplication', 'No title cards, subtitles, logos, credits or watermarks']
    },
    'aspect_ratio': '16:9',
    'duration_mode': 'fixed',
    'total_duration_target': 30,
    'asset_list': assets,
    'chapters': [{
        'id': 'chapter_01', 'chapter_index': 1, 'title': 'Christmas shopping trolley adventure', 'duration': 30,
        'high_level_idea': idea, 'scene_summary': 'Fast comic runaway-trolley shopping adventure with teamwork rescue and ribbon-bow punchline.',
        'prompt': '', 'tagged_assets': [a['tag'] for a in assets], 'linked_asset_ids': [a['id'] for a in assets], 'delinked_asset_ids': [],
        'pacing_reason': 'One requested continuous 30-second generation contains setup, escalation, teamwork save and final visual punchline; the timed beats are internal direction for that single request.',
        'shots': [], 'materials': [], 'storyboards': [], 'selected_storyboard_id': None, 'takes': [], 'active_take_id': None, 'screenshots': [], 'production_state': 'rough_plan_awaiting_asset_approval'
    }],
    'generation_constraints': {'generation_requests': 1, 'duration_seconds': 30, 'ratio': '16:9', 'resolution': '720p', 'generate_audio': True, 'omni_reference_task_type': 'reference', 'output_format': 'mp4', 'watermark': False, 'merge_generated_segments': False, 'video_extension': False, 'other_movie_references': False, 'source_asset_directory': 'xmas-material/'},
    'creative_decisions': ['Use center red ccbug variant from the supplied three-variant image.', 'Do not generate, add, or borrow any character identities.', 'Use nonverbal comedy to keep attention on rapid physical gags.', 'Two original generated references only: mall environment and party trolley prop.', 'Height refers to overall standing height, including headgear/ornament cap, on a shared ground plane.'],
    'production_session_id': 'session_41fc80be622d4ff88cfe8e96eedd92d1',
    'capability_evidence': {'checked_at': now, 'source': 'https://docs.byteplus.com/zh-TW/docs/modelark/seedance-2-5', 'facts': ['Seedance 2.5 supports a single video-generation request of up to 30 seconds', 'Reference-to-video supports ratio 16:9', '720p 16:9 output profile is 1280x720'], 'endpoint_access': 'not yet checked; verify authorized endpoint before submission'}
})
(ROOT / 'proposal-asset-review.json').write_text(json.dumps(project, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(ROOT / 'asset-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(ROOT / 'rough-story-plan.txt').write_text(rough_script + '\n', encoding='utf-8')
print(json.dumps({'prepared_assets': len(assets), 'chapter_count': 1, 'planned_seconds': 30, 'generation_requests': 1, 'proposal': str(ROOT / 'proposal-asset-review.json')}, indent=2))
