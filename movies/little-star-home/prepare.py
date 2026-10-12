"""Fresh production planning and immutable asset registration. No render calls."""
import sys
sys.dont_write_bytecode = True
import importlib.util
import json
import shutil
from pathlib import Path
from datetime import datetime, timezone
from PIL import Image, ImageOps, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
HELPER = Path(r'C:\Users\admina\.codex\skills\movi2\scripts\project.py')
spec = importlib.util.spec_from_file_location('movi2_project', HELPER)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)

STYLE = {
    'medium': 'Premium stylized 3D plush animation with handcrafted miniature felt environments; soft tactile microfiber, embroidered facial features and restrained squash-and-stretch.',
    'palette': 'Cream white, butter yellow, apricot orange, powder blue, blush pink, mint clover, lavender twilight and honey-gold starlight.',
    'lighting': 'Soft peach sunset fading continuously into lavender blue hour; warm motivated star glow, gentle rim light, soft shadows and shallow macro depth of field.',
    'constraints': ['Only the five supplied character identities; no redesign of their facial patterns.', 'No keychains, hanging loops, fabric tags, product hardware, logos or writing.', 'No titles, subtitles, captions, credits, speech bubbles or readable text anywhere.', 'No narration, spoken dialogue or sung words; humming, cute nonverbal reactions, Foley and instrumental music only.', 'If dialogue is added in a later revision, it must be Japanese.', 'No storyboard images in generation inputs.']
}

CHARACTERS = [
    ('mochi', '@Mochi', 'Mochi — cheerful white friend', 'The upper-left white smiling plush in both photographs. Rounded fluffy white body, small triangular ears with pink interiors, tiny black embroidered curved happy eyes, black oval nose, open smiling mouth with pink tongue, round pink cheeks, two short arms and two short feet. No tail visible in the supplied front reference; use a tiny unobtrusive white back tail only. Equal friend scale. Personality: gentle comforter.'),
    ('hina', '@Hina', 'Hina — sunny yellow friend', 'The yellow plush at upper-middle in ls2 and upper-right in ls1. Butter-yellow rounded chick-like body, TWO round yellow nubs/ears on top, black oval eyes with white highlights, orange triangular beak outlined in black, round pink cheeks, small yellow wing-arms, two tiny orange feet. Preserve the round head nubs rather than converting into an ordinary chick. Personality: affectionate and optimistic.'),
    ('tora', '@Tora', 'Tora — brave apricot tiger', 'The apricot orange tiger plush at lower-left in ls2 and upper-middle in ls1. Round scalloped cheek silhouette, small round ears, THREE black vertical forehead markings, black determined half-lidded eyes with white highlights, small white double-lobed muzzle/mouth outlined in black, paired black cheek marks, black arm stripes, black leg patch and tiny black belly dot. Short round limbs. Preserve the slightly determined expression while giving gentle warmth. Personality: brave but tender.'),
    ('sora', '@Sora', 'Sora — floating blue friend', 'The powder-blue plush at upper-right in ls2 and lower-left in ls1. One continuous rounded teardrop body, domed top, tapered lower tip, TWO tiny side flipper-arms, tiny black dot eyes, thin curved embroidered smile, round pink cheeks. No legs, ears, nose or tail. Remove the black hanging loop; it is hardware, not anatomy. Floats very low over the ground. Personality: shy, helpful and buoyant.'),
    ('mimi', '@Mimi', 'Mimi — listening headphone cat', 'The cream-white headphone-cat plush at lower-right in both photographs. Round cream body, small triangular gray ears with pink centers, black dot eyes, tiny black nose and small restrained mouth, rosy pink scalloped flower-shaped cheek embroidery. Gray headphones with dusty-pink circular ear cushions, a subtle gray band behind the ears. Short cream limbs. Headphones are part of this identity and stay on. Personality: perceptive listener.')
]

