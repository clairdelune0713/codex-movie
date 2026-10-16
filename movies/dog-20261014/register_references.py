"""User-authorized one-hour public transport of unchanged approved images.

Registers normal AIGC assets with default moderation. Public staging is hosted
by Litterbox and expires after one hour; no account/legal UI is automated.
Journal before each non-idempotent action and reconcile uncertain CreateAsset.
Never log credentials or expiring public URLs.
"""
import argparse
import hashlib
import time
import uuid
from datetime import datetime, timedelta, timezone
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from seedance_transport import Client, ROOT, read_json, atomic_json, now, ApiFailure

STATE = ROOT / 'exports/reference-registration.json'
AUTHORIZATION = 'if kyc is needed, just use api to upload (use temp public link)'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--assets', required=True)
    parser.add_argument('--wait-seconds', type=int, default=50)
    args = parser.parse_args()
    project = read_json(ROOT / 'project.json')
    group_id = read_json(ROOT / 'exports/private-registration.json')['group_id']
    client = Client()
    group = client.management('GetAssetGroup', {'Id': group_id,
        'ProjectName': client.config['VOLC_PROJECT_NAME']}).get('Result', {})
    if group.get('GroupType') != 'AIGC' or group.get('ProjectName') != client.config['VOLC_PROJECT_NAME']:
        raise RuntimeError('Task group mismatch')
    journal = read_json(STATE) if STATE.exists() else {
        'created_at': now(), 'group_id': group_id, 'user_authorization': AUTHORIZATION,
        'moderation_changed': False, 'legal_terms_accepted_by_agent': False, 'assets': {}}
    assert journal['group_id'] == group_id
    chosen = []
    for aid in args.assets.split(','):
        asset = next(a for a in project['asset_list'] if a['id'] == aid)
        candidate = next(c for c in asset['candidates'] if c['id'] == asset['selected_candidate_id'])
        raw = (ROOT / candidate['path']).read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        entry = journal['assets'].setdefault(aid, {
            'state': 'prepared', 'tag': asset['tag'], 'source_sha256': sha,
            'candidate_id': candidate['id'], 'source_path': candidate['path'],
            'asset_name': 'dog-20261014-' + aid.removeprefix('asset_') + '-' + sha[:12]})
        if entry['source_sha256'] != sha:
            raise RuntimeError('Approved source changed; reconcile before registration')
        atomic_json(STATE, journal)
        if entry['state'] == 'prepared':
            boundary = 'codex-' + uuid.uuid4().hex
            body = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n').encode()
                            for k, v in {'reqtype': 'fileupload', 'time': '1h'}.items())
            body += (f'--{boundary}\r\nContent-Disposition: form-data; name="fileToUpload"; filename="reference.png"\r\nContent-Type: image/png\r\n\r\n').encode()
            body += raw + f'\r\n--{boundary}--\r\n'.encode()
            entry.update(state='uploading', upload_started_at=now(), expiry_requested='1h', host='Litterbox')
            atomic_json(STATE, journal)
            with urlopen(Request('https://litterbox.catbox.moe/resources/internals/api.php', data=body,
                headers={'Content-Type': 'multipart/form-data; boundary=' + boundary}, method='POST'), timeout=120) as response:
                uri = response.read(4096).decode().strip()
            parsed = urlparse(uri)
            if parsed.scheme != 'https' or parsed.hostname != 'litter.catbox.moe' or not parsed.path.endswith('.png'):
                raise RuntimeError('Unexpected staging response; reconcile before another upload')
            entry.update(state='uploaded', source_uri=uri, uploaded_at=now(),
                expected_expiry_at=(datetime.now(timezone.utc) + timedelta(hours=1)).isoformat())
            atomic_json(STATE, journal)
            print({'asset': aid, 'temporary_upload': 'succeeded', 'expiry': '1h'}, flush=True)
        if entry['state'] == 'uploaded':
            with urlopen(entry['source_uri'], timeout=60) as response:
                fetched = response.read(len(raw) + 1)
            if hashlib.sha256(fetched).hexdigest() != sha:
                raise RuntimeError('Hosted bytes differ from approved reference')
            entry.update(state='verified_upload', source_upload_verified_at=now())
            atomic_json(STATE, journal)
        if entry['state'] == 'submitting':
            found = client.management('ListAssets', {'ProjectName': client.config['VOLC_PROJECT_NAME'],
                'Filter': {'GroupType': 'AIGC', 'GroupIds': [group_id], 'Name': entry['asset_name']},
                'MaxResults': 100}).get('Result', {})
            matches = [x for x in found.get('Items', []) if x.get('Name') == entry['asset_name']]
            if len(matches) != 1 or found.get('NextToken'):
                raise RuntimeError('Uncertain asset registration; no duplicate sent')
            entry.update(state='accepted', provider_asset_id=matches[0]['Id'])
            atomic_json(STATE, journal)
        if entry['state'] == 'verified_upload':
            entry.update(state='submitting', submitted_at=now())
            atomic_json(STATE, journal)
            try:
                result = client.management('CreateAsset', {'GroupId': group_id, 'URL': entry['source_uri'],
                    'AssetType': 'Image', 'Name': entry['asset_name'],
                    'ProjectName': client.config['VOLC_PROJECT_NAME']}).get('Result', {})
            except ApiFailure as error:
                entry.update(state='rejected', http_status=error.status, code=error.code)
                atomic_json(STATE, journal)
                raise
            if not result.get('Id'):
                raise RuntimeError('No asset ID returned; reconcile registration')
            entry.update(state='accepted', provider_asset_id=result['Id'])
            atomic_json(STATE, journal)
        if entry['state'] not in ('accepted', 'active'):
            raise RuntimeError('Registration needs reconciliation: ' + aid)
        chosen.append((aid, entry))
    deadline = time.monotonic() + max(0, args.wait_seconds)
    while True:
        pending = 0
        for aid, entry in chosen:
            result = client.management('GetAsset', {'Id': entry['provider_asset_id'],
                'ProjectName': client.config['VOLC_PROJECT_NAME']}).get('Result', {})
            status = result.get('Status')
            if status != entry.get('provider_status'):
                print({'asset': aid, 'registration_status': status}, flush=True)
            entry.update(provider_status=status, checked_at=now())
            atomic_json(STATE, journal)
            if status == 'Failed':
                raise RuntimeError('Default asset preprocessing failed: ' + aid)
            if status == 'Active':
                if result.get('GroupId') != group_id or result.get('AssetType') != 'Image':
                    raise RuntimeError('Registered asset metadata mismatch')
                if result.get('Moderation', {}).get('Strategy', 'Default') != 'Default':
                    raise RuntimeError('Expected default moderation')
                path = ROOT / 'exports/provider-asset-bindings.json'
                bindings = read_json(path) if path.exists() else {}
                bindings[aid] = {'provider_asset_id': entry['provider_asset_id'], 'status': 'Active',
                    'verified_at': now(), 'source_sha256': entry['source_sha256'],
                    'source_upload_verified_at': entry['source_upload_verified_at'],
                    'registration_journal': STATE.relative_to(ROOT).as_posix()}
                atomic_json(path, bindings)
                entry.update(state='active', active_at=entry.get('active_at', now()))
                atomic_json(STATE, journal)
            else:
                pending += 1
        if not pending or time.monotonic() >= deadline:
            print({'references_active': len(chosen) - pending, 'pending': pending,
                   'approved_images_unchanged': True, 'staging_expiry': '1h'}, flush=True)
            return
        time.sleep(15)


if __name__ == '__main__':
    try:
        main()
    except ApiFailure as error:
        print({'http_status': error.status, 'code': error.code}, flush=True)
        raise SystemExit(1)
    except Exception as error:
        print({'error_type': type(error).__name__, 'registration_stopped': True}, flush=True)
        raise SystemExit(1)
