"""Target the observed cross-reference gear spill, preserving source beats and timings."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=json.loads(json.dumps(p))
changed=[]
for c in q['chapters']:
    if c['id']!='s02_c03' and c['chapter_index']<14:continue
    if '@TartWorking' not in c['tagged_assets']:continue
    lock='''CREAM DOG GEAR — TARGETED PHYSICAL LOCK
For cream Tart, the collar D-ring is EMPTY throughout working-harness action. There is no flexible cord, dangling lead, lead loop or orange line attached to his neck. The SILVER RIGID GUIDE HANDLE has two metal arms anchored to the brown harness and one brown cross-grip. During guided walking Ah Ming hand closes around that cross-grip; his hand does not hold a collar lead. While seated/stationary the rigid handle may rest. The orange flexible lead belongs ONLY to brown Tine, held by May. Objects/wardrobe from one dog never transfer to the other across montage cuts. In a Tart-only shot no Tine or orange lead appears. In a Tine-only shot no Tart or guide harness appears.
'''
    if c['id']=='s02_c03':
        lock+='During the first introduction only Ah Ming and cream Tart are present. After the seated greeting, the later-session walking insert shows Ah Ming holding the rigid silver guide handle. The clean cut to May and brown Tine happens after nine seconds; only there does an orange collar lead appear.\n'
    if 'CREAM DOG GEAR — TARGETED PHYSICAL LOCK' in c['prompt']:continue
    c['prompt']=c['prompt'].replace('ACTIVE REFERENCES\n',lock+'\nACTIVE REFERENCES\n',1)
    c.setdefault('prompt_refinements',[]).append({'reason':'Observed orange collar-lead spill onto cream working Tart in the first introduction take. Separate reference ownership and specify rigid handle mechanics.','source_take':'s02_c03/take_01' if c['id']=='s02_c03' else 'preventive before first submission'})
    changed.append(c['id'])
q.setdefault('production_quality_notes',[]).append('Training introduction take 01 requires replacement for an extra flexible lead on working Tart. Future working-dog prompts distinguish the rigid handle from Tine orange collar lead. No selected asset or style changed.')
proposal=ROOT/'proposal-gear-refinement.json';proposal.write_text(json.dumps(q,ensure_ascii=False,indent=2),encoding='utf-8')
print(helper.save(ROOT,p,q,'Refine guide-handle mechanics after first generated training inspection'))
print('Prompt-only refinements:',','.join(changed))
