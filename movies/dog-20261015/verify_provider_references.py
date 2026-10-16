"""Read-only verification of existing private provider assets; no new upload."""
import hashlib
from seedance_transport import Client,ROOT,read_json,atomic_json,now

client=Client()
bindings=read_json(ROOT/'exports/provider-asset-bindings.json')
project=read_json(ROOT/'project.json')
for aid,entry in bindings.items():
    asset=next(a for a in project['asset_list'] if a['id']==aid)
    selected=next(c for c in asset['candidates'] if c['id']==asset['selected_candidate_id'])
    assert hashlib.sha256((ROOT/selected['path']).read_bytes()).hexdigest()==entry['source_sha256']
    data=client.management('GetAsset',{'Id':entry['provider_asset_id'],
        'ProjectName':client.config['VOLC_PROJECT_NAME']}).get('Result',{})
    assert data.get('Status')=='Active' and data.get('AssetType')=='Image',aid
    assert data.get('Moderation',{}).get('Strategy','Default')=='Default',aid
    entry['verified_at']=now()
    entry['status']='Active'
    print(aid,'existing private asset verified Active; approved local bytes match',flush=True)
atomic_json(ROOT/'exports/provider-asset-bindings.json',bindings)
