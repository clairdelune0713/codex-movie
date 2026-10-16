"""Use an earlier inspected outdoor frame after repeated doorway hallucination."""
import json,hashlib,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as h
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=json.loads(json.dumps(p))
source=next(c for c in p['chapters'] if c['id']=='s13_c02')
t=next(t for t in source['takes'] if t['id']==source['active_take_id'])
assert t['visual_review']['inspected'] and not t['visual_review']['requires_repair']
assert t['dependency_fingerprint']==h.chapter_fingerprint(ROOT,p,source)
c=next(c for c in q['chapters'] if c['id']=='s15_c02')
c['continuity_references'].append({'id':'open_air_bay_s13_c02','path':f"chapters/s13_c02/screenshots/{t['id']}_review_04.jpg",'media_type':'Image','role':'reference_image','source_chapter_id':source['id'],'source_take_id':t['id'],'source_sha256':hashlib.sha256((ROOT/t['path']).read_bytes()).hexdigest(),'source_timestamp':16.8,'inspected':True,'reason':'Carry ONLY the OPEN-AIR public harbour paving, LOW round planters, harbour railing and broad sky visible above Bo. The passage here is the gap BETWEEN two LOW PLANTERS, no tall walls, roof, corridor or tunnel. Ignore distant ferry building, old actor action and dialogue. Place stroller and teal suitcase on THIS open paving, clear them aside, then guide pair walks through planter gap toward the bench. Other continuity image controls only rigid guide-handle hand contact.'})
c['prompt']='OPEN SKY IN EVERY SHOT. Full side view across ordinary open harbour paving: two KNEE-HIGH ROUND PLANTERS create a small gap, suitcase partly in that gap and stroller passing horizontally in front. Bo stands just behind the two planters by an OUTDOOR bench. Camera remains OUTSIDE in open air. No shot from inside any doorway. The gap is low pots, never walls. After the case moves aside, pair walks horizontally SCREEN-RIGHT through the pot gap.\n\n'+c['prompt']
c['shots'][0]['camera']='40mm wide SIDE VIEW of two knee-high planters on open harbour path, sky visible, then medium conversation'
c['shots'][1]['camera']='35mm open-air side wide with suitcase owner and passing stroller, low planter pots and sky visible'
c['shots'][2]['camera']='40mm lateral side track across gap between LOW PLANTERS, open sky above'
c['prompt']=c['prompt'].replace('40mm entrance wide then conversational medium.','40mm open-air side wide across knee-high planters with sky visible, then conversational medium.')
c['prompt']=c['prompt'].replace('Hard cut to 35mm wide with owner hands and stroller.','Hard cut to 35mm open-air side wide with owner hands and stroller, knee-high pots and sky visible.')
c['prompt']=c['prompt'].replace('Hard cut to 40mm side track across widened opening.','Hard cut to 40mm lateral side track SCREEN-RIGHT through gap between low planter pots with sky visible.')
c.setdefault('prompt_refinements',[]).append({'reason':'Second generated take still invented corridor despite text. Add minimal actual earlier successful exterior frame and replace entrance camera phrasing with low-planter side views.'})
print(h.save(ROOT,p,q,'Ground seating passage in inspected open-air harbour frame'))
