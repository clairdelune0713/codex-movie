"""Read existing provider jobs; never submit generation requests."""
from urllib.parse import urlencode
from urllib.request import Request
from seedance_transport import Client, response, BASE
import render_finale as render

client=Client();client.resolve()
j=render.journal();take=j['takes']['chapter_41']
assert take['submission_state']=='submitting' and not take.get('task_id')
known={t['task_id'] for t in j['takes'].values() if t.get('task_id')}
for t in j['takes'].values():
    known.update(old['task_id'] for old in t.get('prior_takes',[]) if old.get('task_id'))
items=[];page=1
while True:
    query=urlencode({'page_num':page,'page_size':100,'filter.model':client.endpoint})
    data=response(Request(BASE+'?'+query,headers={'Authorization':'Bearer '+client.get_token(),
        'Content-Type':'application/json','X-Project-Name':client.config['VOLC_PROJECT_NAME']},method='GET'))
    items.extend(data.get('items',[]))
    if len(items)>=data['total']:break
    assert data.get('items') and page<500
    page+=1
unmatched=[t['id'] for t in items if t['id'] not in known]
assert not unmatched, 'Unmatched provider tasks need manual association before any retry'
evidence={'checked_at':render.now(),'complete_endpoint_task_listing':True,
    'provider_task_count':len(items),'unmatched_task_ids':unmatched,
    'source':'https://docs.byteplus.com/en/docs/modelark/list-video-generation-tasks-api',
    'reason':'Every task returned for the verified endpoint is already associated with a different journaled attempt. No accepted scene 41 task exists.'}
take.update(status='failed',submission_state='not_accepted',reconciliation=evidence,
    error={'code':'LocalSubmissionInterrupted','reason':'Provider listing confirms no accepted task; safe to submit remaining planned scene once.'})
render.save(render.ROOT/'exports/scene-41-reconciliation.json',evidence)
render.save(render.JOURNAL,j);render.record(take)
print('Reconciled scene 41: no accepted provider job; all',len(items),'existing tasks accounted for.')
