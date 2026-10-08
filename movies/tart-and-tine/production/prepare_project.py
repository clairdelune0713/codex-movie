"""Build a current-base Movi2 proposal; never overwrite canonical state."""
import copy
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('C:/Users/admina/Downloads/project/dog-test')
project = json.loads((ROOT / 'project.json').read_text(encoding='utf-8'))
original = 'use [$movi2](C:\\Users\\admina\\.codex\\skills\\movi2\\SKILL.md) to create a 60s movie about those two dogs. the beige one is called Tart. The brown one is called Tine'
project.update(source_text=original + '\n\nFollow-up: the style should be like the Up movie.', language='English', input_mode='idea', duration_mode='fixed', total_duration_target=60, aspect_ratio='16:9')
project['high_level_idea'] = 'Two guide-dog puppies in training discover that friendship means lending your courage, then accepting a little help in return.'
project['style'] = {
    'medium': 'Warm, whimsical feature-film 3D animation inspired by Up, retaining the supplied puppy designs',
    'palette': 'Cream and caramel fur, orange vests, saturated teal foliage, sky blue, honey sunlight; soft shadows',
    'lighting': 'One late-afternoon scene with warm sun from upper screen-left, soft skylight and cinematic bounce',
    'constraints': ['Rounded appealing shapes; expressive eye acting; soft detailed fur; playful squash and stretch within canine anatomy', 'Tart is beige; Tine is brown with a pale heart-shaped patch on the right rear haunch', 'Orange gray-edged training vests and blue circular patches remain consistent', 'Exactly two puppies; no humans, extra dogs, copied Up characters, subtitles, watermarks, or inserted franchise music', 'No spoken dialogue; original piano and pizzicato score with garden ambience and canine Foley']
}
project['creative_defaults'] = {'title': project['project_name'], 'genre': 'Gentle friendship adventure', 'dialogue': 'None; visual storytelling', 'delivery_goal': '60.000-second movie; 1920x1080; 30 fps; 1800 frames; stereo 48 kHz audio', 'reference_interpretation': 'Each uploaded sheet shows three views of one dog, not three separate dogs. Vest text is visual costume detail, not an instruction.'}
project['render_state'] = {'status': 'awaiting_video_renderer', 'video_takes_generated': 0, 'discovery': 'No callable video or audio generation tools exposed in the current session. Image generation is available.', 'requested_runtime_seconds': 60, 'actual_video_runtime_seconds': None}
assets = []
for name, file, description in [
    ('Tart', 'tart-young.png', 'Beige puppy with cream muzzle, floppy ears, big dark eyes and dark brown nose. Orange gray-edged guide-dog training vest, blue round side badges. Gentle, thoughtful and initially cautious. Preserve the provided reference identity.'),
    ('Tine', 'tine-young.png', 'Brown caramel puppy with floppy ears, big dark eyes, dark nose and a small pale heart-shaped patch on the right rear haunch. Orange gray-edged guide-dog training vest and blue round side badges. Energetic, brave and occasionally distractible. Preserve the provided reference identity.')
]:
    folder = ROOT / 'assets' / ('asset_' + name.lower())
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / ('reference_01.png')
    if not destination.exists():
        shutil.copy2(SOURCE / file, destination)
    relative = destination.relative_to(ROOT).as_posix()
    assets.append({'id': 'asset_' + name.lower(), 'tag': '@' + name, 'name': name, 'category': 'character', 'description': description, 'source': 'user_provided', 'source_uri': (SOURCE / file).as_uri(), 'media_type': 'Image', 'reference_paths': [relative], 'status_variants': [], 'candidates': [{'id': name.lower() + '_ref01', 'path': relative, 'prompt': 'Original user-provided identity sheet; not generated in this session.', 'source_revision': 0}], 'selected_candidate_id': name.lower() + '_ref01'})
