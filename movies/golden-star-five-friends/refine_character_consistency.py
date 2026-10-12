"""Target demonstrated character-shape failures, retaining approved image assets."""
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
HELPER=Path(r'C:\Users\admina\.codex\skills\movi2\scripts\project.py')

def main():
    p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
    reasons={'chapter_02':'Bubbles incorrectly gains triangular kitten ears.','chapter_05':'Pip incorrectly has a large open orange hole on the head; tiger markings leak onto kitten bodies.','chapter_06':'Mochi is represented as a detached face blob on the rainbow instead of a complete kitten.','chapter_08':'Bubbles incorrectly gains a segmented torso and two blue feet.'}
    selected=sys.argv[1:] or list(reasons)
    for c in p['chapters']:
        if c['id'] not in selected:
            continue
        old=c['prompt']
        header=(
            'PRIMARY FULL-BODY ANATOMY REFERENCE / CRITICAL CORRECTION\n'
            '@ls2 is the user-approved photograph of the FIVE WHOLE plush figures. Use it as the authoritative silhouette and connected-body anatomy reference for all five. '
            'It shows ONE of each friend: top-left white Mochi kitten, top-center yellow Pip chick, top-right blue Bubbles ghost, bottom-left orange Tiggy tiger, bottom-right white Lulu kitten with gray side ear pads. '
            'Ignore all metal key rings, black hanging loops, fabric tags, product photography background, shadows and layout. Do NOT reproduce the photograph as a still image. '
            'The separate character sheets supply face markings and tactile materials only. Their cropped body views are NOT a character design and must never become the character head. '
            'Build FIVE complete recognizable animated plush figures with the approved whole-toy silhouettes.\n\n'
            'CHARACTER-SHAPE LOCK — ONLY THE CORRECT COMPLETE BODIES\n'
            'Mochi: white kitten head visibly connected to a short white torso, two white arms, two short white legs and tiny white tail. Round pink cheeks, smiling mouth. NEVER a head-only round blob. '
            'Lulu: white kitten head visibly connected to a short white torso, two white arms, two white legs and tiny white tail; gray side ear pads and pink flower cheeks only. No tiger stripes or black paw spots on either white kitten. '
            'Tiggy: one orange tiger head connected to one orange tiger body; only Tiggy has black tiger markings and a striped tail. '
            'Pip: completely closed round yellow head with two soft rounded yellow tufts, tiny black eyes, orange triangular beak at FRONT of the face, two yellow wings, closed yellow oval torso and two tiny orange feet at the BOTTOM. '
            'NO neck aperture, NO hole, NO open top, NO bowl or cup shape, NO orange surface on top of the head, NO upside-down torso used as head. '
            'Bubbles: ONE uninterrupted light-blue teardrop ghost silhouette, rounded seamless dome with eyes and mouth on FRONT of the upper dome, two small side flippers, body tapering to exactly one smooth point below. '
            'Bubbles has NO separate head, NO torso seam, NO neck, NO ears, NO cat ears, NO bunny ears, NO feet, NO legs, NO paws, NO paw pads and NO tail. Smooth closed domed top. '
            'Each figure remains anatomically correct in every frame and from every angle, during flight, sitting and cuddling. The ghost remains a tapered floating teardrop even in the group cuddle. '
            'The kittens always show connected shoulders and torso even while seated on a rainbow. Every figure has its own reference colors and markings; do not transfer traits.\n\n'
        )
        fixed=old.replace('Sheet body and portrait views together describe ONE COMPLETE living character with an attached head and normal plush toy proportions.','The whole-toy photograph defines complete anatomy; the sheet defines this individual face and fur markings, not detached anatomy.')
        fixed=fixed.replace('Keep complete heads attached to complete bodies.','Keep kitten/tiger/chick heads attached to complete bodies; Bubbles remains one continuous teardrop without a head/body division.')
        if c['id']=='chapter_05':
            fixed=fixed.replace('35mm medium-wide, slightly elevated to read circle and star; small brisk settling move.','35mm eye-level medium-wide around the circle, show closed rounded character heads and attached torsos; never a steep overhead view.')
            c['shots'][0]['camera']='35mm eye-level medium-wide around the circle; closed rounded heads and attached bodies, no steep overhead view.'
        c['prompt']=header+fixed
        c['prompt_version']=2
        c['refinement_reason']=reasons[c['id']]
        if '@ls2' not in c['tagged_assets']:
            c['tagged_assets'].append('@ls2')
        (ROOT/'chapters'/c['id']/'prompt-v02.txt').write_text(c['prompt']+'\n',encoding='utf-8')
    proposal=ROOT/'proposal-character-corrections.json'
    proposal.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for args in [('commit',ROOT,'--from',proposal,'--reason','Correct demonstrated anatomical artifacts with approved original whole-toy photo'),('render-ready',ROOT)]:
        r=subprocess.run([sys.executable,str(HELPER),*map(str,args)],capture_output=True,text=True)
        if r.returncode:
            raise RuntimeError(r.stdout+r.stderr)
        print(r.stdout)
    record={'reasons':{k:reasons[k] for k in selected},'selected_asset_images_unchanged':True,'original_photo_already_approved':True,'no_new_image_generation':True,'prior_takes_retained':True}
    (ROOT/'exports'/'character-correction-review.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':
    main()
