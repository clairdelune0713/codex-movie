"""Direct Seedance adapter. Credentials stay in memory; paid POSTs are journaled.

Uses only the four user-authorized settings in ../aifx-studio/.env.
Signing is adapted from that repository's src/lib/volcengine.ts.
"""
import argparse
import base64
import hashlib
import hmac
import importlib.util
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = ROOT.parents[2] / 'aifx-studio/.env'
HELPER = Path('C:/Users/admina/.codex/skills/movi2/scripts/project.py')
HOST = 'ark.ap-southeast-1.byteplusapi.com'
BASE = 'https://ark.ap-southeast.bytepluses.com/api/v3'
KEYS = ('VOLC_ACCESS_KEY', 'VOLC_SECRET_KEY_RAW', 'VOLC_PROJECT_NAME', 'VOLC_ENDPOINT_SEEDANCE_25')
JOURNAL = ROOT / 'exports/seedance-journal.json'
ENDPOINT_RESOLUTION = ROOT / 'exports/seedance-endpoint-resolution.json'


def load(file):
    return json.loads(file.read_text(encoding='utf-8-sig'))


def save(file, value):
    file.parent.mkdir(parents=True, exist_ok=True)
    temporary = file.with_suffix(file.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    temporary.replace(file)


def now():
    return datetime.now(timezone.utc).isoformat()


def read_credentials():
    # Only retain the four requested values, without interpolating other secrets.
    values = {}
    for line in ENV_FILE.read_text(encoding='utf-8-sig').splitlines():
        match = re.match(r'^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$', line)
        if not match or match[1] not in KEYS:
            continue
        value = match[2].strip()
        if value.startswith(('"', "'")):
            quote = value[0]
            end = value.rfind(quote)
            if end <= 0:
                raise ValueError('Unterminated quoted setting: ' + match[1])
            value = value[1:end]
        else:
            value = re.split(r'\s+#', value, maxsplit=1)[0].strip()
        values[match[1]] = value
    missing = [key for key in KEYS if not values.get(key)]
    if missing:
        raise ValueError('Missing named settings: ' + ', '.join(missing))
    if not values['VOLC_ENDPOINT_SEEDANCE_25'].startswith('ep-'):
        raise ValueError('Configured Seedance endpoint is not an ep- endpoint ID.')
    return values


def resolved_settings(values):
    settings = dict(values)
    if ENDPOINT_RESOLUTION.exists():
        resolution = load(ENDPOINT_RESOLUTION)
        if values['VOLC_ENDPOINT_SEEDANCE_25'] == resolution['configured_endpoint']:
            settings['VOLC_ENDPOINT_SEEDANCE_25'] = resolution['resolved_endpoint']
    return settings


class Client:
    def __init__(self, settings):
        self.settings = settings
        self.token = None
        self.token_time = 0

    def clean(self, value):
        text = str(value)
        for secret in (self.settings['VOLC_ACCESS_KEY'], self.settings['VOLC_SECRET_KEY_RAW'], self.token):
            if secret:
                text = text.replace(secret, '[redacted]')
        return text

    def request(self, url, method, body=None, headers=None):
        encoded = None if body is None else json.dumps(body, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
        request = urllib.request.Request(url, data=encoded, headers=headers or {}, method=method)
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                result = json.loads(response.read())
        except urllib.error.HTTPError as error:
            raw = error.read().decode('utf-8', errors='replace')
            try:
                data = json.loads(raw)
                obj = data.get('error') or data.get('Error') or data.get('ResponseMetadata', {}).get('Error') or {}
                code = obj.get('code', obj.get('Code', 'HTTPError'))
                message = obj.get('message', obj.get('Message', 'Request rejected'))
            except (ValueError, AttributeError):
                code, message = 'HTTPError', raw[:500]
            raise RuntimeError(self.clean(f'HTTP {error.code}: {code}: {message}')) from None
        obj = result.get('Error') or result.get('ResponseMetadata', {}).get('Error')
        if obj:
            raise RuntimeError(self.clean(str(obj)))
        return result

    def authenticate(self):
        if self.token and time.monotonic() - self.token_time < 3000:
            return
        body = {'DurationSeconds': 3600, 'ResourceType': 'endpoint', 'ResourceIds': [self.settings['VOLC_ENDPOINT_SEEDANCE_25']]}
        serialized = json.dumps(body, ensure_ascii=False, separators=(',', ':'))
        digest = hashlib.sha256(serialized.encode()).hexdigest()
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
        date = stamp[:8]
        query = urllib.parse.urlencode({'Action': 'GetApiKey', 'Version': '2024-01-01'}, quote_via=urllib.parse.quote)
        signed = 'content-type;host;x-content-sha256;x-date'
        canonical_headers = f'content-type:application/json\nhost:{HOST}\nx-content-sha256:{digest}\nx-date:{stamp}\n'
        canonical = '\n'.join(['POST', '/', query, canonical_headers, signed, digest])
        scope = f'{date}/ap-southeast-1/ark/request'
        to_sign = '\n'.join(['HMAC-SHA256', stamp, scope, hashlib.sha256(canonical.encode()).hexdigest()])
        key = self.settings['VOLC_SECRET_KEY_RAW'].encode()
        for item in (date, 'ap-southeast-1', 'ark', 'request'):
            key = hmac.new(key, item.encode(), hashlib.sha256).digest()
        signature = hmac.new(key, to_sign.encode(), hashlib.sha256).hexdigest()
        authorization = f"HMAC-SHA256 Credential={self.settings['VOLC_ACCESS_KEY']}/{scope}, SignedHeaders={signed}, Signature={signature}"
        response = self.request(f'https://{HOST}/?{query}', 'POST', body, {'Content-Type': 'application/json', 'Host': HOST, 'X-Date': stamp, 'X-Content-Sha256': digest, 'Authorization': authorization})
        self.token = response.get('Result', {}).get('ApiKey') or response.get('ApiKey')
        if not self.token:
            raise RuntimeError('GetApiKey did not return a token; response not logged to protect secrets.')
        self.token_time = time.monotonic()

    def ark(self, method, suffix='', body=None):
        self.authenticate()
        return self.request(BASE + '/contents/generations/tasks' + suffix, method, body, {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + self.token, 'X-Project-Name': self.settings['VOLC_PROJECT_NAME']})


def helper_module():
    spec = importlib.util.spec_from_file_location('movi2_helper', HELPER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def prepare(project, chapter, settings, resolution):
    helper = helper_module()
    bindings = []
    content = []
    for asset in helper.active_assets(project, chapter):
        selected = helper.selected_media(asset)
        if not selected:
            raise ValueError('Missing selected reference: ' + asset['tag'])
        path = ROOT / selected['path']
        bindings.append({'tag': asset['tag'], 'reference_token': '@Image' + str(len(bindings)+1), 'path': selected['path'], 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'role': 'reference_image'})
        content.append({'type': 'image_url', 'image_url': {'url': 'data:image/png;base64,' + base64.b64encode(path.read_bytes()).decode()}, 'role': 'reference_image'})
    prompt = chapter['prompt']
    for binding in bindings:
        prompt = re.sub(re.escape(binding['tag']) + r'(?![\w-])', binding['reference_token'], prompt, flags=re.I)
    selected_board = next(item for item in chapter['storyboards'] if item['id'] == chapter['selected_storyboard_id'])
    board = ROOT / selected_board['path']
    board_token = '@Image' + str(len(bindings)+1)
    bindings.append({'tag': 'storyboard_' + chapter['id'], 'reference_token': board_token, 'path': selected_board['path'], 'sha256': hashlib.sha256(board.read_bytes()).hexdigest(), 'role': 'reference_image'})
    content.append({'type': 'image_url', 'image_url': {'url': 'data:image/png;base64,' + base64.b64encode(board.read_bytes()).decode()}, 'role': 'reference_image'})
    prompt += f'\nREFERENCE ROLES: @Image1 is ONLY the beige Tart identity sheet; @Image2 is ONLY brown Tine identity sheet. Each sheet shows multiple angles of ONE puppy. @Image3 supplies fixed garden geometry and sunlight. @Image4 supplies the one small blue ball with cream stripe. {board_token} is a four-panel STORYBOARD, read left-to-right/top-to-bottom, for composition and emotion only. Generate one full-screen moving film, NEVER a grid, split screen, montage of stills, character sheet, panel borders, or frozen slideshow. Do not reproduce the image reference backgrounds from the dog sheets.\nOUTPUT: Exactly 10 seconds of genuine animated action with three shots, two hard cuts, and the timings above, cinematic 16:9. At most two dogs and one ball in any scene. Consistent orange vests and Tine right-rear heart patch. Native synchronized garden ambience, canine Foley and original gentle piano/pizzicato music; absolutely no human speech or narration.'
    body = {'model': settings['VOLC_ENDPOINT_SEEDANCE_25'], 'content': [{'type': 'text', 'text': prompt}] + content, 'duration': chapter['duration'], 'ratio': '16:9', 'resolution': resolution, 'generate_audio': True, 'watermark': False, 'return_last_frame': True, 'output_format': 'mp4', 'omni_reference_task_type': 'reference', 'seed': 18426 + chapter['chapter_index']}
    data_size = len(json.dumps(body, ensure_ascii=False, separators=(',', ':')).encode())
    if data_size >= 64*1024*1024:
        raise ValueError('Request exceeds documented 64 MB limit.')
    return body, {'chapter_id': chapter['id'], 'take_id': chapter['id'] + '_take01', 'take_number': 1, 'status': 'pending', 'submission_state': 'not_submitted', 'created_at': now(), 'source_revision': project['revision'], 'dependency_fingerprint': helper.chapter_fingerprint(ROOT, project, chapter), 'prompt': chapter['prompt'], 'submitted_prompt': prompt, 'bindings': bindings, 'duration': chapter['duration'], 'resolution': resolution, 'model': 'dreamina-seedance-2-5-260628', 'endpoint_id': settings['VOLC_ENDPOINT_SEEDANCE_25'], 'settings': {k: v for k, v in body.items() if k != 'content'}, 'request_bytes': data_size}


def download(url, target):
    if target.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + '.part')
    with urllib.request.urlopen(url, timeout=180) as response, temporary.open('wb') as output:
        while True:
            chunk = response.read(1024*1024)
            if not chunk:
                break
            output.write(chunk)
    temporary.replace(target)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=('inspect', 'probe', 'submit', 'poll'))
    parser.add_argument('--chapters', default='1,2,3,4,5,6')
    parser.add_argument('--resolution', default='480p', choices=('480p','720p','1080p'))
    args = parser.parse_args()
    settings = resolved_settings(read_credentials())
    client = Client(settings)
    project = load(ROOT / 'project.json')
    chapters = [project['chapters'][int(n)-1] for n in args.chapters.split(',')]
    journal = load(JOURNAL) if JOURNAL.exists() else {'project_id': project['id'], 'model': 'dreamina-seedance-2-5-260628', 'credential_source': '../aifx-studio/.env (four named variables only; values never persisted)', 'takes': {}}
    if args.command == 'inspect':
        bodies = [prepare(project, c, settings, args.resolution)[1] for c in chapters]
        print(json.dumps({'credential_presence': {key: True for key in KEYS}, 'endpoint_kind': 'ep-', 'configured_project_present': True, 'planned_takes': [{key: t[key] for key in ('chapter_id','resolution','duration','request_bytes')} for t in bodies], 'reference_count_per_take': len(bodies[0]['bindings'])}))
        return
    if args.command == 'probe':
        client.authenticate()
        print('AK/SK signature accepted; temporary endpoint token obtained and retained only in memory.')
        return
    if args.command == 'submit':
        client.authenticate()
        for chapter in chapters:
            existing = journal['takes'].get(chapter['id'])
            if existing:
                print(chapter['id'], 'already journaled', existing['submission_state'], 'no duplicate submitted', flush=True)
                continue
            body, take = prepare(project, chapter, settings, args.resolution)
            take['submission_state'] = 'submitting'
            journal['takes'][chapter['id']] = take
            save(JOURNAL, journal)
            try:
                response = client.ark('POST', body=body)
            except Exception as error:
                # Network timeouts may hide successful jobs: never retry a POST blindly.
                take['submission_state'] = 'rejected' if str(error).startswith('HTTP ') else 'uncertain'
                take['error'] = client.clean(error)
                if take['submission_state'] == 'rejected':
                    take['status'] = 'failed'
                save(JOURNAL, journal)
                raise
            task_id = response.get('id') or response.get('Result', {}).get('Id')
            if not task_id:
                take['submission_state'] = 'uncertain'
                save(JOURNAL, journal)
                raise RuntimeError('Submission returned no task ID. No automatic retry.')
            take.update(task_id=task_id, submission_state='accepted', status='pending', submitted_at=now())
            save(JOURNAL, journal)
            print(chapter['id'], 'accepted', task_id, args.resolution, '10s, audio enabled', flush=True)
        return
    for chapter in chapters:
        take = journal['takes'].get(chapter['id'])
        if not take or not take.get('task_id'):
            print(chapter['id'], 'no accepted task to poll', flush=True)
            continue
        if take['status'] == 'succeeded' and take.get('path') and (ROOT / take['path']).exists():
            print(chapter['id'], 'succeeded, local take already saved', flush=True)
            continue
        response = client.ark('GET', '/' + urllib.parse.quote(take['task_id'], safe=''))
        status = response.get('status')
        take['provider_status'] = status
        take['checked_at'] = now()
        if status == 'succeeded':
            content = response.get('content', {})
            if not content.get('video_url'):
                raise RuntimeError('Succeeded task has no video URL.')
            target = ROOT / 'chapters' / chapter['id'] / 'takes' / (take['take_id'] + '.mp4')
            download(content['video_url'], target)
            take['path'] = target.relative_to(ROOT).as_posix()
            if content.get('last_frame_url'):
                last = target.with_name(take['take_id'] + '_last.jpg')
                download(content['last_frame_url'], last)
                take['last_frame_path'] = last.relative_to(ROOT).as_posix()
            take.update(status='succeeded', provider_result={k:v for k,v in response.items() if k != 'content'}, completed_at=now())
            print(chapter['id'], 'succeeded and downloaded', target.stat().st_size, 'bytes', flush=True)
        elif status in ('failed','cancelled','expired'):
            take.update(status='failed', error=client.clean(response.get('error', status)))
            print(chapter['id'], status, take['error'], flush=True)
        else:
            take['status'] = 'processing' if status == 'running' else 'pending'
            print(chapter['id'], status, flush=True)
        save(JOURNAL, journal)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        # Never emit a traceback containing request headers or response token bodies.
        print(type(error).__name__ + ': ' + str(error), file=sys.stderr)
        sys.exit(1)
