from pathlib import Path
import json, re, shlex
workspace=Path(__file__).resolve().parents[2]
env=workspace/'.env'
required=['VOLC_ACCESS_KEY','VOLC_SECRET_KEY_RAW','VOLC_PROJECT_NAME','VOLC_ENDPOINT_SEEDANCE_25']
data={}
if env.exists():
    for line in env.read_text(encoding='utf-8-sig').splitlines():
        match=re.match(r'^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*?)\s*$',line)
        if match and match.group(1) in required:
            value=match.group(2)
            if value.startswith(('"',"'")):
                quote=value[0]; end=value.find(quote,1)
                value=value[1:end] if end>0 else ''
            else:
                value=re.split(r'\s+#',value,1)[0].strip()
            data[match.group(1)]=value
report={'env_path':str(env),'file_exists':env.exists(),'required_keys_present':{k:bool(data.get(k)) for k in required},'project_name_policy':'intentionally_blank_per_user','network_calls':0}
out=Path(__file__).resolve().parent/'exports'/'provider-config-presence.json'
out.write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