COMMON = '''Use case: stylized-concept. Asset type: a single character production reference sheet for a lovely two-minute animated short. Input images: ls1.jpg and ls2.jpg are identity references for the same five plush friends; extract ONLY the specified subject, ignore the other four, the photographed background and all keychain hardware. Style: premium stylized 3D animation, fine short soft microfiber plush, sewn seams and black embroidered facial details, a handcrafted tactile toy brought to life, delicate studio lighting, cute compact original proportions. Horizontal 16:9 canvas with exactly THREE side-by-side equally spaced views, on one seamless warm ivory background, no borders: LEFT front torso/limbs cropped below the face so there is no head or facial detail; MIDDLE matching back torso/limbs also cropped below the head; RIGHT only a large detailed head/face portrait. These are views of ONE character, never three different beings; keep color, material, anatomy and scale coherent. For a continuous rounded plush without a neck, the torso crops start below the facial embroidery; do not invent a neck, clothing or accessories. No text, labels, title, subtitles, watermark, hanging ring/loop, metallic hardware or sewn product label. Do not include any other character, landscape, scene, storyboard or decorative objects.'''

ENV = '''Use case: stylized-concept. Asset type: clean wide environment establishing plate, horizontal 16:9. Create a lovely handcrafted miniature twilight clover meadow for a premium stylized 3D plush animation. Low felt clover leaves, rounded mint-green moss hummocks, tiny blush wildflowers and dew, a small shallow moss-lined hollow in the near left foreground where a little object could nest later, a gently rising open grassy slope center-right with an unobstructed crest and clear view of the enormous lavender sky. Round distant felt trees far left; spacious central clearing for five tiny friends. Camera at plush eye level, tactile soft wool/felt landscape, subtle miniature macro depth of field, peach sunset rim light from camera-left, lavender blue-hour ambient fill, dreamy warm pastel palette, soft shadows. Preserve usable spatial geography and enough empty sky for a star to return home. Absolutely no characters, people, creatures, silhouettes, crowds, headphones, featured story props, lanterns, baskets, hero objects or foreground star. No writing, letters, logo, watermark, titles or subtitles. Empty setting only.'''

STAR = '''Use case: stylized-concept. Asset type: main story prop hero view on seamless warm ivory studio background, horizontal 16:9. A single palm-sized five-point baby star for a premium stylized 3D plush short, with softly rounded chubby points and a warm creamy-gold fuzzy felt surface, faint stitched seams, two tiny black embroidered dot eyes and one tiny softly curved mouth, subtle blush cheeks. Simple sweet and shy, about one third of a friend's head width, no limbs, no clothing, no accessories, no extra points. The same star starts dim and becomes luminous; show its canonical softly glowing state with a restrained honey-gold halo, retaining clearly visible tactile material, not a hard plastic or glass object. Single three-quarter hero view centered with slight soft grounding shadow; delicate warm studio key and fill. No other characters or props, no sky, no meadow, no multi-panel story, no text, title, subtitle, logo or watermark.'''

