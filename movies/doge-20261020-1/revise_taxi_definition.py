from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
a=next(a for a in p['asset_list'] if a['id']=='red-taxi')
a['description']='Original generic Hong Kong red four-door taxi with light silver roof, compact rounded sedan shape, right-hand drive, small illuminated WHITE roof light with the exact word TAXI in clear BLACK uppercase letters centered on its visible front face, dark wheels, closed doors and no driver. Full vehicle three-quarter hero view. No licensed logos or other lettering.'
p['production_stage']='asset_revision_requested'
p['production_notes'].append('User requested: for the hong kong taxi, there should be the word "TAXI" on the roof light. Revise only that prop and replace the pending asset review after inspection.')
(ROOT/'proposal.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