assets.extend([
    {'id': 'asset_garden', 'tag': '@garden', 'name': 'Training garden', 'category': 'environment', 'description': 'A whimsical enclosed puppy training garden in a single late-afternoon lighting state. A gravel path runs west to east, screen-left to screen-right, over a very low arched wooden training bridge above a shallow dry gravel bed. Rounded teal shrubs, daisies at the far ramp, and an oak tree with grass beyond. No water, traffic, dangerous heights, people, or dogs in the environment plate. Bridge is permanent landscape architecture.', 'source': 'generated', 'media_type': 'Image', 'reference_paths': [], 'status_variants': [], 'candidates': [], 'selected_candidate_id': None},
    {'id': 'asset_ball', 'tag': '@ball', 'name': 'Blue training ball', 'category': 'prop', 'description': 'One small sky-blue rubber training ball, matte surface, one narrow cream stripe around its equator, no lettering. Fits under a puppy forepaw. Stable scale, roundness, color and stripe; roll, never teleport.', 'source': 'generated', 'media_type': 'Image', 'reference_paths': [], 'status_variants': [], 'candidates': [], 'selected_candidate_id': None}
])
project['asset_list'] = assets

# Each tuple contains action, camera, audio and an observable end state.
scenes = [
    ('Two little trainees', 'Meet Tart and Tine; a gentle game begins.', 'Tart sits left, Tine right, blue ball between them on the near side of the bridge.', [
        ('@Tart and @Tine sit together in @garden, ears perked. @Tart glances shyly at @Tine; @Tine answers with a bright tail wag.', '35mm wide at puppy eye height; slow push toward both puppies', 'Soft breeze, distant birds; original playful piano motif begins.', 'Tart looks toward the ball; Tine lifts one forepaw.'),
        ('@Tine lowers a forepaw onto @ball and gently nudges it along the gravel path; @Tart tilts the head in delight.', '50mm medium two-shot; paws and faces in one coherent composition', 'Soft rubber tap and gravel tick; pizzicato joins piano.', 'The ball starts rolling east, screen-left to screen-right.'),
        ('@Tart and @Tine trot after @ball through @garden toward the near bridge ramp. @Tine leads by half a body length.', '35mm lateral tracking, consistent left-to-right travel', 'Light paw patter; vest cloth flutter; upbeat motif.', 'Ball reaches the near bridge ramp; both dogs are approaching behind it.')]),
    ('A tiny big obstacle', 'The ball crosses a small bridge that feels very big to Tart.', 'Ball rolls onto the low bridge; both puppies approach from screen-left.', [
        ('@ball rolls slowly over the low wooden bridge in @garden and settles in grass beside the far-side daisies.', '50mm ground-level follow; show near ramp, bridge crown, far ramp and destination', 'Gentle wood roll, then soft grass rustle.', 'Ball is stationary beside the far ramp, on the right.'),
        ('@Tine crosses the bridge confidently and stops beside @ball. @Tart reaches the near ramp and slows.', '35mm wide side view; both ramps visible; no axis crossing', 'Paw taps on wood; piano skips upward.', 'Tine stands at the far ramp; Tart remains at the near ramp.'),
        ('@Tart places one paw on the first bridge plank in @garden, hears a tiny creak, and withdraws the paw. Ears droop; eyes look across toward @Tine.', '65mm close-up from near-side three-quarter view; bridge stays low and safe', 'A small wood creak; a soft canine breath; score thins to two piano notes.', 'Tart has all four paws on near-side gravel, hesitant but safe.')]),
    ('Coming back', 'Tine notices the hesitation and chooses friendship over the ball.', 'Tine at far ramp right, Tart at near ramp left; ball remains by daisies.', [
        ('@Tine looks from stationary @ball to @Tart across the bridge in @garden. Playful expression softens into concern.', '65mm medium close-up; rack focus from ball to Tart across bridge', 'Bird ambience; piano holds a warm chord.', 'Tine turns body toward Tart.'),
        ('@Tine walks back across the bridge in @garden, right to left, slowing as the puppy reaches @Tart on near-side gravel.', '35mm wide profile maintains the established axis; return direction visibly motivated', 'Measured wooden paw taps; gentle pizzicato pulse.', 'Both puppies are together at the near ramp; ball remains far-side.'),
        ('@Tine gently touches noses with @Tart and waits. @Tart raises the ears, takes a steadying breath and returns the nose touch.', '85mm close two-shot at nose height; tiny slow push', 'Quiet sniff and soft exhale; a tender original piano phrase.', 'Both turn to face the bridge, Tart left and Tine right, shoulder to shoulder.')]),
    ('One paw at a time', 'They cross together, at Tart’s pace.', 'Both puppies at near ramp facing east; Tine leads by only a paw length.', [
        ('@Tine places a paw onto the first plank in @garden and waits for @Tart to match the step. Both then advance slowly.', '50mm low medium two-shot includes both faces and front paws', 'Two gentle synchronized taps; encouraging piano phrase.', 'Both puppies have their front paws on the bridge.'),
        ('At the bridge crown in @garden, @Tart glances at @Tine, then straight ahead. Their ears lift and tails begin to wag as they keep walking.', '65mm eye-level moving two-shot; subtle background parallax', 'Soft wood taps and fur movement; pizzicato grows warmer.', 'Both puppies pass the midpoint, continuing left to right.'),
        ('@Tart and @Tine step off the far ramp onto grass beside @ball in @garden. @Tart straightens proudly; @Tine gives a little happy bounce.', '35mm wider side view; small upward camera settle at landing', 'Grass pawfalls and one happy woof; score opens into a bright chord.', 'Both stand safely on far-side grass; ball sits ahead beside daisies.')]),
    ('Your turn to help', 'Tart returns the kindness when Tine becomes distracted.', 'Both at far ramp; ball stationary nearby; daisies on the path edge.', [
        ('@Tine leans toward fragrant daisies in @garden, captivated by the flowers. @Tart looks at @Tine, then at @ball with a knowing smile.', '50mm medium two-shot; flowers foreground, ball lower center', 'Sniff-sniff, leaf rustle; playful flute-like score accent without speech.', 'Tine faces daisies; Tart steps closer to ball.'),
        ('@Tart nudges @ball gently into @Tine’s field of view. @Tine notices, turns back, and touches a paw to the ball beside Tart’s paw.', '65mm close view of noses, ball and paws; tilt up to their expressions', 'Rubber brushing grass, surprised sniff; familiar piano motif returns.', 'Both puppies are focused together again, ball between their paws.'),
        ('@Tart and @Tine exchange a delighted look, then gently roll @ball together toward the oak tree in @garden.', '35mm lateral follow resumes left-to-right travel; no fast chase', 'Two soft happy woofs; paw patter; lively but tender score.', 'Ball rolls toward tree; both puppies follow side by side.')]),
    ('A little braver together', 'Their small adventure ends in quiet shared confidence.', 'Both puppies reach grass beneath the oak; ball rolls to a gentle stop.', [
        ('@ball settles beneath the oak in @garden. @Tart and @Tine arrive together and slow to a stop, breathing lightly after their small adventure.', '35mm wide eye-level; oak frames the pair and bridge remains visible behind', 'Soft grass steps; piano cadence begins; garden ambience continues.', 'Ball rests before both puppies; Tart left, Tine right.'),
        ('@Tart and @Tine sit with shoulders touching in @garden. @Tart rests the head lightly against @Tine; Tine leans back in return. Tails wag softly.', '65mm medium two-shot, gentle push; cream and brown faces clearly distinct', 'Tiny contented sighs, soft vest fabric; original piano resolves.', 'Both rest together peacefully; ball stationary at their paws.'),
        ('Hold @Tart and @Tine together under the oak in @garden with @ball at their feet. Camera eases back to reveal the little bridge they crossed; warm light catches their orange vests.', '35mm slow pullback; last composition holds during the final second', 'Last piano chord rings and fades naturally; birds and breeze continue.', 'Calm wide final frame with both puppies together; no fade or title changes the runtime.')])
]
chapters = []
script = ['# Tart & Tine: A Little Braver Together', '', '**Prepared screenplay — animated video rendering is pending.**', '', '60 seconds • 16:9 • warm whimsical 3D inspired by Up • no dialogue', '', project['high_level_idea'], '']
master_panels = []
for index, (title, summary, blocking, rows) in enumerate(scenes, 1):
    shots = []
    for shot_index, (start, end, row) in enumerate(zip([0, 3, 6], [3, 6, 10], rows), 1):
        action, camera, audio, end_state = row
        shots.append(dict(start=start, end=end, action=action, camera=camera, audio=audio, end_state=end_state))
        master_panels.append({'number': len(master_panels)+1, 'chapter_id': f'chapter_{index:02d}', 'shot_index': shot_index, 'movie_start': (index-1)*10+start, 'movie_end': (index-1)*10+end, 'description': action, 'camera': camera})
    tags = [a['tag'] for a in assets if any(a['tag'] in s['action'] for s in shots)]
    # Location and both identities remain explicit throughout every chapter.
    tags = list(dict.fromkeys(['@Tart', '@Tine', '@garden'] + tags))
    breakdown = '\n'.join(f"Shot {j} ({s['start']}s-{s['end']}s): {s['action']} Camera: {s['camera']}. Audio: {s['audio']} End state: {s['end_state']}" + (' Hard cut.' if j < 3 else '') for j, s in enumerate(shots, 1))
    prompt = f"GLOBAL STYLE: {project['style']['medium']}. 16:9. Rounded forms, expressive eyes, soft detailed fur, warm honey light and teal foliage.\nSCENE: {summary} @Tart and @Tine in @garden.\nLOCATION: Fixed enclosed training garden; gravel path, low wooden bridge over a dry bed, daisies at far ramp and oak beyond.\nFIRST FRAME AND BLOCKING: {blocking}\nSHOT-BY-SHOT BREAKDOWN:\n{breakdown}\nOPTICS and CAMERA: Puppy eye height. Use the stated 35mm, 50mm, 65mm or 85mm-equivalent lenses; gentle dolly movement, readable actions and moderate depth of field.\nPHYSICS: Four anatomically consistent paws per puppy, natural canine locomotion; ear and vest secondary motion; the rubber ball rolls with friction and slows on grass. Bridge is low and stable; a harmless creak does not signify structural failure.\nLIGHTING: Same late-afternoon sun from upper screen-left throughout, soft skylight, bounced gold light, no change of weather or time.\nAUDIO: No spoken dialogue, narration or subtitles. The shot-level Foley and ambience remain audible. Use an original gentle piano/pizzicato score, never a film soundtrack.\nCONTINUITY LOCKS: @Tart is beige; @Tine is caramel brown with a pale heart on the right rear haunch. Preserve their reference faces, orange gray-trimmed training vests and blue circular patches. Reference sheets show multiple views of only one dog each. Two dogs total. Normal travel is left to right; Tine's motivated return is right to left. Ball never changes color, size, stripe, ownership or location without a visible action. Keep the bridge ramps, daisies and oak fixed. No duplicate dogs, morphing, floating paws, extra limbs, watermarks or on-screen text."
    chapter = dict(id=f'chapter_{index:02d}', chapter_index=index, title=title, duration=10, movie_start=(index-1)*10, movie_end=index*10, high_level_idea=project['high_level_idea'], scene_summary=summary, prompt=prompt, initial_prompt=prompt, tagged_assets=tags, linked_asset_ids=[a['id'] for a in assets if a['tag'] in tags], delinked_asset_ids=[], shots=shots, materials=[], storyboards=[], selected_storyboard_id=None, takes=[], active_take_id=None, screenshots=[], audio={'mode': 'visual_story_no_dialogue', 'score': 'Original piano and pizzicato; continuous across cuts', 'ambience': 'Garden breeze and birds; wooden pawsteps, rubber ball and canine breaths'}, handoff={'entry': blocking, 'exit': shots[-1]['end_state']})
    chapters.append(chapter)
    script += [f"## {(index-1)*10:02d}–{index*10:02d}s — {title}", '', summary, '']
    for s in shots:
        absolute_start = (index-1)*10+s['start']
        absolute_end = (index-1)*10+s['end']
        script += [f"**{absolute_start:02d}–{absolute_end:02d}s:** {s['action'].replace('@', '')}", f"Camera: {s['camera']}. Sound: {s['audio']}", '']
project['chapters'] = chapters
project['detailed_script'] = '\n'.join(script)
project['master_prompt_raw'] = project['high_level_idea'] + '\n' + '\n'.join(project['style']['constraints']) + '\nSix consecutive 10-second chapters. Shot durations 3, 3, 4 seconds per chapter. Use hard cuts; no overlap. Preserve the original dog references.'
project['master_panels'] = master_panels
(ROOT / 'source.txt').write_text(project['source_text'] + '\nReference files: tart-young.png; tine-young.png\n', encoding='utf-8')
(ROOT / 'screenplay.md').write_text(project['detailed_script'] + '\n', encoding='utf-8')
(ROOT / 'proposal-r000001.json').write_text(json.dumps(project, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print('Prepared six 10-second chapters, 18 shots, identity references, and current-base proposal.')
