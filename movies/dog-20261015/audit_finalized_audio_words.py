"""Local word timing evidence for reusing the finalized Cantonese performance."""
import json
import check_dialogue as a
snapshots=a.AUDIT_TOOLS/'asr-models/models--Systran--faster-whisper-large-v3/snapshots'
model_dir=next(d for d in snapshots.iterdir() if (d/'model.bin').is_file())
model=a.WhisperModel(str(model_dir),device='cuda',compute_type='float16',local_files_only=True)
out={}
for cid in ['s14_c02','s16_c04','s16_c06']:
 source=a.ROOT.parent/('dog-20261014/chapters/'+cid+'/takes/take_01.mp4')
 r=a.subprocess.run([str(a.FF),'-v','error','-i',str(source),'-vn','-ac','1','-ar','16000','-f','f32le','pipe:1'],capture_output=True,check=True)
 audio=a.np.frombuffer(r.stdout,dtype=a.np.float32)
 segments,info=model.transcribe(audio,language='yue',beam_size=5,vad_filter=True,word_timestamps=True,condition_on_previous_text=False)
 out[cid]=[{'start':s.start,'end':s.end,'text':s.text,'words':[{'word':w.word,'start':w.start,'end':w.end} for w in s.words]} for s in segments]
 print(cid,json.dumps(out[cid],ensure_ascii=False),flush=True)
(a.ROOT/'exports/finalized_cantonese_word_timing.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
