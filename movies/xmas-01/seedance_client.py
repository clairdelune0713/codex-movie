from pathlib import Path
from datetime import datetime, timezone
import hashlib
import hmac
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parent.parent
MANAGEMENT_HOST = 'ark.ap-southeast-1.byteplusapi.com'
TASK_BASE = 'https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks'
KEYS = ('VOLC_ACCESS_KEY', 'VOLC_SECRET_KEY_RAW', 'VOLC_PROJECT_NAME', 'VOLC_ENDPOINT_SEEDANCE_25')

def now():
    return datetime.now(timezone.utc).isoformat()

def atomic_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.partial')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)

def load_settings():
    path = WORKSPACE / '.env'
    settings = {}
    escapes = {'n':'\n','r':'\r','t':'\t','b':'\b','f':'\f','v':'\v','a':'\a','\\':'\\','"':'"',"'":"'"}
    for line in path.read_text(encoding='utf-8-sig').splitlines():
        m = re.match(r'^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$', line)
        if not m or m.group(1) not in KEYS:
            continue
        key, raw = m.groups()
        raw = raw.strip()
        if raw[:1] in ('"', "'"):
            quote = raw[0]
            matched = re.match(r'^' + re.escape(quote) + r'((?:\\.|[^' + re.escape(quote) + r'])*)' + re.escape(quote) + r'\s*(?:#.*)?$', raw)
            if not matched:
                raise RuntimeError('Malformed quoted environment setting: ' + key)
            value = matched.group(1)
            if quote == '"':
                value = re.sub(r'\\([\\\x22\x27abfnrtv])', lambda x: escapes[x.group(1)], value)
            else:
                value = value.replace("\\'", "'").replace('\\\\', '\\')
        else:
            value = re.sub(r'\s+#.*$', '', raw).rstrip()
        settings[key] = value
    missing = [k for k in KEYS if k != 'VOLC_PROJECT_NAME' and not settings.get(k)]
    if missing:
        raise RuntimeError('Missing settings in workspace .env: ' + ', '.join(missing))
    return settings

class ProviderError(RuntimeError):
    def __init__(self, status, code):
        self.status = status
        self.code = code
        super().__init__('Provider HTTP ' + str(status) + ': ' + str(code))

