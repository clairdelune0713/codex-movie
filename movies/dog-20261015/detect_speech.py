"""Independent local language detection for actual speech, not forced-language ASR."""
import argparse,json,hashlib
import check_dialogue as audit
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--chapters',required=True);ap.add_argument('--take');args=ap.parse_args()
ROOT=audit.ROOT
snapshots=audit.AUDIT_TOOLS/'asr-models/models--Systran--faster-whisper-large-v3/snapshots'
model_dir=next(d for d in snapshots.iterdir() if (d/'model.bin').is_file())
model=audit.WhisperModel(str(model_dir),device='cuda',compute_type='float16',local_files_only=True)
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));j=json.loads((ROOT/'exports/task-journal.json').read_text(encoding='utf-8'))
out=[]
for n in args.chapters.split(','):
    c=p['chapters'][int(n)-1];t=j['takes'][c['id']]
    if args.take:
        t=next(x for x in t.get('prior_takes',[])+[t] if x['id']==args.take)
    if t['status']!='succeeded':continue
    f=ROOT/t['path']
    r=audit.subprocess.run([str(audit.FF),'-v','error','-i',str(f),'-vn','-ac','1','-ar','16000','-f','f32le','pipe:1'],capture_output=True,check=True)
    audio=audit.np.frombuffer(r.stdout,dtype=audit.np.float32)
    segments,info=model.transcribe(audio,language=None,beam_size=5,vad_filter=True,condition_on_previous_text=False)
    item={'chapter':c['id'],'take':t['id'],'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),
          'detected_language':info.language,'language_probability':info.language_probability,
          'top_languages':sorted(info.all_language_probs or [],key=lambda x:-x[1])[:4],
          'text':' '.join(s.text for s in segments),'limitation':'Language classifier and ASR are evidence, not an exact human listening review.'}
    out.append(item);print(json.dumps(item,ensure_ascii=False),flush=True)
(ROOT/'exports/language-detection.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
