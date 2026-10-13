"""Targeted existing-video repair definitions, to use after edit strategy inspection."""
from project_ops import ROOT,helper,commit,write_json
targets={
1:'Match Riff, Pip and Guard EXACT equal standing sole-to-highest-head/cap height,1:1:1. Guard is too large: reduce guard uniformly to same standing model size as brothers, retaining costume, feet, acting and placement. Maintain flat tucked Riff collar. Same-plane actors must not have different model sizes. Pip always wire-rim glasses.',
3:'Crow is too small. Keep Crow full model size and SCALE DOWN Riff and Pip whole models to ONE HALF current size so Crow is FOUR TIMES their standing sole-to-head height. Keep hero shoe/floor anchors and bin-climbing paths, scaled limb movement. Bin is ordinary fixed environment; exactly two attached symmetrical lids stay open; no outdoor feathers. One Crow, no flying disconnected beak.',
4:'Keep actual pistol firing, two attached open bin lids and departure. Crow is too small: SCALE DOWN both brothers whole models to half current size so Crow stands FOUR TIMES each hero total standing height. Match Riff and Pip equal standing size. Pip head pops up from INSIDE bin at9seconds before shown climb-out. Both feet land on pavement only after climbing. Pistol drawn from right-hip holster; barrel fires, then visibly reholstered. Crow deep dark ominous same baritone as voice guide, no pitch/identity change.',
6:'Scale Riff and Pip uniformly to HALF current size so full Crow remains4x their standing heights. Preserve the shown close ramp and adjacent tower-window launch, separate badger driver in cab and truck outside. The main two-coil machine MUST REMAIN at fixed rear-center anchor throughout, including final wide after clock detail; restore it when source frame empties platform. In first interior shot rope already hangs left-center, cable already clamped and static, controller remains behind right curtain. Numberless clock face only ticks and two nearly still hands, no new numbers. No room-layout shift.',
7:'Scale both brothers uniformly DOWN to HALF existing size, exact equal1H standing height, while Crow model and anchored set remain unchanged4H. Heroes heads near Crow ankle/lower shin, never hip/belly. Preserve same deep dark ominous voice. Riff must stay tiny when challenging and standing on trapdoor. Existing rope visible throughout before trap opens, stationary clamped red cable from firstframe. Keep machine fixed REAR CENTER, one Crow at RIGHT, diamond in same talon.',
8:'Repair first0-4seconds: Start Riff STANDING on CLOSED trapdoor left beside the already visible rope. Trapdoor opens visibly; Riff drops DOWN0.5H, reaches SIDEWAYS and grips existing rope with BOTH gloves to stop fall. Never jump UP to rope or begin suspended above floor. After4seconds Riff remains low at same rope, no bouncing. Uniformly shrink Riff/Pip whole models to HALF current size so Crow4H versus each1H. Cable route remains IDENTICAL immobile clamped path from framezero: Crow feet along floor to right-curtain controller, no new loop/curve, no dragging/following Pip. Pip WALKS beside cable to curtain, glasses on face. Machine rearcenter unchanged.',
9:'Crow4H, Riff/Pip/guard each1H: uniformly shrink all three small actor models to HALF current size, equal standing heights despite different builds. Same fore-aft plane, feet remain existing world anchors. Guard feet naturally BOTH forward. Fixed console at far-right curtain, only one console, remove newly appearing red switch fixture on wall right. Clamped red floor cable stationary. Riff remains HOLDING same rope in low suspended position throughout, feet near hole rim rather than standing or floating high. Preserve reveal, mudtread clue, dialogue and pacing.',
10:'Uniformly shrink Riff,Pip,Guard whole models to HALF source size, exact equal standing1H while existing full Crow remains4H. Keep backward-forward pendulum swing on same rope; on forward arc extend ONLY ONE right leg to kick guard belly, other knee tucked. Do not bounce up/down. Guard kicked backward to fixed Machine LEFT FRONT CORNER, which is exact final slumped guard anchor for following clips. Guard never goes to window or robot feet. Riff releases only afterkick then lands on solidleftfloor. Machine anchored REARCENTER never moves; Crow full4H feetplantedRIGHT. Preserve launch single diamond and existing3,2,1countdown.',
11:'Uniformly scale both brothers and slumped guard DOWN to HALF current model size, equal1H standing bounds, full Crow unchanged4H right. Move slumped guard from wrong window/leftforeground to fixed Machine LEFT FRONT CORNER, same place collision left guard at previous ending. Keep guard at that world anchor throughout with body intact. Machine rearcenter, Crow right in place fully attached body, dark eyes after powerdown; no scrap or disappearing body. Preserve single diamond catch, midnightchimes, citylightsstayON.',
12:'Uniformly shrink Riff,Pip,Guard whole models to HALF current size; enforce equal standing1H heights for brothers despite stocky/slimbuilds. Full Crow stays4H. Crow eyes must be DARK/inactive throughout this banter, neverred; robot fullyintactuprightRIGHT. Guard slumped at Machine LEFT FRONT CORNER, samepreviousclipanchor, not infrontofCrowfeet. Machine offREARCENTER unchanged. Preserve existing banter and diamond inPipglove. Fixed cable/console/rope allpresent.'}

