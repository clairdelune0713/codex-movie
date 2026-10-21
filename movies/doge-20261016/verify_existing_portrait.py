"""Read-only check for an already approved, byte-identical provider portrait.

No new upload, no moderation changes, no creation or generation requests.
Uses only official trusted-asset approval as documented by BytePlus.
"""
import hashlib,json
from pathlib import Path
from seedance_transport import Client,ROOT,atomic_json,now
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
old=json.loads((ROOT.parent/'dog-20261015/exports/provider-asset-bindings.json').read_text(encoding='utf-8'))
a=next(a for a in p['asset_list'] if a['tag']=='@Mr-Ko')
c=next(c for c in a['candidates'] if c['id']==a['selected_candidate_id'])
sha=hashlib.sha256((ROOT/c['path']).read_bytes()).hexdigest()
matches=[v for v in old.values() if v.get('source_sha256')==sha]
assert len(matches)==1,'Need exactly one previously approved identical image'
entry=matches[0];client=Client()
body={'Id':entry['provider_asset_id']}
if client.config['VOLC_PROJECT_NAME']:body['ProjectName']=client.config['VOLC_PROJECT_NAME']
data=client.management('GetAsset',body).get('Result',{})
assert data.get('Status')=='Active' and data.get('AssetType')=='Image','Provider approval is not active'
assert data.get('Moderation',{}).get('Strategy','Default')=='Default','Only full default review is acceptable'
body={'Id':data['GroupId']}
if client.config['VOLC_PROJECT_NAME']:body['ProjectName']=client.config['VOLC_PROJECT_NAME']
group=client.management('GetAssetGroup',body).get('Result',{})
assert group.get('GroupType')=='AIGC','Only original fictional virtual portraits, no real-person identity assertion'
atomic_json(ROOT/'exports/provider-asset-bindings.json',{a['id']:{'provider_asset_id':entry['provider_asset_id'],'source_sha256':sha,'status':'Active','verified_at':now(),'moderation_strategy':'Default','group_type':'AIGC','approval_basis':'Byte-identical original cartoon Ko already approved in provider private AIGC library; status and default moderation independently verified live. No new upload, image changes or moderation relaxation.','official_workflow_uri':'https://docs.byteplus.com/en/docs/modelark/private-virtual-avatar-library-guide-preview'}})
print({'unchanged_cartoon_portrait':'Mr Ko','provider_approval':'Active','moderation':'Default','fictional_group':'AIGC','new_uploads':0})
