import copy, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('h','C:/Users/admina/.codex/skills/movi2/scripts/project.py')
h=importlib.util.module_from_spec(s);s.loader.exec_module(h)
p=h.read(ROOT/'project.json');q=copy.deepcopy(p);c=q['chapters'][27]
c['audio_mode']='local_original_ambience'
c['prompt']+='\nVIDEO-ONLY GENERATION: Do not synthesize audio. This chapter will receive a locally synthesized original wind-and-paw ambience track in post-production, with no music, human voice or recorded content.\n'
print(h.save(ROOT,p,q,'Use video-only flashback generation and locally composed original ambience after repeated provider audio rejection'))
