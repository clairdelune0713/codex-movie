"""Repair observed time-of-day and public-pavement continuity, keep all source beats."""
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as h
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=json.loads(json.dumps(p))
source=next(c for c in p['chapters'] if c['id']=='s07_c02');take=next(t for t in source['takes'] if t['id']==source['active_take_id'])
assert take['visual_review']['inspected'] and not take['visual_review']['requires_repair'] and take['dependency_fingerprint']==h.chapter_fingerprint(ROOT,p,source)
for c in q['chapters']:
    if c['id']=='s07_c03':
        c['prompt']='EVENING CONTINUITY LOCK: It is still the SAME MONDAY EVENING AFTER DARK as the preceding toy tug. Use the NIGHT flat view. Warm practical lamps, deep blue exterior windows with lit Hong Kong building windows, no sun or daylight beams. The next editing scene is the same evening.\n\n'+c['prompt']
        c['continuity_references']=[{'id':'night_toy_handoff','path':f"chapters/s07_c02/screenshots/{take['id']}_review_04.jpg",'media_type':'Image','role':'reference_image','source_chapter_id':'s07_c02','source_take_id':take['id'],'source_sha256':hashlib.sha256((ROOT/take['path']).read_bytes()).hexdigest(),'source_timestamp':16.8,'inspected':True,'reason':'Carry the same after-dark blue-window/warm-lamp flat, oatmeal chair/side-table/cushion geometry, collar-only Tart and one toy initially shared between man hand and dog mouth. New action is release, cushion plop, laugh, toy return; do not repeat preceding dialogue/tug or its framing.'}]
        c.setdefault('prompt_refinements',[]).append({'reason':'Observed first take switched to daylight between two evening clips; preserve exact same night and toy handoff.'})
    if c['id']=='s08_c02':
        c['prompt']='本段冇對白、冇旁白，只有街聲、腳步聲、領圈輕響同輕配樂。阿May同阿華田沿公眾行人路向畫面右邊行離港鐵入口，始終留喺地面行人路；入口樓梯留喺左邊背景。\n\nPUBLIC PAVEMENT GEOMETRY LOCK: MTR stair opening stays LEFT background behind its stone wall and railing. The public pavement runs HORIZONTALLY SCREEN-RIGHT along the wall towards the centre. Last shot shows May and Tine WALKING SIDEWAYS SCREEN-RIGHT AWAY FROM THE STAIR OPENING, not walking into depth toward stairs. All their paws/feet remain on level public paving; the stair opening drops behind them at left. Crop the stair opening out of the final walking shot if necessary. No railway threshold or descent.\n\n'+c['prompt']
        c['first_frame']+=' The eventual departure follows the level public path horizontally right, away from the left-background stair opening.'
        c['shots'][-1]['action']+=' May and Tine leave horizontally SCREEN-RIGHT along the level PUBLIC PAVEMENT toward the centre, with station opening behind them to LEFT. They remain on level paving and never step toward or down the station stairs. No spoken line in this clip.'
        # Keep the structured action and cinematic timeline synchronized.
        c['prompt']=c['prompt'].replace('Time check, one last look, willing follow toward centre; keep Tine outside station.','Time check, one last look, then May/Tine walk horizontally SCREEN-RIGHT away from the left-background stairs along level public paving toward centre; keep Tine outside station. No dialogue.')
        c.setdefault('prompt_refinements',[]).append({'reason':'Observed ending points May/Tine toward MTR stairs; public visiting dog must stay outside and travel along pavement to centre. Remove unrequested spoken adlib in this wordless near miss.'})
print(h.save(ROOT,p,q,'Repair evening lighting and keep visiting pair on public pavement'))