def apply(chapter_numbers):
 p=helper.read(ROOT/'project.json');report=helper.read(ROOT/'exports/continuity-v02-first-pass-review.json')
 for n in chapter_numbers:
  ch=next(c for c in p['chapters'] if c['chapter_index']==n);source=next(t for t in ch['takes'] if t['id']==('take_03' if n==1 else 'take_02'))
  if source['status']!='succeeded':raise RuntimeError('Repair source not successful')
  aid=f'asset_edit_source_{n:02d}';tag=f'@EditSource{n:02d}'
  if any(a['id']==aid for a in p['asset_list']):raise RuntimeError('Repair already prepared '+aid)
  p['asset_list'].append({'id':aid,'tag':tag,'name':f'Existing chapter{n:02d} v02 motion source','category':'reference','description':'Existing successful generated motion/audio clip for targeted continuity repair. Source scale/placement mistakes are corrected by text instructions and approved numeric scale/image identity guides.','media_type':'Video','source':'generated','reference_paths':[],'status_variants':[],'candidates':[{'id':'source_v02','path':source['path'],'provider_task_id':source['task_id'],'duration':source['duration']}],'selected_candidate_id':'source_v02'})
  source['quality_disposition']='needs_targeted_continuity_edit';source['quality_notes']=next(o['notes'] for o in report['chapters'] if o['chapter_id']==ch['id'])
  ch.setdefault('director_history',[]).append({'prompt':ch['prompt'],'shots':ch['shots'],'handoff':ch['handoff'],'source_take_id':source['id'],'reason':source['quality_notes']})
  old=ch['prompt'];refs=old.split('ACTIVE REFERENCES\n',1)[1].split('LOCATION MAP\n',1)[0];timing=old.split('ACTION TIMING\n',1)[1].split('PHYSICS / IDENTITY / SCALE\n',1)[0]
  ch['prompt']=f'''SCENE CONTEXT / VIDEO EDIT
EDIT THE VIDEO {tag}, the existing {ch['duration']}second21:9 native720p original hand-drawn cartoon. Keep source original story, English words, score, Foley, voices and real-time pace. Repair the following actual continuity mistakes while preserving successful staging and action:

TARGETED REPAIR
{targets[n]}

PRECISE DIMENSION LOCK
The old video has actors TOO LARGE. Change actual whole model size, not just labels or cropping. Riff=Pip=Guard1H; full Crow4H. Four complete equal hero heights stacked vertically equal Crow sole-to-crest height. If Crow projected standing height480px, each same-plane small actor120px. All models uniformly scaled including heads, torsos, limbs and costume. Do not keep old near-human-sized Crow proportion. Body pose does not rescale the model. Same floor anchors and depth; no perspective tricks. @ScaleReference is numeric dimension diagram only, not visible boxes in art. Maintain every face/costume exactly, Pip glasses and Riff flat tucked collar/holster. No green glow on hero eyes. Red/green belongs only to Crow in prescribed state.

ACTIVE REFERENCES
{tag}: source video to EDIT, motion/audio/timing source only. Its wrong scale and object drift must be corrected.
{refs}

FIXED GEOGRAPHY
When tower visible: approved TowerLayout controls immutable WORLD anchors, windowLEFT, ropeLEFTCENTER attachedsamebeam, trapdoorbelow, mainmachineREARCENTER against clockwork, completeCrowRIGHT feetneverrelocate, stationaryclampedredfloorcable to simplecontroller behindFARRIGHTcurtain. One machine and one Crow only; map/sheets are same actor/prop as source, no duplicates. Keep slumpedguard atmachineLEFTFRONTCORNER aftercollision; in banter all three remainvisible. Only actor movement specified in story, neversetmovement.

ACTION TIMING
{timing}

PHYSICS AND AUDIO
Keep existing rhythm and cause/contact/gravity, no teleport or new props. No slow motion, speedramp, dreamypause or timestretch. Preserve source English words/score/Foley and speakeridentity. If Crow speaks, same deep dark ominous voice as reference AUDIO, neverthe guide's samplewords. Real-time cartoon acting remains funny yetthrilling.

POSITIVE CONSTRAINTS
Targeted VIDEO EDIT, retain input21:9 andduration, native720p. Do not reconstruct unrelatedscene. No referenceboxes,labels,panels,numericalclocks,extraactors or floatinghead. Characterprops/clothingandsetpositionsstable. Ending follows existing story handoff with repairedscale/geography.
'''
  ch['tagged_assets'].append(tag);ch['generation_mode']='edit'
  write_json(ROOT/f'chapters/{ch["id"]}/director-v02-edit.json',{'prompt':ch['prompt'],'shots':ch['shots'],'source_take_id':source['id']})
 commit(p,'Prepare targeted existing-video continuity edits using unchanged approved visual references')
 print('Prepared edits',chapter_numbers,'image approval',helper.review_state(ROOT,p)['status'])

if __name__=='__main__':
 import sys
 apply([int(x) for x in sys.argv[1:]])
