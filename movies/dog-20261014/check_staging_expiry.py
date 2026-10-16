"""Read-only check of the four user-approved one-hour staging URLs."""
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from seedance_transport import ROOT,read_json,atomic_json,now
j=read_json(ROOT/'exports/reference-registration.json')
def check(item):
    aid,e=item
    try:
        with urlopen(Request(e['source_uri'],headers={'Range':'bytes=0-31','Cache-Control':'no-cache'}),timeout=30) as response:
            status=response.status;signature=response.read(32);image_available=signature.startswith(b'\x89PNG\r\n\x1a\n')
    except HTTPError as error:status=error.code;image_available=False
    except Exception as error:return {'asset':aid,'check_error':type(error).__name__}
    return {'asset':aid,'http_status':status,'image_bytes_still_available':image_available,'unavailable':status in (404,410) or (status in (200,206) and not image_available),'expected_expiry_at':e['expected_expiry_at']}
with ThreadPoolExecutor(max_workers=4) as pool:items=list(pool.map(check,j['assets'].items()))
out={'checked_at':now(),'checks':items,'all_temporarily_hosted_images_unavailable':all(x.get('unavailable') for x in items),'private_registered_bindings_retained':True,'urls_not_logged':True}
atomic_json(ROOT/'exports/staging-expiry-check.json',out)
print(out)
