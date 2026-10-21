"""Record direct human report; acceptance is verified by the next provider response."""
import copy,json,sys,uuid
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=copy.deepcopy(p)
assert helper.review_state(ROOT,p)['ready'],'Approved image set changed'
j=json.loads((ROOT/'exports/task-journal.json').read_text(encoding='utf-8'))
q['user_reported_provider_clearance']={'id':'clearance_'+uuid.uuid4().hex,'reported_at':datetime.now(timezone.utc).isoformat(),'confirmation':"it's cleared",'source':'Direct human user statement in this chat','provider_clearance_independently_verified':False,'covered_prior_attempt_ids':[t['attempt_id'] for t in j['takes'].values() if t['status']=='failed'],'conditions':'One new submission of each previously failed scene. Preserve approved references/settings and full provider filtering. Any new protective refusal stops submissions; no automatic repeat.'}
q['provider_review_required']=False
q['stage']='resume_after_user_reported_clearance'
q['render_status']='ready_for_authorized_submission'
print(helper.save(ROOT,p,q,'Record user report that provider block is cleared; resume approved scope with provider checks intact'))