BEATS = [
    (12, 'An unexpected twinkle', 'Five friends finish a peaceful evening game in a clover clearing. A small gold glimmer drifts down and settles safely into the shallow moss hollow. Mochi notices it, and everyone turns toward the sound.', 'Establish all five identities and shared geography, then allow a readable discovery.', ['@Mochi','@Hina','@Tora','@Sora','@Mimi','@Meadow','@Star']),
    (14, 'A little star feels far from home', 'Mochi kneels beside the dim star and cups it softly. The star tilts one point toward the sky, where there is a small gap among distant points of light. Mochi cuddles it; Hina touches its side. Its first tiny pulse answers their care.', 'Read the star’s wish without speech and establish that affection makes it brighten.', ['@Mochi','@Hina','@Meadow','@Star']),
    (14, 'A brave little try', 'On soft grass beside the hollow, Tora gently raises the star, makes one modest hop and releases it upward only a paw-height. It descends slowly like a feather; Mochi catches it safely. Tora looks bashful; Mochi nudges his shoulder reassuringly.', 'Give the attempted solution a clear setup, gentle failure and affectionate reaction.', ['@Tora','@Mochi','@Meadow','@Star']),
    (16, 'A blue lift and a warm cuddle', 'Sora offers its rounded top as a cushion. The star settles on it, and Sora floats upward to roughly one friend-height. The star looks toward the much higher sky; Sora eases back down. Hina folds its small wings around the star, which brightens briefly with a soft chime.', 'Let the blue friend help through its own physical gift, and repeat the glow clue through warmth.', ['@Sora','@Hina','@Meadow','@Star']),
    (12, 'Mimi hears the answer', 'Mimi listens close to the star through its headphones. The star chimes a tiny three-note pattern. Mimi hums that wordless pattern gently. The star pulses brighter and floats a finger-width. Mimi’s ears perk; the friends notice the discovery.', 'Give the listener a specific observation, response and visible cause-and-effect.', ['@Mimi','@Mochi','@Meadow','@Star']),
    (18, 'Five small voices, one big kindness', 'At the lower slope, the five form a loose circle around the star. Mimi begins the same three-note hum; Mochi, Hina, Tora and Sora join one by one, each briefly seen. With each voice, one of the star’s five points brightens. The star begins hovering steadily between them.', 'Allow every character a turn and make collective warmth the earned solution.', ['@Mochi','@Hina','@Tora','@Sora','@Mimi','@Meadow','@Star']),
    (20, 'Homeward on a lullaby', 'The friends take tiny steps up the short slope while continuing their gentle hum, with the floating star at chest level in front of them. At the crest they settle together. The fully lit star slowly rises, circles them once in gratitude, then lifts toward the open lavender sky. All five wave or raise their little arms.', 'Preserve a calm emotional payoff with readable ascent, gratitude and collective goodbye.', ['@Mochi','@Hina','@Tora','@Sora','@Mimi','@Meadow','@Star']),
    (14, 'A thank-you above the meadow', 'The star takes its place among the distant lights and sends the same three-note chime. Below, the five nestle shoulder to shoulder on the crest. Tora leans into Mochi, Hina rests close, Sora floats just above the grass, and Mimi smiles. One final gold twinkle lights their cheeks. Hold on their quiet happiness; end on the image with no text or credits.', 'Resolve the homecoming, confirm the friendship and leave a gentle final hold.', ['@Mochi','@Hina','@Tora','@Sora','@Mimi','@Meadow','@Star'])
]

