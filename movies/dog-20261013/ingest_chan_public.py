"""User-authorized expiring public transport into the movie's AIGC asset group."""
import argparse
import hashlib
import time
import uuid
from datetime import datetime, timezone, timedelta
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from seedance_transport import Client, ROOT, read_json, atomic_json, now, ApiFailure

JOURNAL = ROOT / 'exports/chan-public-ingestion.json'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--wait-seconds', type=int, default=1200)
    args = parser.parse_args()
    p = read_json(ROOT / 'project.json')
    a = next(a for a in p['asset_list'] if a['id'] == 'asset_009')
    c = next(c for c in a['candidates'] if c['id'] == a['selected_candidate_id'])
    raw = (ROOT / c['path']).read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    if sha != read_json(ROOT / 'exports/reference-upload-check.json')['source_sha256']:
        raise RuntimeError('Original approved Chan bytes have changed')
    client = Client()
    group_id = read_json(ROOT / 'exports/private-character-group.json')['id']
    group = client.management('GetAssetGroup', {'Id': group_id,
        'ProjectName': client.config['VOLC_PROJECT_NAME']}).get('Result', {})
    if group.get('GroupType') != 'AIGC' or group.get('ProjectName') != client.config['VOLC_PROJECT_NAME']:
        raise RuntimeError('Private group type/project mismatch')
    if JOURNAL.exists():
        journal = read_json(JOURNAL)
        if journal['source_sha256'] != sha or journal['group_id'] != group_id:
            raise RuntimeError('Existing ingestion journal differs')
    else:
        journal = {'created_at': now(), 'source_asset_id': a['id'], 'source_sha256': sha,
            'group_id': group_id, 'asset_name': 'dog-20261013-chan-' + sha[:16],
            'state': 'prepared', 'temporary_public_host': 'Litterbox', 'expiry_requested': '1h',
            'moderation_changed': False,
            'user_authorization': "it's ok if they are not private, just find a way to upload and use them in seedance video gen"}
        atomic_json(JOURNAL, journal)
    if journal['state'] == 'prepared':
        boundary = 'codex-' + uuid.uuid4().hex
        body = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name="{key}"\r\n\r\n{value}\r\n').encode()
                       for key, value in {'reqtype': 'fileupload', 'time': '1h'}.items())
        body += (f'--{boundary}\r\nContent-Disposition: form-data; name="fileToUpload"; filename="chan.png"\r\nContent-Type: image/png\r\n\r\n').encode()
        body += raw + f'\r\n--{boundary}--\r\n'.encode()
        with urlopen(Request('https://litterbox.catbox.moe/resources/internals/api.php', data=body,
            headers={'Content-Type': 'multipart/form-data; boundary=' + boundary}, method='POST'), timeout=120) as uploaded:
            public_url = uploaded.read(4096).decode().strip()
        parsed = urlparse(public_url)
        if parsed.scheme != 'https' or parsed.hostname != 'litter.catbox.moe' or not parsed.path.endswith('.png'):
            raise RuntimeError('Temporary host did not return the expected image URL')
        journal.update(state='uploaded', source_uri=public_url, uploaded_at=now(),
            expected_expiry_at=(datetime.now(timezone.utc) + timedelta(hours=1)).isoformat())
        atomic_json(JOURNAL, journal)
        print({'public_upload': 'succeeded', 'expiry_requested': '1h'}, flush=True)
    if journal['state'] == 'uploaded':
        with urlopen(journal['source_uri'], timeout=60) as verified:
            fetched = verified.read(len(raw) + 1)
        if hashlib.sha256(fetched).hexdigest() != sha:
            raise RuntimeError('Hosted bytes differ from approved original')
        journal.update(state='verified_upload', source_upload_verified_at=now())
        atomic_json(JOURNAL, journal)
        print({'source_bytes_verified': True}, flush=True)
    if journal['state'] == 'submitting':
        items = client.management('ListAssets', {'ProjectName': client.config['VOLC_PROJECT_NAME'],
            'Filter': {'GroupType': 'AIGC', 'GroupIds': [group_id], 'Name': journal['asset_name']},
            'MaxResults': 100}).get('Result', {}).get('Items', [])
        matches = [x for x in items if x.get('Name') == journal['asset_name']]
        if len(matches) != 1:
            raise RuntimeError('Uncertain asset submission; no duplicate sent')
        journal.update(state='accepted', provider_asset_id=matches[0]['Id'])
        atomic_json(JOURNAL, journal)
    if journal['state'] == 'verified_upload':
        journal['state'] = 'submitting'
        atomic_json(JOURNAL, journal)
        try:
            data = client.management('CreateAsset', {'GroupId': group_id,
                'URL': journal['source_uri'], 'AssetType': 'Image', 'Name': journal['asset_name'],
                'ProjectName': client.config['VOLC_PROJECT_NAME']}).get('Result', {})
        except ApiFailure as error:
            journal.update(state='rejected', http_status=error.status, code=error.code)
            atomic_json(JOURNAL, journal)
            raise
        if not data.get('Id'):
            raise RuntimeError('No asset ID returned; reconcile before retrying')
        journal.update(state='accepted', provider_asset_id=data['Id'])
        atomic_json(JOURNAL, journal)
    if journal['state'] not in ('accepted', 'active'):
        raise RuntimeError('Ingestion requires reconciliation')
    deadline = time.monotonic() + max(0, args.wait_seconds)
    previous = None
    while True:
        data = client.management('GetAsset', {'Id': journal['provider_asset_id'],
            'ProjectName': client.config['VOLC_PROJECT_NAME']}).get('Result', {})
        status = data.get('Status')
        journal.update(provider_status=status, checked_at=now())
        atomic_json(JOURNAL, journal)
        if status != previous:
            print({'virtual_asset_status': status}, flush=True)
            previous = status
        if status == 'Active':
            if data.get('GroupId') != group_id or data.get('AssetType') != 'Image':
                raise RuntimeError('Active asset metadata mismatch')
            if data.get('Moderation', {}).get('Strategy', 'Default') != 'Default':
                raise RuntimeError('Expected default moderation')
            path = ROOT / 'exports/provider-asset-bindings.json'
            bindings = read_json(path) if path.exists() else {}
            bindings[a['id']] = {'provider_asset_id': journal['provider_asset_id'], 'status': 'Active',
                'verified_at': now(), 'source_sha256': sha,
                'source_upload_verified_at': journal['source_upload_verified_at']}
            atomic_json(path, bindings)
            journal['state'] = 'active'
            atomic_json(JOURNAL, journal)
            print({'binding_ready': True, 'source_unchanged': True}, flush=True)
            return
        if status == 'Failed':
            raise RuntimeError('Virtual asset preprocessing failed; no video submission')
        if time.monotonic() >= deadline:
            print({'ingestion_pending': True, 'resumable': True}, flush=True)
            return
        time.sleep(30)


if __name__ == '__main__':
    try:
        main()
    except ApiFailure as error:
        print({'http_status': error.status, 'code': error.code})
        raise SystemExit(1)
    except Exception as error:
        print({'error_type': type(error).__name__, 'ingestion_stopped': True})
        raise SystemExit(1)
