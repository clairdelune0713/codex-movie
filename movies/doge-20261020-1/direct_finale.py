"""Finalize only approved scenes 37-51. No model calls or changes to source assets."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
assert p['asset_review']['status']=='approved'
assets={a['id']:a for a in p['asset_list']}

start={
37:'Wide waterfront vista, Clock Tower left and harbour beyond. One green-white ferry has a visible uniformed captain in its wheelhouse and seated passengers on its deck. Then @adult-tart-harness guides @blind-guy left-to-right: Leung left hand on curved silver handle, Tart slightly ahead at his anatomical left. Clear bench alcove frame-left, right approach lane. Kiki and Tine approach from screen right, separated from the bench by twelve paces.',
38:'Dog-height close on @adult-tart-harness beside seated @blind-guy\'s left knee. Harness handle remains in Leung\'s LEFT hand. Across the open pedestrian lane, @adult-tine stands beside @animal-companion-worker with blue tail-half in his mouth. They notice each other from separate positions; neither dog departs.',
39:'Seated @blind-guy on left of the same bench, his LEFT hand on @adult-tart-harness handle. One cream dog only: @adult-tart-harness and @adult-tart-leash are two costume states of that same Tart, never two dogs. The folded brown leash is ready in Leung\'s free hand; harness remains ON until the final six-second change.',
40:'One cream @adult-tart-leash off duty by seated @blind-guy\'s left shoe. Leung holds the slack brown lead. @adult-tine and @animal-companion-worker stand screen-right with held slack orange lead, facing the bench. Harness rests ON bench. Two dogs remain about four metres apart; only Kiki and Tine cross the clear lane.',
41:'At the bench alcove: @adult-tart-leash by Leung\'s left knee screen-left; @adult-tine beside Kiki screen-right, blue tail-half in mouth. @lonely-old-man sits at adjoining bench end near the ground-level drain, closed cage secure beside him. A seller crosses foreground holding EVERY balloon ribbon; wind briefly sweeps balloons across view.',
42:'Tail-half is stopped at the drain lip by the curved end of Mr Ko\'s cane; Ko remains seated. @animal-companion-worker stands beside @adult-tine, orange leash held. @adult-tart-leash waits by @blind-guy, brown leash held. Cane draws toy onto CLEAR paving; humans retrieve and offer it before the dogs greet.',
43:'Blue-hour dog-height two-shot beside bench. Exactly ONE adult cream @adult-tart-leash left and ONE adult fox-red @adult-tine right, nose to nose within human arm\'s reach. Both held leads slack and separated, harness ON bench. Tail-half placed between Tine\'s paws. Ranch puppy images occur ONLY inside the four hard-cut memory inserts.',
44:'Blue-hour dog two-shot beside bench, one cream Tart left and one fox-red Tine right, tail-half between their paws. Leung\'s resting hand above Tart and brown lead held; Kiki beside Tine holding orange lead. Head-half is NOT present in this scene.',
45:'@animal-companion-worker sits to the screen-right of seated @blind-guy. Both face slightly inward for conversation; Leung turns toward her VOICE without visual eye contact. One cream dog and one red dog gently wriggle at their feet, leashes held. Bench and skyline remain established.',
46:'@lonely-old-man sits beside @blind-guy on the same bench, cane resting securely against it. Kiki sits to their right. Dogs lie shoulder to shoulder at their feet, each lead held. The sky transitions from blue hour to night; the light show begins only in the final five seconds.',
47:'Night-time alternating medium/close coverage of two original animated men on the same bench: completely blind @blind-guy at screen-left, @lonely-old-man at screen-right. Both remain seated. Leung\'s opaque sunglasses cover his eyes at ALL times. His head tilts to the SOUND of music, then toward Ko\'s voice. He cannot perceive the skyline or colors.',
48:'Night, same bench alcove. One cream Tart and one fox-red Tine sit shoulder to shoulder at feet of their seated people, facing the harbour. Held brown and orange leads form separate easy curves on paving away from public path. Harness lies on bench. Kiki has counter in free hand; Leung has tart bag in free hand.',
49:'NEXT FRIDAY, golden hour, same bench. Ensemble is soft background, limited foreground pairs: Leung seated with Tart off duty on held brown lead; Kiki with Tine on held orange lead. Ko has closed cage, Bo has egg tarts and wears secure clear-bubble cat backpack containing ONLY Boss. Tart has HEAD-half, Tine TAIL-half. Collar-only public off-duty state, no harness on either dog.',
50:'Golden hour aerial starts above the same tiny reunion group beside the bench. The camera rises away from the group toward the harbour. Any visible ferry has a captain in the wheelhouse and passengers. Preserve an uncluttered warm sky for editorial transition to the original parchment map and title; no model-generated words.',
51:'Sunny Hill Ranch daytime. Medium three-quarter view of original @mags at veranda edge holding @postcard by one corner. The picture side shows a small reunion photograph of the cream and red dogs together at Victoria Harbour, not live dogs on the ranch. @gertrude stands below her hand ready to snatch the card; @kookaburra on nearby fence post as third soft background animal.'}
end={
37:'Tine holds tail-half beside Kiki and gives low HONK. Tart remains working by Leung at the bench offscreen.',38:'Dogs recognize each other across the walkway but remain with handlers, Tart harness still on.',39:'Leung holds brown leash clipped to Tart collar. Harness removed and resting visibly on bench. Tart stays beside Leung\'s knee.',40:'Kiki and Tine reach the bench alcove, still one pace away from Tart. Tine still carries tail-half.',41:'Ko\'s cane has caught toy at drain lip. Both dogs remain beside people, no lead released.',42:'Two dogs close final inches nose to nose, tail-half offered to Tine, held leads separated.',43:'Adult dogs forehead-to-forehead by bench; tail-half on ground between paws.',44:'Tine chin rests in Leung\'s offered hand, four paws grounded. Toy remains close to dogs.',45:'Kiki realizes the dogs are brothers; both bark naturally together once.',46:'Harbour light show starts, group remains seated safely by bench.',47:'Leung smiles through a tear below sunglasses, listening to Ko. No visual gaze or sight recovery.',48:'Dogs complete gentle paw promise; humans share egg tarts and Kiki counts 101.',49:'Boss purrs and slow-blinks from inside closed clear bubble carrier; dogs reunited with complementary halves.',50:'Clean warm harbour sky/parchment-style neutral editorial plate for exact map and title compositing.',51:'Gertrude waddles off with postcard; Mags calls OI; kookaburra laughs. Normal-speed final cut to black.'}
extras={
(37,1):'Boat captain and passengers visible as small original animated figures; no empty self-driving ferry. Camera 24mm equivalent, eye-level waterfront wide, no dizzying drone arc.',
(37,2):'35mm parallel tracking. Leung listens to ferry horn and ice-cream splat; never directs eyes to boat/child. Tart makes a steady straight guide route, no sudden jerks.',
(37,3):'50mm seated-handler coverage. Leung feels seat with free hand BEFORE sitting; left handle hand stays in contact. End with Tart at left knee.',
(37,4):'35mm track right-to-left. Focus Ko and Kiki/Tine sequentially; three grannies soft in back, cage door latched. Do not turn ensemble into a lineup.',
(37,5):'50mm medium. Kiki removes only tail-half from bandana knot, offers it, Tine takes then compresses it. One coherent handoff; orange leash stays in other hand.',
(38,6):'85mm alternating two separated pairs across clear opening. Dogs remain distinct, no convergence or phantom duplicate, real-time pedestrian motion.',
(39,4):'50mm stable close coverage of hands and collar. Show the SILVER leash snap fastened to collar first, brown leash firmly held. THEN lift tan harness away and place on bench. No instantaneous costume morph. Leung locates buckle and collar by TOUCH.',
(40,4):'35mm simple group crossing foreground. Only one foreground guide with yellow flag; tourist faces soft. Dogs and people stop and yield, no collisions.',
(41,2):'50mm low three-quarter insert. One blue tail-half drops, lands once, rolls only a short distance along paving toward the low drain; mouth opens, gravity acts, one object throughout.',
(41,6):'50mm cane-tip insert, seated Ko remains weight-supported. Curved handle catches toy edge on paving, does not spear toy or pass through bars.',
(42,1):'35mm medium-wide, one action at a time: cane slides toy to clear paving, Kiki bends and picks it up, then offers to Ko free hand. Both leads remain held in opposite hands with enough slack.',
(42,3):'35mm side view, Kiki moves along RIGHT flank of Tine, keeps orange leash right of him; Tart brown leash left, no crossing strands.',
(43,3):'50mm two-shot: one small play-bow and one gentle cheek rub, quick natural licks; no tumbling, swapping coat colors or dropping/releasing leads.',
(44,2):'70mm low insert. Tart gently takes ONE tail-half, compresses for HONK, returns same part to Tine. Never converts into whole toy or grows orange bill.',
(45,3):'65mm two-shot, focus Kiki talking then Leung head tilts toward sound. Dogs are background paws/backs, not extra foreground subjects.',
(46,3):'24mm wide, original abstract light show, original newly composed cue; no real concert footage, logos or recognizable music.',
(47,2):'75mm close on Ko, spoken memories flow warmly. Leung remains soft shoulder foreground, not shown seeing color.',
(47,3):'85mm close on Leung, opaque sunglasses never lift; a small tear appears below lower rim, smile follows memory not recovered vision.',
(48,4):'85mm paw insert, exactly two canine paws touch softly and separate naturally, no human hands, extra paws or finger anatomy.',
(49,1):'35mm wide, three featured subjects maximum per focal group, ensemble far behind. Boss remains securely inside bubble carrier, cage stays closed. Do not give handlers floating leashes.',
(49,3):'70mm close, exactly two complementary blue plush halves: orange-bill head-half at Tart mouth LEFT, flat blue tail-half at Tine mouth RIGHT. They press torn edges together and squeeze at same time, remain visibly two worn parts, no magical healing/morph.',
(49,4):'85mm close on ONE original orange tabby Boss through curved clear carrier bubble, left-ear notch correct, natural quiet purr, no lip-sync.',
(50,1):'24mm rising boom/drone, tiny group below, stable horizon and no new facial close-ups. Editorial map will replace middle portion. No printed lettering or logos in generated frames.',
(50,2):'Hold a stable warm parchment/sky editorial plate; exact title is added in local edit, not synthesized by model.',
(51,1):'40mm medium: Mags reads card, chuckles line; goose gently snatches a CORNER from her hand and waddles off, Mags OI, kookaburra laugh. No destruction of fingers, no teleporting prop, no live adult dogs on ranch.'}

name_map=[('Puppy Tart','puppy-tart'),('Puppy Tine','puppy-tine'),('Mr. Leung','blind-guy'),('Mr. Ko','lonely-old-man'),('Auntie Bo','barista'),('Granny Wong','granny-wong'),('Granny Lee','granny-lee'),('Granny Chan','granny-chan'),('Gertrude','gertrude'),('Mags','mags'),('Kookaburra','kookaburra'),('Kiki','animal-companion-worker'),('Boss','boss'),('Jade','jade')]
def tagtext(text,n):
    text=re.sub(r'^\*\*\d+\.\d+\*\* · \d+–\d+s · ','',text)
    text=text.replace('**','').replace('*','')
    text=re.sub(r'^- CAPTION:.*$','[Exact caption reserved for local edit; no generated text.]',text,flags=re.M)
    for name,id in name_map:
        text=re.sub(r'(?<![\w@-])'+re.escape(name)+r'(?![\w-])','@'+id,text,flags=re.I)
    tart='adult-tart-harness' if n<=39 else 'adult-tart-leash'
    text=re.sub(r'(?<![\w@-])Tart(?![\w-])','@'+tart,text,flags=re.I)
    text=re.sub(r'(?<![\w@-])Tine(?![\w-])','@adult-tine',text,flags=re.I)
    text=text.replace('the Up-style waltz','an original lilting orchestral waltz').replace('Up-style','rounded warm animated')
    return text.strip()

common='Original warm rounded stylized 3D feature animation, gentle saturated colors, expressive faces and tactile plush fur, soft global illumination and painterly sky. This entire film is animation with fictional drawn/stylized people. No live-action footage or real-person likeness. Original characters and original newly composed music only. 480p, ultrawide 21:9. REAL-TIME ONLY, NO slow motion, speed ramp, time stretch, frozen-photo animation or frame blending. Explicit internal hard cuts at stated times, no transitions that alter runtime.'
locks='Mr. Leung is completely blind: opaque black sunglasses ALWAYS ON, no visual gaze, pointing at sights, tracking lights/objects, or sight restoration. His left hand holds guide-harness handle while Tart works. Dogs never speak human words or lip-sync; humans alone speak English, natural barks/whines/panting only for dogs. One cream Tart and one fox-red Tine, never swapped or duplicated. Tart tan guide harness and silver handle stay ON until39.4; brown leash clipped and held BEFORE harness removal; harness then ON BENCH. Orange leash clipped to collar BELOW bandana and always held by Kiki. Both leads slack, separate, no crossing/dragging. Tine heart marking remains above tail. No animals chase birds, jump on elderly people, leave their people, enter road/water, fly with balloons or perform roof stunts. Balloon seller holds ALL ribbons. One main physical action, at most three sharp foreground subjects per shot; others soft background/offscreen. Every visible road vehicle has a driver; every visible bus has driver AND passengers; ferry captain and passengers are present. No driverless vehicles. No existing Pixar/Disney characters, logos, watermarks or subtitles. Only scripted editorial captions/title added later.'

for c in p['chapters']:
    n=c['chapter_index']
    if n<37:continue
    ids=list(c['rough_asset_ids'])
    if n==43:
        ids+=['puppy-tart','puppy-tine','gertrude','mags','ranch','veranda','hayloft','bucket-helmet','aviator-goggles','sir-squeaks-whole','sir-squeaks-head']
    if n==50:ids+=['adult-tart-leash','adult-tine','blind-guy','animal-companion-worker','lonely-old-man']
    ids=list(dict.fromkeys(ids))
    shots=[]
    for i,s in enumerate(c['source_shots'],1):
        if n==43 and i==2:
            memories=[(3,4.5,'Golden ranch memory: @puppy-tine in @bucket-helmet beside @puppy-tart in @aviator-goggles; two tiny original puppy faces grin, normal-speed head tilt.','35mm two-puppy close, original @ranch geography.'),(4.5,6,'Golden ranch memory: @gertrude flaps behind two sprinting puppies, @puppy-tart and @puppy-tine, across the open @ranch yard. One normal-speed chase beat.','35mm side-track, exactly three animals, no adult dogs.'),(6,7.5,'Golden veranda memory: the puppies tug @sir-squeaks-whole once and its middle seam separates, leaving @sir-squeaks-head at cream puppy Tart and @sir-squeaks-tail at red puppy Tine.','70mm insert, only toy and puppy paws/mouth corners, @veranda soft behind.'),(7.5,9,'Golden night-loft memory: @mags gently presses @puppy-tart and @puppy-tine front paws together under the stars. One pinky-paw promise.','65mm paws and hand insert, @hayloft soft behind.')]
            for a,b,action,cam in memories:shots.append({'start':a,'end':b,'action':action,'camera':cam,'audio':'Original SQUEE-HONK motif, tiny natural puppy yips; no spoken animal words.','end_state':'Hard cut into next memory or present-day dogs.'})
            continue
        action=tagtext(s['source_text'],n)
        if n==50:
            action=('EXTREME WIDE: Rise from tiny reunion group over the harbour; continue a gentle stable rise to a clean warm skyline/sky plate. No lettering or generated map. Map transition will be added in local edit inside this interval.' if i==1 else 'Stable clean warm harbour sky editorial plate with no text, title, logos or symbols. Exact final title and subtitle will be composited locally over this interval.')
        cam='35mm equivalent for wide action, 50mm medium, 75-85mm close reactions; stable support and shallow but readable depth. '+extras.get((n,i),'Frame the named action and speaker clearly; other cast soft or offscreen. Preserve feet/paw ground contact and a usable cut end state.')
        if n==39 and i==4:action=action.replace('@adult-tart-harness','@adult-tart-leash')+' One Tart, transitioning from working harness reference to the brown-leash reference, exactly in the specified order.'
        shots.append({'start':s['start'],'end':s['end'],'action':action,'camera':cam,'audio':'Exact human English lines and animal SFX stated in action; duck score under speech.','end_state':end[n] if i==len(c['source_shots']) else 'Conclude the stated physical beat before the hard cut; retain prop ownership and held leads.'})
    # Bind tags introduced in dialogue/shot descriptions, then only the chosen explicit links.
    blob=' '.join(s['action']+' '+s['camera'] for s in shots)+' '+start[n]
    ids+= [m[1:] for m in re.findall(r'@[\w-]+',blob) if m[1:] in assets]
    ids=list(dict.fromkeys(ids))
    roles=[]
    for id in ids:
        a=assets[id]
        role='identity/wardrobe only; sheet background and multiple views are NOT scene objects' if a['category']=='character' else 'fixed layout/materials only; relight for this scene time, populate solely from specified cast' if a['category']=='environment' else 'one physical object or stated prop state only; ignore studio background and reference insets'
        roles.append(f"{a['tag']}: {role}. {a['description']}")
    if n==43:roles.append('PUPPY/ADULT SEPARATION: puppy identities, Mags/goose and ranch references apply ONLY3-9s memory inserts; adult dogs/handlers/harbour apply ONLY0-3s and9-23s. All reference views are one identity, never duplicate actors.')
    if n==39:roles.append('@adult-tart-harness and @adult-tart-leash are the SAME Tart in consecutive outfit states, never two dogs.')
    light='Motivated warm golden-hour sunset from harbour side, no flicker.' if n<=42 or n in (49,50) else 'Cool blue-hour harbour fill, warm bench practical accents and distant skyline.' if n<=45 else 'Night harbour practical lights, soft colored skyline reflections; no strobing faces.'
    if n==51:light='Warm Australian ranch daylight, coherent veranda shadows.'
    audio=c['music_cue'].replace('Up-style','original').replace('the Squee-Honk motif','an original high-low two-note SQUEE-HONK motif')
    sequence=[]
    for i,s in enumerate(shots,1):sequence.append(f"Shot {i} ({s['start']}s-{s['end']}s): {s['action']} Camera/Focus: {s['camera']} Lighting: {light} Audio: {s['audio']} End state: {s['end_state']}"+(' Hard cut.' if i<len(shots) else ''))
    c.update({'prompt':'\n\n'.join(['SCENE CONTEXT\n'+c['title']+'. '+c['high_level_idea'],'OUTPUT SETTINGS\n'+str(c['duration'])+' seconds exactly. '+common,'ACTIVE REFERENCES\n'+'\n'.join(roles),'LOCATION MAP / FIRST FRAME AND BLOCKING\n'+start[n],'TIMELINE AND SHOT SEQUENCE\n'+'\n'.join(sequence),'PHYSICS AND CONTACT\nActual paw and foot weight, fabric resistance and toy compression; hands grasp physical handles/clips, leads attach to collars and form continuous curves. No intersecting hands/paws, floating prop transfers or spontaneous costume morphs.','LIGHTING\n'+light,'AUDIO\n'+audio+'. Newly composed original score only, no known tune, film soundtrack or recording. Preserve exact human lines and natural animal SFX specified above; one speaker at a time. Matching same fictional voice per human; Mr Leung warm radio baritone, Kiki bright young adult, Ko older textured gentle voice, Mags warm Australian accent. Harbour ambience and original effects sit below clear speech.','CONTINUITY / POSITIVE CONSTRAINTS\n'+locks,'END STATE\n'+end[n]]),'initial_prompt':'','prompt_status':'finalized_after_asset_approval','tagged_assets':['@'+id for id in ids],'linked_asset_ids':ids,'delinked_asset_ids':[],'shots':shots,'resolution':'480p','generate_audio':True,'aspect_ratio':'21:9','handoff':{'shared_environment':'harbour' if n<51 else 'ranch','previous_end_state':'Previous source-scene ending retained; no automatic prior-video input.','next_start_state':start[n],'end_state':end[n],'cut_type':'hard cut','reference_decision':'Approved environment plus explicit written geography suffices for independent coverage. Add a single inspected selected frame only if an observed mismatch requires it.','audio_boundary':'Original score cues and harbour/ranch ambience, speech kept inside each original scene duration.'}})
    c['initial_prompt']=c['prompt']
    if n==50:c['editorial_graphics']=[{'start':2.5,'end':6,'kind':'original_animated_map','labels':['VICTORIA, AUSTRALIA','VICTORIA HARBOUR, HONG KONG']},{'start':6,'end':9,'kind':'title','title':'TART & TINE','subtitle':'From Victoria to Victoria'}]
    if n==37:c['editorial_graphics']=[{'start':0.5,'end':4.5,'kind':'caption','text':'Victoria Harbour. Friday.'}]
    if n==49:c['editorial_graphics']=[{'start':0.5,'end':4.5,'kind':'caption','text':'Next Friday.'}]
    (ROOT/'chapters'/c['id']).mkdir(parents=True,exist_ok=True)
    (ROOT/'chapters'/c['id']/'director-prompt.txt').write_text(c['prompt'],encoding='utf-8')
p['aspect_ratio']='21:9'
p['render_scope']={'first_scene':37,'last_scene':51,'scene_ids':[f'scene_{i:02d}' for i in range(37,52)],'duration_seconds':305,'resolution':'480p','aspect_ratio':'21:9','other_scenes_authorized':False}
p['production_stage']='finale_directed'
p['production_notes'].append('Latest user scope: ONLY scenes37-51, stitch 305-second finale at480p21:9. Vehicles must have driver; bus includes driver/passengers. Public inline reference route only; no private asset library. Original score, no named copyrighted music. Scene43 memory inserts generated within scene43 only; earlier chapters remain unsubmitted.')
p['prompt_library_references']=['prompt-library/TEMPLATE.md','prompt-library/shots/scene-01/17_a-man-and-a-woman-sit-facing-each-other-at-a-table.md','prompt-library/shots/scene-08/22_medium-shot-on-the-armored-captain-two-agents-carr.md']
(ROOT/'proposal.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'scenes':15,'seconds':sum(c['duration'] for c in p['chapters'][36:51]),'profile':'480p 21:9','maximum_references':max(len(c['linked_asset_ids']) for c in p['chapters'][36:51])}))
