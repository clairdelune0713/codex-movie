"""Unforced multilingual transcription of finished scene audio; no media upload."""
import hashlib,json,os,re,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'tools/asr-runtime'))
os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN']='1'
os.environ['HF_HUB_DISABLE_TELEMETRY']='1'
from faster_whisper import WhisperModel
import numpy as np


def transcribe(model,audio):
    segments,info=model.transcribe(audio,language=None,task='transcribe',beam_size=5,
                                  vad_filter=True,condition_on_previous_text=False)
    records=[{'start':s.start,'end':s.end,'text':s.text.strip(),
              'avg_logprob':s.avg_logprob,'no_speech_prob':s.no_speech_prob} for s in segments]
    return {'language':info.language,'language_probability':info.language_probability,
            'top_languages':sorted(info.all_language_probs or [],key=lambda x:x[1],reverse=True)[:4],
            'text':' '.join(s['text'] for s in records),'segments':records}


def main():
    model=WhisperModel(str(ROOT/'tools/asr-model-base-multilingual'),device='cpu',
                       compute_type='int8',cpu_threads=4,num_workers=1,local_files_only=True)
    manifest=json.loads((ROOT/'exports/whole-movie-refresh-20261021-v06-manifest.json').read_text(encoding='utf-8'))
    folder=ROOT/'exports/language-inspection-refresh-20261021';folder.mkdir(exist_ok=True)
    results=[]
    for chapter,spec in zip(manifest['chapters'][36:],manifest['normalized_inputs'][36:]):
        source=ROOT/spec['path'];digest=hashlib.sha256(source.read_bytes()).hexdigest()
        target=folder/f'{chapter["chapter_id"]}_{digest[:10]}.json'
        if target.exists():
            record=json.loads(target.read_text(encoding='utf-8'))
        else:
            decoded=subprocess.run([str(ROOT/'tools/ffmpeg.exe'),'-v','error','-i',str(source),
                                    '-vn','-ac','1','-ar','16000','-f','f32le','pipe:1'],capture_output=True)
            assert decoded.returncode==0
            audio=np.frombuffer(decoded.stdout,dtype=np.float32)
            whole=transcribe(model,audio)
            windows=[]
            for start in np.arange(0,max(0,chapter['duration']-1.4),4.5):
                end=min(start+5.5,chapter['duration'])
                window=transcribe(model,audio[int(start*16000):int(end*16000)])
                window.update(start=float(start),end=float(end));windows.append(window)
            flagged=[w for w in windows if w['text'] and (
                (w['language']!='en' and w['language_probability']>=.5) or re.search(r'[\u3400-\u9fff]',w['text']))]
            record={'scene':chapter['scene'],'chapter_id':chapter['chapter_id'],
                    'source_path':spec['path'],'source_sha256':digest,'whole_scene':whole,
                    'windows':windows,'flagged_windows':flagged,
                    'method':'Local multilingual Whisper base CPU int8. Language auto-detected without forcing English or translating; whole scene plus overlapping 5.5-second windows. Movie audio never uploaded.',
                    'limitation':'ASR can misclassify music, short cries, laughter, animal calls and accented words. Flags require interpretation; detection is not proof of perfect language or word accuracy.'}
            target.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
        results.append({'scene':record['scene'],'path':target.relative_to(ROOT).as_posix(),
                        'language':record['whole_scene']['language'],
                        'probability':record['whole_scene']['language_probability'],
                        'flagged_windows':record['flagged_windows']})
        print('SCENE',record['scene'],record['whole_scene']['language'],round(record['whole_scene']['language_probability'],3),record['whole_scene']['text'],flush=True)
        for w in record['flagged_windows']:
            print('  REVIEW',w['start'],w['end'],w['language'],round(w['language_probability'],3),w['text'],flush=True)
    (folder/'index.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')


if __name__=='__main__':main()
