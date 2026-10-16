"""Use a zero-byte disposable object to prove private transport before image upload."""
import json
import sys
import uuid
from urllib.request import urlopen
from urllib.error import HTTPError
from seedance_transport import ROOT, settings, atomic_json
sys.path.insert(0,str(ROOT/'tools/storage-deps'))
import tos
from tos.enum import ACLType, HttpMethodType

def main():
    cfg=settings()
    client=tos.TosClientV2(cfg['VOLC_ACCESS_KEY'],cfg['VOLC_SECRET_KEY_RAW'],'https://tos-ap-southeast-1.bytepluses.com','ap-southeast-1')
    candidates=json.loads((ROOT/'exports/private-storage-check.json').read_text(encoding='utf-8'))['existing_buckets']
    diagnostics=[]
    for b in candidates:
        if b['location']!='ap-southeast-1':continue
        key='codex-movie/dog-20261013/temporary/'+uuid.uuid4().hex+'/chan.png'
        try:
            result=client.put_object(b['name'],key,content=b'',content_length=0,acl=ACLType.ACL_Private,forbid_overwrite=True)
        except tos.exceptions.TosServerError as e:
            diagnostics.append({'bucket':b['name'],'put_status':e.status_code,'code':e.code})
            continue
        record={'bucket':b['name'],'object_key':key,'bytes':0,'etag':result.etag,'temporary':True,'private_acl_requested':True}
        atomic_json(ROOT/'exports/private-object-probe.json',record)
        unsigned=client.pre_signed_url(HttpMethodType.Http_Method_Get,b['name'],key,expires=3600).signed_url.split('?',1)[0]
        try:
            with urlopen(unsigned,timeout=30) as response:
                anonymous=response.status
        except HTTPError as e:anonymous=e.code
        record['anonymous_get_status']=anonymous
        atomic_json(ROOT/'exports/private-object-probe.json',record)
        if anonymous!=403:
            client.delete_object(b['name'],key)
            record['deleted']=True;atomic_json(ROOT/'exports/private-object-probe.json',record)
            raise RuntimeError('Object privacy could not be proved; empty test removed, no image uploaded')
        print({'private_object_upload':'available','anonymous_read':'denied','sensitive_bytes_uploaded':0},flush=True)
        return
    atomic_json(ROOT/'exports/private-object-probe-errors.json',diagnostics)
    print({'private_object_upload':'unavailable','sensitive_bytes_uploaded':0,'diagnostics':diagnostics},flush=True)

if __name__=='__main__':
    try:main()
    except Exception as e:print(type(e).__name__+': '+str(e));raise SystemExit(1)
