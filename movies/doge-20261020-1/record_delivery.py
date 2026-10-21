"""Record the inspected verified final master in canonical project history."""
import json,sys
from render_finale import ROOT,read,save,now
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper
p=read(ROOT/'project.json');q=json.loads(json.dumps(p));v=read(ROOT/'exports/final-verification.json');audio=read(ROOT/'exports/audio-mastering.json')
assert v['technical']['duration']==305 and v['decoded_frames']==7320 and v['full_decode_verified'] and audio['video_stream_identical']
v['export_visual_inspection']='inspected';v['inspected_at']=now();v['inspection_notes']='All selected source scenes inspected across real frame sheets; final picture master inspected across scene midpoints and targeted transformed shots/captions/graphics/ending. Audio-mastered delivery retains identical verified video packet hash; mastered-export key frames inspected. No generated scenes1-36. Minor incidental cartoon shape/dressing variations remain; spoken dialogue not independently transcribed.';save(ROOT/'exports/final-verification.json',v)
q['stage']='delivered';q['render_status']='complete';q['finale_delivery']={'path':v['path'],'sha256':v['sha256'],'source_scenes':[37,51],'duration_seconds':305,'requested_resolution':'480p','native_dimensions':[992,432],'display_aspect_ratio':'21:9','fps':24,'decoded_frames':7320,'audio':'48kHz stereo AAC, mastered approximately-18LUFS','verification_path':'exports/final-verification.json','assembly_manifest':'exports/finale-assembly-manifest.json','delivered_at':now(),'all_selected_takes_current':True,'all_selected_takes_inspected':True,'earlier_scenes_generated':False}
print(helper.save(ROOT,p,q,'Deliver verified scenes37-51 master:305s, native480p,21:9 display,24fps and mastered stereo audio'))
