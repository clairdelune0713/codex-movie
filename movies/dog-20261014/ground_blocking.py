"""Use narrowly scoped, inspected earlier frames for demonstrated physical errors."""
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as h
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=json.loads(json.dumps(p));j=json.loads((ROOT/'exports/task-journal.json').read_text(encoding='utf-8'))
sources={c['id']:c for c in p['chapters']}
def ref(cid,tid,frame,timestamp,reason):
    source=sources[cid];take=next(t for t in source['takes'] if t['id']==tid)
    assert source['active_take_id']==tid and take['visual_review']['inspected'] and not take['visual_review']['requires_repair']
    assert take['dependency_fingerprint']==h.chapter_fingerprint(ROOT,p,source)
    return {'id':'pose_'+cid,'path':f'chapters/{cid}/screenshots/{tid}_review_{frame:02}.jpg','media_type':'Image','role':'reference_image',
            'source_chapter_id':cid,'source_take_id':tid,'source_sha256':hashlib.sha256((ROOT/take['path']).read_bytes()).hexdigest(),
            'source_timestamp':timestamp,'reason':reason,'inspected':True}
grip=ref('s03_c03','take_02',4,17.8,'Carry ONLY the literal solid silver two-arm guide handle, brown cross-grip inside Ah Ming left hand, and EMPTY collar ring while cream Tart working harness is ON. No flexible collar lead and no deployed cane during guide travel. Ignore tram, pavement, bag contents, camera crop, lighting and prior action; use the new scene environment/timing. If this chapter removes the harness, the frame applies only BEFORE removal; after it is completely OFF use the explicitly timed brown collar lead state.')
floor=ref('s02_c02','take_01',3,10.67,'Carry ONLY brown Tine seated/standing with all paws on the ROOM FLOOR beside chair legs, his body below the human seated shoulder, with open non-intrusive space. Ignore this frame handler/volunteer identity and training-room background. In the new centre scene only May holds the orange collar lead; Lok and mother do not hold it. No dog sits on a human chair.')
changed=[]
for c in q['chapters']:
    if c['chapter_index']<14:continue
    current=j['takes'].get(c['id'])
    if current and current['status'] in ('pending','processing'):continue
    known=c['id'] in ('s04_c01','s04_c02','s04_c04')
    if current and not known:continue
    refs=[]
    if '@TartWorking' in c['tagged_assets']:refs.append(grip)
    if '@TineAdult' in c['tagged_assets'] and any(t in c['tagged_assets'] for t in ('@CentreMorning','@CentreAfternoon')):refs.append(floor)
    if not refs:continue
    c['continuity_references']=json.loads(json.dumps(refs))
    c['handoff']={'decision':'Inspected earlier pose/prop-state image references are useful after generated lead/cane/chair errors; no automatic previous-clip chaining.',
                  'carry':'Only hand-to-rigid-handle ownership and/or dog-on-floor geometry, as specified in each reference.',
                  'do_not_carry':'Earlier location, camera, action, music, dialogue, other human identities or time of day.',
                  'cut':'New cinematic framing per timeline; no first-frame lock.',
                  'distinct_roles_reason':'Two refs only where a split montage separately needs cream guide-handle contact and brown dog floor height; these cannot be combined into a sheet.' if len(refs)>1 else 'One minimal pose reference.'}
    if known:
        c.setdefault('prompt_refinements',[]).append({'reason':'Actual first take added a deployed cane/extra collar lead or placed Tine on a chair with wrong lead holder. Ground in inspected earlier successful pose frames without changing approved designs.'})
        c['prompt']+='\n\nTARGETED BLOCKING REPAIR\nFolded cane remains INSIDE CLOSED navy bag during public guide travel. Only Ah Ming holds the rigid guide handle. In the centre May holds Tine orange lead; mother hands stay on her own lap. Tine remains on the floor at chair-leg height, never on chair seat. Follow the narrow inspected pose inputs for these physical details, not their backgrounds.\n'
    changed.append(c['id'])
q.setdefault('production_quality_notes',[]).append('Added actual inspected source frames from selected s03_c03/take_02 and s02_c02/take_01 only where demonstrated prop-state/floor-height errors justify them. No new identity/style/reference-sheet assets; pending accepted jobs retain original frozen inputs.')
print(h.save(ROOT,p,q,'Ground demonstrated guide-control and dog-floor blocking errors in inspected earlier frames'))
print('Chapters:',','.join(changed))
