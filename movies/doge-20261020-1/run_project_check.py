from pathlib import Path
import json,subprocess,sys,collections
ROOT=Path(__file__).resolve().parent
helper='C:/Users/Admin 3/.codex/skills/movi2/scripts/project.py'
r=subprocess.run([sys.executable,'-X','utf8',helper,'check',str(ROOT)],capture_output=True,text=True,encoding='utf-8')
report=json.loads(r.stdout)
(ROOT/'exports'/'asset-review'/'project-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'revision':report.get('revision'),'duration':report.get('duration'),'errors':report.get('errors'),'warnings':report.get('warnings'),'asset_review':report.get('asset_review'),'candidate_freshness':dict(collections.Counter(a.get('freshness') for a in report.get('artifacts',[]) if a.get('kind')=='candidate'))},indent=2))
sys.exit(r.returncode)
