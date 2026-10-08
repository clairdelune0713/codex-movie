const fs = require('node:fs');
const path = require('node:path');
const {execFileSync} = require('node:child_process');
const repo = path.resolve(__dirname,'../../../../aifx-studio');
const names = ['VOLC_ACCESS_KEY','VOLC_SECRET_KEY_RAW','VOLC_PROJECT_NAME','VOLC_ENDPOINT_SEEDANCE_25'];
const dotenv = require(path.join(repo,'node_modules/dotenv'));
const text = fs.readFileSync(path.join(repo,'.env'),'utf8');
const selected = text.split(/\r?\n/).filter(line=>names.some(name=>new RegExp('^\\s*(?:export\\s+)?'+name+'\\s*=').test(line))).join('\n');
const literal = dotenv.parse(selected);
const python = 'C:/Users/admina/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe';
const script = "import json,importlib.util,sys;s=importlib.util.spec_from_file_location('r',sys.argv[1]);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);print(json.dumps(m.read_credentials()))";
const adapter = JSON.parse(execFileSync(python,['-c',script,path.join(__dirname,'seedance_render.py')],{encoding:'utf8'}));
const nextEnv = require(path.join(repo,'node_modules/@next/env'));
const loaded = nextEnv.loadEnvConfig(repo,true,{info(){},error(){}});
const report = {
  checked_at:new Date().toISOString(),
  next_env_files:loaded.loadedEnvFiles.map(file=>file.path),
  setting_comparison:names.map(name=>({name,python_matches_dotenv:adapter[name]===literal[name],python_matches_next:adapter[name]===loaded.combinedEnv[name],python_length:adapter[name]?.length,dotenv_length:literal[name]?.length,next_length:loaded.combinedEnv[name]?.length})),
  credential_routing_variable_presence:Object.fromEntries(['VOLC_ACCESS_KEY_M','VOLC_SECRET_KEY_RAW_M','VOLC_PROJECT_NAME_M'].map(name=>[name,text.split(/\r?\n/).some(line=>new RegExp('^\\s*(?:export\\s+)?'+name+'\\s*=').test(line))])),
  values_logged:false
};
fs.writeFileSync(path.join(__dirname,'env-loading-comparison.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report));
