"""Prepare the approved original-cast director and verified provider adapter."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent
OLD=ROOT.parent/'midnight-phantom'
for filename in ['project_ops.py','seedance_client.py','assemble_movie.py']:
    target=ROOT/filename
    if target.exists():raise RuntimeError('Production file exists; inspect before changing '+filename)
    code=(OLD/filename).read_text(encoding='utf-8')
    if filename=='assemble_movie.py':
        code=code.replace("FFMPEG=ROOT/'.media-tools/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe'","FFMPEG=ROOT.parent/'midnight-phantom/.media-tools/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe'")
    target.write_text(code,encoding='utf-8')
source=(OLD/'finalize_prompts.py').read_text(encoding='utf-8')
source=source.replace("    if '@UserReference' not in chapter['tagged_assets']:chapter['tagged_assets'].append('@UserReference')\n",'')
changes=[('CUPHEAD','RIFF'),('MUGMAN','PIP'),('Cuphead','Riff'),('Mugman','Pip'),('Inkwell City','Inkbell City'),('ceramic brothers','otter brothers'),('ceramic heads','otter heads'),('red shorts/shoes/straw and Pip blue','rust waistcoat/green trousers and Pip teal cardigan/russet trousers'),('Riff red, Pip blue','Riff ginger in rust/green, Pip chocolate in teal/mustard'),('Riff has red shorts/shoes/straw and Pip blue','Riff has rust waistcoat and green trousers; Pip has teal cardigan and russet trousers'),('pulls his straw below cover','ducks his rounded ears below cover'),('head, handles, straws, gloves, shorts and shoe colors','fur, muzzle, ears, tails, glasses, gloves, costumes and shoe colors'),('heads, handles, straws, gloves, shorts and shoe colors','fur, muzzle, ears, tails, glasses, gloves, costumes and shoe colors'),('straws fully inside frame','ears and tails fully inside frame'),('red shorts','forest-green trouser cuffs'),('red and blue','rust/green and teal/mustard'),('shorts pocket','trouser pocket'),('thin cream legs','fur-covered legs'),('youthful brash medium-pitched expressive male cartoon voice, sharp Brooklyn-flavored comic delivery','warm brash baritone cartoon voice, rapid playful delivery'),('youthful lighter nervous male cartoon voice, clear diction, becoming assured during deduction','lighter dry tenor cartoon voice, clear nervous diction becoming assured during deduction')]
for before,after in changes:source=source.replace(before,after)
source=source.replace("p['detailed_script']=p['detailed_script'].replace('16:9','21:9')", "p['detailed_script']=p['detailed_script'].replace('MUGMAN','PIP').replace('CUPHEAD','RIFF').replace('Recast screenplay awaiting revised asset approval','Approved original-cast production screenplay').replace('16:9','21:9')")
source=source.replace("p['render_tool_discovery']['direct_api_authorization']=", "for c in p['chapters']:\n    for line in c['dialogue']:line['text']=line['text'].replace('MUGMAN','PIP').replace('CUPHEAD','RIFF')\np['render_tool_discovery']['direct_api_authorization']=")
source=source.replace("p['master_prompt_raw']=p['master_prompt_raw'].replace('16:9','21:9')", "p['master_prompt_raw']=p['master_prompt_raw'].replace('Final director prompts wait for approval of the revised image set.','Approved original-cast director prompts and native audio.').replace('16:9','21:9')")
source=source.replace('Finish in the exact end state for the next cut.','Finish in the exact end state for the next cut. Entirely original otter detective characters; only the approved eleven original character/location/prop references guide this film.')
(ROOT/'finalize_prompts.py').write_text(source,encoding='utf-8')
print('Original-cast director, adapter and assembly tools prepared; existing FFmpeg runtime reused.')
