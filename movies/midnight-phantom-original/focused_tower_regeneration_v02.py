from project_ops import ROOT,helper,commit,write_json
p=helper.read(ROOT/'project.json')
base='''OUTPUT SETTINGS
Original hand-drawn2D rubber-hose detective cartoon, bold ink, painted indigo/amber clock tower, lively funny/thrilling acting. Fullframe21:9 native720p. ONE CONTINUOUS LOCKED WIDE SHOT, no cuts, zooms or camera moves. Real time, no slow motion, no speedramp. Do not copy source video; generate new prescribed action.

ACTIVE REFERENCES
@Riff ONE ginger otter, rust waistcoat, tucked flat ivory shirt collar, green trousers, brown brogues, white gloves, small leather right-hip holster. Bare furry head, no hat.
@Pip ONE chocolate otter, WIRE-RIM GLASSES, teal cardigan, mustard shirt, russet trousers, navy shoes, white gloves. Black/white eyes, no green glow.
@Crow ONE colossal black riveted mechanical bird, complete attached head/body/wings/legs/claws, red eyes, beak and chest speaker. Uniform complete model4METERS TALL. Otters each1METER TALL. The bird is FOUR TIMES each whole otter height, not just a bigger head.
@TowerLayout FIXED environment and same bird/diamond: moon windowLEFT, machineREAR-CENTER against clockwork, hanging hoist ropeLEFT-CENTER attached to beam, trapdoor belowropeLEFT, red cable clamped along floor to fixed joystick console behindFAR-RIGHT curtain. This is same one bird and one machine, not duplicate props. Geometry stays unchanged.
@ScaleReference mathematically EXACT standing height1:1:1:4. Dimensions only; no boxes, grid or text appear in art. Character sheets supply faces and wardrobe, assemble ONE fullbody per sheet.

MEASURED FIXED STAGING — ABSOLUTE SIZE
Flat stage at same depth, level nearly orthographic widecamera. At1470x630 output, Crow sole/claw baseline near y550, highest crest near y70:480px total standingheight. Riff and Pip feet on SAME floor liney550; their highest head tips near y430:120px total standingheight. Whole Crow equals exactly FOUR stacked whole otters. Heroes heads near Crow ankle/lower-shin, not belly/hips. Riff and Pip exactly SAME standingheight120px, although one stocky and one slim. Never make them200-300px tall. Explicit1meter otters versus4meter robot, roomceiling6meters. Uniform modelscale remains120px/480px when posed. Feet positions: tiny Pipx270, tiny Riffx410 beside permanent ropex450 and trapdoor; birdx1100right. Machine stays rearcenter x750, nevermovesforward. All actors remain on same depthplane; no perspective cheating. Camera holds ENTIRE room, complete Crow crest/body/feet, both small actors and fixedmachine at all times.

LIGHT AND CONTINUITY
Amber clockwork practicals, indigo moon/windowleft. ONE goldendiamond stays in birdtalon above rear machine receiver. Permanentrope and clamp-fixed red floorcable visible fromframeZERO. Cable shape and endpoints do not change; no following actor, dragging or newloops. Numberlessclockwork, onlytickmarks if dialvisible; nearlystationaryhour/minutehands. Riffcollar/glasses/holster fixed. No unlisted actor or weapon discharge.
'''
for n in (7,8):
 ch=p['chapters'][n-1];src=ch['takes'][-1]
 if src['status']!='succeeded':raise RuntimeError('Wait for prior task completion')
 src['quality_disposition']='rejected_edit_did_not_fix_scale_or_action';ch['director_history'].append({'prompt':ch['prompt'],'shots':ch['shots'],'source_take_id':src['id'],'reason':src['quality_disposition']})
 if n==7:
  context='SCENE CONTEXT\nTwo TINY1meter otter detectives confront a towering4meter robot bird in a fixed clocktower. The robot threatens midnightdarkness; Riff challenges it before trap unlatches.\nExactly14seconds.\n'
  timing='''ACTION TIMING
Shot 1 (0-7s): Complete4meter Crow staysRIGHT with feetplanted, holds diamond over rearmachine and delivers deep ominous warning. Tiny1meter Riff andPip stayLEFT, solesy550, headsat430. Fullroom staysvisible.0.7-6.2s Crow: "At midnight, this diamond will drain every light in Inkbell City!"
Shot 2 (7-10s): In SAME lockedwide, tinyRiff takes one short step to CLOSED trapdoor beside alreadyhangingrope, points at giantbird. Pip stayson safe solidfloorleft.7.2-9.2s Riff: "Game over, birdbrain!"
Shot 3 (10-14s): SAMEwide, giantbird chuckles and triggers floorlatch with freeattachedtalon; feetstayplantedRIGHT, diamondstaysotherhand.10.3-12.4s Crow: "Too late, detectives!" Trapdoor latchCLICK13.8s, floorstillclosed atfinalframe. Riff stands tiny on trapdoor beside rope; no fall yet.
AUDIO
@CrowVoice referenceaudio supplies same deep,dark,ominous baritone timbre/pitch for warning andtaunt. No pitched caw-cartoonvoice. Exact Englishlinesabove; original briskquiet swing-jazz mysteryscore andsteellatch/tickingFoley. Riffcockymidrangevoice. Musicducksspeech.
'''
  shots=[dict(start=0,end=7,action='Full4meter Crow warns tiny1meter brothers left; diamond held.',camera='Locked full stage wide.',audio='Crow midnight warning.',end_state='Crow feet right, tiny heroes left.'),dict(start=7,end=10,action='Tiny Riff steps onto closed trapdoor beside rope and challenges.',camera='Same locked wide.',audio='Game over birdbrain.',end_state='Riff atop trapdoor.'),dict(start=10,end=14,action='Crow taunts, latch clicks; no fall yet.',camera='Same locked wide.',audio='Too late detectives; latch click.',end_state='Riff tiny standing beside existing rope, trap unlatches.')]
 else:
  context='SCENE CONTEXT\nExistingtrapdoor opens under tinyRiff; he visibly fallsDOWN then catches alreadyvisible rope SIDEWAYS. TinyPipdeducesrobotcontrol andfollowsimmobileredcable tocurtain.\nExactly13seconds.\n'
  timing='''ACTION TIMING — FALL HAS THREE SEPARATE CAUSAL STEPS
Shot 1 (0-1s): FIRST fullsecondtinyRiff is STANDING with both shoes on CLOSED trapdoor atx410; heady430, feety550. Pipstands safeleftx270, same120pxheight. Existingropex450hangs frombeam toknottedend near y450, within sidewaysreach. Full4meterCrow feety550 crest70 staysRIGHT. No suspendedRiffinopeningframe.
Shot 2 (1-4s):1.0-1.7s trapdoor hinges openDOWN underRiff.1.7-2.3s Riff FALLS DOWN under gravity halfhisheight60px, feet descendy550to610, head430to490.2.3-3.0s he reaches SIDEWAYS to rope ALREADY HANGING atx450, both glovesclosearoundit abouty450, ropebecomestaut andhaltsfall.3-4sRiffdanglesLOWwithbothhands, feetnearholeopening, no upwardleap orverticalbounce. Pipremains solidfloorleft. Riff3.0-4.0s: "PIP! HELP!"
Shot 3 (4-8s): SAMEwide, RiffhangssteadilyLOW on originalrope; tinyPipturnsto4meterrobot chest and stationaryclampedredfloorcable, eyeswiden.4.7-6.0sPip: "Wait a minute..." No camera closeup, exact120pxstandingPip.
Shot 4 (8-13s): TinyPipWALKS RIGHT parallel to floor/lens alongALREADYVISIBLE FIXED cable, headstill120pxabovehisfeet. Cable staysclampedandsameshape;neverfollowsPip.8.2-11.8sPip: "The crow is a robot! Someone is controlling it!"12.0-12.7sRiff: "WHAT?!" Pip reaches farrightcurtain, Riffstilllow onropeleft. CompleteCrow480pxstaysRIGHT, machinefixedrearCENTER, no actorresizing.
AUDIO
Exact Englishlinesabove, Riffcockymidrange/Pipbrighterprecisevoice, quietbrisk swing-jazz/ticking/ropetwang/trapdoorFoley, no narration. Normalpace.
'''
  shots=[dict(start=0,end=1,action='Tiny Riff stands on closed trapdoor beside existing rope.',camera='Locked full stage wide.',audio='Tick.',end_state='Riff standing tiny at rim.'),dict(start=1,end=4,action='Trap opens, Riff dropsDOWN60px, then catches existing ropeSIDEWAYS with bothgloves.',camera='Same locked wide.',audio='PIP HELP; trap thump/ropecreak.',end_state='Riff low holdingrope.'),dict(start=4,end=8,action='TinyPipdeducescontrol, cableimmobile.',camera='Same locked wide.',audio='Waitaminute.',end_state='Pip followsfixedcableroute.'),dict(start=8,end=13,action='Pipwalksparalleltoflooralongstationarycabletocurtain;Riffhangsleft.',camera='Same locked wide.',audio='Robotcontrollerdeduction;WHAT.',end_state='Pipcurtainright,Riffonropeleft.')]
 ch['prompt']=context+base+'\n'+timing+'\nPOSITIVE CONSTRAINTS\nONE uncut wide with timedbeats above, complete4meterCrow and exactlytwo1meterotters. Existingrope/cable/machinepositionclear andconstant; ALL movement and contactsvisible. Native720p21:9, real-time cartoonanimation, no numericalclockfaces, no diagrams or subtitles.'
 ch['shots']=shots;ch['handoff']=shots[-1]['end_state'];ch['generation_mode']='reference';ch['tagged_assets']=['@Riff','@Pip','@Crow','@TowerLayout','@ScaleReference']+(['@CrowVoice'] if n==7 else [])
 ch['audio']={'generate_audio':True,'dialogue_language':'English','score':'quietbriskoriginalswingjazz','crow_voice_reference':'@CrowVoice' if n==7 else None}
 write_json(ROOT/f'chapters/{ch["id"]}/director-v02-focused.json',{'prompt':ch['prompt'],'shots':shots})
commit(p,'Reject ineffective video edits; regenerate tower warning and downward rope catch with explicit1meter/4meter staging and a fixed wide camera')
print('Focused reference regeneration prepared for chapters07/08; approval',helper.review_state(ROOT,p)['status'])
