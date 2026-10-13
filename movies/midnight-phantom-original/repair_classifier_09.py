from project_ops import ROOT,helper,commit
p=helper.read(ROOT/'project.json');c=p['chapters'][8]
if c['takes'][-1]['status']!='failed':raise RuntimeError('Only retry confirmed failed job')
c['director_history'].append({'prompt':c['prompt'],'source_take_id':c['takes'][-1]['id'],'reason':'Provider classified long edit prompt as extension; simplify to explicit in-place edits.'})
c['prompt']='''VIDEO EDIT: modify the EXISTING frames of @EditSource09. This is a12second video repair; use exactly the original12second action and audio.
RESIZE the three existing small characters @Riff, @Pip and @Guard uniformly so each complete standing sole-to-highest-head/cap height is precisely ONE QUARTER the existing complete mechanical bird's sole-to-crest standing height. Bird remains original size and anchor. Exact Riff1:Pip1:Guard1:Crow4 scale from @ScaleReference. The source small actors are too large; reduce actual full body models including heads/limbs/clothes; feet remain in same floor positions. The hound guard and both otters have EQUAL standing heights despite different builds. Guard both boots point naturally forward.
RESTORE wire-rim glasses from @Pip portrait in every visible face. @Riff flat tucked ivory shirt collar, rust waistcoat, green trousers, hip holster stay consistent. @Guard navy uniform/tan trousers/boots remain.
DELETE only the extra red wall-switch fixture at far right; keep original one brass joystick on wood pedestal behind right curtain, its fixed red floor cable and original control action.
CORRECT the ginger otter's pose in final wide frames: both gloves still hold the EXISTING hanging rope; torso sits lower with feet suspended just beside hole rim, not standing on floor. Same rope and ceiling attachment, no new rope.
Keep original room, rear-center machine, full attached mechanical bird body at right, numberless clockwork, camera, speech, sound and original timing. No new scene or extra action. No extension or continuation; EDIT THE ORIGINAL VIDEO. Native720p retains input21:9 and12seconds. All motion real-time, no slow motion. Dimension diagram is measurement only, no labels/boxes in movie.'''
c['tagged_assets']=['@EditSource09','@Riff','@Pip','@Guard','@ScaleReference'];c['generation_mode']='edit'
commit(p,'Simplify confirmed failed chapter09 edit to unambiguous in-place resize and prop/pose correction')
print('Confirmed failed edit prepared for single corrected retry')
