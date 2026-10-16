"""Commit a clearer ground-plane ending using one inspected identity-neutral frame."""
import copy,hashlib
from render_movie import ROOT,read,helper
p=read(ROOT/'project.json');j=read(ROOT/'exports/task-journal.json');proposal=copy.deepcopy(p)
c=proposal['chapters'][69];assert c['id']=='s16_c08'
source=j['takes']['s16_c03'];assert source['status']=='succeeded'
c['continuity_references']=[{'id':'reunion_ground_plane','path':'chapters/s16_c03/screenshots/take_01_review_01.jpg',
 'media_type':'Image','role':'reference_image','source_chapter_id':'s16_c03','source_take_id':source['id'],
 'source_timestamp':0.2,'source_sha256':hashlib.sha256((ROOT/source['path']).read_bytes()).hexdigest(),
 'inspected':True,'reason':'Only use the visible tiled PAVING under both adult dogs in front of the human bench and the dog-to-human scale. Keep adults seated behind. Do not repeat toy tug, standing poses or any old audio. In this new final scene both dogs settle on these same floor tiles, strictly below the bench seat.'}]
lock='FINAL GROUND PLANE - ALL THREE SHOTS\nThe camera begins at tile level and shows four paws touching the stone PAVING IN FRONT OF the bench. The dogs sit, fold and lie on that same stone paving only. The wooden slat bench seat behind remains occupied only by the two human handlers and the removed harness. Never place either dog on wooden slats. Their sleeping forelegs and toy rest on clearly visible stone tile grout. Human hands reach down only by leaning forward; do not raise the dogs to meet hands. The final wide must show both dogs BELOW the bench seat beside the adults\' shoes, on paving, with Tart chin resting across Tine forelegs.\n\n'
c['prompt']=lock+c['prompt']
c['prompt']=c['prompt'].replace('Tine sits close and leans, Tart makes a fractional shift; both are adult dogs throughout.',
 'Both adult dogs are on the stone floor in front of the bench: paws and tile grout visible. Tine sits close and leans, Tart makes a fractional shift. Human knees and bench seat stay behind and above them.')
c['prompt']=c['prompt'].replace('Ah Ming leaves his hand lightly on Tart\'s back. May\'s hand rests near Tine.',
 'Both handlers lean forward, reaching down toward their dogs on the paving. Ah Ming leaves his hand lightly on Tart\'s back. May\'s hand rests near Tine. Both dogs stay below knee level on the stone tiles.')
c['shots'][0]['action']='Both dogs remain on visible stone paving with tile grout in front of bench; human shoes behind. '+c['shots'][0]['action']
c['shots'][1]['action']='Ground-level insert: chins, forelegs and toy rest on stone tiles below human knees. '+c['shots'][1]['action']
c['shots'][2]['action']='Wide establishes humans on wood bench and dogs on stone ground in front, never on seat. '+c['shots'][2]['action']
print(helper.save(ROOT,p,proposal,'Repair ending dogs on bench by grounding all three shots to inspected paving reference'))
