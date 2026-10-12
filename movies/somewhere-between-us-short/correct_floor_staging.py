"""Fix a demonstrated table-placement error without changing approved assets."""
import copy, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('h','C:/Users/admina/.codex/skills/movi2/scripts/project.py')
h=importlib.util.module_from_spec(s);s.loader.exec_module(h)
p=h.read(ROOT/'project.json');q=copy.deepcopy(p);c=q['chapters'][8]
lock='''FLOOR AND FURNITURE LOCK
@Tine 全身在木椅左前方的地板瓷磚上，絕不在桌子、椅子、沙發、檯面或老人膝上。鏡頭前景只見瓷磚，沒有桌面。@Elder 坐在椅上，兩腳踏地，椅子座面離地約0.45米。犬頭伏在地板上，頭比老人膝低，老人必須垂眼才能看見牠。維持成年拉布拉多正常比例，不為同框把狗放大。最少一個前景爪、鼻子、瓷磚接觸點全程可見。家具從來不支持犬身。攝影機置於距地板0.25米，取兩者的低機位中景，狗在畫左下角，老人臉在右上。
'''
c['prompt']=c['prompt'].replace('LOCATION MAP\n','LOCATION MAP\n'+lock)
c['prompt']=c['prompt'].replace('Tine在他左前方一臂外','Tine在他左前方地板上、一臂外')
c['prompt']=c['prompt'].replace('50mm雙主體中景，犬眼高度，鎖定單一鏡頭','50mm雙主體中景，距地板0.25米，瓷磚前景可見，鎖定單一鏡頭')
c['shots'][0]['camera']='50mm雙主體中景，距地板0.25米，瓷磚前景可見，鎖定單一鏡頭'
c['quality_correction']='First take placed the adult dog on a table. Replacement locks normal dog scale, floor contact, low camera and seated elder eyeline.'
errors,warnings=h.validate(ROOT,q);assert not errors,errors
assert h.review_state(ROOT,q)['ready']
print(h.save(ROOT,p,q,'Correct chapter 9 demonstrated table-placement error using explicit floor contact and scale'))
(ROOT/'chapters/chapter_09/prompt-v02.txt').write_text(c['prompt'],encoding='utf-8')
