from project_ops import ROOT,helper,commit
p=helper.read(ROOT/'project.json')
c=p['chapters'][6];src=c['takes'][-1]
if src['status']!='succeeded':raise RuntimeError('Wait for accepted source')
src['quality_disposition']='rejected_wrong_trapdoor_under_crow_and_premature_diamond_release'
c['director_history'].append({'prompt':c['prompt'],'shots':c['shots'],'audio':c['audio'],'handoff':c['handoff'],'source_take_id':src['id'],'reason':src['quality_disposition']})
c['prompt']='''SCENE CONTEXT
Generate14seconds of an original2D1930s rubber-hose cartoon. Two TINY1meter otter detectives face a COLOSSAL6meter robot bird inside an immenseclocktower. Exaggerate giant-versus-tiny staging, keep entirebody of robot insideframe. The bird threatensmidnightdarkness, gingerotter defiantly challengesit, bird taunts. Exactlyonebird,twootters,nohound yet.
OUTPUT SETTINGS
14seconds,21:9,native720p,ONE LOCKEDOFF CONTINUOUS ULTRAWIDE shot, levelparallelstageperspective, fullbodyactors throughout. Real-time dialogue/action, no slowmotion,no zoom orcamera moves,cuts or growingactors. Hand-drawn ink/celcolor and richpainted amber/indigo backgrounds, funny/thrilling expressions.
ACTIVE REFERENCES
@Riff one gingerotter,rustwaistcoat/flat tuckedivoryshirtcollar/greentrousers/brownbrogues/whitegloves/smallrighthipholster. ONE completeactor assembledfrombodyandhead sheet; barefurryhead.
@Pip one chocolatetinyotter,tealcardigan/mustardshirt/russettrousers/navyshoes/whitegloves/WIRE-RIMGLASSES. Samecomplete standingheight asRiff,slimmerbuild. Normalblack/whiteeyes.
@Crow one giant blackrivetedrobotbird, completeattachedhead/beak/body/wings/legs/claws/redlit eyes/chestspeaker. Giant6meterstaging tocounter prior render makingrobotnearlyhero-sized; otters1meter, trulyTINYbycomparison, headsnearrobotankles. Do not make2meterrobot.
@TowerLayout fixedroomandSAMErobot: windowLEFT, permanentropeLEFTCENTER, CLOSEDtrapdoorLEFTunderrope, golden-diamondreceiver machineREARCENTER againstclockgears, giantrobotRIGHT feetplanted, fixedredcablefloortojoystickbehindFARRIGHTcurtain. One machine/onebirdonly, nopanel/reviewannotations. Geometryunchanged.
@CrowVoice same deepdarkominous mechanicalBARITONE timbreandpitchforEVERYbirdline. Generate wordsbelow, not guide's samplemusic.
STAGING
Birdcompleteheightfills almostentireframefromcrestnear y60 toclawsneary550; tinyotters heightONLY80pixels in1470x630 image, feetneary550, headneary470. This is a distant wide fullbody view, tinyfiguresmuststaytiny. Birdcenterx1100RIGHT, Riffx420LEFT,Pipx280LEFT, machinex750REARCENTER. Robotdoesnotmovefeet,crouch,steporchangeitsfullmodelsize. Cameraandfloorplaneconstant.
ACTION TIMING
Shot 1 (0-7s): GiantrobotRIGHT holds SINGLEgoldendiamond inmetal handabove rearmachine; gemstone stayssecurelyheldforwholeclip. TinyottersLEFT, existingrope/trapdoorclear.0.6-6.2s robotchestspeaker: "At midnight, this diamond will drain every light in Inkbell City!"
Shot 2 (7-10s): Samewide: tinyRiff takesoneshortstep ontoLEFTCLOSEDtrapdoor besideALREADYhangingrope andpointsatbird. TinyPipstayson solidfloorLEFT.7.2-9.2sRiff: "Game over, birdbrain!"
Shot 3 (10-14s): Samewide: robotbriefdeeplaugh, gemstoneHANDstaysraised, NEVER RELEASESdiamond orputsintofloor.10.2-12.5srobot: "Too late, detectives!" Only latchCLICK13.8s heard underRiffLEFT; trapdoorremainsvisiblyCLOSED tillfinalframe. BirdRIGHTfloorNEVERopens,noholeunderbird. RiffstillSTANDINGontoplefttrapdoornearrope.
AUDIO/LIGHT
Exact Englishwords, brisksoftswingjazz belowvoices, electricalchestcrackle/tick/latchclick. Riffcockymidrange, Pipsilent. Paintedambersclockwork andindigowindowleft. Clockfacesnumeral-freeandhandsalmoststatic.
POSITIVE CONSTRAINTS
Tinyottersremain tiny besidegiantrobot, fixedcamera/set, oneuncut14second21:9native720p cartoon. Keep ropealreadyvisible, cableimmobile, machineanchoredrearcenter, robotcompletebodyRIGHT. NOdiamondrelease,noinsertion,noholebeneathrobot, nootheractor ornewprop.
'''
c['tagged_assets']=['@Riff','@Pip','@Crow','@TowerLayout','@CrowVoice'];c['generation_mode']='reference';c['scale_probe']={'target_output_ratio':4,'exaggerated_prompt_ratio':6,'reason':'Model has compressed 4:1 instructions to observed approximately2.7:1; inspect actual output before choosing.'}

c=p['chapters'][10];src=c['takes'][-1]
if src['status']!='succeeded':raise RuntimeError('Wait for prior shutdown edit')
c['director_history'].append({'prompt':c['prompt'],'shots':c['shots'],'audio':c['audio'],'handoff':c['handoff'],'source_take_id':src['id'],'reason':'Guard still at window instead of machine corner.'})
c['prompt']='''VIDEO EDIT: edit the EXISTING11second @EditSource11. Move ONLY the small TAN HOUND IN NAVY UNIFORM LYING ON THE FLOOR beside LEFT window. Relocate its complete slumpedbody/cap/legs from leftwindowfloor to directly in front of the mainmachine at its RIGHT FRONT CORNER, justLEFT of giantrobotfeet. In1470x630frame this is approximately bodycenterx800,y540. Keep the houndlying/slumped, no standinganimation. Remove its oldleft-windowcopy and fillthatspotwithmatchingfloor. ExactlyONEhound, nobodyvanishes. Keep houndatnewmachinecornerthroughout allwideshots. The twootters,diamondcatch,giantrobot,machine,window,rope,cable,controller, originalEnglishsound/Foley/music, shotcuts,timing andpowerdown action remainunchanged. No otheredits, noextraobjects, no newscene orvideoextension. Native720p retainsinput21:9and11seconds. Normal speed, no slowmotion.'''
for shot in c['shots']:
 for key,value in list(shot.items()):
  if isinstance(value,str):shot[key]=value.replace('@','')
c['tagged_assets']=['@EditSource11'];c['generation_mode']='edit'
commit(p,'Run isolated size calibration for warning; fix shutdown guard placement with one explicit video-edit operation')
print('Final focused repair tests prepared; output size target remains4x')
