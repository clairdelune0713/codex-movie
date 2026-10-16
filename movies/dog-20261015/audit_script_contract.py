"""Check final directed dialogue against the unchanged supplied screenplay."""
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
source=ROOT/'source/SOMEWHERE_BETWEEN_US_READY/06_CONTINUITY/SCREENPLAY_STRUCTURE.json'
s=json.loads(source.read_text(encoding='utf-8'))
original=[b['text'] for sc in s['scenes'] for b in sc['blocks'] if b['type']=='dialogue']
planned=[b['text'] for c in p['chapters'] for b in c['planning_source_blocks'] if b['type']=='dialogue']
directed=[line for c in p['chapters'] for line in re.findall(r'EXACT DIALOGUE[^\n]*?「([^」]+)」',c['prompt'])]
result={'source_revision':p['revision'],'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'original_entries':len(original),'planned_entries':len(planned),'prompt_entries':len(directed),
    'exact_original_order':original==planned,'exact_prompt_order':original==directed,
    'duration_seconds':sum(c['duration'] for c in p['chapters']),'chapters':len(p['chapters']),
    'shots':sum(len(c['shots']) for c in p['chapters']),
    'scope':'Script/preflight only. Does not establish word-perfect generated audio.'}
assert original==planned==directed, 'Directed dialogue differs from supplied original'
assert result['duration_seconds']==600
path=ROOT/'exports'/('script-contract-r%06d.json'%p['revision'])
path.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
