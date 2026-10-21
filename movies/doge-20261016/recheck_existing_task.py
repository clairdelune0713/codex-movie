"""Recheck existing accepted task only. Never POST a new generation."""
import json
from seedance_transport import Client,ROOT,atomic_json,now,ApiFailure
try:
    j=json.loads((ROOT/'exports/task-journal.json').read_text(encoding='utf-8'))
    client=Client();client.resolve()
    results=[]
    for cid,t in j['takes'].items():
        if not t.get('task_id'):continue
        data=client.task(task_id=t['task_id'])
        results.append({'chapter_id':cid,'task_id':t['task_id'],'status':data.get('status'),'error_code':(data.get('error') or {}).get('code'),'usage':data.get('usage',{})})
    result={'checked_at':now(),'operation':'GET existing task status only; no generation POST or altered references','new_generation_attempts':0,'results':results}
    atomic_json(ROOT/'exports/provider-status-recheck.json',result)
    print(json.dumps(result,indent=2))
except ApiFailure as e:
    print(json.dumps({'status_lookup_failed':True,'http_status':e.status,'code':e.code,'new_generation_attempts':0}))
    raise SystemExit(1)
except Exception as e:
    print(json.dumps({'status_lookup_failed':True,'error_type':type(e).__name__,'new_generation_attempts':0}))
    raise SystemExit(1)
