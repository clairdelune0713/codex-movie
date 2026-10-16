"""Repair observed premature proximity and May/mother identity mixing."""
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as h
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=json.loads(json.dumps(p))
source=next(c for c in p['chapters'] if c['id']=='s06_c03');t=next(t for t in source['takes'] if t['id']==source['active_take_id'])
assert t['visual_review']['inspected'] and not t['visual_review']['requires_repair']
assert t['dependency_fingerprint']==h.chapter_fingerprint(ROOT,p,source)
for c in q['chapters']:
    if c['id']=='s13_c01':
        for tag,aid in (('@FerryExterior','asset_ferry_exterior'),('@StreetAndFerryCast','asset_street_and_ferry_cast')):
            c['tagged_assets'].remove(tag);c['linked_asset_ids'].remove(aid)
            c['prompt']='\n'.join(line for line in c['prompt'].split('\n') if not line.startswith(tag+':'))
        c['prompt']='SPATIAL SEPARATION: This is the FIRST wide frame containing both dogs, still SEVERAL METRES APART. Cream Tart and Ah Ming occupy the LOWER LEFT by the terminal exit. Brown Tine and May with the centre group occupy the UPPER RIGHT across SIX METRES of open public forecourt beside low planters. Both pairs move along DIFFERENT routes. Maintain visible empty paving and passing pedestrians BETWEEN the dogs. They never stand side by side or share a doorway. Tine remains outside the terminal. Both respond slightly to the offscreen horn, without looking toward each other or greeting yet.\n\n'+c['prompt']
        c['shots'][1]['camera']='28mm elevated wide, both pairs small and at different depths with six metres of public paving between them'
        c['shots'][1]['action']+=' Keep cream pair lower-left at terminal exit and visiting brown pair upper-right six metres across open paving, with pedestrians between. Do not move either dog into the other pair close foreground.'
        c['prompt']=c['prompt'].replace('Hard cut to 40mm wide lowering to dog height.','Hard cut to 28mm elevated wide: cream pair LOWER LEFT near terminal exit; visiting brown pair UPPER RIGHT, SIX METRES of public paving and pedestrians between. Keep both pairs small in frame at different depths.')
        c['prompt']=c['prompt'].replace('only a few metres apart.','still six metres apart across the forecourt, with passing pedestrians between them, unaware of each other.')
        c.setdefault('prompt_refinements',[]).append({'reason':'Actual first take placed both dogs adjacent in one doorway, undermining planned suitcase near miss and later recognition. Preserve the source first shared WIDE frame but enforce several metres of exterior separation and different routes.'})
    if c['id']=='s14_c02':
        for tag,aid in (('@LokAndMother','asset_lok_and_mother'),('@CentreMembers','asset_centre_members')):
            c['tagged_assets'].remove(tag);c['linked_asset_ids'].remove(aid)
            c['prompt']='\n'.join(line for line in c['prompt'].split('\n') if not line.startswith(tag+':'))
        c['prompt']='MAY IDENTITY LOCK: The woman beside Chan is MAY, the approved young adult with dark low ponytail, sage overshirt, white inner top, tan cross-body bag and CLEAR UNOBSCURED EYES. Her face exactly matches her separately bound original master and the inspected May portrait. Mother and other women are not in these foreground shots. Bo, in short pixie hair and teal polo, can be soft background while the group continues away.\n\n'+c['prompt']
        start=c['prompt'].index('@NearerSeatingBay:');end=c['prompt'].index('\n',start)
        c['prompt']=c['prompt'][:start]+'@NearerSeatingBay: Environment GEOMETRY AND DAYLIGHT ONLY: open public paving, low planters, ordinary wooden bench, railing and harbour. Ignore any prepopulated human/dog faces or wardrobe; bind foreground identities only from their individual character references.'+c['prompt'][end:]
        c['continuity_references']=[{'id':'may_face_s06_c03','path':f"chapters/s06_c03/screenshots/{t['id']}_review_03.jpg",'media_type':'Image','role':'reference_image','source_chapter_id':source['id'],'source_take_id':t['id'],'source_sha256':hashlib.sha256((ROOT/t['path']).read_bytes()).hexdigest(),'source_timestamp':14.67,'inspected':True,'reason':'Carry ONLY May exact original young-adult face, dark low ponytail, unobscured eyes and sage/white shirt from this successful earlier May portrait. Ignore centre room, chair, Chan foreground head, prior dialogue and lighting. New action is sitting with Chan on the outdoor harbour bench while holding Tine orange lead. Mother glasses/bun/blue blouse do not belong to May.'}]
        c.setdefault('prompt_refinements',[]).append({'reason':'Actual first take puts mother glasses/bun on May. Restrict unrelated foreground cast and environment role, ground May identity in her inspected selected earlier portrait. Keep exact horn/pause/sitting choice and original dialogue.'})
print(h.save(ROOT,p,q,'Preserve harbour near-miss distance and restore May distinct original face'))
