"""Direct the authorized remaining source scenes without changing approved images."""
import copy,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper

ROLES={
'@puppy-tart':'ONE small cream Labrador puppy Tart, exactly the supplied puppy image: plush cream fur, floppy ears, dark brown eyes and nose, earnest serious expression. Four legs. No adult dog in ranch scenes.',
'@puppy-tine':'ONE small fox-red Labrador puppy Tine, exactly the supplied puppy image: fluffy red fur, floppy ears, expressive eyebrows, small white heart on HIS ANATOMICAL LEFT rear flank above tail. Four legs; endearing and impulsive.',
'@Tart-working':'ONE adult cream Labrador Tart, plush cream fur, brown collar, tan/brown leather guide harness, curved silver handle with caramel grip. Serious kind face. This is a wardrobe state of Tart, not a second cream dog.',
'@Tart-off-duty':'ONE adult cream Labrador Tart in brown collar ONLY; no guide harness, no vest. Same identity as harnessed Tart, not an additional dog.',
'@Tart-leash':'ONE adult cream Labrador Tart in brown collar and ordinary brown lead; no guide harness. Same single Tart identity.',
'@Tine':'ONE adult fox-red fluffy Labrador Tine, same white heart on HIS LEFT rear flank, orange lead. Orange bandana with round white badge from scene 13 onward; before its first tying in scene 13 use plain collar only. Same dog at every age, never duplicate views.',
'@Mr-Leung':'ONE completely blind middle-aged Hong Kong man, swept dark-grey hair, teal jacket, cream shirt, charcoal trousers, opaque black sunglasses ALWAYS ON. He cannot see, visually track, read, notice visual details or make eye contact. His head responds to sound; hands find objects by touch. LEFT hand grips silver guide handle whenever walking with harnessed Tart.',
'@Kiki':'ONE young Hong Kong community worker, low black ponytail, sage overshirt, cream tee, navy trousers, white sneakers and tan shoulder satchel. Warm quick female English voice. Holds orange lead slack, never pulls dog by neck.',
'@Auntie-Bo':'ONE warm round Hong Kong barista, short curly black hair, salmon blouse, dark green apron, original supplied face. Warm hearty older female English voice. Same Bo in cafe and later harbour.',
'@Mr-Ko':'ONE elderly slender Hong Kong man, messy grey hair, original approved rounded cartoon face, beige cardigan, pale-blue shirt, dark trousers and hooked wooden cane. Gruff but vulnerable; no franchise costume or recognizable borrowed character.',
'@mags':'ONE original Australian ranch woman Mags, long silver braid, straw hat, red plaid shirt, denim overalls and green rubber boots. Brisk warm Australian female voice. Her straw hat can be off her head when the goose has it.',
'@boss':'ONE plump orange tabby shop cat Boss, notched LEFT ear, cream muzzle/chest, smug sleepy eyes. In cafe scenes he lounges on the counter; no backpack unless the scene explicitly requires one. Natural meows/purrs only.',
'@gertrude':'ONE large white goose Gertrude, orange bill and webbed feet, indignant eyebrows. A comical original ranch goose, no speech.',
'@jade':'ONE very small green white-eye songbird Jade, pale belly, white eye-ring. In cage until scene 28 escape; free-flying during rescue, then safely perched alive. She never becomes a pigeon or raptor.',
'@granny-wong':'ONE granny Wong, short grey bob, round glasses and pink cardigan; original approved cartoon face.',
'@granny-lee':'ONE granny Lee, large grey perm, purple cardigan; original approved cartoon face.',
'@granny-chan':'ONE granny Chan, grey bun, yellow cardigan and walking stick; original approved cartoon face.',
'@kookaburra':'ONE cream-and-brown kookaburra with dark eye stripe, perched on ranch fence or veranda. Natural laughing bird call.',
'@black-kite':'ONE black kite raptor, dark brown wings, forked tail and hooked beak, a different much larger bird from tiny green Jade. Threatening flyby only, no animal injury.',
'@sunny-hill-ranch':'ENVIRONMENT geography/materials: original red-roofed weatherboard farmhouse, cream veranda, white picket fence, eucalyptus trees, golden rolling Victorian pasture, red-dust driveway and windmill. Adapt camera crop to 21:9; not an empty plate throughout.',
'@ranch-veranda':'ENVIRONMENT geography/materials: warm timber veranda boards, cream posts and railing, farmhouse door at left, pasture beyond. Same ranch. Adapt camera crop, no reference-sheet framing.',
'@hay-loft':'ENVIRONMENT: open timber hay loft, golden hay, ladder and warm lantern at side; open barn door frames a starry Australian night. Stable physical floor, safe distance from opening.',
'@training-yards':'ENVIRONMENT: blue guide-training yard and separate yellow companion-training yard, practice curbs and simple cones, a solid shared divider. Scene 11 crops them into separate panels; scene 13 alone reveals they are adjacent.',
'@training-hallway':'ENVIRONMENT: bright uncluttered Hong Kong dog-training hallway with pale floor, plant and yellow/blue yard doors. No office signs or floating labels.',
'@leung-flat':'ENVIRONMENT: small tidy Hong Kong high-rise flat, vintage radio, side table with clock, mug/keys, round dog bed near window, towers outside. Bed and tables remain in stable places.',
'@sheung-wan-street':'ENVIRONMENT: colorful old Hong Kong street, green tram tracks, shop awnings, broad pedestrian pavement. Hong Kong LEFT-side traffic and right-hand-drive vehicles.',
'@bo-cafe':'ENVIRONMENT: original tiny green-and-cream tiled corner cafe with golden egg-tart counter; FRONT door camera LEFT, SIDE door camera RIGHT. Keep these two exits fixed through near-miss sequence.',
'@steep-street':'ENVIRONMENT: steep side street descends from fruit stall at top into a level road at bottom; zebra crossing and pedestrian signal at bottom; cafe on corner. Keep downhill axis and crossing distinct.',
'@radio-booth':'ENVIRONMENT: warm acoustic radio booth, microphone, headphones and small red recording lamp. Tart can lie under desk; no editorial ON AIR lettering required.',
'@elder-centre':'ENVIRONMENT: bright Hong Kong community hall, mahjong tables and open space, large windows, low ground-floor sill, Ko quiet window armchair/cage/photo corner. Preserve window position during bird escape.',
'@market-street':'ENVIRONMENT: stepped Hong Kong market lane with striped awnings, dry-fish baskets, shallow street-level passage to stairs leading to rooftops. Keep path open and readable.',
'@rooftops':'ENVIRONMENT: flat adjoining Hong Kong roofs with low parapets, laundry poles, water tanks and tomato planters, one narrow gap. Door/stair arrival stays landward. Clear roof-edge geometry, no impossible maze.',
'@victoria-harbour':'ENVIRONMENT: Tsim Sha Tsui promenade, Clock Tower on landward left, broad terracotta paving, wooden benches, silver water-side railing and Hong Kong Island skyline. Use appropriate source time of day.',
'@mtr-interior':'ENVIRONMENT: Hong Kong subway carriage, blue seats, vertical poles, long windows and driver cab at front; a second train on adjacent track. Populate with a driver and a few passengers.',
'@kiki-flat':'ENVIRONMENT: Kiki warm Hong Kong flat at night, orange dog bed by large window, city lights across rain. No duplicated dogs in windows.',
'@sir-squeaks-whole':'PROP STATE A: ONE intact small BLUE plush platypus, orange bill, two front feet, two rear feet and flat navy tail. Entire before scene 5 final seam tear only. Match blue reference, never brown.',
'@sir-squeaks-head':'PROP STATE B: ONE BLUE torn HEAD HALF only, orange bill, two FRONT feet, ragged open rear seam with white stuffing. No tail or rear feet. Belongs to cream Tart. High SQUEE sound.',
'@sir-squeaks-tail':'PROP STATE C: ONE BLUE torn REAR HALF only, rounded rump, broad flat navy tail, exactly TWO REAR feet and ragged open front seam with white stuffing. NO head, eyes, bill or front legs. Belongs to red Tine. Low HONK sound.',
'@smile-counter':'ONE small silver mechanical handheld tally counter in Kiki hand. Physical rolling digits are incidental; Kiki speaks the count. Progress 0 to 99 in scene 19, stays 99 until scene 33 clicks to 100.',
'@jade-cage':'ONE domed bamboo birdcage with tiny side door/latch. Jade inside until 28; empty during chase. Cage stays safely on sill/floor, not attached to cane or flying with bird.',
'@mei-photo':'ONE physical framed photograph of young Ko and Mei with the bamboo birdcage. BOTH people are stylized original cartoon characters as in approved corrected reference, never realistic human portraits. Mei appears only printed inside this frame, not as a live character.',
'@transport-van':'ONE white puppy transport van with simple blue paw symbol and ventilated secured travel crate. Human DRIVER visibly at wheel in cab whenever van moves. Puppy is safely inside crate, not loose beside driver.',
'@red-taxi':'ONE Hong Kong red taxi, silver roof, roof light with exact black uppercase TAXI. Right-hand-drive HUMAN DRIVER visibly seated at controls through windshield/side window in every vehicle shot. Driver brakes and steers.',
'@green-tram':'ONE green-and-cream Hong Kong double-decker tram. HUMAN DRIVER visible in lower FRONT cab and seated PASSENGERS visible behind windows, even in a passing shot.',
'@orange-cart':'ONE wooden handcart of oranges, two large wheels and handles. This unpowered plot object rolls away because its seller leaves it unsecured; seller chases on foot. It is the intentional runaway cart, not a driverless motor vehicle.',
'@explorer-kit':'Rusty tin bucket used as puppy Tine helmet and oversized brown leather aviator goggles worn by puppy Tart. TWO separate props, one per puppy. Never cover nostrils or glue props to faces.',
}

