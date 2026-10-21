from pathlib import Path
import json,subprocess,sys
ROOT=Path(__file__).resolve().parent
helper='C:/Users/Admin 3/.codex/skills/movi2/scripts/project.py'
r=subprocess.run([sys.executable,'-X','utf8',helper,'review-assets',str(ROOT)],capture_output=True,text=True,encoding='utf-8')
if r.returncode:
    print(r.stdout);print(r.stderr);sys.exit(r.returncode)
report=json.loads(r.stdout)
(ROOT/'exports'/'asset-review'/'review-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ['gallery','images','assets']},indent=2))