def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def setup():
    p = helper.read(ROOT/'project.json')
    if p['revision'] != 0:
        raise RuntimeError('Setup only runs on the fresh initializer state.')
    originals = ROOT/'assets'/'reference'
    originals.mkdir(parents=True, exist_ok=True)
    for filename in ['ls1.jpg','ls2.jpg']:
        shutil.copy2(Path(r'C:\Users\admina\Downloads')/filename, originals/filename)
    p.update(source_text='user movi2 skill. make a 2min movie (do not ref any existing projects in moves/). the story is based on the 5 cute cartoon figures (the two uploaded images are for your reference). Please design the story plot. Please choose the optimal style. the story has to be lovely and cute. if dialogues are included, please be in Japanese. no titles or subtitles.', input_mode='idea', language='English', high_level_idea='Five tiny plush friends discover that their shared warmth and a wordless lullaby can help a fallen baby star find its way home.', style=STYLE, aspect_ratio='16:9', duration_mode='fixed', total_duration_target=120, resolution='720p', audio_policy='Instrumental celesta, soft pizzicato and Japanese-style wordless humming; no speech, lyrics or narration.', production_stage='asset_generation', reference_policy='Fresh project. No existing movie project was consulted. Uploaded photographs ground the five identities. Separate character/environment/prop images; no storyboard stage.', dialogue_language='Japanese', script_changes=['Original plot designed from the five supplied figures; no existing project, film or named franchise referenced.'], rendering={'requested': True, 'route': 'unbound', 'new_submissions': 0, 'note': 'Requires displayed asset approval and an available authorized video route.'})
    prompt_set = {}
    assets = []
    for aid, tag, name, desc in CHARACTERS:
        prompt = COMMON+'\nSpecified subject: '+desc
        prompt_set[aid] = {'prompt':prompt, 'reference_paths':['assets/reference/ls1.jpg','assets/reference/ls2.jpg']}
        assets.append(dict(id='asset_'+aid, tag=tag, name=name, category='character', description=desc, source='generated', media_type='Image', status_variants=[], reference_paths=['assets/reference/ls1.jpg','assets/reference/ls2.jpg'], candidates=[], selected_candidate_id=None))
    for aid, tag, name, category, desc, prompt in [
        ('meadow','@Meadow','Twilight clover meadow','environment','A single empty miniature felt meadow, shallow moss hollow foreground-left, clover clearing center and low slope/crest right, lavender open sky. Sunset fades naturally into blue hour.',ENV),
        ('star','@Star','Baby star','prop','One palm-sized creamy-gold five-point rounded felt star, black embroidered dot eyes, tiny curved mouth, blush cheeks. Same shape across dim and luminous states; responds to care and shared three-note humming by glowing and floating.',STAR)]:
        prompt_set[aid]={'prompt':prompt,'reference_paths':[]}
        assets.append(dict(id='asset_'+aid, tag=tag, name=name, category=category, description=desc, source='generated', media_type='Image', status_variants=[], reference_paths=[], candidates=[], selected_candidate_id=None))
    for i in (1,2):
        assets.append(dict(id=f'asset_reference_{i}', tag=f'@Reference{i}', name=f'Supplied plush photograph {i}', category='reference', description='Uploaded photograph used only to preserve the five figures, colors and embroidered face patterns; ignore background, keychain hardware and product labels.', source='user_upload', media_type='Image', reference_paths=[], candidates=[{'id':f'reference_{i}_original','path':f'assets/reference/ls{i}.jpg','created_at':datetime.now(timezone.utc).isoformat()}], selected_candidate_id=f'reference_{i}_original'))
    p['asset_list'] = assets
    start=0
    chapters=[]
    script=['# A Little Star Finds Home\n\nInternal working name only; no title card. Runtime: exactly 120 seconds. Aspect: 16:9. Planned output: 720p.\n\nA lovely wordless story in soft tactile 3D plush animation. No titles, subtitles, speech, lyrics, credits or narration. Humming and affectionate nonverbal sounds are allowed. Any later added dialogue must be Japanese.\n']
    for i,(duration,title,summary,reason,tags) in enumerate(BEATS,1):
        end=start+duration
        chapters.append(dict(id=f'chapter_{i:02d}',chapter_index=i,title=title,duration=duration,movie_start=start,movie_end=end,high_level_idea=p['high_level_idea'],scene_summary=summary,pacing_reason=reason,planning_status='rough_beat_only_until_asset_approval',prompt='',initial_prompt='',tagged_assets=tags,linked_asset_ids=[],delinked_asset_ids=[],shots=[],materials=[],takes=[],active_take_id=None,screenshots=[],resolution='720p',audio='Wordless humming, cute nonverbal reactions, light instrumental score and gentle Foley. No spoken dialogue.'))
        script.append(f'## {start//60:02d}:{start%60:02d}–{end//60:02d}:{end%60:02d} ({duration}s) — {title}\n\n{summary}\n\nPacing: {reason}\n')
        start=end
    assert start==120
    p['chapters']=chapters
    p['detailed_script']='\n'.join(script)
    p['continuity_notes']=['Five source figures only; baby star is the one narrative prop.','Star floats only after the shared-humming clue is established.','No dangerous throwing, fright, injury or distress. Failed tries land softly and receive reassurance.','Keep the star’s five points, character embroidery, headphone design, distinct colors and friend scale stable.','One continuous evening and meadow geography; hollow lower-left, slope/crest toward screen-right, open sky above.','Celesta echoes the same three-note star motif. Keep incidental score modest so the humming clue reads.']
    (ROOT/'script.md').write_text(p['detailed_script'],encoding='utf-8')
    (ROOT/'source-request.txt').write_text(p['source_text'],encoding='utf-8')
    write_json(ROOT/'exports'/'asset-prompts.json',prompt_set)
    write_json(ROOT/'proposal.json',p)
    print(json.dumps(helper.save(ROOT,helper.read(ROOT/'project.json'),p,'Design fresh 120-second story and supplied-reference asset inventory')))
    current=helper.read(ROOT/'project.json')
    write_json(ROOT/'exports'/'generation-plan.json',{'source_revision':current['revision'],'assets':{a['id']:{'dependency_fingerprint':helper.asset_fingerprint(ROOT,current,a)} for a in current['asset_list'] if a['source']=='generated'}})

