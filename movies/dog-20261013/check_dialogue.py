"""Local-only Cantonese ASR audit. No movie audio leaves this computer."""
import argparse
import hashlib
import json
import os
import re
import sys
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'tools/asr-deps'))
os.environ['HF_HOME']=str(ROOT/'tools/asr-models')
os.environ['HF_HUB_DISABLE_TELEMETRY']='1'
os.environ['HF_HUB_DISABLE_PROGRESS_BARS']='1'
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING']='1'
# Use the existing NVIDIA runtime DLLs, without modifying machine PATH/settings.
handles=[]
for d in [Path('C:/pinokio/bin/miniforge/Library/bin')]:
    if d.exists():
        handles.append(os.add_dll_directory(str(d)))
        os.environ['PATH']=str(d)+os.pathsep+os.environ['PATH']
from faster_whisper import WhisperModel
import numpy as np
FF=next((ROOT/'tools/python-deps/imageio_ffmpeg/binaries').glob('ffmpeg*.exe'))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--chapters',default='all');args=ap.parse_args()
    p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
    j=json.loads((ROOT/'exports/task-journal.json').read_text(encoding='utf-8'))
    chosen=p['chapters'] if args.chapters=='all' else [p['chapters'][int(n)-1] for n in args.chapters.split(',')]
    print('Loading local large-v3 Cantonese speech audit model; first use downloads public weights.',flush=True)
    model=WhisperModel('large-v3',device='cuda',compute_type='float16',download_root=str(ROOT/'tools/asr-models'))
    folder=ROOT/'exports/dialogue-audit';folder.mkdir(parents=True,exist_ok=True)
    for c in chosen:
        t=j['takes'].get(c['id'])
        if not t or t['status']!='succeeded':continue
        dest=folder/f"{c['id']}_{t['id']}.json"
        if dest.exists():continue
        source=ROOT/t['path'];digest=hashlib.sha256(source.read_bytes()).hexdigest()
        decoded=subprocess.run([str(FF),'-v','error','-i',str(source),'-vn','-ac','1','-ar','16000','-f','f32le','pipe:1'],capture_output=True,check=True)
        audio=np.frombuffer(decoded.stdout,dtype=np.float32)
        lang='en' if c['id']=='chapter_002' else 'yue'
        hint='Australian English.' if lang=='en' else '香港粵語，繁體中文。'
        segments,info=model.transcribe(audio,language=lang,beam_size=5,
            vad_filter=True,condition_on_previous_text=False,initial_prompt=hint)
        actual=[{'start':s.start,'end':s.end,'text':s.text,'avg_logprob':s.avg_logprob,'no_speech_prob':s.no_speech_prob} for s in segments]
        expected=re.findall(r'\{([^{}]+)\}',t['prompt'])
        dest.write_text(json.dumps({'chapter_id':c['id'],'take_id':t['id'],'source_sha256':digest,
            'asr_model':'Whisper large-v3 via faster-whisper, local CUDA','language':lang,
            'expected_lines':expected,'actual_segments':actual,'inspected':False,
            'limitation':'ASR is evidence for review, not proof of verbatim speech or speaker identity.'},ensure_ascii=False,indent=2),encoding='utf-8')
        print(c['id'],t['id'],'expected:', ' / '.join(expected),'heard:', ''.join(s['text'] for s in actual),flush=True)

if __name__=='__main__':main()
