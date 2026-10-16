"""Read-only paginated private-library search; no names, signed URLs or keys logged."""
import hashlib
import io
import math
import re
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import urlopen
from urllib.parse import urlparse
from PIL import Image, ImageChops, ImageStat
from seedance_transport import Client, ROOT, read_json, atomic_json, now, ApiFailure


def paginate(client, action, kind):
    items, token, pages = [], None, 0
    while True:
        body = {'ProjectName': client.config['VOLC_PROJECT_NAME'],
                'Filter': {'GroupType': kind}, 'MaxResults': 100,
                'SortBy': 'CreateTime', 'SortOrder': 'Desc'}
        if token:
            body['NextToken'] = token
        result = client.management(action, body).get('Result', {})
        items.extend(result.get('Items', []))
        pages += 1
        token = result.get('NextToken')
        if not token:
            return items, pages


def main():
    client = Client()
    project = read_json(ROOT / 'project.json')
    asset = next(a for a in project['asset_list'] if a['id'] == 'asset_009')
    candidate = next(c for c in asset['candidates'] if c['id'] == asset['selected_candidate_id'])
    raw = (ROOT / candidate['path']).read_bytes()
    source_hash = hashlib.sha256(raw).hexdigest()
    source = Image.open(io.BytesIO(raw)).convert('RGB')
    target = source.resize((192, 108), Image.Resampling.LANCZOS)
    report = {'checked_at': now(), 'read_only': True,
              'source_sha256': source_hash, 'libraries': {}, 'assets': []}
    work = []
    metadata_only = '--metadata-only' in sys.argv
    for kind in ('AIGC',):
        try:
            groups, group_pages = paginate(client, 'ListAssetGroups', kind)
            items, asset_pages = paginate(client, 'ListAssets', kind)
            report['libraries'][kind] = {
                'group_count': len(groups), 'asset_count': len(items),
                'group_pages': group_pages, 'asset_pages': asset_pages,
                'pagination_complete': True,
                'statuses': dict(Counter(a.get('Status') for a in items)),
                'types': dict(Counter(a.get('AssetType') for a in items)),
            }
            for item in items:
                record = {key: item.get(key) for key in ('Id', 'Status', 'AssetType')}
                record['library'] = kind
                # Only asset metadata is inspected broadly. Restrict image retrieval
                # to the exact supplied filename/character name, never generic faces.
                name = str(item.get('Name', ''))
                url_path = urlparse(str(item.get('URL', ''))).path
                from urllib.parse import unquote
                hint = unquote(name + ' ' + url_path).lower()
                specific = any(s in hint for s in ('陳伯', '陈伯', 'chenbo',
                    'chen_bo', 'chen-bo', 'dog-20261013-chan', source_hash))
                record['chan_specific_metadata_match'] = specific
                if specific:
                    record['matching_name'] = name
                report['assets'].append(record)
                if specific and item.get('Status') == 'Active' and item.get('AssetType') == 'Image':
                    work.append((item, record))
            print({'library': kind, **report['libraries'][kind]}, flush=True)
        except ApiFailure as error:
            report['libraries'][kind] = {'http_status': error.status, 'code': error.code,
                                          'pagination_complete': False}
            print({'library': kind, **report['libraries'][kind]}, flush=True)
    atomic_json(ROOT / 'exports/private-library-discovery.json', report)

    if metadata_only:
        print({'metadata_scan_complete': True,
               'specific_chan_candidates': [r for r in report['assets']
                   if r.get('chan_specific_metadata_match')],
               'images_downloaded': 0}, flush=True)
        return

    def compare(pair):
        item, record = pair
        url = item.get('URL')
        if not url:
            item = client.management('GetAsset', {'Id': item['Id'],
                'ProjectName': client.config['VOLC_PROJECT_NAME']}).get('Result', {})
            url = item.get('URL')
        if not url or urlparse(url).scheme != 'https':
            return record, {'comparison': 'no_https_image_url'}
        try:
            with urlopen(url, timeout=25) as response:
                content = response.read(30 * 1024 * 1024 + 1)
            if len(content) > 30 * 1024 * 1024:
                return record, {'comparison': 'size_limit'}
            digest = hashlib.sha256(content).hexdigest()
            image = Image.open(io.BytesIO(content)).convert('RGB')
            similar_ratio = abs(image.width / image.height - source.width / source.height) < 0.02
            diff = ImageChops.difference(image.resize((192, 108), Image.Resampling.LANCZOS), target)
            error = sum(ImageStat.Stat(diff).mean) / 3
            data = {'comparison': 'completed', 'size': list(image.size),
                    'exact_source_sha256_match': digest == source_hash,
                    'same_aspect_ratio': similar_ratio, 'mean_pixel_difference': round(error, 3)}
            if digest == source_hash or (similar_ratio and error < 15):
                folder = ROOT / 'exports/private-library-candidates'
                folder.mkdir(parents=True, exist_ok=True)
                filename = item['Id'] + '-' + digest[:12] + '.png'
                path = folder / filename
                if not path.exists():
                    image.save(path)
                data['inspection_path'] = str(path)
                data['remote_sha256'] = digest
            return record, data
        except Exception as error:
            # URL-bearing exception messages are deliberately suppressed.
            return record, {'comparison': 'failed', 'error_type': type(error).__name__}

    done = 0
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(compare, pair) for pair in work]
        for future in as_completed(futures):
            record, data = future.result()
            record.update(data)
            done += 1
            if done % 20 == 0:
                atomic_json(ROOT / 'exports/private-library-discovery.json', report)
                print({'images_compared': done, 'active_images': len(work)}, flush=True)
    report['completed_at'] = now()
    atomic_json(ROOT / 'exports/private-library-discovery.json', report)
    exact = [a for a in report['assets'] if a.get('exact_source_sha256_match')]
    possible = [a for a in report['assets'] if a.get('inspection_path')]
    print({'images_compared': done, 'exact_matches': exact,
           'possible_match_count': len(possible),
           'closest_images': sorted([a for a in report['assets'] if 'mean_pixel_difference' in a],
                                   key=lambda a: a['mean_pixel_difference'])[:5]}, flush=True)


if __name__ == '__main__':
    main()
