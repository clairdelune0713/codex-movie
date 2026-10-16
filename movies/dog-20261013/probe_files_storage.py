"""Test documented Files-to-existing-TOS transport using a harmless disposable PDF.

No character image is uploaded. No bucket, ACL or permission is changed.
Every accepted probe file is journaled and removed through the Files API.
"""
import io
import uuid
import json
import re
import base64
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import quote
from reportlab.pdfgen import canvas
from seedance_transport import Client, ROOT, atomic_json, read_json, response, ApiFailure, now


def upload_response(request, config, sensitive):
    try:
        with urlopen(request, timeout=40) as output:
            return json.loads(output.read())
    except HTTPError as error:
        payload = json.loads(error.read())
        detail = payload.get('error', {})
        message = str(detail.get('message', ''))
        for value in list(config.values()) + sensitive:
            message = message.replace(value, '[redacted]')
        message = re.sub(r'https?://\S+', '[URL]', message)
        failure = ApiFailure(error.code, detail.get('code', 'HTTPError'))
        failure.safe_message = message[:400]
        raise failure from None


def main():
    client = Client()
    client.resolve()
    buffer = io.BytesIO()
    document = canvas.Canvas(buffer)
    document.drawString(40, 800, 'Disposable movie storage transport probe. No personal data.')
    document.showPage()
    document.save()
    harmless = buffer.getvalue()
    base = 'https://ark.ap-southeast.bytepluses.com/api/v3/files'
    headers = {'Authorization': 'Bearer ' + client.get_token(),
               'X-Project-Name': client.config['VOLC_PROJECT_NAME']}
    # The provider explicitly requires account/project metadata for this route.
    # Use only the account claim from this same provider-issued scoped token.
    # Never guess another account, change scope, or persist the claim/token.
    token_parts = client.get_token().split('.')
    if len(token_parts) != 3:
        raise RuntimeError('Provider-issued account context unavailable')
    claim = json.loads(base64.urlsafe_b64decode(token_parts[1] + '==='))
    account = claim.get('aid')
    if not account:
        raise RuntimeError('Provider-issued account context unavailable')
    headers['X-Ark-Meta-Account-Id'] = str(account)
    headers['X-Ark-Meta-Project-Name'] = client.config['VOLC_PROJECT_NAME']
    buckets = read_json(ROOT / 'exports/private-storage-check.json')['existing_buckets']
    result = {'checked_at': now(), 'character_image_uploaded': False,
              'bucket_or_permission_changed': False, 'probes': []}
    path = ROOT / ('exports/files-storage-probe-' + uuid.uuid4().hex[:8] + '.json')
    for bucket in buckets[:1]:
        if bucket['location'] != 'ap-southeast-1':
            continue
        boundary = 'codex-' + uuid.uuid4().hex
        prefix = 'codex-movie/dog-20261013/temporary-probe/' + uuid.uuid4().hex + '/'
        fields = {'purpose': 'user_data', 'tos[bucket]': bucket['name'], 'tos[prefix]': prefix}
        body = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name="{key}"\r\n\r\n{value}\r\n').encode()
                        for key, value in fields.items())
        body += (f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="transport-probe.pdf"\r\nContent-Type: application/pdf\r\n\r\n').encode()
        body += harmless + f'\r\n--{boundary}--\r\n'.encode()
        record = {'bucket': bucket['name'], 'temporary': True}
        result['probes'].append(record)
        try:
            uploaded = upload_response(Request(base, data=body, method='POST', headers={**headers,
                'Content-Type': 'multipart/form-data; boundary=' + boundary}), client.config,
                [bucket['name'], prefix, str(account)])
        except ApiFailure as error:
            record.update({'http_status': error.status, 'code': error.code,
                           'reason': getattr(error, 'safe_message', '')})
            atomic_json(path, result)
            print(record, flush=True)
            continue
        fid = uploaded.get('id')
        record.update({'file_id': fid, 'status': uploaded.get('status'),
                       'stored_in_requested_bucket': uploaded.get('tos', {}).get('bucket') == bucket['name']})
        atomic_json(path, result)
        try:
            key = uploaded.get('tos', {}).get('object_key')
            if key:
                unsigned = 'https://' + bucket['name'] + '.tos-ap-southeast-1.bytepluses.com/' + quote(key, safe='/')
                try:
                    with urlopen(unsigned, timeout=20) as accessed:
                        record['anonymous_get_status'] = accessed.status
                except HTTPError as error:
                    record['anonymous_get_status'] = error.code
        finally:
            if fid:
                deleted = response(Request(base + '/' + fid, headers=headers, method='DELETE'))
                record['deleted'] = bool(deleted.get('deleted'))
                atomic_json(path, result)
        print(record, flush=True)
        if record.get('stored_in_requested_bucket') and record.get('anonymous_get_status') == 403 and record.get('deleted'):
            result['available_private_transport_bucket'] = bucket['name']
            atomic_json(path, result)
            return
    atomic_json(path, result)


if __name__ == '__main__':
    main()
