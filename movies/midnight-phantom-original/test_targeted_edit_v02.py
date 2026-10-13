from project_ops import ROOT,helper,commit,write_json
p=helper.read(ROOT/'project.json');ch=next(c for c in p['chapters'] if c['id']=='chapter_13');source=ch['takes'][-1]
if source['status']!='succeeded':raise RuntimeError('Existing ending required')
source['quality_disposition']='rejected_v02_scale_and_pip_green_eyes'
asset={'id':'asset_edit_source_13','tag':'@EditSource13','name':'Existing v02 ending to edit','category':'reference','description':'Successful native v02 ending take02; motion/audio source for targeted scaling and eye-color correction. Preserve successful geometry and whole Crow body. Video not image reference.','source':'generated','media_type':'Video','reference_paths':[],'status_variants':[],'candidates':[{'id':'source_take02','path':source['path'],'provider_task_id':source['task_id'],'duration':source['duration']}],'selected_candidate_id':'source_take02'}
if any(a['id']==asset['id'] for a in p['asset_list']):raise RuntimeError('Edit already prepared')
p['asset_list'].append(asset)
ch.setdefault('director_history',[]).append({'prompt':ch['prompt'],'shots':ch['shots'],'source_take_id':source['id'],'reason':'Scale about2x instead4x; Pip eyes incorrectly green.'})
ch['prompt']='''SCENE CONTEXT / VIDEO EDIT
EDIT THE VIDEO @EditSource13. It is an existing9second21:9native720p original cartoon ending. Preserve its scene, shot timing, complete mechanical Crow body, machine at rear-center, slumped guard, floor, rope, cable, curtain, score, spoken words, voice identity and normal-speed run. Make these targeted visible corrections:

1. SCALE: The two brothers and hound guard are TOO LARGE relative to Crow. SCALE DOWN ALL THREE SMALL ACTORS UNIFORMLY TO ONE HALF their current model size, head/body/limbs/clothes together. Their floor-contact anchors and movement paths remain in exactly the same world locations. Do not scale the background or Crow. Crow must be FOUR TIMES the complete standing sole-to-highest-head/cap height of each small actor. Riff=Pip=Guard1H, Crow4H. Use @ScaleReference for mathematically exact1:1:1:4. Crow near560px sole-to-crest in a1470x630wide, EACH small standing hero only140px high. If Crow is450px in a frame, each hero is112.5px, not200px. Heroes heads near Crow ankles/lower shin, never belly or hip. Guard slumped body remains proportionate to the same1H standing model. All same floor plane, no forced-perspective cheat. Riff and Pip standing heights EQUAL.
2. EYES: ONLY @Crow eyes and mechanical chest speaker turn green. @Pip eyes stay black/white with wire-rim GLASSES; no green glow on Pip or Riff. Crow eyes start DARK, then turn green within firstsecond, never red during warning.
3. BODY/PLACE: complete attached Crow head/body/wings/legs/claws remain upright at exact RIGHT anchor throughout. One robot, no floating head. Fixed rear-center @Machine, slumped @Guard at machine left-front, stationary clamped cable and right controller remain present. Never move machine closer to camera.

IDENTITY REFERENCES
@Riff ginger stocky otter, rust waistcoat, flat tucked ivory shirt collar, green trousers, brown shoes, white gloves, small right-hip holster. @Pip chocolate slim otter, teal cardigan, mustard shirt, russet trousers, navy shoes, white gloves, wire-rim glasses. @Guard same tan hound guard navy uniform/tan trousers, slumped at existing position. Sheets depict ONE character with attached head, no duplicated actors.
@TowerLayout fixed world placement only; it describes the SAME robot/machine in video, not additional copies. @Diamond single recovered golden diamond remains in Pip glove. @CrowVoice voice timbre/pitch guide only for existing warning, not its sample words or score.

TIMING AND AUDIO
Shot1(0-1s): Full robot in fixed wide stage: dark eyes turngreen. Small brothers recoil normally.
Shot2(1-6s): SAME deep dark ominous Crow baritone says "Very impressive, detectives... but that was only the first test." Entire scaled stage intact. Heroes eyes normal.
Shot3(6-9s): Riff says "RUN AGAIN?!" Pip says "RUN AGAIN!" Both tiny1H brothers run visibly LEFT holding diamond; full4H robot and guard/machine stay. TO BE CONTINUED at end. Preserve the source English words, brisk jazz, Foley and voice identity; normal speed, no slow motion or slow reactions.

POSITIVE CONSTRAINTS
This is an EDIT of source video, not new scene reconstruction. Change actual actor SIZE and eye colors, not labels. Exact1:1:1:4 with stable model proportions. Preserve input aspect ratio21:9 and runtime. Native720p. No diagrams, labels, extra figures or missing background elements.
'''
ch['tagged_assets']=['@EditSource13','@Riff','@Pip','@Guard','@Crow','@Diamond','@Machine','@TowerLayout','@ScaleReference','@CrowVoice'];ch['generation_mode']='edit'
ch['shots']=[dict(start=0,end=1,action='Dark Crow eyes become green; tiny1H heroes react.',camera='Existing source wide.',audio='Crackle',end_state='Green Crow eyes, normal hero eyes.'),dict(start=1,end=6,action='Full4H Crow delivers existing warning; all scene elements present.',camera='Existing source wide.',audio='Same warning and Crow voice.',end_state='Tiny heroes ready to run.'),dict(start=6,end=9,action='Tiny1H brothers visibly run left holding diamond; Crow/guard/machine remain.',camera='Existing source wide.',audio='RUN AGAIN exchange and existing music.',end_state='Full Crow right, other set anchors remain.')]
ch['handoff']=ch['shots'][-1]['end_state']
commit(p,'Reject underscaled ending and prepare targeted video edit using approved images and existing generated motion source')
print('Ending scale/eye edit prepared; image approval remains',helper.review_state(ROOT,p)['status'])
