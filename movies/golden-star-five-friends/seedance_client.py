"""Authorized direct Seedance transport. Credentials remain only in memory."""
import base64
import hashlib
import hmac
import json
import mimetypes
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent
ENV=ROOT.parents[2]/'aifx-studio'/'.env'
SETTINGS=('VOLC_ACCESS_KEY','VOLC_SECRET_KEY_RAW','VOLC_PROJECT_NAME','VOLC_ENDPOINT_SEEDANCE_25')
MANAGEMENT='ark.ap-southeast-1.byteplusapi.com'
TASKS='https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks'

def write_json(path,value):
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    temporary.replace(path)

class ProviderError(RuntimeError):
    def __init__(self,status,code,message=''):
        self.status=status
        self.code=code
        self.message=message
        super().__init__(f'Provider HTTP {status}; code={code}; {message}')

class Client:
    def __init__(self):
        self.settings={}
        for raw in ENV.read_text(encoding='utf-8-sig').splitlines():
            line=raw.strip()
            if line.startswith('export '):
                line=line[7:].lstrip()
            if '=' not in line or line.startswith('#'):
                continue
            key,value=line.split('=',1)
            key=key.strip()
            if key not in SETTINGS:
                continue
            value=value.strip()
            if value[:1] in ('"',"'"):
                quote=value[0]
                end=value.rfind(quote)
                if end>0:
                    value=value[1:end]
            else:
                value=re.split(r'\s+#',value,1)[0].rstrip()
            self.settings[key]=value
        missing=[k for k in SETTINGS if not self.settings.get(k)]
        if missing:
            raise RuntimeError('Missing authorized settings: '+','.join(missing))
        self.endpoint=None
        self.token=None
        self.token_time=0

    def safe(self,text):
        result=str(text)
        for value in self.settings.values():
            if value:
                result=result.replace(value,'[redacted]')
        if self.token:
            result=result.replace(self.token,'[redacted]')
        return re.sub(r'https?://\S+','[provider-url]',result)[:900]

    def request(self,url,method='GET',payload=None,headers=None,timeout=120):
        data=None if payload is None else json.dumps(payload,separators=(',',':'),ensure_ascii=False).encode('utf-8')
        request=urllib.request.Request(url,data=data,headers=headers or {},method=method)
        try:
            with urllib.request.urlopen(request,timeout=timeout) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            try:
                body=json.loads(error.read())
                detail=body.get('error') or body.get('ResponseMetadata',{}).get('Error') or {}
                code=detail.get('code') or detail.get('Code') or 'unspecified'
                message=detail.get('message') or detail.get('Message') or ''
            except Exception:
                code,message='unparsed',''
            raise ProviderError(error.code,self.safe(code),self.safe(message)) from None

    def management(self,action,payload):
        body=json.dumps(payload,separators=(',',':'),ensure_ascii=False).encode('utf-8')
        hashed=hashlib.sha256(body).hexdigest()
        stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
        date=stamp[:8]
        query=urllib.parse.urlencode(sorted({'Action':action,'Version':'2024-01-01'}.items()),quote_via=urllib.parse.quote)
        canonical_headers=f'content-type:application/json\nhost:{MANAGEMENT}\nx-content-sha256:{hashed}\nx-date:{stamp}\n'
        signed='content-type;host;x-content-sha256;x-date'
        canonical='\n'.join(('POST','/',query,canonical_headers,signed,hashed))
        scope=f'{date}/ap-southeast-1/ark/request'
        to_sign='\n'.join(('HMAC-SHA256',stamp,scope,hashlib.sha256(canonical.encode()).hexdigest()))
        key=self.settings['VOLC_SECRET_KEY_RAW'].encode()
        for item in (date,'ap-southeast-1','ark','request'):
            key=hmac.new(key,item.encode(),hashlib.sha256).digest()
        signature=hmac.new(key,to_sign.encode(),hashlib.sha256).hexdigest()
        authorization=f"HMAC-SHA256 Credential={self.settings['VOLC_ACCESS_KEY']}/{scope}, SignedHeaders={signed}, Signature={signature}"
        result=self.request(f'https://{MANAGEMENT}/?{query}','POST',payload,{'Content-Type':'application/json','Host':MANAGEMENT,'X-Content-Sha256':hashed,'X-Date':stamp,'Authorization':authorization})
        if result.get('ResponseMetadata',{}).get('Error'):
            detail=result['ResponseMetadata']['Error']
            raise ProviderError(200,self.safe(detail.get('Code','unspecified')),self.safe(detail.get('Message','')))
        return result

    def resolve_endpoint(self):
        items=[]
        page=1
        while True:
            response=self.management('ListEndpoints',{'ProjectName':self.settings['VOLC_PROJECT_NAME'],'PageNumber':page,'PageSize':100})
            result=response.get('Result',{})
            batch=result.get('Items',[])
            items.extend(batch)
            if len(items)>=result.get('TotalCount',len(items)) or not batch:
                break
            page+=1
        eligible=[]
        for item in items:
            model=json.dumps(item.get('ModelReference',{})).lower()
            status=str(item.get('Status','')).lower()
            if 'seedance' in model and re.search(r'2[-._ ]?5',model) and status in ('running','active'):
                eligible.append(item)
        configured=self.settings['VOLC_ENDPOINT_SEEDANCE_25']
        match=next((x for x in eligible if x.get('Id')==configured),None)
        if not match and len(eligible)==1:
            match=eligible[0]
        if not match:
            raise RuntimeError(f'No unambiguous running Seedance 2.5 endpoint: {len(eligible)} eligible endpoints.')
        self.endpoint=match['Id']
        record={'verified_at':datetime.now(timezone.utc).isoformat(),'model_reference':match.get('ModelReference'),'endpoint_id':self.endpoint,'configured_endpoint_matches':self.endpoint==configured,'reason':'Use authorized projects running Seedance 2.5 endpoint','visible_endpoint_count':len(items),'eligible_endpoint_count':len(eligible)}
        write_json(ROOT/'exports'/'endpoint-resolution.json',record)
        return {k:v for k,v in record.items() if k not in ('endpoint_id','model_reference')}

    def authenticate(self):
        if not self.endpoint:
            self.resolve_endpoint()
        response=self.management('GetApiKey',{'DurationSeconds':3600,'ResourceType':'endpoint','ResourceIds':[self.endpoint]})
        self.token=response.get('Result',{}).get('ApiKey') or response.get('ApiKey')
        if not self.token:
            raise RuntimeError('GetApiKey returned no temporary API key.')
        self.token_time=time.time()

    def headers(self):
        if not self.token or time.time()-self.token_time>2700:
            self.authenticate()
        return {'Authorization':'Bearer '+self.token,'Content-Type':'application/json','X-Project-Name':self.settings['VOLC_PROJECT_NAME']}

    def submit(self,payload):
        return self.request(TASKS,'POST',payload,self.headers(),timeout=240)

    def poll(self,task_id):
        return self.request(TASKS+'/'+urllib.parse.quote(task_id,safe=''),'GET',headers=self.headers())

    def download(self,url,path):
        path=Path(path)
        path.parent.mkdir(parents=True,exist_ok=True)
        partial=path.with_suffix(path.suffix+'.partial')
        with urllib.request.urlopen(url,timeout=180) as response, partial.open('wb') as target:
            while True:
                block=response.read(1024*1024)
                if not block:
                    break
                target.write(block)
        partial.replace(path)

if __name__=='__main__':
    client=Client()
    print(json.dumps({'authorized_settings_present':{k:bool(client.settings.get(k)) for k in SETTINGS},'endpoint_resolution':client.resolve_endpoint()},indent=2))
    client.authenticate()
    print(json.dumps({'temporary_authentication_succeeded':bool(client.token)}))