# Scene-specific geography and demonstrated-risk locks, read alongside source shots.
STARTS={
1:'Morning at original ranch. Establish fence bird and farmhouse, then puppy Tine camera right in bucket, puppy Tart left in goggles. Mags on veranda behind. Exactly two puppies.',
2:'Same ranch morning. Goose sits on Mags straw hat beyond hay bale. Tine bucket and Tart goggles remain. Puppies move left to right toward cabbage patch; goose stays beyond their cover until next scene.',
3:'Tart goggles at left distracts goose at centre, Tine bucket sneaks behind goose at right. Hat lies physically under goose until Tine pulls it free. Pursuit then goes left to right.',
4:'Continue ranch chase: two puppies emerge from sheep and slide downhill left to right into mud at Mags green boots. Tine carries recovered hat. No extra puppy or goose required in foreground.',
5:'Same veranda, now clean wet puppies in shallow tin tub. Mags behind; blue WHOLE toy enters only at 8s. Cream Tart left, red Tine right; no goggles or bucket during bath.',
6:'Immediately after toy tear, same veranda. Exactly two puppies and TWO small separate blue toy halves: cream Tart left owns head/front feet, red Tine right owns rump/tail/rear feet. Visible gap between white torn seams.',
7:'Night hay loft. Puppies curled side by side well inside barn, each with his own blue half. Lantern warms Mags and paws; stars visible beyond open door. Simple intimate three-subject action.',
8:'A few months later inferred through slightly older puppy posture, no caption. White van at red-dust drive, human driver at wheel. Tart ready to leave with HEAD half; Tine stays behind fence with TAIL half.',
9:'Same driveway departure. Human driver moves same white van left to right. Tart safely in secured crate visible through rear window, Tine runs on inside of fence with tail half, then stops at fence corner.',
10:'Full-frame original painted travel-map vignette on warm parchment, no text or labels. Unlabelled Australia lower right, East Asia upper left, blue ocean between. One red dotted travel line; two separate departures one week apart conveyed by clean cut. Original simple plane icons with visible pilots, puppy portrait in passenger window, no copied movie design.',
11:'Hong Kong daytime, then two separate training-yard views in a clean vertical split screen WITHOUT dividing labels. Cream Tart in left panel, red Tine in right. Adults now, plain collars, Tine no bandana yet. Shared-wall relationship not revealed yet.',
12:'Blue guide-training yard. One cream adult Tart in working harness, trainer visible only hands/khaki legs and blue shoes. Open practice hole safely ahead; dog and trainer stay on solid paving.',
13:'Red Tine waits in hallway, plain collar and separate tail-half by paws. Kiki arrives; at 11s she ties orange bandana on Tine for FIRST time. Other panel shows single cream Tart harnessed; final crane reveals solid wall between adjacent yards.',
14:'Two years later conveyed by adult dog, established home and human routine, no caption. Tart collar-only in dog bed hugging HEAD half. Blind Leung sits on bed wearing opaque sunglasses; clock within reach on nightstand.',
15:'Same flat and morning. One Tart starts collar-only beside seated blind Leung. At 11s Leung fits guide harness by touch; after click only ONE fully harnessed Tart remains.',
16:'Morning Sheung Wan. One harnessed Tart guides Leung left to right with LEFT hand on silver handle, pavement separate from tram tracks. Tram driver and passengers visible. Market fish gag, then fixed cafe front-left entry.',
17:'Cafe inside. Bo behind counter, Leung at counter with left hand guide handle, harnessed Tart beside leg. One orange cat Boss lounging on counter. Cat is outside backpack here. Two doorway geography remains fixed.',
18:'Same day at radio desk. Blind Leung wears sunglasses AND headphones and faces microphone by learned position/touch, not by looking at display. One harnessed Tart lies below desk. Small plain red recording light.',
19:'Morning elder centre; Kiki and red bandana Tine approach right to left. Indoors feature dog/Kiki and at most one granny per speaking close-up; other elders soft background. Ko corner remains separate and quiet.',
20:'Same elder hall. Kiki and Tine foreground, isolated Ko window corner with armchair, closed Jade cage and framed CARTOON couple photo. Tiny green Jade stays inside cage. Tine tail half in bandana knot.',
21:'Same Ko chair and window corner. Keep room axes. One pink slipper gag then one tea spill onto raised newspaper; no hot liquid touches a person or dog. Granny Chan in yellow is slipper owner.',
22:'Ko armchair encircled by only four folding chairs, simple readable opening toward camera. Tine creeps beneath one rug, Kiki nearby. Frame of young cartoon Ko/Mei and closed cage on sill stay beside chair.',
23:'Afternoon cafe SIDE-RIGHT entry for Kiki and Tine, SIDE-RIGHT exit later. Bo behind counter, Boss on counter. Heart on Tine LEFT rear. Cat kiss before next scene explains damp ruffled face.',
24:'Exactly one second after Tine left, front-LEFT door admits guide Tart and Leung. Tine and Kiki are already fully out of cafe, never visible through side door. Boss damp and ruffled. Tram outside blocks last chance.',
25:'Morning steep street: fruit cart at top, junction and zebra crossing at bottom. Leung/Tart on pavement at near curb, never in taxi lane. ONE taxi with human driver approaches on level road; seller leaves handcart unsecured.',
26:'Same crossing. Handcart descends hill toward junction; occupied red TAXI travels across level road. Tart and blind Leung stay on near pavement. Hold stable geography: downhill cart behind intersection, taxi crosses screen, humans safely foreground.',
27:'Immediately after near miss. Taxi stops with driver at wheel, cart now stopped in cardboard boxes. Leung/Tart safely on curb, falling oranges land gently. Leung kneels by TOUCH/SOUND; he never watches crash.',
28:'Back at elder centre. Ko armchair with same bamboo cage on low windowsill, side latch facing Tine tail. Tiny Jade inside. Tail-half in bandana knot is a BLUE plush object, not the live green bird.',
29:'Same hall just after Jade escape. Cage EMPTY, window OPEN at ground floor. Tine red bandana listens to Ko, looks at CARTOON photo then open window. Clear safe low window exit onto pavement.',
30:'Market chase right to left: tiny GREEN Jade ahead, red Tine behind, Kiki behind crop. Dried fish attaches to one ear at 5–9s and stays through scene 33. On opposite pavement Tart/Leung walk left to right; occupied tram separates them.',
31:'Tine scrambles from visible stair onto first flat roof, follows green Jade across ONE narrow roof gap. Laundry sheet corner hangs from line; wind pulls sheet across gap. Fish remains on ear. Tomato lands on head at 8–12s and stays through scene 33.',
32:'Continue on second flat roof: Tine has live Jade gently sheltered in closed soft mouth; no biting or swallowing. Dark kite above, fish on ear and tomato on crown. Kiki/grannies/Ko approach through same stair door behind.',
33:'Same rooftop at warm sunset. Fish on ear, tomato still atop Tine head; tiny green Jade steps safely from dog head to Ko finger. Soft background Kiki with counter, three grannies. This is the FIRST laugh/100th smile.',
34:'Same rooftop sunset. Ko seated safely against planter, never roof-edge dangling. Fish/tomato now removed offscreen between scenes. Tine leans into Ko, Jade alive on Ko shoulder. Kiki and three grannies behind.',
35:'Four clean-cut near-miss vignettes. Working Tart/Leung left-to-right, red bandana Tine/Kiki right-to-left. Each location is a separate cut, not all landmarks in one frame; dogs remain unaware of each other.',
36:'Busy crossing daylight, working Tart/Leung safely on pavement; taxi honk, occupied minibus honk, human nose-trumpet. Then clean night cut to two separate bedrooms/toy halves, then city windows. No real reunion until scene 38–43.',
}
LOCKS={
1:'Bucket is Tine helmet; goggles are Tart only. Four paws each, props move with normal weight. Natural bird laugh, no human words from bird.',
2:'Mags voice only, no extra Mags body. Hat must leave Mags head before goose sits on it. Goat/sheep are far background; no third puppy.',
3:'Goose never bites or harms puppies. Laundry boxer gag rests on goose head while bill remains clear. Two real sheep hide puppies; no dog-sheep body morph. The attempted baa is a wavering puppy whine, not spoken words.',
4:'Mud changes surface fur only, not puppy colors/identity. Hat visibly drops at green boots before Mags picks it up. Play briskly, no slow motion on mud splash.',
5:'Whole toy until 20s. At the 20s close cut its middle fabric seam separates once with tiny stuffing tuft; Tart holds HEAD/FRONT feet on LEFT, Tine holds TAIL/REAR feet on RIGHT. Exactly TWO pieces after rip, no duplicate whole toy. Do not attach a head/front feet to the rear half.',
6:'TWO separate blue halves always remain separate physical objects. Tart head half left; Tine rear half right with exactly two rear feet and flat tail. Show white torn seams when pressed edge-to-edge, never fuse or exchange owners. Paired SQUEE-HONK timing, no talking toys.',
7:'Mags gently brings one puppy paw from each dog together, then releases; puppies keep contact. Four legs per puppy. Toy pieces rest on hay, not floating. Star streak is brief; all acting normal speed.',
8:'The van has an actual human driver visibly seated before departure; crate stays safely secured in rear. Tine remains on ranch side of fence and never enters van.',
9:'Tart is seen THROUGH rear glazing and crate bars, not perched outside vehicle. Same driver remains in front; no camera angle that accidentally empties cab. Tine keeps his tail half, Tart keeps head half.',
10:'Retain original travel-map beat without any titles, place labels, captions, week numbers or text boxes. Two unlabelled plane icons, first cream puppy in passenger window, second red puppy; a small distinct HUMAN PILOT visible in each cockpit. No real dogs in cockpit and no franchise planes.',
11:'Native split-screen has two independent yard views, not cloned dogs. At most ONE Tart per left panel and ONE Tine per right panel; no bandana before scene 13. Trainers cropped at knees. Pigeon attraction is Tine only; disciplined Tart never chases.',
12:'Leung is NOT the trainer in this scene. Trainer feet stop before practice hole; dog blocks path on firm ground. No falling person. Harness stays fitted; handle connects hand to back, never mouth.',
13:'Tine tail-half stows in loose orange bandana KNOT, no constriction. Two schools separated by a SOLID brick wall: no peeking through and no eye contact between dogs. Crane reveals both backs against opposite faces of same wall, still apart.',
14:'Blind Leung finds clock/keys/mug only by touch; sniff/head tilt reports garlic and warm air. No sight or eye tracking. Sunglasses on from first appearance. One Tart only; head half remains bed, keys go to open palm.',
15:'Two Tart reference states describe one continuous dog. Collar-only becomes harnessed after tactile buckling; never two cream dogs. Leung left hand finds and holds handle after fitting.',
16:'Tram has human driver and visible passengers. Fish is a slapstick market fish, retrieved without harm; no permanent fish remains on Tart entering cafe. Leung reacts to grouper smell and harness pressure, never sees fish or boxes.',
17:'One cat on counter, one harnessed dog below, no cat backpack. Leung identifies wag by transmitted handle movement and touch. Biscuit remains in harness pocket for later; no eating while working.',
18:'No readable floating ON AIR caption. Red physical lamp sufficient. Leung never reads monitor or paper. One human voice at a time, radio lines brisk but intelligible, dog reacts with huff only.',
19:'Three grannies always pink/purple/yellow. Simple mahjong tile on dog forehead only, no character-text close-up required. One brief hind-leg tai chi wobble then lands cushion, no sustained human anatomy. The count reaches 99 only, Kiki says numbers aloud.',
20:'Jade remains behind cage bars. Mei and young Ko exist only PRINTED in frame, both CARTOON style; no realistic portrait. Ko reads ordinary newspaper prop; avoid editorial text added over image. No smile yet.',
21:'Cup contains cooled tea, spill catches raised newspaper; Ko face remains dry. No harm, no scalding, no impossible multiplying cups. Attempt numbers are NOT displayed as text.',
22:'Kiki guides Tine back using loose orange lead/hand near chest, not yanking neck bandana. Ko taps cage gently with Jade safe inside. Photo couple is cartoon; Tine understands loneliness through body acting.',
23:'Maintain front-left/side-right cafe map. Tine genuinely licks Boss once; no biting. Hand-propelled delivery trolley has worker pushing it. Dogs not yet near each other on screen.',
24:'Tine absent throughout this chapter. Tart briefly follows scent but stops because working, never abandons blind handler. Handle stays in LEFT hand. Occupied tram has human driver and passengers through windows; Boss damp fur continuity.',
25:'Only the unpowered runaway handcart is intentionally unattended; powered traffic always occupied. Slow/fast beeps motivate Leung command. Safety axis clear: dog/human wait BEHIND curb, cart comes from hill, taxi travels level road.',
26:'Tart refuses forward movement and pulls blind Leung BACK from curb; Leung does not dodge because he sees danger. He infers walk signal from beeps. Taxi DRIVER at wheel steering/braking, roof light TAXI; no collision with person/dog. Cart crashes only into EMPTY cardboard boxes.',
27:'Driver speaks from visibly occupied taxi window. Leung responds to tires/wind/touch, not visual crash. Orange perched briefly on Tart head is gentle comic impact; no blood or injury. Tail wag is natural acting at normal playback.',
28:'Cage latch opens due to visible tail CONTACT once; green Jade exits exactly ONE side door then open hall window. Tail plush remains blue and distinct from bird. No duplicate birds. Counter still 99.',
29:'Exactly ONE small green Jade has already left, not still in cage/photo. Tine jumps low ground-floor window to safe pavement, not from high storey. Ko is frightened and grieving; no physical violence.',
30:'Pigeon is grey, Jade green, kite not here yet. Tine resists pigeon distraction, keeps rescuing Jade. Fish hides scent at near miss. Tram driver and passengers present. Dogs never notice one another.',
31:'One narrow gap, sheet attached to taut laundry line, wind swings dog to next roof. No teleporting rooftop maze. Kite misses Jade; Tine shelters bird softly, no wounds/blood/biting. Fish and tomato retained as light gags.',
32:'Green Jade ALIVE and intact in soft mouth, no visible biting or swallowing. Dog opens mouth once; tiny bird hops to nose then crown. Fish stays on one ear and tomato on crown beside bird, no object morph. Kite flies away.',
33:'Jade hops from crown onto Ko finger; tomato remains until end of scene. Counter changes 99 to 100 once, Kiki announces ONE HUNDRED; no giant number overlay. Ko laughter is first softened reaction to dog.',
34:'Cleaned fish/tomato props absent now. Ko scratches behind ear and dog hind leg thumps naturally. Jade perched on shoulder, not cage. Three grannies soft background, no extra lead/cage multiplying.',
35:'No place/date/caption cards. Four locations conveyed by lion dance, lanterns, occupied trains, rain. Every moving train has a HUMAN DRIVER in cab and passengers; a brief exterior/cab angle can show this before window near miss. Lion/rabbit are generic festival crafts, no franchise characters. Typhoon windows use collar-only Tart.',
36:'Red taxi roof light TAXI and human driver. Green MINIBUS has human driver plus at least two seated passengers visibly through glazing. Old man alone makes trumpet-like nose sound. Bedroom Tart collar-only; head half belongs Tart, tail half Tine, no reunion or shared room.',
}

