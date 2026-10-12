import sys
sys.dont_write_bytecode=True
import json
import prepare

ROOT=prepare.ROOT
current=prepare.helper.read(ROOT/'project.json')
proposal=json.loads(json.dumps(current))
chapter=next(c for c in proposal['chapters'] if c['id']=='chapter_07')
lock='''FIVE-FRIEND COUNT AND BLUE IDENTITY LOCK
This is a group of EXACTLY FIVE living plush friends, not six. Count and separate them throughout every shot: ONE white smiling friend, ONE yellow beak friend, ONE orange tiger, ONE powder-blue teardrop, ONE gray-headphone cream cat. The blue reference is a sheet showing multiple views of ONE friend; the RIGHTMOST complete teardrop view is its assembled silhouette. The cropped blue torso views are NOT extra characters, heads, floating pieces, balloons or background toys. Only ONE blue teardrop exists anywhere in foreground, midground, background or sky. No blue spare head, no blank blue rounded body, no blue cube-like plush behind the group. No second blue entity may follow the walking group. At the crest each friend is shoulder to shoulder in the order white, yellow, orange, blue, headphone cat; all five faces are recognizable and countable. The star floats ahead of or above them with an air gap, never attached to the tiger's forehead or used as a face or head.\n\n'''
chapter['prompt']=chapter['prompt'].replace('POSITIVE CONSTRAINTS / CONTINUITY LOCKS',lock+'POSITIVE CONSTRAINTS / CONTINUITY LOCKS')
chapter['prompt_revision_notes']=['Inspected first take rendered an extra blank blue body from the multiview sheet. Add exact five-friend count and one-blue-character locks.']
for take in chapter['takes']: take['quality_disposition']='not_selected_duplicate_blue_character'
(ROOT/'chapters'/chapter['id']/'prompt-v02.txt').write_text(chapter['prompt'],encoding='utf-8')
prepare.write_json(ROOT/'proposal.json',proposal)
print(json.dumps(prepare.helper.save(ROOT,current,proposal,'Correct duplicate blue reference-view body in inspected homecoming scene')))