def register(aid, source):
    p=helper.read(ROOT/'project.json')
    asset=next(a for a in p['asset_list'] if a['id']=='asset_'+aid)
    if asset['candidates']:
        raise RuntimeError('Register a new candidate ID for a further variation; never overwrite.')
    destination=ROOT/'assets'/asset['id']/f'{aid}_c01.png'
    destination.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(source,destination)
    with Image.open(destination) as img:
        img.verify()
    with Image.open(destination) as img:
        width,height=img.size
    definition=helper.read(ROOT/'exports'/'asset-prompts.json')[aid]
    plan=helper.read(ROOT/'exports'/'generation-plan.json')
    asset['candidates'].append({'id':f'{aid}_c01','path':destination.relative_to(ROOT).as_posix(),'prompt':definition['prompt'],'input_reference_paths':definition['reference_paths'],'requested_style':STYLE,'source_revision':plan['source_revision'],'dependency_fingerprint':plan['assets'][asset['id']]['dependency_fingerprint'],'created_at':datetime.now(timezone.utc).isoformat(),'tool':'built-in imagegen','width':width,'height':height,'actual_aspect_ratio':f'{width}:{height}'})
    asset['selected_candidate_id']=f'{aid}_c01'
    helper.save(ROOT,helper.read(ROOT/'project.json'),p,f'Retain inspected {asset["tag"]} candidate {aid}_c01')
    print(json.dumps({'asset':asset['tag'],'path':str(destination),'width':width,'height':height}))

def gallery():
    p=helper.read(ROOT/'project.json')
    groups=[('characters',[a for a in p['asset_list'] if a['category']=='character'],1000,560),('setting-and-star',[a for a in p['asset_list'] if a['category'] in ('environment','prop')],1000,600),('supplied-references',[a for a in p['asset_list'] if a['category']=='reference'],600,720)]
    try:
        font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',22)
    except OSError:
        font=ImageFont.load_default()
    for name,items,w,h in groups:
        out=Image.new('RGB',(w,h*len(items)),(247,244,237))
        draw=ImageDraw.Draw(out)
        for row,a in enumerate(items):
            c=helper.selected_media(a)
            with Image.open(ROOT/c['path']) as im:
                tile=ImageOps.contain(im.convert('RGB'),(w-36,h-58))
                out.paste(tile,((w-tile.width)//2,row*h+48+(h-58-tile.height)//2))
            label=f'{a["name"]} | {a["tag"]} | {c["id"]}'
            row_font=font
            size=22
            while row_font.getlength(label)>w-40 and size>12:
                size-=1
                row_font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',size)
            draw.text((20,row*h+14),label,fill=(58,54,70),font=row_font)
        path=ROOT/'exports'/f'asset-review-{name}.jpg'
        out.save(path,quality=92)
        print(str(path))
    links=['# Asset gallery\n\nReview files only; never video inputs. The script and generation prompts are saved separately.\n']
    for a in p['asset_list']:
        c=helper.selected_media(a)
        links.append(f'- {a["name"]} — {a["tag"]} — `{c["id"]}` — [{c["id"]}]({(ROOT/c["path"]).as_posix()})')
    (ROOT/'exports'/'asset-gallery.md').write_text('\n'.join(links)+'\n',encoding='utf-8')

def finish():
    p=helper.read(ROOT/'project.json')
    p['production_stage']='awaiting_asset_review'
    p['quality_review']={'inspected_at':datetime.now(timezone.utc).isoformat(),'all_seven_generated_assets_inspected':True,'findings':['Character sheets retain five distinct source identities, facial embroidery and colors.','Mimi retains gray and pink headphones and flower-shaped cheeks.','Sora remains a single blue teardrop without legs or keychain hardware; the right reference view includes its continuous silhouette.','Meadow is empty of characters and featured story props; foreground hollow and right slope are readable.','Baby star has exactly five rounded points, one face and a soft gold felt surface.','All output images decode; source copies are preserved. Actual image dimensions are recorded rather than assuming exact 16:9.'],'limitations':['Video motion, shot continuity and audio await actual rendering.','Reference sheets depict cropped body views and a facial view of one individual; these must be bound as identity references and never copied as scene composition.']}
    helper.save(ROOT,helper.read(ROOT/'project.json'),p,'Complete visual inspection and prepare user asset review')
    write_json(ROOT/'exports'/'quality-review.json',p['quality_review'])
    print('Inspection saved; no video submitted.')

if __name__=='__main__':
    if sys.argv[1]=='setup': setup()
    elif sys.argv[1]=='register': register(sys.argv[2],sys.argv[3])
    elif sys.argv[1]=='gallery': gallery()
    elif sys.argv[1]=='finish': finish()
