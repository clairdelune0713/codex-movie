/* Run the repository's actual signing helper with only the four authorized values.
 * Logging hooks are local no-ops, so no AIFX database or API logger is invoked.
 */
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const crypto = require('node:crypto');
const { execFileSync } = require('node:child_process');

const repo = path.resolve(__dirname, '../../../../aifx-studio');
const ts = require(path.join(repo, 'node_modules/typescript'));
const dotenv = require(path.join(repo, 'node_modules/dotenv'));
const names = ['VOLC_ACCESS_KEY', 'VOLC_SECRET_KEY_RAW', 'VOLC_PROJECT_NAME', 'VOLC_ENDPOINT_SEEDANCE_25'];
const envText = fs.readFileSync(path.join(repo, '.env'), 'utf8');
const selectedLines = envText.split(/\r?\n/).filter(line => names.some(name => new RegExp('^\\s*(?:export\\s+)?'+name+'\\s*=').test(line))).join('\n');
const values = dotenv.parse(selectedLines);
for (const name of names) if (!values[name]) throw new Error('Missing '+name);
const sourceFile = path.join(repo, 'src/lib/volcengine.ts');
const source = fs.readFileSync(sourceFile, 'utf8');
const js = ts.transpileModule(source, {compilerOptions: {module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022, esModuleInterop: true}}).outputText;
const quietLogger = {info(){},warn(){},error(){},debug(){}};

function loadHelper(settings, request) {
  const exports = {};
  const context = {
    exports, Buffer, Date, setTimeout, console: quietLogger,
    fetch: request,
    require(name) {
      if (name === 'crypto') return crypto;
      if (name === './env') return {env: settings};
      if (name === './logger') return quietLogger;
      if (name === '@/lib/api-logger') return {withApiLogging: async callback => await callback()};
      throw new Error('Unexpected import '+name);
    }
  };
  vm.runInNewContext(js, context, {filename: sourceFile});
  return exports;
}

function redact(message) {
  let text = String(message);
  for (const name of ['VOLC_ACCESS_KEY', 'VOLC_SECRET_KEY_RAW']) text = text.split(values[name]).join('[redacted]');
  return text;
}

async function main() {
  if (process.argv.includes('--inspect-endpoints')) {
    const sourceHelper = loadHelper(values, (url, options) => fetch(url, {...options,signal:AbortSignal.timeout(30000)}));
    const response = await sourceHelper.makeSignedVolcRequest({action:'ListEndpoints',body:{ProjectName:values.VOLC_PROJECT_NAME,PageNumber:1,PageSize:100},ak:values.VOLC_ACCESS_KEY,sk:values.VOLC_SECRET_KEY_RAW});
    const items = response.Result?.Items || [];
    const report = {checked_at:new Date().toISOString(),credential_route:'Four named base settings only',configured_endpoint_visible:items.some(item=>item.Id===values.VOLC_ENDPOINT_SEEDANCE_25),total_count:response.Result?.TotalCount,items:items.map(item=>({id:item.Id,status:item.Status,model_reference:item.ModelReference,project_matches_named_setting:item.ProjectName===values.VOLC_PROJECT_NAME})),values_logged:false};
    fs.writeFileSync(path.join(__dirname,'base-project-endpoints.json'),JSON.stringify(report,null,2)+'\n');
    console.log(JSON.stringify(report));
    return;
  }
  const captured = [];
  const synthetic = {VOLC_ACCESS_KEY: 'example-access-key', VOLC_SECRET_KEY_RAW: 'example-secret-key', VOLC_PROJECT_NAME:'example-project', VOLC_ENDPOINT_SEEDANCE_25:'ep-example'};
  const helper = loadHelper(synthetic, async (url, options) => {
    captured.push({url, options});
    return {ok:true,status:200,text:async()=>JSON.stringify({Result:{ApiKey:'example-token'}})};
  });
  await helper.getTemporaryApiKeyForEndpoint('ep-example');
  const fixture = captured[0];
  const compare = `import importlib.util,json,sys\np=sys.argv[1]\ns=importlib.util.spec_from_file_location('render_client',p)\nm=importlib.util.module_from_spec(s);s.loader.exec_module(m)\nv=json.loads(sys.stdin.read())\nc=m.Client(v['settings'])\nclass FixedClock:\n @staticmethod\n def now(tz):\n  return m._fixture_parse_date(v['date'])\nfrom datetime import datetime\nm._fixture_parse_date=lambda value: datetime.strptime(value,'%Y%m%dT%H%M%SZ')\nm.datetime=FixedClock\nactual={}\ndef capture(url,method,body=None,headers=None):\n actual.update(url=url,method=method,body=body,headers=headers);return {'Result':{'ApiKey':'example-token'}}\nc.request=capture;c.authenticate()\nprint(json.dumps(actual))`;
  const python = 'C:/Users/admina/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe';
  const input = {settings:synthetic,date:fixture.options.headers['X-Date']};
  const actual = JSON.parse(execFileSync(python, ['-c',compare,path.join(__dirname,'seedance_render.py')], {input:JSON.stringify(input),encoding:'utf8'}));
  const matches = actual.url === fixture.url && actual.method === fixture.options.method && JSON.stringify(actual.body) === fixture.options.body && JSON.stringify(actual.headers) === JSON.stringify(fixture.options.headers);
  const report = {source: 'aifx-studio/src/lib/volcengine.ts', source_sha256:crypto.createHash('sha256').update(source).digest('hex'), signing_matches_python_client:matches, credential_keys_used:names, excluded_credentials:'All _M and other credentials excluded', other_aifx_services_invoked:false};
  if (!matches) {
    // Compare header fields individually because object order is irrelevant.
    report.signing_matches_python_client = actual.url === fixture.url && Object.entries(fixture.options.headers).every(([key,value])=>actual.headers[key]===value) && JSON.stringify(actual.body)===fixture.options.body;
  }
  if (!report.signing_matches_python_client) throw new Error('Source helper and adapter signing differ. No live request sent.');
  console.log('Offline comparison: repository helper and Python client produce identical signed requests.');
  let status = null;
  const original = loadHelper(values, async (url, options) => {
    const response = await fetch(url, {...options,signal:AbortSignal.timeout(30000)});
    status = response.status;
    return response;
  });
  try {
    // Omit the optional model name so the original helper selects the named base AK/SK.
    // The endpoint itself still comes from VOLC_ENDPOINT_SEEDANCE_25.
    const token = await original.getTemporaryApiKeyForEndpoint(values.VOLC_ENDPOINT_SEEDANCE_25);
    report.live_result = {http_status:status,authenticated:!!token,temporary_token_persisted:false};
    console.log('Live repository helper: authentication succeeded. Token not printed or persisted.');
  } catch (error) {
    report.live_result = {http_status:status,authenticated:false,error:redact(error.message)};
    console.log('Live repository helper:',status,redact(error.message));
  }
  report.checked_at = new Date().toISOString();
  fs.writeFileSync(path.join(__dirname,'aifx-auth-comparison.json'), JSON.stringify(report,null,2)+'\n');
  if (!report.live_result.authenticated) process.exitCode=2;
}
main().catch(error=>{console.error(redact(error.message));process.exitCode=1;});
