"""Poll accepted tasks only; never submits or retries generation jobs."""
import json
import subprocess
import sys
import time
from pathlib import Path

root=Path(__file__).resolve().parents[1]
journal_file=root/'exports/seedance-journal.json'
previous=None
while True:
    result=subprocess.run([sys.executable,str(root/'exports/seedance_render.py'),'poll','--resolution','480p'],capture_output=True,text=True)
    if result.returncode:
        print(result.stdout+result.stderr,flush=True)
        raise SystemExit(result.returncode)
    journal=json.loads(journal_file.read_text(encoding='utf-8'))
    states={key:(item['status'],item.get('provider_status'),bool(item.get('path'))) for key,item in journal['takes'].items()}
    if states!=previous:
        print(result.stdout.strip(),flush=True)
        previous=states
    if len(states)==6 and all(state[0] in ('succeeded','failed') for state in states.values()):
        if any(state[0]=='failed' for state in states.values()):
            raise SystemExit(2)
        print('All six accepted jobs succeeded and downloaded.',flush=True)
        break
    time.sleep(30)
