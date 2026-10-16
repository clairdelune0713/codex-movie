"""Repair observed exterior-bay geography and reunion floor-height mistakes."""
import hashlib
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as h
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
q=json.loads(json.dumps(p))
source=next(c for c in p['chapters'] if c['id']=='s15_c04')
take=next(t for t in source['takes'] if t['id']==source['active_take_id'])
assert take['visual_review']['inspected'] and not take['visual_review']['requires_repair']
assert take['dependency_fingerprint']==h.chapter_fingerprint(ROOT,p,source)
pose={'id':'off_duty_floor_s15_c04','path':f"chapters/s15_c04/screenshots/{take['id']}_review_04.jpg",
      'media_type':'Image','role':'reference_image','source_chapter_id':source['id'],
      'source_take_id':take['id'],'source_sha256':hashlib.sha256((ROOT/take['path']).read_bytes()).hexdigest(),
      'source_timestamp':18.8,'inspected':True,
      'reason':'Carry ONLY adult dog height on the PUBLIC PAVING in front of and outside human knees, cream Tart collar-only with separate brown lead held by Ah Ming, brown Tine orange lead held by May, and open harbour daylight. Both dogs stay entirely below bench seat height on the ground throughout the new action. Do not copy May standing pose: she sits on the bench in this chapter while keeping her lead end. No prior action/audio, no harness on Tart, no dog on bench or under legs.'}
floor='FLOOR AND LEAD OWNERSHIP: Both adult dogs stand or sit on the stone PAVING IN FRONT OF the bench, all four paws below human shoe height in every shot. Human bench seats hold only people, bag and folded harness. Ah Ming keeps one brown collar lead end in his hand; May keeps the orange collar lead end in her hand. Both lines are slack but their human ends never lie free on the ground. Dogs never climb onto the bench. Frame humans waist-up when dogs are irrelevant; a dog close-up has paving, bench LEGS and seated human knees behind it, never the top of a seat.'
for c in q['chapters']:
    if c['id']=='s15_c02':
        c['tagged_assets'].remove('@FerryForecourt')
        c['linked_asset_ids'].remove('asset_ferry_forecourt')
        c['prompt']='OUTDOOR SEATING BAY GEOGRAPHY: This is the open-air nearer harbour rest bay, NOT a ferry building. Its entrance is a gap between two low PLANTERS on the same level stone path, with an ordinary outdoor bench beyond. Open sky and the harbour railing remain visible. No roof, doorway, columns, terminal interior or ferry crew at this gap. The stroller continues along the PUBLIC PATH while the suitcase owner clears the planter gap.\n\n'+c['prompt']
        c['prompt']='\n'.join(line for line in c['prompt'].split('\n') if not line.startswith('@FerryForecourt:'))
        begin=c['prompt'].index('@StreetAndFerryCast:')
        end=c['prompt'].index('\n',begin)
        c['prompt']=c['prompt'][:begin]+'@StreetAndFerryCast: Use ONLY the navy-clothed traveller who owns the teal suitcase. No other library role is present here. Stroller parent is an ordinary passing Hong Kong adult, no uniform.'+c['prompt'][end:]
        c['first_frame']='On the open-air harbour path, Tart stops before a narrow gap between two LOW PLANTERS. Stroller and teal suitcase temporarily obstruct that gap. Open sky, railing and the outdoor bench beyond remain visible; Bo stands inside this outdoor rest bay.'
        c['shots'][0]['action']+=' The entrance is the same-level gap between low planters, no building doorway; Bo stands in open air by the bench.'
        c['prompt']=c['prompt'].replace('Bo calls, Ah Ming asks obstruction question; keep obstacle visible.','Bo calls, Ah Ming asks obstruction question; keep obstacle visible. The entrance is an outdoor gap between low planters, open sky above and bench beyond; no building doorway.')
        c.setdefault('prompt_refinements',[]).append({'reason':'Actual first take wrongly stages an outdoor rest-bay entrance as a ferry-terminal doorway with crew. Use the approved nearer-bay environment only and restrict cast library to suitcase owner.'})
    if c['id'] in ('s16_c02','s16_c05'):
        c['prompt']=floor+'\n\n'+c['prompt']
        c['prompt']=c['prompt'].replace('Four paws on floor except brief scripted attempted lap gag.','Four paws stay on the public paving throughout this chapter; no lap gag here.')
        c['continuity_references']=[json.loads(json.dumps(pose))]
        c.setdefault('prompt_refinements',[]).append({'reason':'Actual first take puts adult dogs on a human bench and/or leaves loose public lead ends. Ground floor height and held collar-lead states in selected earlier harness-removal take, preserving all source actions and dialogue.'})
    if c['id']=='s16_c02':
        c['shots'][1]['camera']='65mm medium: seated May hand lowers toy to Tine standing on paving, bench legs in background'
        c['shots'][1]['action']+=' May bends her hand DOWN BELOW HER KNEE to offer the toy to Tine on the paving. Orange lead end stays in her other hand; no lifting or bench climbing.'
        c['prompt']=c['prompt'].replace('Hard cut to 65mm May bag to Tine mouth medium.','Hard cut to 65mm medium, seated May hand lowering from bag below knee to Tine mouth on the paving, bench legs behind.')
        c['prompt']=c['prompt'].replace('May sits and produces single familiar two-ended toy, Tine takes it with soft squeak; Tart ears lift.','May sits and produces single familiar two-ended toy, lowering her hand below her knee to Tine standing on the paving; Tine takes it with soft squeak and Tart ears lift. May holds the orange lead in her other hand.')
    if c['id']=='s16_c05':
        c['first_frame']='May sits on the bench, both dogs on paving in front of her knees. Tine leans his shoulder toward Tart at ground level; May connects this familiar shape to the old photo.'
        c['prompt']=c['prompt'].replace('May watches Tine lean towards Tart again.','May watches Tine lean towards Tart again, both dogs on the paving below the bench seat, each slack lead still held by its seated handler.')
print(h.save(ROOT,p,q,'Repair outdoor seating-bay geography and keep reunion dogs on paving with held leads'))
