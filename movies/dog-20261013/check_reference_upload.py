"""Test documented private Files upload for the unchanged fictional Chan sheet.

No moderation settings are changed, no public server/bucket is created, and
authorization headers or transient download URLs are never printed or saved.
"""
import hashlib
import json
import uuid
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import HTTPError
from seedance_transport import Client, response, ROOT, atomic_json

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):return None

def main():
    p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
    a=next(a for a in p['asset_list'] if a['id']=='asset_009')
    selected=next(c for c in a['candidates'] if c['id']==a['selected_candidate_id'])
    raw=(ROOT/selected['path']).read_bytes()
    client=Client();client.resolve()
    token=client.get_token()
    boundary='codex-'+uuid.uuid4().hex
    body=(f'--{boundary}\r\nContent-Disposition: form-data; name="purpose"\r\n\r\nuser_data\r\n'
        f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="dog-20261013-chan.png"\r\nContent-Type: image/png\r\n\r\n').encode()+raw+f'\r\n--{boundary}--\r\n'.encode()
    base='https://ark.ap-southeast.bytepluses.com/api/v3/files'
    headers={'Authorization':'Bearer '+token,'X-Project-Name':client.config['VOLC_PROJECT_NAME']}
    result=response(Request(base,data=body,headers={**headers,'Content-Type':'multipart/form-data; boundary='+boundary},method='POST'))
    fid=result.get('id')
    if not fid:raise RuntimeError('Files upload returned no file ID')
    atomic_json(ROOT/'exports/reference-upload-check.json',{
        'source_asset_id':a['id'],'source_sha256':hashlib.sha256(raw).hexdigest(),
        'provider_file_id':fid,'status':result.get('status'),'response_fields':list(result),
        'purpose':'Supported virtual-character library ingestion investigation; unchanged original bytes',
        'signed_url_saved':False,'moderation_changed':False})
    print({'file_upload':'succeeded','status':result.get('status'),'response_fields':list(result)},flush=True)
    # Read-only capability probe: no cross-domain auth forwarding.
    opener=build_opener(NoRedirect())
    try:
        with opener.open(Request(base+'/'+fid+'/content',headers=headers),timeout=30) as output:
            print({'content_route_status':output.status,'redirect_available':False},flush=True)
    except HTTPError as error:
        print({'content_route_status':error.code,'redirect_available':bool(error.headers.get('Location'))},flush=True)

if __name__=='__main__':
    try:main()
    except Exception as e:print(type(e).__name__+': '+str(e));raise SystemExit(1)
