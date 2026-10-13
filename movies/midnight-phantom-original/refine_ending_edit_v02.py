from project_ops import ROOT,helper,commit
p=helper.read(ROOT/'project.json');ch=p['chapters'][-1];src=ch['takes'][-1]
if src['status']!='succeeded':raise RuntimeError('Wait for edit result')
src['quality_disposition']='rejected_partial_scale_edit_pip_green_guard_unchanged'
ch['director_history'].append({'prompt':ch['prompt'],'shots':ch['shots'],'source_take_id':src['id'],'reason':src['quality_disposition']})
a=next(a for a in p['asset_list'] if a['tag']=='@EditSource13');a['candidates'].append({'id':'source_take03','path':src['path'],'provider_task_id':src['task_id'],'duration':src['duration']});a['selected_candidate_id']='source_take03'
ch['prompt']='''VIDEO EDIT — TWO PRECISE CORRECTIONS
Edit @EditSource13, the existing9second21:9 cartoon ending. Keep original action, dialogue, audio, machine/background placement, robot body, and normal speed.

FIRST: REMOVE the GREEN GLOW from the small brown otter in teal cardigan/mustard shirt/russet trousers holding the diamond. This is @Pip. Restore his eyes to plain BLACK pupils on WHITE sclera and put the wire-rim glasses of @Pip portrait on his nose. His eyes never emit light. The ginger otter @Riff eyes also stay BLACK/WHITE. ONLY the gigantic black mechanical bird has GREEN glowing eyes and chest speaker. This color correction applies to ALL frames, including fleeing at7-8seconds.

SECOND: correct ACTUAL FULL BODY SIZE, frame by frame. Keep the complete mechanical bird at exactly its current standing height and RIGHT foot anchor. Make BOTH standing otters precisely ONE QUARTER that complete bird's standing sole-to-crest height: the bird4H, eachotter1H. Relative to current source, SHRINK both otters another25percent uniformly including heads/body/clothes/limbs, fixed shoe/floor pivots. Standing Riff and Pip EXACT equal height despite stocky/slim builds. SHRINK the seated NAVY UNIFORM HOUND near the machine LEFT FRONT CORNER to HALF current complete model size; its lying/seated pose belongs to the same1H standing model as the otters. It is @Guard, not part of machine. Preserve its cap/head/legs and same resting anchor. Do not leave that hound disproportionately large. Use @ScaleReference exact1:1:1:4 dimension diagram only; never show diagrams/labels.
All actor scale reductions persist through the ENTIRE video, INCLUDING the final run; actors must never pop back to their old size. No sudden perspective enlargement. Keep a level fixed ultrawide camera, move brothers LEFT across floor parallel to lens to exit, not toward camera. Crow complete body stays RIGHT, fixed machine rearCENTER, seated hound at machineLEFTFRONTCORNER, rope/window/cable/controller remain.

Shot 1 (0-1s): Crow dark eyes turn green, tiny otter eyes remain normalblackwhite.
Shot 2 (1-6s): Same existing deep dark mechanical baritone: "Very impressive, detectives... but that was only the first test." Complete bird4H, tiny heroes1H and smallseatedhound remain fixedset.
Shot 3 (6-9s): Riff "RUN AGAIN?!" Pip "RUN AGAIN!" Both SAME smallmodelsize run LEFT parallel tocamera with diamond. TO BE CONTINUED at end; fullbird/guard/machine remain.
Identity references @Riff ginger otter rust waistcoat/green trousers/flat ivory inner collar/holster; @Pip chocolate otter teal cardigan/russet trousers/GLASSES; @Guard tan hound navy uniform/tan trousers. These sheets are single actors, not duplicated figures. Original soundtrack/dialogue/voices retained. No slow motion.
'''
ch['tagged_assets']=['@EditSource13','@Riff','@Pip','@Guard','@ScaleReference'];ch['audio']={'generate_audio':True,'dialogue_language':'English','score':'preserve existing native score','crow_voice_reference':'preserve source voice from audio-guided take'}
commit(p,'Refine existing ending edit: remove Pip eye glow, correct guard and tighten quarter-height actors for every frame')
print('Ending focused correction prepared, visual approval',helper.review_state(ROOT,p)['status'])
