"""Fix the demonstrated unintended hat without changing approved images."""
from project_ops import ROOT,helper,commit
p=helper.read(ROOT/'project.json')
for ch in p['chapters']:
    if ch['takes'] and ch['id']!='chapter_01':raise RuntimeError('Later chapters already submitted; preserve prompts')
    for shot in ch['shots']:
        if ch['id']=='chapter_01':
            shot['action']=shot['action'].replace('@Riff adjusts an IMAGINARY detective hat with his white glove, raises one eyebrow and boasts.','@Riff taps his BARE forehead with his white glove, raises one eyebrow and boasts.').replace('No physical detective hat appears.','His ginger forelock and rounded ears remain completely uncovered.')
    ch['prompt']=ch['prompt'].replace('No physical detective hat appears.','His ginger forelock and rounded ears remain completely uncovered.').replace('No physical detective hat.','Riff remains bareheaded with his ginger forelock and rounded ears fully visible.')
    ch['prompt']=ch['prompt'].replace('@Riff adjusts an IMAGINARY detective hat with his white glove, raises one eyebrow and boasts.','@Riff taps his BARE forehead with his white glove, raises one eyebrow and boasts.')
    ch['prompt']+='\nCHARACTER CONTINUITY: Riff has a bare ginger-furred forehead, visible rounded ears and short forelock. Pip keeps his round wire-rim glasses. Follow the approved clothing sheets and preserve fur, ears, whiskers and tails. Only the explicitly timed removable dumpster-lid gag can temporarily cover Riffs forehead; it is dropped immediately afterward.'
    ch['handoff']=ch['shots'][-1]['end_state']
    (ROOT/'chapters'/ch['id']/'prompt-v02.txt').write_text(ch['prompt'],encoding='utf-8')
first=p['chapters'][0]
first['scene_summary']=first['scene_summary'].replace('Riff mimes a detective hat.','Riff theatrically taps his bare forehead.')
p['detailed_script']=p['detailed_script'].replace('Riff mimes a detective hat.','Riff theatrically taps his bare forehead.')
for t in first['takes']:
    t['quality_disposition']='Retained first take: unexpected physical fedora appears; replacement fixes character continuity.'
p['script_changes'].append('Replace the imaginary-hat mime with a bare-forehead detective gesture after the first generated take introduced an unintended fedora. All approved asset images remain unchanged.')
result=commit(p,'Refine original-cast bare-head continuity after first successful render; preserve initial take')
(ROOT/'screenplay.md').write_text(p['detailed_script'],encoding='utf-8')
print('Continuity refinement committed; image approval unchanged.')
