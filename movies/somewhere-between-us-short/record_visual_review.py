"""Record the selected take samples actually inspected by the operator."""
import argparse, json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--chapters',required=True);ap.add_argument('--note',required=True);a=ap.parse_args()
path=ROOT/'exports/visual-review/review-notes.json'
review=json.loads(path.read_text(encoding='utf-8')) if path.exists() else {
 'method':'Human visual inspection of six decoded frame samples per selected take; targeted larger frames for uncertain staging.',
 'scope':'Visible identity, scale, blocking, environment, story beat, title/credit exclusions. No independent audio listening or transcription.',
 'takes':{}}
j=json.loads((ROOT/'exports/seedance-journal.json').read_text(encoding='utf-8'))
for index in map(int,a.chapters.split(',')):
 t=j['takes'][f'chapter_{index:02d}']
 assert t['status']=='succeeded' and t.get('verification',{}).get('decode_verified')
 review['takes'][t['id']]={'reviewed':True,'at':datetime.now(timezone.utc).isoformat(),'note':a.note,
  'samples':[s['path'] for s in t['verification']['samples']]}
path.write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Recorded sample review for',a.chapters)
