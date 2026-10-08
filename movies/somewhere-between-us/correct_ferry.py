"""A bounded continuity correction, committed through the Movi2 helper."""
import importlib.util,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('h','C:/Users/admina/.codex/skills/movi2/scripts/project.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
p=h.read(ROOT/'project.json');q=json.loads(json.dumps(p));c=q['chapters'][16]
c['scene_summary']='阿華田與領犬員獨自坐小輪離岸；空碼頭承接前章已離開的蛋撻，兩犬仍未相遇。'
actions=['@Tine 與 @Handler 在小輪船艙入口安穩坐下，鬆牽繩清晰。画面只有一隻焦糖棕色成年犬與一位珊瑚外套女性。','由小輪船窗望向空碼頭，岸線向右退後。鏡頭內沒有任何人或狗，海水與欄杆保持真實離岸視差。','硬切岸上的空長椅，遠景小輪離開，風輕輕吹過。整個碼頭空無人犬，保持未相遇的期待。']
c['tagged_assets']=['@Tine','@Handler','@pier']
audio=['船機低鳴與犬呼吸','海浪與船身震動','海風、远處船機逐漸消失']
for s,action,sound in zip(c['shots'],actions,audio):
    s.update(action=action,audio=sound,end_state=action+' 最後一秒保持自然穩定剪接狀態。')
c['handoff']={'in':actions[0],'out':c['shots'][-1]['end_state']}
old=c['prompt']
refs=old.split('ACTIVE REFERENCES\n')[1].split('\nLOCATION MAP')[0]
refs='\n'.join(line for line in refs.splitlines() if not line.startswith(('@Tart：','@Owner：')))
timing='\n'.join(f"Shot {i+1} ({s['start']}s-{s['end']}s): {s['action']}\n鏡頭：{s['camera']}。聲音：{s['audio']}。結束：{s['end_state']}"+(' Hard cut.' if i<2 else '') for i,s in enumerate(c['shots']))
c['prompt']=f'''SCENE CONTEXT
{c['scene_summary']}
本章是600秒電影中的第17段，電影絕對時間320-340秒。
OUTPUT SETTINGS
20秒，原生720p，21:9。三個6秒、7秒、7秒鏡頭，明確hard cut。
GLOBAL STYLE
溫暖圓潤的原創高品質3D動畫，柔毛、表情眼神、柔和光線與有質感的服飾。真實成年犬比例。
ACTIVE REFERENCES
{refs}
LOCATION MAP
@pier 為右側候船門與後景小輪泊位。前章另一組人犬已離開，這章岸上不出現任何人犬。
FIRST FRAME AND SPATIAL BLOCKING
直接開始船艙中的 @Tine 與 @Handler，只有一隻棕犬及一位女性。
ACTION TIMING
{timing}
OPTICS AND CAMERA
自然視差與重量，鏡頭轉換只在明確剪輯；不複製參考多視角排版。最後兩鏡只拍空間。
PHYSICS
四爪有重量，鬆牽繩接觸正確；犬自然眨眼呼吸，不說話，不具人手。
LIGHTING
左側蜜金日光，柔和動畫反射光，白天小輪與海港。
AUDIO
只有原創自然環境聲、船機、海浪、海風、犬呼吸。無背景音樂、無人類或犬台詞。
CONTINUITY LOCKS
本章只出現一隻焦糖棕色 @Tine 與一位 @Handler。犬橙色灰邊背心與右後臀淡心形斑穩定；不出現米金犬、男性或額外犬。岸上完全空。兩犬重逢發生於後續夜晚，不在小輪。
POSITIVE CONSTRAINTS
完整20秒全屏角色與環境動畫，無字幕、片尾文字、姓名標籤、水印、白底圖格。最後留自然穩定剪接姿態。'''
c['audio']='Ferry departure ambience only. No dialogue or music.'
result=h.save(ROOT,p,q,'Correct ferry near miss: only Tine and handler on boat; Tart remains off-screen until reunion')
print(json.dumps({'revision':result['revision'],'chapter':c['id'],'refs':c['tagged_assets']}))
