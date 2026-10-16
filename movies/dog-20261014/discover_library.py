"""Read-only search for an already registered exact character, no broad image scan."""
import hashlib,json
from urllib.request import urlopen
from seedance_transport import Client,ROOT,atomic_json,now
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
a=next(a for a in p['asset_list'] if a['id']=='asset_uncle_chan')
candidate=next(x for x in a['candidates'] if x['id']==a['selected_candidate_id'])
digest=hashlib.sha256((ROOT/candidate['path']).read_bytes()).hexdigest()
client=Client();report={'checked_at':now(),'source_sha256':digest,'read_only':True,'libraries':{},'specific_matches':[]}
for action in ('ListAssetGroups','ListAssets'):
    token=None;count=0;pages=0
    while True:
        body={'ProjectName':client.config['VOLC_PROJECT_NAME'],'Filter':{'GroupType':'AIGC'},'MaxResults':100,'SortBy':'CreateTime','SortOrder':'Desc'}
        if token:body['NextToken']=token
        result=client.management(action,body).get('Result',{})
        items=result.get('Items',[]);count+=len(items);pages+=1
        if action=='ListAssets':
            for x in items:
                name=str(x.get('Name','')).lower()
                if not any(s in name for s in ('uncle_chan','unclechan','uncle-chan','chenbo','chen_bo','陳伯','陈伯','dog-20261013-chan',digest)):continue
                record={k:x.get(k) for k in ('Id','Status','AssetType')}
                record['specific_metadata_match']=True
                if x.get('Status')=='Active' and x.get('AssetType')=='Image':
                    full=client.management('GetAsset',{'Id':x['Id'],'ProjectName':client.config['VOLC_PROJECT_NAME']}).get('Result',{})
                    url=full.get('URL')
                    if url:
                        with urlopen(url,timeout=30) as response:raw=response.read(30*1024*1024)
                        record['exact_source_sha256_match']=hashlib.sha256(raw).hexdigest()==digest
                report['specific_matches'].append(record)
        token=result.get('NextToken')
        if not token:break
    report['libraries'][action]={'count':count,'pages':pages}
atomic_json(ROOT/'exports/private-library-discovery.json',report)
print(json.dumps(report,ensure_ascii=False))
