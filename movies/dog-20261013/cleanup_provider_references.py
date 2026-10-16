"""Remove only this movie's documented temporary uploads after verified delivery."""
from urllib.request import Request
from seedance_transport import Client, ROOT, read_json, atomic_json, now, response, ApiFailure


def main():
    project = read_json(ROOT / 'project.json')
    verified = read_json(ROOT / 'exports/verification.json')
    if (project.get('render_status') != 'completed' or not verified.get('decode_verified')
            or verified.get('native_takes_verified') != 55 or verified.get('frame_count') != 24480):
        raise RuntimeError('Verified full delivery is required before cleanup')
    journal = read_json(ROOT / 'exports/task-journal.json')
    if len(journal['takes']) != 55 or any(t['status'] != 'succeeded' for t in journal['takes'].values()):
        raise RuntimeError('All accepted movie tasks must be complete and downloaded')
    record_path = ROOT / 'exports/provider-reference-cleanup.json'
    record = read_json(record_path) if record_path.exists() else {'started_at': now()}
    upload = read_json(ROOT / 'exports/chan-public-ingestion.json')
    group = read_json(ROOT / 'exports/private-character-group.json')
    if not group.get('temporary') or upload['group_id'] != group['id']:
        raise RuntimeError('Temporary ownership record mismatch')
    client = Client()
    project_arg = {'ProjectName': client.config['VOLC_PROJECT_NAME']}
    query = {**project_arg, 'Filter': {'GroupType': 'AIGC', 'GroupIds': [group['id']]}, 'MaxResults': 100}
    if not record.get('virtual_asset_deleted'):
        items = client.management('ListAssets', query).get('Result', {})
        if items.get('NextToken') or any(x['Id'] != upload['provider_asset_id'] for x in items.get('Items', [])):
            raise RuntimeError('Group contains an unrelated asset; cleanup stopped')
        client.management('DeleteAsset', {**project_arg, 'Id': upload['provider_asset_id']})
        record.update(virtual_asset_deleted=True, virtual_asset_deleted_at=now())
        atomic_json(record_path, record)
        bindings_path = ROOT / 'exports/provider-asset-bindings.json'
        bindings = read_json(bindings_path)
        bindings['asset_009'].update(status='Deleted', deleted_at=now())
        atomic_json(bindings_path, bindings)
    if not record.get('virtual_group_deleted'):
        items = client.management('ListAssets', query).get('Result', {})
        if items.get('Items') or items.get('NextToken'):
            raise RuntimeError('Virtual group is not empty')
        try:
            client.management('DeleteAssetGroup', {**project_arg, 'Id': group['id']})
            record.update(virtual_group_deleted=True, virtual_group_deleted_at=now())
        except ApiFailure as error:
            record['group_cleanup_error'] = {'http_status': error.status, 'code': error.code}
        atomic_json(record_path, record)
    if not record.get('files_upload_deleted'):
        client.resolve()
        file_record = read_json(ROOT / 'exports/reference-upload-check.json')
        if file_record['source_sha256'] != upload['source_sha256']:
            raise RuntimeError('Temporary Files upload provenance mismatch')
        fid = file_record['provider_file_id']
        headers = {'Authorization': 'Bearer ' + client.get_token(),
                   'X-Project-Name': client.config['VOLC_PROJECT_NAME']}
        data = response(Request('https://ark.ap-southeast.bytepluses.com/api/v3/files/' + fid,
                                headers=headers, method='DELETE'))
        record.update(files_upload_deleted=bool(data.get('deleted')), files_cleanup_checked_at=now())
        atomic_json(record_path, record)
    record.update(completed_at=now(), original_local_images_unchanged=True,
                  public_host_expiry_requested=upload['expiry_requested'],
                  public_host_expected_expiry_at=upload['expected_expiry_at'])
    atomic_json(record_path, record)
    print({key: record.get(key) for key in ('virtual_asset_deleted', 'virtual_group_deleted', 'files_upload_deleted')})


if __name__ == '__main__':
    main()
