import copy,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=copy.deepcopy(p)
c=q['chapters'][50]
for tag in ['@Tart-off-duty','@Tine','@victoria-harbour']:
    if tag not in c['tagged_assets']:c['tagged_assets'].append(tag)
c['prompt']+='\nPOSTCARD PRINT REFERENCES ONLY\n@Tart-off-duty and @Tine identify the TWO ADULT DOGS printed side by side on the small postcard, with @victoria-harbour printed behind them. These three images apply ONLY to the small photograph, not to live subjects or the ranch environment. No dogs physically at the ranch. The postcard shows original adult cream Tart in brown collar beside original fox-red Tine in orange bandana. Keep the printed photo simple and small in the medium shot.'
c['initial_prompt']=c['prompt']
print(helper.save(ROOT,p,q,'Bind approved adult dogs only to scene 51 postcard photograph'))
