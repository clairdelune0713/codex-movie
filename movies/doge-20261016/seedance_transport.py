"""Project-local Seedance adapter. Credentials are read only at runtime and never saved."""
import argparse
import base64
import hashlib
import hmac
import importlib.util
import json
import os
import re
import ssl
import subprocess
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
HELPER = Path('C:/Users/Admin 3/.codex/skills/movi2/scripts/project.py')
ENV_FILE = Path('C:/Users/Admin 3/Downloads/codex-movie/.env')
SETTINGS = ('VOLC_ACCESS_KEY','VOLC_SECRET_KEY_RAW','VOLC_PROJECT_NAME','VOLC_ENDPOINT_SEEDANCE_25')
HOST = 'ark.ap-southeast-1.byteplusapi.com'
BASE = 'https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks'
JOURNAL = ROOT / 'exports' / 'task-journal.json'
LOCK = threading.RLock()

def now():
    return datetime.now(timezone.utc).isoformat()

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def atomic_json(path, value):
    path.parent.mkdir(parents=True,exist_ok=True)
    temp = path.with_suffix(path.suffix+'.'+uuid.uuid4().hex+'.partial')
    temp.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
    os.replace(temp,path)

def settings():
    # Parse only the four explicitly authorized settings. Never load sibling variables.
    found = {}
    for line in ENV_FILE.read_text(encoding='utf-8-sig').splitlines():
        match = re.match(r'^\s*(?:export\s+)?([A-Z0-9_]+)\s*=\s*(.*)$',line)
        if not match or match[1] not in SETTINGS:
            continue
        value = match[2].strip()
        if value[:1] in ('"',"'"):
            mark = value[0]
            end = value.find(mark,1)
            if end == -1:
                raise ValueError('Invalid quoting in an authorized setting')
            value = value[1:end]
        else:
            value = re.split(r'\s+#',value,1)[0].strip()
        found[match[1]] = value
    # User explicitly confirmed that the workspace project value should be EMPTY.
    # Preserve that value rather than substituting another project/account.
    missing = [key for key in SETTINGS if key not in found or (key!='VOLC_PROJECT_NAME' and not found.get(key))]
    if missing:
        raise ValueError('Missing authorized settings: '+', '.join(missing))
    return found

class ApiFailure(Exception):
    def __init__(self, status, code):
        self.status, self.code = status, str(code)
        super().__init__(f'Provider request rejected: HTTP {status}, code {self.code}')

def response(request, timeout=120):
    try:
        with urlopen(request,timeout=timeout) as result:
            data = json.loads(result.read())
    except HTTPError as error:
        try:
            data = json.loads(error.read())
            info = data.get('error') or data.get('Error') or data.get('ResponseMetadata',{}).get('Error') or {}
            code = info.get('code') or info.get('Code') or 'HTTPError'
        except Exception:
            code = 'HTTPError'
        raise ApiFailure(error.code,code) from None
    error = data.get('Error') or data.get('ResponseMetadata',{}).get('Error')
    if error:
        raise ApiFailure(200,error.get('Code','ApiError'))
    return data

class Client:
    def __init__(self):
        self.config = settings()
        self.endpoint = None
        self.token = None
        self.token_time = 0
        self.token_lock = threading.Lock()

    def management(self, action, body):
        raw = json.dumps(body,separators=(',',':'),ensure_ascii=False).encode('utf-8')
        query = urlencode(sorted({'Action':action,'Version':'2024-01-01'}.items()),quote_via=quote)
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
        day = stamp[:8]
        sha = hashlib.sha256(raw).hexdigest()
        headers = 'content-type:application/json\nhost:'+HOST+'\nx-content-sha256:'+sha+'\nx-date:'+stamp+'\n'
        signed = 'content-type;host;x-content-sha256;x-date'
        canonical = '\n'.join(['POST','/',query,headers,signed,sha])
        scope = day+'/ap-southeast-1/ark/request'
        string = '\n'.join(['HMAC-SHA256',stamp,scope,hashlib.sha256(canonical.encode()).hexdigest()])
        key = self.config['VOLC_SECRET_KEY_RAW'].encode()
        for word in [day,'ap-southeast-1','ark','request']:
            key = hmac.new(key,word.encode(),hashlib.sha256).digest()
        signature = hmac.new(key,string.encode(),hashlib.sha256).hexdigest()
        authorization = 'HMAC-SHA256 Credential='+self.config['VOLC_ACCESS_KEY']+'/'+scope+', SignedHeaders='+signed+', Signature='+signature
        request = Request('https://'+HOST+'/?'+query,data=raw,method='POST',headers={
            'Content-Type':'application/json','Host':HOST,'X-Date':stamp,
            'X-Content-Sha256':sha,'Authorization':authorization})
        return response(request)

    def resolve(self):
        items, page = [], 1
        while True:
            data = self.management('ListEndpoints',{'ProjectName':self.config['VOLC_PROJECT_NAME'],'PageNumber':page,'PageSize':100})
            result = data.get('Result',data)
            batch = result.get('Items',[])
            items.extend(batch)
            if len(items)>=result.get('TotalCount',len(items)) or not batch:
                break
            page += 1
        candidates = []
        for item in items:
            desc = json.dumps(item.get('ModelReference',{})).lower()
            desc += ' '+str(item.get('Name','')).lower()
            status = str(item.get('Status','')).lower()
            if re.search(r'seedance[-_. ]2[-_. ]5',desc) and status in ('running','active','ready'):
                candidates.append(item)
        configured = self.config['VOLC_ENDPOINT_SEEDANCE_25']
        exact = [item for item in candidates if item.get('Id')==configured]
        if exact:
            chosen = exact[0]
        elif len(candidates)==1:
            chosen = candidates[0]
        else:
            raise ValueError('No unique running Seedance 2.5 endpoint in the authorized project; matching count='+str(len(candidates)))
        self.endpoint = chosen['Id']
        # Operational endpoint ID is not a credential; do not persist AK/SK/project/token values.
        atomic_json(ROOT/'exports/endpoint-resolution.json',{
            'verified_at':now(),'model_family':'Seedance 2.5',
            'configured_endpoint_matches':self.endpoint==configured,
            'running_matching_endpoint_count':len(candidates),
            'resolved_endpoint_id':self.endpoint,
            'reason':'Configured endpoint verified' if self.endpoint==configured else 'Unambiguous running Seedance 2.5 endpoint in authorized project'})
        self.get_token()
        return {'model_family':'Seedance 2.5','configured_endpoint_matches':self.endpoint==configured,
                'running_matching_endpoint_count':len(candidates),'authentication':'verified'}

    def get_token(self):
        with self.token_lock:
            if self.token and time.monotonic()-self.token_time<2900:
                return self.token
            data = self.management('GetApiKey',{'DurationSeconds':3600,'ResourceType':'endpoint','ResourceIds':[self.endpoint]})
            self.token = data.get('Result',{}).get('ApiKey') or data.get('ApiKey')
            if not self.token:
                raise ValueError('Provider did not return a temporary API key')
            self.token_time = time.monotonic()
            return self.token

    def task(self, task_id=None, payload=None):
        headers = {'Authorization':'Bearer '+self.get_token(),'Content-Type':'application/json',
                   'X-Project-Name':self.config['VOLC_PROJECT_NAME']}
        url = BASE if task_id is None else BASE+'/'+quote(task_id,safe='')
        raw = None if payload is None else json.dumps(payload,separators=(',',':'),ensure_ascii=False).encode()
        return response(Request(url,data=raw,headers=headers,method='POST' if payload is not None else 'GET'))

