"""Check only two specific existing candidates for transport re-encoding equivalence."""
import hashlib,io,json
from urllib.request import urlopen
from PIL import Image,ImageChops,ImageStat
from seedance_transport import Client,ROOT,atomic_json,now
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
a=next(a for a in p['asset_list'] if a['id']=='asset_uncle_chan');c=next(c for c in a['candidates'] if c['id']==a['selected_candidate_id'])
source=Image.open(ROOT/c['path']).convert('RGB');previous=json.loads((ROOT/'exports/private-library-discovery.json').read_text(encoding='utf-8'))
client=Client();rows=[]
for item in previous['specific_matches']:
    if item['Status']!='Active':continue
    full=client.management('GetAsset',{'Id':item['Id'],'ProjectName':client.config['VOLC_PROJECT_NAME']}).get('Result',{})
    with urlopen(full['URL'],timeout=30) as response:raw=response.read(30*1024*1024)
    remote=Image.open(io.BytesIO(raw)).convert('RGB')
    same_size=remote.size==source.size
    error=sum(ImageStat.Stat(ImageChops.difference(source.resize((384,256)),remote.resize((384,256)))).mean)/3
    rows.append({'id':item['Id'],'dimensions':remote.size,'same_dimensions':same_size,'mean_pixel_error_255':round(error,4),'transport_equivalent':same_size and error<1.5,'remote_sha256':hashlib.sha256(raw).hexdigest()})
atomic_json(ROOT/'exports/private-candidate-comparison.json',{'checked_at':now(),'source_dimensions':source.size,'candidates':rows})
print(json.dumps(rows))
