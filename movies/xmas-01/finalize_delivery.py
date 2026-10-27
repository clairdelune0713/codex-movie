from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
HELPER = Path('C:/Users/Admin 3/.codex/skills/movi2/scripts/project.py')
USAGE = HELPER.with_name('usage.py')
SESSION = 'session_41fc80be622d4ff88cfe8e96eedd92d1'

def write(path,data):
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def command(script,*args):
    result=subprocess.run([sys.executable,str(script),*map(str,args)],capture_output=True,text=True,encoding='utf-8')
    if result.returncode:
        raise RuntimeError(result.stdout[-1500:]+result.stderr[-300:])
    return json.loads(result.stdout)

project=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
source=json.loads((ROOT/'exports/source-technical-verification.json').read_text(encoding='utf-8'))
final=json.loads((ROOT/'exports/final-technical-verification.json').read_text(encoding='utf-8'))
job=json.loads((ROOT/'exports/usage-attempt_01.json').read_text(encoding='utf-8'))
pricing=json.loads((ROOT/'exports/pricing-evidence.json').read_text(encoding='utf-8'))
ledger=json.loads((ROOT/'usage.json').read_text(encoding='utf-8'))
if len(ledger['jobs'])!=1 or job['state']!='succeeded' or not final['full_decode']['passed']:
    raise RuntimeError('Single successful generation and verified export required')
tokens=int(job['usage']['completion_tokens'])
amount=Decimal(tokens)/Decimal(1000000)*Decimal(pricing['rate_per_million_completion_tokens'])
job['cost']={'kind':'estimated','currency':'USD','amount':str(amount),'basis':str(tokens)+' measured usage.completion_tokens / 1000000 * USD '+pricing['rate_per_million_completion_tokens']+' for Seedance 2.5 720p without video input; public rate checked '+pricing['checked_date']+'; '+pricing['source']+'. Account discounts, resource-pack deductions, taxes and actual invoice not verified.'}
job['usage']['pricing_rate_usd_per_million_completion_tokens']=pricing['rate_per_million_completion_tokens']
write(ROOT/'exports/usage-attempt_01.json',job)
command(USAGE,'record',ROOT,'--session',SESSION,'--from',ROOT/'exports/usage-attempt_01.json')

inspection={
    'inspected_at':datetime.now(timezone.utc).isoformat(),
    'method':'20 decoded frames across 0.2-28.8 seconds, plus full-size opening and final group views; original and export fully decoded with audio signal checks.',
    'observations':[
        'The FIRST mall reference is visibly retained: curving galleries, golden Christmas decor, red curtains, tree and Hong Kong harbour skyline.',
        'One Louis, one charcoal Kooloo cat and one red ccbug ornament remain recognizable; no pink alternative ornaments appear.',
        'Louis sweater, pink glasses, hair, antenna and pointed ears are preserved; Kooloo retains antlers, bells, yellow eyes and forehead mark; ccbug retains red glass body and green/gold band.',
        'Opening and final wide views show Kooloo near half Louis overall height and ccbug near one third Kooloo; the perspective/depth varies and physical ratios cannot be certified exactly from 2D video.',
        'Clear trolley chase, ribbon unwinding, cooperative stop and giant-bow reveal are present; party star and shopping supplies remain recognizable.',
        'No visible title cards, captions, reference grids, watermarks or existing entertainment characters in inspected frames.'
    ],
    'limitations':['Generated staging differs slightly from the written choreography.','Visual review used sampled frames rather than frame-by-frame inspection.','Audio presence, stereo channels, signal levels and decode were checked; exact sound design was not independently transcribed or certified.'],
    'technical_source_report':'exports/source-technical-verification.json',
    'technical_final_report':'exports/final-technical-verification.json',
    'gallery':'exports/source-inspection-contact-sheet.jpg'
}
write(ROOT/'exports/creative-inspection.json',inspection)
chapter=project['chapters'][0]
take=next(t for t in chapter['takes'] if t['id']=='take_01')
take['verification']={'status':'inspected','source_full_decode':source['full_decode'],'source_duration':float(source['probe']['format']['duration']),'source_dimensions':[1280,720],'source_fps':24,'source_frames':721,'visual_report':'exports/creative-inspection.json'}
chapter['active_take_id']='take_01'
chapter['production_state']='delivered'
chapter['screenshots']=json.loads((ROOT/'exports/source-screenshot-manifest.json').read_text(encoding='utf-8'))
project['delivery']={'status':'delivered','path':final['output'],'sha256':final['output_sha256'],'duration_seconds':30.0,'aspect_ratio':'16:9','dimensions':[1280,720],'fps':24,'frame_count':720,'audio':{'codec':'aac','sample_rate':48000,'channels':2},'generation_requests':1,'merged_segments':False,'source_take_id':'take_01','inspection_report':'exports/creative-inspection.json','technical_report':'exports/final-technical-verification.json','cost_estimate_usd':str(amount)}
proposal=ROOT/'proposal-delivery-v01.json'
write(proposal,project)
check=command(HELPER,'check',ROOT,'--from',proposal)
commit=command(HELPER,'commit',ROOT,'--from',proposal,'--reason','Deliver verified single-generation 30-second Christmas shopping adventure')
export=command(HELPER,'export',ROOT)
status=command(HELPER,'status',ROOT)
write(ROOT/'exports/delivery-project-status.json',status)
finished=command(USAGE,'finish',ROOT,'--session',SESSION,'--outcome','delivered')
report=command(USAGE,'report',ROOT,'--session',SESSION)
write(ROOT/('exports/usage-report-'+SESSION+'.json'),report)
write(ROOT/'exports/delivery-summary.json',{'delivery':project['delivery'],'usage':report,'project_revision':commit['revision'],'errors':check['errors'],'warnings':check['warnings']})
print(json.dumps({'delivery':project['delivery'],'revision':commit['revision'],'errors':check['errors'],'warnings':check['warnings'],'usage_report':report},ensure_ascii=False,indent=2))
