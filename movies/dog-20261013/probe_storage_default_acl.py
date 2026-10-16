"""Check upload permission without requesting an ACL, using only empty probes."""
import sys
import uuid
import re
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import quote
from seedance_transport import ROOT, settings, read_json, atomic_json, now
sys.path.insert(0, str(ROOT / 'tools/storage-deps'))
import tos


def main():
    config = settings()
    client = tos.TosClientV2(config['VOLC_ACCESS_KEY'], config['VOLC_SECRET_KEY_RAW'],
                            'https://tos-ap-southeast-1.bytepluses.com', 'ap-southeast-1')
    records = []
    path = ROOT / ('exports/storage-default-acl-probe-' + uuid.uuid4().hex[:8] + '.json')
    for bucket in read_json(ROOT / 'exports/private-storage-check.json')['existing_buckets']:
        if bucket['location'] != 'ap-southeast-1':
            continue
        key = 'codex-movie/dog-20261013/temporary-empty/' + uuid.uuid4().hex
        record = {'bucket': bucket['name'], 'bytes_uploaded': 0, 'acl_requested': False}
        records.append(record)
        try:
            uploaded = client.put_object(bucket['name'], key, content=b'', content_length=0,
                                          forbid_overwrite=True)
        except tos.exceptions.TosServerError as error:
            message = str(error.message)
            for value in list(config.values()) + [bucket['name'], key]:
                message = message.replace(value, '[redacted]')
            message = re.sub(r'https?://\S+', '[URL]', message)
            record.update({'http_status': error.status_code, 'code': error.code,
                           'reason': message[:300]})
            atomic_json(path, {'checked_at': now(), 'probes': records})
            print(record, flush=True)
            continue
        record['object_key'] = key
        atomic_json(path, {'checked_at': now(), 'probes': records})
        try:
            unsigned = 'https://' + bucket['name'] + '.tos-ap-southeast-1.bytepluses.com/' + quote(key, safe='/')
            try:
                with urlopen(unsigned, timeout=20) as result:
                    record['anonymous_get_status'] = result.status
            except HTTPError as error:
                record['anonymous_get_status'] = error.code
            record['put_succeeded'] = True
        finally:
            client.delete_object(bucket['name'], key)
            record['probe_deleted'] = True
            atomic_json(path, {'checked_at': now(), 'probes': records})
        print(record, flush=True)


if __name__ == '__main__':
    main()
