"""Read-only checks of the movie's private group and original file upload."""
from urllib.request import Request
from seedance_transport import Client, ROOT, read_json, atomic_json, now, response, ApiFailure


def main():
    client = Client()
    group = read_json(ROOT / 'exports/private-character-group.json')
    result = {'checked_at': now(), 'read_only': True}
    body = {'Id': group['id'], 'ProjectName': client.config['VOLC_PROJECT_NAME']}
    data = client.management('GetAssetGroup', body).get('Result', {})
    result['group'] = {key: data.get(key) for key in ('Id', 'Name', 'GroupType')}
    query = {
        'ProjectName': client.config['VOLC_PROJECT_NAME'],
        'Filter': {'GroupIds': [group['id']], 'GroupType': 'AIGC'},
        'PageNumber': 1, 'PageSize': 100,
    }
    data = client.management('ListAssets', query).get('Result', {})
    result['movie_group_assets'] = [
        {key: item.get(key) for key in ('Id', 'Name', 'Status', 'AssetType')}
        for item in data.get('Items', [])
    ]
    query['Filter'] = {'Name': '陳伯', 'GroupType': 'AIGC'}
    data = client.management('ListAssets', query).get('Result', {})
    result['matching_chan_assets'] = [
        {key: item.get(key) for key in ('Id', 'Name', 'Status', 'AssetType')}
        for item in data.get('Items', [])
    ]
    client.resolve()
    upload = read_json(ROOT / 'exports/reference-upload-check.json')
    headers = {
        'Authorization': 'Bearer ' + client.get_token(),
        'X-Project-Name': client.config['VOLC_PROJECT_NAME'],
    }
    try:
        data = response(Request(
            'https://ark.ap-southeast.bytepluses.com/api/v3/files/' + upload['provider_file_id'],
            headers=headers,
        ))
        result['files_upload'] = {
            'status': data.get('status'),
            'response_fields': list(data),
            'has_download_url': any('url' in key.lower() and data[key] for key in data),
        }
    except ApiFailure as error:
        result['files_upload'] = {'http_status': error.status, 'code': error.code}
    atomic_json(ROOT / 'exports/private-library-status.json', result)
    print(result)


if __name__ == '__main__':
    main()
