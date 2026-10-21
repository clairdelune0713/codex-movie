"""Targeted creative repair after inspecting a successful generated take."""
import copy
import render_finale as r

p=r.read(r.ROOT/'project.json');q=copy.deepcopy(p);c=q['chapters'][48]
assert p['revision']==18 and c['id']=='chapter_49'
old=r.journal()['takes']['chapter_49'];assert old['status']=='succeeded'
reviews=r.read(r.ROOT/'exports/visual-reviews.json')
frames=r.read(r.ROOT/'exports/visual-inspection/chapter_49_take_01_4c94e1504c/frames.json')
review={'take_id':old['id'],'source_sha256':frames['source_sha256'],'inspected':True,
    'requires_repair':True,'inspected_at':r.now(),'method':'Both actual-frame contact pages viewed.',
    'notes':['Generated take merged the two distinct toy pieces into one apparently intact toy and reversed head/tail ownership. Preserve as rejected creative candidate; repair only scene 49.']}
reviews[c['id']]=review
r.save(r.ROOT/'exports/visual-review-history/chapter_49_take_01.json',review)
r.save(r.ROOT/'exports/visual-reviews.json',reviews)

second='''MEDIUM — At dog height, cream Tart is CAMERA LEFT and red Tine CAMERA RIGHT, both in three-quarter front view. Tart trots in on his brown ordinary leash carrying ONLY the short blue HEAD HALF: orange bill and two front feet, open ragged rear seam. Tine already has ONLY the separate blue REAR HALF on the paving at his own front paws: broad flat navy tail, two rear feet, white stuffing at its torn front. Tine sniffs his own rear piece. Both separate pieces are clearly visible at once, with air between them.
- **MR. LEUNG:** "He insisted on bringing it. Sleeps with it every night."'''
third='''CLOSE — Locked low frontal two-shot of the TWO DISTINCT BROKEN PLUSH PIECES on the paving. Cream Tart stays left, red Tine stays right; mouths remain clear of both props. Tart sets his head/front-feet piece beneath his own left-side paws, bill pointing outward LEFT. Tine's tail/rear-feet piece stays under his own right-side paws, flat tail pointing outward RIGHT. The two ragged white-stuffing seams face the middle, separated by a plainly visible eight-centimetre strip of bare paving. The two dogs simultaneously press their OWN separate piece once with a front paw: high "SQUEE" from Tart's head half, low "HONK" from Tine's rear half. Their ears pop and tails wag; everybody laughs. The two pieces remain separate on the ground, each next to its owner.
- **AUNTIE BO:** "Hahaha! Again! AGAIN!"'''

old_timeline=c['prompt'].split('TIMELINE / PERFORMANCE\n',1)[1].split('\nCONTACT / PHYSICS / CRITICAL LOCKS',1)[0]
c['shots'][1]['action']=second;c['shots'][2]['action']=third
timeline='\n\n'.join(f"SHOT {i+1} ({s['start']}–{s['end']}s). "+('OPEN. ' if i==0 else 'CLEAN CUT. ')+s['action'] for i,s in enumerate(c['shots']))+'\n'
c['prompt']=c['prompt'].replace(old_timeline,timeline)
start=c['prompt'].index('CONTACT / PHYSICS / CRITICAL LOCKS\n')
end=c['prompt'].index('\nLIGHTING / CONTINUITY',start)
c['prompt']=c['prompt'][:start]+'''CONTACT / PHYSICS / CRITICAL LOCKS
TWO SEPARATE TOY PIECES — DEMONSTRATED-FAILURE REPAIR
Two small broken objects, never an intact animal. @sir-squeaks-head is exclusively Tart's left-screen piece: blue face, orange bill, two FRONT feet, torn open back; no flat tail or rear feet. @sir-squeaks-tail is exclusively Tine's right-screen piece: blue rounded rear body, flat navy tail, TWO REAR feet, torn open front with white stuffing; no face, eyes, bill or front legs. Match their separate approved reference images. The entire 10–14s close shot shows bare paving between the two exposed seams; each paw compresses a DIFFERENT piece. Pieces do not touch, cross sides, trade owners, fuse, grow missing parts or pass between mouths. This simple parallel paw squeeze preserves the paired SQUEE-HONK reunion joke. Do not create a second whole platypus. All dogs retain intact natural anatomy.
Ensemble backgrounds simple and softly focused. Blind Leung remains seated and holds Tart's ordinary brown lead by touch. At 14s cut to ONE Boss inside ONE clear bubble backpack. No cat outside backpack.
'''+c['prompt'][end:]
c['prompt']=c['prompt'].replace('50mm dog approach; 85mm paired toy detail','50mm dog approach; locked frontal 85mm two-piece prop detail with a visible gap')
c.setdefault('script_changes',[]).append({'at':r.now(),'reason':'Successful take 01 fused the split toy and swapped ownership. Simplified the four-second paired squeak to separate paw presses with an exposed gap. Same story beat, duration, dialogue, cast, approved images and 480p 16:9 output.','library_reference':'references/prompt-library/shots/scene-08/07_frontal-close-up-of-a-kneeling-older-man-hands-lac.md — fixed frontal framing and targeted demonstrated-failure lock; user animation style preserved.'})
c['active_take_id']=None
q['render_status']='repairing_scene_49_prop_continuity'
print(r.helper.save(r.ROOT,p,q,'Repair scene 49 split-toy ownership and distinct rear-half anatomy after inspecting take 01'))
