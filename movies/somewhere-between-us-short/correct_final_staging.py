import copy, importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('h','C:/Users/admina/.codex/skills/movi2/scripts/project.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
p=h.read(ROOT/'project.json');q=copy.deepcopy(p)
c=q['chapters'][15]
assert c['id']=='chapter_16'
old=c['shots']
new=[
 {'start':0,'end':6,'action':'@Tine 與 @Handler 在渡輪碼頭左前景，朝陸地方向走。@Tart 穿橙背心外的黑導盲鞍，帶 @Owner 在右後景、至少十二米外朝船舷走。人流在兩組之間穿過。兩犬始終背向或側向彼此，絕不相望、絕不並肩。','camera':'28mm碼頭固定廣角全景；兩組在画面兩端，無中途拉近','audio':'渡輪低引擎、腳步、海風；只有環境聲，沒有音樂或人聲','end_state':'Tart與主人被右側人流遮住；Tine仍在左側'},
 {'start':6,'end':12,'action':'只拍 @Tine 和 @Handler 在左側出口。Tine聽到船的引擎，稍轉頭看船，隨領犬員離開。成年米金Tart與主人完全在鏡頭外，不在Tine身旁或背景。','camera':'50mm只包含棕犬、領犬員下身及遠處船身的側面中景','audio':'接續同一渡輪低引擎、海風與腳步；無音樂，無人聲','end_state':'棕犬跟領犬員離開，牠們沒有見到另一組'}]
for before,after in zip(old,new):
 for key in ('action','camera','audio','end_state'):c['prompt']=c['prompt'].replace(before[key],after[key])
c['shots']=new
c['prompt']=c['prompt'].replace('Shot 1 (0s-5s)', 'Shot 1 (0s-6s)').replace('Shot 2 (5s-12s)', 'Shot 2 (6s-12s)')
c['prompt']+='\nFERRY NEAR-MISS LOCK: The dogs do not meet in this chapter. In shot 1 the two pairs stay at least twelve meters apart with intervening people; Tart wears the black working harness over his vest. In shot 2 only ONE brown adult dog and his female handler are visible. No beige dog in this close shot. No shared portrait, no nose touch, no reunion. Ambience only, no speech and no music.\n'
c=q['chapters'][26]
assert c['id']=='chapter_27'
c['prompt']+='\nPUPPY MARKING AND FRAMING: BabyTine has a pale heart only on his anatomical RIGHT REAR HAUNCH, behind the hip, never on shoulder, chest, ribs or upper back. Stage his right hindquarter away from camera. After the running shot, frame ONLY the two puppy faces, necks and front paws; their hindquarters are outside the frame. Thus no heart marking is visible in the close shot. BabyTart remains beige without any heart.\n'
c['shots'][-1]['camera']='65mm緊密雙幼犬頭頸和前爪近景；後臀完全出畫，Tine右後臀背向鏡頭，近景無可見心形斑'
c=q['chapters'][27]
assert c['id']=='chapter_28'
c['prompt']=c['prompt'].replace('兩幼犬聽到不同方向的畫外無語口哨','兩幼犬望向不同方向，聽到畫外草步')
c['prompt']=c['prompt'].replace('兩個不同方向低口哨、草步；原創鋼琴稍分開','兩個不同方向草步、柔和草風；沒有音樂、沒有口哨、沒有人聲')
c['prompt']=c['prompt'].replace('草風直接切海風；原創鋼琴主題重新合在一起','草風直接切海風、犬腳步、遠處船引擎；没有音樂、沒有人聲')
for shot in c['shots']:
 shot['action']=shot['action'].replace('兩幼犬聽到不同方向的畫外無語口哨','兩幼犬望向不同方向，聽到畫外草步')
c['shots'][0]['audio']='兩個不同方向草步、柔和草風；沒有音樂、沒有口哨、沒有人聲'
c['shots'][1]['audio']='草風直接切海風、犬腳步、遠處船引擎；没有音樂、沒有人聲'
c['prompt']+='\nAUDIO FOR THIS ENTIRE CHAPTER: Natural grass rustle, footsteps, dog breathing, then sea breeze and a distant boat engine only. No score, music, melody, singing, whistling, spoken words, narration or existing recorded audio.\n'
result=h.save(ROOT,p,q,'Correct ferry near-miss separation and puppy marking; replace rejected flashback audio with natural ambience')
print(result)