def json_request(url, body=None, headers=None, method=None, timeout=60):
    data = None if body is None else json.dumps(body, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    request = urllib.request.Request(url, data=data, headers=headers or {}, method=method or ('GET' if data is None else 'POST'))
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as error:
        raw = error.read()
        try:
            content = json.loads(raw)
            info = content.get('ResponseMetadata', {}).get('Error') or content.get('error') or {}
            code = info.get('Code') or info.get('code') or 'unknown'
        except (ValueError, AttributeError):
            code = 'unparsed_response'
        raise ProviderError(error.code, code) from None

def management(settings, action, body):
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    day = stamp[:8]
    query = urllib.parse.urlencode(sorted({'Action': action, 'Version': '2024-01-01'}.items()), quote_via=urllib.parse.quote)
    body_bytes = json.dumps(body, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    digest = hashlib.sha256(body_bytes).hexdigest()
    canonical_headers = 'content-type:application/json\nhost:' + MANAGEMENT_HOST + '\nx-content-sha256:' + digest + '\nx-date:' + stamp + '\n'
    signed = 'content-type;host;x-content-sha256;x-date'
    canonical = '\n'.join(['POST', '/', query, canonical_headers, signed, digest])
    scope = day + '/ap-southeast-1/ark/request'
    string_to_sign = '\n'.join(['HMAC-SHA256', stamp, scope, hashlib.sha256(canonical.encode()).hexdigest()])
    secret = settings['VOLC_SECRET_KEY_RAW'].encode()
    for part in (day, 'ap-southeast-1', 'ark', 'request'):
        secret = hmac.new(secret, part.encode(), hashlib.sha256).digest()
    signature = hmac.new(secret, string_to_sign.encode(), hashlib.sha256).hexdigest()
    headers = {'Content-Type': 'application/json', 'Host': MANAGEMENT_HOST, 'X-Content-Sha256': digest, 'X-Date': stamp,
               'Authorization': 'HMAC-SHA256 Credential=' + settings['VOLC_ACCESS_KEY'] + '/' + scope + ', SignedHeaders=' + signed + ', Signature=' + signature}
    response = json_request('https://' + MANAGEMENT_HOST + '/?' + query, body, headers)
    error = response.get('ResponseMetadata', {}).get('Error')
    if error:
        raise ProviderError(200, error.get('Code', 'management_error'))
    return response

def resolve():
    settings = load_settings()
    requested = settings['VOLC_ENDPOINT_SEEDANCE_25']
    body = {'PageNumber': 1, 'PageSize': 100, 'Filter': {'Ids': [requested]}}
    if settings.get('VOLC_PROJECT_NAME'):
        body['ProjectName'] = settings['VOLC_PROJECT_NAME']
    response = management(settings, 'ListEndpoints', body)
    result = response.get('Result', {})
    exact = [x for x in result.get('Items', []) if x.get('Id') == requested]
    if len(exact) != 1:
        atomic_json(ROOT / 'exports' / 'endpoint-check.json', {'checked_at': now(), 'configured_endpoint_found': False, 'returned_count': result.get('TotalCount'), 'project_setting_empty': not bool(settings.get('VOLC_PROJECT_NAME'))})
        raise RuntimeError('Configured endpoint not found in authorized account; no generation submitted')
    endpoint = exact[0]
    model = endpoint.get('ModelReference', {})
    if not re.search(r'seedance[^a-z0-9]*2[^a-z0-9]*5', json.dumps(model), re.I):
        raise RuntimeError('Configured endpoint does not verify as Seedance 2.5')
    if str(endpoint.get('Status', '')).lower() != 'running':
        raise RuntimeError('Configured endpoint is not running')
    provider_project = endpoint.get('ProjectName') or ''
    if not provider_project:
        raise RuntimeError('Provider did not return a project name')
    if settings.get('VOLC_PROJECT_NAME') and settings['VOLC_PROJECT_NAME'] != provider_project:
        raise RuntimeError('Configured project and endpoint project differ')
    record = {'checked_at': now(), 'environment_source': str(WORKSPACE / '.env'), 'endpoint': requested,
              'project_name': provider_project, 'model_reference': model, 'status': endpoint['Status'],
              'project_name_source': 'workspace .env' if settings.get('VOLC_PROJECT_NAME') else 'ProjectName returned by read-only ListEndpoints for the exact configured endpoint',
              'configured_endpoint_unchanged': True, 'credentials_source_unchanged': True,
              'documentation': 'https://docs.byteplus.com/pt/docs/ModelArk/1262430'}
    atomic_json(ROOT / 'exports' / 'endpoint-resolution.json', record)
    print(json.dumps({'verified_seedance_2_5': True, 'running': True, 'configured_endpoint_unchanged': True, 'project_name_resolved_from_endpoint': not bool(settings.get('VOLC_PROJECT_NAME')), 'model_reference': model}, ensure_ascii=False))

def authenticated_headers(settings, route):
    if settings['VOLC_ENDPOINT_SEEDANCE_25'] != route['endpoint']:
        raise RuntimeError('Endpoint configuration changed; resolve again')
    if settings.get('VOLC_PROJECT_NAME') and settings['VOLC_PROJECT_NAME'] != route['project_name']:
        raise RuntimeError('Project configuration changed; resolve again')
    response = management(settings, 'GetApiKey', {'DurationSeconds': 3600, 'ResourceType': 'endpoint', 'ResourceIds': [route['endpoint']]})
    token = response.get('Result', {}).get('ApiKey') or response.get('ApiKey')
    if not token:
        raise RuntimeError('Temporary token absent from provider response')
    return {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json', 'X-Project-Name': route['project_name']}

if __name__ == '__main__':
    try:
        if sys.argv[1:] == ['resolve']:
            resolve()
        else:
            raise RuntimeError('Only read-only resolve command is currently enabled')
    except (RuntimeError, urllib.error.URLError, OSError) as error:
        print(json.dumps({'error_type': type(error).__name__, 'error': str(error)[:220]}))
        sys.exit(1)
