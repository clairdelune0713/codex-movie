"""Local Movi2 helpers; no secrets or provider calls."""
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
HELPER=Path(r'C:\Users\Admin 3\.codex\skills\movi2\scripts\project.py')
spec=importlib.util.spec_from_file_location('movi_project',HELPER)
helper=importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
def write_json(path,value):
    helper.atomic_write(path,value)
def commit(proposal,reason):
    current=helper.read(ROOT/'project.json')
    if proposal['revision']!=current['revision']:
        raise RuntimeError('Stale proposal')
    return helper.save(ROOT,current,proposal,reason)
