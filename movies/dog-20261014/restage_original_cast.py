"""Material guide-control repair and original-cast/photo scene restaging."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as h
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=json.loads(json.dumps(p))
grip=next(c for c in p['chapters'] if c['id']=='s04_c01')['continuity_references'][0]
for c in q['chapters']:
    if c['id']=='s04_c06':
        c['continuity_references']=[json.loads(json.dumps(grip))]
        c['prompt']='STROLLER BEAT: Ah Ming left hand visibly encloses the solid silver guide-frame cross-grip. His navy bag is closed and the folded cane is INSIDE it for the whole montage. Tart collar ring stays EMPTY while working. Stroller clears, then pair moves right with the same solid handle-to-hand contact; never add a cane or flexible collar line.\n\n'+c['prompt']
        c.setdefault('prompt_refinements',[]).append({'reason':'Inspected take02 first shot adds deployed cane and collar line; ground that brief working beat in already selected earlier literal rigid-handle pose. No changed montage actions.'})
    if c['id']=='s12_c02':
        c['prompt']='ORIGINAL CAST DESIGN AND SIMPLE CABIN COMPOSITION: Use the approved original Hong Kong Chinese cast exactly. The small boy has short black hair, a plain forest-green jumper, navy trousers and pale trainers, seated beside his adult father in a plain beige jacket. Ah Ming is the approved young adult with dark glasses, textured teal jacket and open white shirt. Tart is the approved cream Labrador in brown guide harness. These are distinct original fictional designs. No scouts, scout uniforms, neckerchiefs, badges, floating houses, talking dogs, franchise props, or borrowed film characters.\n\n'+c['prompt']
        c['prompt']=c['prompt'].replace('Original designs throughout; no existing Pixar characters.','Original approved designs throughout, with individual Hong Kong faces, plain everyday clothing and original silhouettes.')
        # This conversation is entirely within the cabin; no exterior shot or
        # full-ship design is needed to tell this beat.
        c['tagged_assets'].remove('@FerryExterior')
        c['linked_asset_ids'].remove('asset_ferry_exterior')
        c['prompt']='\n'.join(line for line in c['prompt'].split('\n') if not line.startswith('@FerryExterior:'))
        c['shots'][0]['camera']='40mm simple cabin two-bench medium, boy seated next to father across aisle from Ah Ming and dog'
        c['prompt']=c['prompt'].replace('40mm aisle-side group medium.','40mm simple cabin two-bench medium: boy beside father on the right, Ah Ming and resting dog opposite on the left.')
        c.setdefault('prompt_refinements',[]).append({'reason':'Provider rejected generated output with copyright-restrictions error and returned no clip. Restage as simple cabin-only conversation using explicitly original approved cast, everyday clothing and distinct identities. No copyrighted character designs requested and normal provider moderation remains unchanged.'})
    if c['id']=='s16_c05':
        for tag,aid in (('@TartOffDuty','asset_tart_off_duty'),('@TineAdult','asset_tine_adult')):
            c['tagged_assets'].remove(tag);c['linked_asset_ids'].remove(aid)
            c['prompt']='\n'.join(line for line in c['prompt'].split('\n') if not line.startswith(tag+':'))
        c.pop('continuity_references',None)
        c['prompt']='CAMERA RESTAGING: This entire chapter is TIGHT SEATED HUMAN PORTRAITS and a PHYSICAL PHOTO INSERT. Crop from the humans upper chest UP, above the bench seat. Both adult dogs stay on paving OUTSIDE THE BOTTOM OF FRAME; they are not visible during these close-ups. May glances DOWN toward their off-screen ground-level lean, then takes the puppy photo from her bag below frame and raises it into the portrait. Never show adult dogs at human chest height or seated between people. The dogs are visible ONLY as two puppies in the exact physical archive photo.\n\n'+c['prompt']
        c['first_frame']='Tight upper-chest portrait of seated May, harbour softly behind. She glances DOWN at offscreen dogs on paving, then recognition crosses her face. Bench seat and adult dogs are outside the bottom crop.'
        c['shots'][0]['camera']='85mm upper-chest May recognition portrait, reverse 85mm Ah Ming portrait, adult dogs below frame'
        c['shots'][1]['camera']='85mm actual puppy print and hands at seated human chest height, reverse human face; adult dogs below frame'
        c['prompt']=c['prompt'].replace('65mm May recognition and physical print retrieval, reverse Ah Ming.','85mm upper-chest May recognition portrait and physical print raised from bag below frame, reverse upper-chest Ah Ming portrait; adult dogs below frame.')
        c['prompt']=c['prompt'].replace('Hard cut to 65mm photo/hands with handlers reverse.','Hard cut to 85mm exact puppy photo/hands insert at human chest height, then tight handler face reverse; adult dogs below frame.')
        c['prompt']=c['prompt'].replace('May watches Tine lean towards Tart again, both dogs on the paving below the bench seat, each slack lead still held by its seated handler.','May looks DOWN toward Tine leaning towards Tart on the paving outside the frame. The adult dogs remain outside the bottom crop while the camera stays on her face.')
        c.setdefault('prompt_refinements',[]).append({'reason':'Take02 still places both adult dogs on human bench despite floor input. Use ordinary tight human portraits and exact physical photo insert for this dialogue beat, leaving ground-level adult dogs below frame. All original dialogue and recognition order unchanged; reunion/play remain clearly shown in preceding chapters.'})
print(h.save(ROOT,p,q,'Restage original ferry cast and photo recognition; repair montage guide control'))
