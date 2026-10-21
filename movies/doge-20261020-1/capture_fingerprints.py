import importlib.util, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
helper=Path('C:/Users/Admin 3/.codex/skills/movi2/scripts/project.py')
spec=importlib.util.spec_from_file_location('movi2_project',helper)
module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
project=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
data={'revision':project['revision'],'assets':{a['id']:module.asset_fingerprint(ROOT,project,a) for a in project['asset_list']}}
(ROOT/f"generation-baseline-r{project['revision']}.json").write_text(json.dumps(data,indent=2),encoding='utf-8')
print(json.dumps(data))
