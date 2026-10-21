"""Local anonymous-model ASR for generated dialogue QA; never uploads audio."""
import argparse,hashlib,json,os,sys,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'tools/asr-runtime'))
os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN']='1'
os.environ['HF_HUB_DISABLE_TELEMETRY']='1'
MODEL=ROOT/'tools/asr-model-base-en'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--download',action='store_true');ap.add_argument('--chapters',default='all');args=ap.parse_args()
    if args.download:
        from huggingface_hub import snapshot_download
        snapshot_download('Systran/faster-whisper-base.en',local_dir=str(MODEL),
            cache_dir=str(ROOT/'tools/asr-download-cache'),token=False,
            allow_patterns=['config.json','model.bin','tokenizer.json','vocabulary.*'],max_workers=2)
        print('Public English ASR model downloaded locally. No audio was uploaded.');return
    from faster_whisper import WhisperModel
    import numpy as np
    model=WhisperModel(str(MODEL),device='cpu',compute_type='int8',cpu_threads=4,num_workers=1,local_files_only=True)
    project=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
    journals=[]
    for filename in ['task-journal-scenes-01-36.json','task-journal.json']:
        f=ROOT/'exports'/filename
        if f.exists():journals.append(json.loads(f.read_text(encoding='utf-8')))
    takes={cid:t for j in journals for cid,t in j['takes'].items() if t['status']=='succeeded'}
    wanted=set(range(1,52)) if args.chapters=='all' else {int(n) for n in args.chapters.split(',')}
    for c in project['chapters']:
        if c['chapter_index'] not in wanted or c['id'] not in takes:continue
        t=takes[c['id']];src=ROOT/t['path'];sha=hashlib.sha256(src.read_bytes()).hexdigest()
        dest=ROOT/'exports/dialogue-inspection'/f"{c['id']}_{t['id']}_{sha[:10]}.json"
        if dest.exists():continue
        decoded=subprocess.run([str(ROOT/'tools/ffmpeg.exe'),'-v','error','-i',str(src),'-vn','-ac','1','-ar','16000','-f','f32le','pipe:1'],capture_output=True)
        assert decoded.returncode==0
        audio=np.frombuffer(decoded.stdout,dtype=np.float32)
        segments,info=model.transcribe(audio,language='en',beam_size=5,vad_filter=True,
            condition_on_previous_text=False,word_timestamps=False)
        transcript=[{'start':s.start,'end':s.end,'text':s.text.strip(),'avg_logprob':s.avg_logprob,'no_speech_prob':s.no_speech_prob} for s in segments]
        record={'chapter_id':c['id'],'take_id':t['id'],'source_sha256':sha,
            'method':'Local faster-whisper base.en CPU int8; no media upload. ASR observations need human interpretation, especially animal sounds/names/accents.',
            'segments':transcript,'text':' '.join(s['text'] for s in transcript)}
        dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
        print(c['id'],record['text'],flush=True)

if __name__=='__main__':main()
