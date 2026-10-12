import copy, hashlib, importlib.util, json, shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OLD=ROOT.parent/'somewhere-between-us'
spec=importlib.util.spec_from_file_location('h','C:/Users/admina/.codex/skills/movi2/scripts/project.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
initial=h.read(ROOT/'project.json')
assert initial['revision']==0
approved=h.read(ROOT/'source/approved-adaptation-state.json')
assert approved['asset_review']['status']=='approved'
files=set([approved['source_pdf_path']])
for asset in approved['asset_list']:
    files.update(c['path'] for c in asset['candidates'])
    files.update(asset.get('reference_paths',[]))
for relative in files:
    src=OLD/relative;dst=ROOT/relative
    dst.parent.mkdir(parents=True,exist_ok=True)
    if not dst.exists():shutil.copy2(src,dst)
    else:assert hashlib.sha256(dst.read_bytes()).digest()==hashlib.sha256(src.read_bytes()).digest()
proposal=copy.deepcopy(approved)
proposal.update(id=initial['id'],revision=initial['revision'],project_name=initial['project_name'],
    created_at=initial['created_at'],updated_at=initial['updated_at'])
proposal['asset_review']=None
proposal['render_state']={'status':'finalizing_prompts','video_generation':'not_submitted','delivery':'not_rendered','video_takes_generated':0}
proposal['creation_note']='Separate new movie requested on 2026-10-09; approved design set reused, no earlier rendered takes imported.'
for c in proposal['chapters']:
    c.update(takes=[],active_take_id=None,screenshots=[],storyboards=[],selected_storyboard_id=None,
             initial_prompt='',materials=[])
h.atomic_write(ROOT/'exports/initial-proposal.json',proposal)
errors,warnings=h.validate(ROOT,proposal)
assert not errors,errors
print(h.save(ROOT,initial,proposal,'Create separate 352-second movie from approved image assets; no previous takes'))
# This is precisely the already displayed and approved image set, with unchanged relative paths and bytes.
assert h.review_manifest(ROOT,proposal)['fingerprint']==approved['asset_review']['fingerprint']
original=h.read(OLD/'history/revision-000014.json');current=h.read(OLD/'project.json')
assert current['id']==original['id'] and current['asset_list']==original['asset_list'] and current['chapters']==original['chapters']
assert current['render_state']==original['render_state'] and current['detailed_script']==original['detailed_script']
print('Verified original movie state restored; new movie has its own identity and no old takes.')
