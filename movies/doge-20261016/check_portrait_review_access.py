"""Read-only capability check for provider-reviewed fictional cartoon portraits."""
import sys
from seedance_transport import Client,ROOT,atomic_json,now
sys.path.insert(0,str(ROOT.parent/'dog-20261013/tools/storage-deps'))
import tos,logging
logging.getLogger('tos').setLevel(logging.CRITICAL)
try:
    client=Client()
    body={'Filter':{'GroupType':'AIGC'},'MaxResults':100}
    if client.config['VOLC_PROJECT_NAME']:body['ProjectName']=client.config['VOLC_PROJECT_NAME']
    r=client.management('ListAssetGroups',body).get('Result',{})
    groups=r.get('Items',[])
    # Only metadata for the existing provider account's private staging capability.
    storage=tos.TosClientV2(client.config['VOLC_ACCESS_KEY'],client.config['VOLC_SECRET_KEY_RAW'],'https://tos-ap-southeast-1.bytepluses.com','ap-southeast-1')
    result=storage.list_buckets()
    buckets=[{'name':b.name,'location':b.location} for b in result.buckets if b.location=='ap-southeast-1']
    atomic_json(ROOT/'exports/portrait-review-access.json',{'checked_at':now(),'groups':[{'id':g['Id'],'type':g.get('GroupType'),'name':g.get('Name'),'project':g.get('ProjectName')} for g in groups],'existing_regional_buckets':buckets,'next_token_present':bool(r.get('NextToken')),'moderation_change_permitted':False,'new_bucket_creation_permitted':False})
    print({'existing_aigc_groups':len(groups),'existing_regional_staging_buckets':len(buckets),'new_uploads':0,'standard_review_required':True})
except Exception as e:
    print({'check_stopped':True,'error_type':type(e).__name__,'code':getattr(e,'code',None),'http_status':getattr(e,'status_code',None)})
    raise SystemExit(1)