def clean_action(action):
    # User explicitly prohibited editorial titles/captions; source stays immutable.
    action=re.sub(r'\*CAPTION:\s*"[^"]*"\*','',action)
    action=re.sub(r'^\s*-\s*$','',action,flags=re.M)
    action=re.sub(r'ATTEMPT #\d+:\s*','',action)
    action=re.sub(r'\n---\s*$','',action)
    return action.strip()

def main():
    p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=copy.deepcopy(p)
    assert p['revision']==22,'Resume from current canonical state; do not overwrite later edits'
    q.setdefault('render_scope_history',[]).append(copy.deepcopy(p['render_scope']))
    q['render_scope']={'scene_start':1,'scene_end':36,'duration_seconds':740,'resolution':'480p','aspect_ratio':'21:9','assembly_scene_start':1,'assembly_scene_end':51,'assembly_duration_seconds':1045,'authorization':'Direct user request 2026-10-20: generate remaining scenes 1–36, 480p 21:9, and stitch whole movie 1–51.'}
    # Preserve the historical base ratio in dependency hashes of the existing finale.
    # Each NEW prompt and actual API request explicitly binds its own 21:9 profile.
    q['source_format_mode']='mixed_source_profiles'
    q['generation_profiles']={'scenes_01_36':{'aspect_ratio':'21:9','resolution':'480p','reason':'Latest explicit user request'},'scenes_37_51':{'aspect_ratio':'16:9','resolution':'480p','reason':'Previously generated and delivered immutable sources; reuse only'}}
    q['assembly_profile']={'aspect_ratio':'21:9','resolution':'480p','fit_existing_16x9':'preserve_full_frame_with_sidebars_pending_optional_user_preference','fps':24}
    q['render_constraints']=['NEW generation scope: chapter_01 through chapter_36 only; reuse existing 37–51 footage','New API request resolution 480p, ratio 21:9','All powered vehicles have drivers; buses/minibuses/trams/trains have driver and passengers','Blind Leung cannot see; opaque sunglasses and sensory acting','Supplied puppy identities preserved; original cast, no franchise characters','Blue toy halves have fixed owners; rear half exactly two rear legs, no head/front legs','No slow motion, speed ramps or stretch-to-fill','No title, subtitles, captions, text boxes or graphic overlays; scene 10 travel motif is within the native scene with no lettering']
    q['continuity_bible']['edit']='Keep original scene boundaries. No title/caption/text overlays. Scene 10 travel vignette has no labels; scene 50 uses existing clean harbour aerial. Source/native sound retained; full movie assembled in scene order.'
    q['continuity_bible']['tine']='Orange bandana first tied in scene 13; blue tail-half in its knot thereafter. Fish on ear scenes 30–33; tomato on crown scenes 31–33; both removed before 34. Left rear white heart follows supplied reference.'
    q['stage']='remaining_scenes_directed';q['render_status']='ready_for_scenes_01_to_36'
    q.setdefault('script_changes',[]).append({'at':'2026-10-20','scope':'1–36','change':'Retain source duration and every scene. Remove editorial captions/title labels; keep scene 10 journey motif without words. Use tactile/sound blindness locks, occupied vehicles, blue split-toy anatomy, simple staging. Existing scenes 37–51 and assets unchanged.'})
    package=ROOT/'exports/scenes-01-36-render-package-r23';package.mkdir(parents=True,exist_ok=False)
    for c in q['chapters'][:36]:
        n=c['chapter_index'];c['resolution']='480p';c['generation_profile']={'ratio':'21:9','resolution':'480p','generate_audio':True}
        for s in c['shots']:
            s['action']=clean_action(s['action']);s['status']='directed'
        if n==10:
            c['shots'][0]['action']='TRAVEL VIGNETTE — Original warm painted parchment map with unlabelled Australia, Asia and blue ocean. Red dotted path draws toward Hong Kong coast as a simple original rounded plane icon flies along it. Cream Tart visible in passenger window holding BLUE head half; distinct small human pilot in cockpit. No lettering, captions or week numbers.'
            c['shots'][1]['action']='CLEAN CUT TO SECOND DEPARTURE — Same route and framing, now a second separate plane icon carries red Tine with BLUE rear/tail half in passenger window, its own small HUMAN PILOT in cockpit. Route ends beside a simple Hong Kong skyline silhouette. Dogs travel on separate journeys, not one shared plane. No labels or titles.'
        if n==18:
            c['shots'][0]['action']=c['shots'][0]['action'].replace('A red "ON AIR" light glows.','A small plain red recording lamp glows.')
        if n==6:
            c['shots'][2]['action']='TWO-SHOT — Tine tail begins wagging. Red Tine noses his own blue tail/rear-feet half toward cream Tart own head/front-feet half, stopping with a visible small gap between the white torn seams. Each dog keeps his own piece, left cream/right red.'
            c['shots'][3]['action']='MEDIUM — Cream Tart gently compresses his separate head/front-feet half while red Tine compresses his separate tail/rear-feet half: paired "SQUEE-HONK!" The torn edges remain visible and do not fuse. Both puppies roll and yip with joy.\n- **MAGS** *(smiling)*: "Two halves of the same silly thing. That\'s you two, alright."'
        if n==22:
            c['shots'][2]['action']=c['shots'][2]['action'].replace('gently pulls Tine back by his bandana','gently guides Tine back using his slack orange lead and a hand near his chest')
        active=helper.active_assets(q,c)
        roles='\n'.join(a['tag']+': '+ROLES.get(a['tag'],a['description']) for a in active)
        timeline='\n\n'.join(f"SHOT {i+1} ({s['start']}–{s['end']}s). "+('OPEN. ' if i==0 else 'CLEAN CUT. ')+s['action'] for i,s in enumerate(c['shots']))
        lens=('24–35mm low tracking for clear physical action, 50mm medium performance, 85mm brief expression/prop insert; fixed screen axis during each action, motivated hard cuts.' if n in [2,3,4,11,16,25,26,28,30,31,32,35,36] else '35mm establishing/two-shot, 50mm medium human/dog interaction, 75–85mm expression or tactile prop insert. Keep faces and needed hands/paws inside the 21:9 crop; no empty padding.')
        c['prompt']=f'''SCENE CONTEXT
Scene {n}: {c['title']}. An original animated Tart-and-Tine story. Follow the consecutive timed shots and their causal actions, not a summary montage. {c['scene_summary']}

OUTPUT / FORMAT
Exactly {c['duration']} seconds. Native provider 480p profile, 21:9 widescreen. All action at normal speed: no slow motion, speed ramps, time stretching, frozen padding or copied franchise characters. Original warm rounded cinematic 3D animation with tactile plush fur, expressive original faces, soft warm global illumination, painterly sky, cream/fox-red/teal/gold palette, saturated gentle colours and cinematic depth of field. These are fictional cartoon characters, not realistic human portraits. Scene 10 alone is the screenplay's original painted travel vignette rendered as moving native footage, with no lettering.

ACTIVE APPROVED REFERENCES
{roles}
Multi-view sheets each represent ONE identity. Use reference images for identity, wardrobe states, prop shape and environment geometry, not studio backgrounds, turnarounds or duplicated subjects. Different Tart state references are one dog, never multiple cream dogs. Only subjects called for by each timed shot are visible; other references stay out of crop or soft background.

FIRST FRAME / LOCATION MAP
{STARTS[n]}

FRAMING / OPTICS / CAMERA
{lens} One main physical action per shot, clear foreground/midground/background, generally at most three featured acting subjects; others are background. Keep simple paths, grounded contacts and readable spacing. No copied reference borders.

TIMELINE / PERFORMANCE
{timeline}

CONTACT / PHYSICS / CONTINUITY LOCKS
{LOCKS[n]}
Every visible powered vehicle has a human driver/pilot/captain at controls. Every bus, minibus, tram or train also has passengers. Hong Kong traffic is left-side and taxis right-hand-drive. The unpowered runaway handcart is the intentional story exception and has its seller chasing it. Keep animal anatomy coherent, no extra legs or duplicate dogs. Toy is BLUE; head/front-feet half belongs Tart, tail/rear-feet half belongs Tine. Completely blind Leung responds ONLY to sound, smell, touch and memory, never visually tracks anything; opaque sunglasses stay on, left hand on harness handle whenever guiding.

LIGHTING / EDIT HANDOFF
Match the source scene's time of day and approved location materials, stable motivated lighting within each shot. Preserve props and axis: Tart left to right and Tine right to left in parallel Hong Kong journeys; ranch chase uses explicit source left-to-right. Clean cuts between source shots; no dissolve that merges dogs or objects. Last instant remains a usable living pose/action for the following scene, never a frozen still.

AUDIO
Native synchronized English HUMAN dialogue only, exact quoted lines in timed shots, one speaker at a time with natural brisk articulation and expressive pauses. Distinct consistent original voices: Mags warm brisk Australian woman; Leung gentle middle-aged Hong Kong male with radio-host delivery; Kiki bright warm young Hong Kong female; Ko gravelly elderly Hong Kong male; Bo hearty older Hong Kong female. Trainers/market seller/taxi driver/grannies are short supporting voices as labelled. Animals make natural barks, whines, panting, meows, bird chirps and goose honks, never human words or word lip-sync. Original playful orchestral/pizzicato waltz and paired high-SQUEE/low-HONK motif below dialogue, source scene music mood; no copied film recording. Foley follows real contacts, with atmosphere appropriate to ranch/city/interior. No forced silence or audio-text captions.

FINAL DELIVERY LOCK
Native moving animation fills the 21:9 frame. NO opening title, ending title, subtitle, caption, text box, speech bubble, watermark, reference-sheet label or editorial graphic overlay. No place/date/week/attempt labels. Human dialogue is heard only. Physical prop details such as TAXI roof light or small mechanical counter digits may exist naturally inside the scene. Scene 10's map geography and route are unlabelled. No Pixar/Disney characters, logos, copied costumes or recognizable replicas.
'''
        c['prompt_status']='directed_approved_assets_ready'
        c['initial_prompt']=c['initial_prompt'] or c['prompt']
        c['handoff']={'mode':'approved_environment_and_explicit_text','reason':'Use approved identity/location references and written prop/axis state; clean-cut new camera angles and time/location changes do not require automatic previous-clip input. Inspect actual handoffs and derive one narrow frame only if a demonstrated mismatch warrants it.','start_state':STARTS[n],'end_state':c['shots'][-1]['action'],'audio_boundary':'Native ambience/dialogue preserved, short local edge fades only; no time stretching.'}
        (package/(c['id']+'-director.txt')).write_text(c['prompt'],encoding='utf-8')
    # Old finale dependencies must stay current and remain selected.
    for before,after in zip(p['chapters'][36:],q['chapters'][36:]):
        assert before==after
        assert helper.chapter_fingerprint(ROOT,p,before)==helper.chapter_fingerprint(ROOT,q,after)
    print(helper.save(ROOT,p,q,'Direct remaining original scenes 1–36 for approved 480p 21:9 generation; preserve existing finale and source assets'))
    print('Directed 36 scenes, total',sum(c['duration'] for c in q['chapters'][:36]),'seconds; finale fingerprints unchanged.')

if __name__=='__main__':main()
