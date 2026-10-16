"""Prepare the supported private AIGC group; never accept terms or publish files."""
from seedance_transport import Client,ROOT,atomic_json,read_json,now
client=Client();state=ROOT/'exports/private-registration.json'
if state.exists():
    print({'state':'already journaled','path':state.name});raise SystemExit(0)
name='dog-20261014-approved-references'
token=None;matches=[]
while True:
    body={'ProjectName':client.config['VOLC_PROJECT_NAME'],'Filter':{'GroupType':'AIGC'},'MaxResults':100}
    if token:body['NextToken']=token
    result=client.management('ListAssetGroups',body).get('Result',{})
    matches.extend(x for x in result.get('Items',[]) if x.get('Name')==name)
    token=result.get('NextToken')
    if not token:break
if len(matches)>1:raise RuntimeError('Ambiguous existing task group; inspect before creating')
if matches:
    group=matches[0];reason='Existing exact task group reused'
else:
    atomic_json(state,{'state':'creating_group','name':name,'at':now(),'images_uploaded':0,'public_staging':False,'legal_terms_accepted_by_agent':False})
    result=client.management('CreateAssetGroup',{'Name':name,'Description':'Approved original fictional stylized 3D references for user-requested dog-20261014 movie; local originals remain canonical.','GroupType':'AIGC','ProjectName':client.config['VOLC_PROJECT_NAME']})
    group=result.get('Result',result);reason='Empty task-specific private AIGC group created, no image upload'
if not group.get('Id'):raise RuntimeError('No group ID; reconcile creation journal before retry')
atomic_json(state,{'state':'group_ready','name':name,'group_id':group['Id'],'verified_at':now(),'images_uploaded':0,'public_staging':False,'legal_terms_accepted_by_agent':False,'reason':reason})
print({'state':'group_ready','name':name,'images_uploaded':0,'public_staging':False})
