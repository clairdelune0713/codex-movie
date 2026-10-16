"""Resumable unchanged Chan ingestion into the existing private AIGC group.

Requires scoped TOS PutObject/GetObject/DeleteObject access, plus permission to
set the new temporary object's private ACL. Never creates buckets or changes
bucket policies. No signed URL, token, or credential is logged or persisted.
"""
import argparse
import hashlib
import sys
import time
import uuid
from urllib.request import urlopen
from urllib.error import HTTPError
from seedance_transport import Client, ROOT, read_json, atomic_json, now
sys.path.insert(0, str(ROOT / 'tools/storage-deps'))
import tos
from tos.enum import ACLType, HttpMethodType
import logging
logging.getLogger('tos').setLevel(logging.CRITICAL)

JOURNAL = ROOT / 'exports/chan-private-ingestion.json'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket', required=True)
    parser.add_argument('--wait-seconds', type=int, default=1200)
    args = parser.parse_args()
    existing = read_json(ROOT / 'exports/private-storage-check.json')['existing_buckets']
    if not any(b['name'] == args.bucket and b['location'] == 'ap-southeast-1' for b in existing):
        raise RuntimeError('Use a previously verified existing regional bucket')
    client = Client()
    p = read_json(ROOT / 'project.json')
    a = next(a for a in p['asset_list'] if a['id'] == 'asset_009')
    c = next(c for c in a['candidates'] if c['id'] == a['selected_candidate_id'])
    raw = (ROOT / c['path']).read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    if sha != read_json(ROOT / 'exports/reference-upload-check.json')['source_sha256']:
        raise RuntimeError('Original approved Chan bytes have changed')
    group_id = read_json(ROOT / 'exports/private-character-group.json')['id']
    group = client.management('GetAssetGroup', {'Id': group_id,
        'ProjectName': client.config['VOLC_PROJECT_NAME']}).get('Result', {})
    if group.get('GroupType') != 'AIGC' or group.get('ProjectName') != client.config['VOLC_PROJECT_NAME']:
        raise RuntimeError('Private group type/project mismatch')
    storage = tos.TosClientV2(client.config['VOLC_ACCESS_KEY'], client.config['VOLC_SECRET_KEY_RAW'],
                             'https://tos-ap-southeast-1.bytepluses.com', 'ap-southeast-1')
    if JOURNAL.exists():
        journal = read_json(JOURNAL)
        if journal['source_sha256'] != sha or journal['bucket'] != args.bucket or journal['group_id'] != group_id:
            raise RuntimeError('Existing upload journal differs; inspect before continuing')
    else:
        journal = {'created_at': now(), 'source_asset_id': a['id'], 'source_sha256': sha,
                   'group_id': group_id, 'bucket': args.bucket, 'temporary': True,
                   'moderation_changed': False,
                   'object_key': 'codex-movie/dog-20261013/temporary/' + uuid.uuid4().hex + '/chan.png',
                   'asset_name': 'dog-20261013-chan-' + sha[:16], 'state': 'prepared'}
        atomic_json(JOURNAL, journal)
    key = journal['object_key']
    if journal['state'] == 'prepared':
        # A harmless zero-byte probe verifies ACL and cleanup permissions first.
        probe_key = key + '.permission-probe-' + uuid.uuid4().hex
        journal['permission_probe_key'] = probe_key
        atomic_json(JOURNAL, journal)
        storage.put_object(args.bucket, probe_key, content=b'', content_length=0,
                           acl=ACLType.ACL_Private, forbid_overwrite=True)
        journal['permission_probe_created'] = True
        atomic_json(JOURNAL, journal)
        storage.delete_object(args.bucket, probe_key)
        journal['permission_probe_deleted'] = True
        atomic_json(JOURNAL, journal)
        journal['state'] = 'uploading'
        atomic_json(JOURNAL, journal)
        storage.put_object(args.bucket, key, content=raw, content_length=len(raw),
                           content_type='image/png', acl=ACLType.ACL_Private, forbid_overwrite=True)
        journal['state'] = 'uploaded'
        atomic_json(JOURNAL, journal)
    # An interrupted upload is reconciled with the exact object, never overwritten.
    if journal['state'] in ('uploading', 'uploaded'):
        signed = storage.pre_signed_url(HttpMethodType.Http_Method_Get, args.bucket, key, expires=3600).signed_url
        try:
            with urlopen(signed.split('?', 1)[0], timeout=30) as anonymous:
                anonymous_status = anonymous.status
        except HTTPError as error:
            anonymous_status = error.code
        if anonymous_status != 403:
            raise RuntimeError('Private object access verification failed; ingestion stopped')
        with urlopen(signed, timeout=60) as downloaded:
            fetched = downloaded.read(len(raw) + 1)
        if hashlib.sha256(fetched).hexdigest() != sha:
            raise RuntimeError('Uploaded object does not match original bytes')
        journal['source_upload_verified_at'] = now()
        journal['anonymous_get_status'] = anonymous_status
        journal['state'] = 'verified_upload'
        atomic_json(JOURNAL, journal)
    if journal['state'] == 'submitting':
        found = client.management('ListAssets', {'ProjectName': client.config['VOLC_PROJECT_NAME'],
            'Filter': {'GroupType': 'AIGC', 'GroupIds': [group_id], 'Name': journal['asset_name']},
            'MaxResults': 100}).get('Result', {}).get('Items', [])
        matches = [x for x in found if x.get('Name') == journal['asset_name']]
        if len(matches) != 1:
            raise RuntimeError('Uncertain CreateAsset submission needs reconciliation; no duplicate sent')
        journal['provider_asset_id'] = matches[0]['Id']
        journal['state'] = 'accepted'
        atomic_json(JOURNAL, journal)
    if journal['state'] == 'verified_upload':
        signed = storage.pre_signed_url(HttpMethodType.Http_Method_Get, args.bucket, key, expires=3600).signed_url
        journal['state'] = 'submitting'
        atomic_json(JOURNAL, journal)
        data = client.management('CreateAsset', {'GroupId': group_id, 'URL': signed,
            'AssetType': 'Image', 'Name': journal['asset_name'],
            'ProjectName': client.config['VOLC_PROJECT_NAME']}).get('Result', {})
        if not data.get('Id'):
            raise RuntimeError('No asset ID returned; reconcile before retrying')
        journal['provider_asset_id'] = data['Id']
        journal['state'] = 'accepted'
        atomic_json(JOURNAL, journal)
    deadline = time.monotonic() + max(0, args.wait_seconds)
    previous = None
    while True:
        data = client.management('GetAsset', {'Id': journal['provider_asset_id'],
            'ProjectName': client.config['VOLC_PROJECT_NAME']}).get('Result', {})
        status = data.get('Status')
        journal['provider_status'] = status
        journal['checked_at'] = now()
        atomic_json(JOURNAL, journal)
        if status != previous:
            print({'private_asset_status': status}, flush=True)
            previous = status
        if status == 'Active':
            if data.get('GroupId') != group_id or data.get('AssetType') != 'Image':
                raise RuntimeError('Active asset metadata mismatch')
            if data.get('Moderation', {}).get('Strategy', 'Default') != 'Default':
                raise RuntimeError('Expected default asset moderation')
            bindings_path = ROOT / 'exports/provider-asset-bindings.json'
            bindings = read_json(bindings_path) if bindings_path.exists() else {}
            bindings[a['id']] = {'provider_asset_id': journal['provider_asset_id'], 'status': 'Active',
                                'verified_at': now(), 'source_sha256': sha,
                                'source_upload_verified_at': journal['source_upload_verified_at']}
            atomic_json(bindings_path, bindings)
            journal['state'] = 'active'
            atomic_json(JOURNAL, journal)
            print({'binding_ready': True, 'source_unchanged': True}, flush=True)
            return
        if status == 'Failed':
            raise RuntimeError('Private asset preprocessing failed; no video submission')
        if time.monotonic() >= deadline:
            print({'ingestion_pending': True, 'resumable': True}, flush=True)
            return
        time.sleep(30)


if __name__ == '__main__':
    try:
        main()
    except tos.exceptions.TosServerError as error:
        print({'storage_status': error.status_code, 'code': error.code})
        raise SystemExit(1)
    except Exception as error:
        # Transport exception messages can contain signed URLs; never print them.
        print({'error_type': type(error).__name__, 'ingestion_stopped': True})
        raise SystemExit(1)
