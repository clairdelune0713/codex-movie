"""Tighten inspected near-miss/ferry failures; remove rejected flashback music."""
from pathlib import Path
# Reuse only the local director's function definitions, without its authoring run.
definitions=(Path(__file__).parent/'tighten_staging.py').read_text(encoding='utf-8').split('\ngrip=')[0]
exec(compile(definitions,'local_staging_functions','exec'))

revise(38,[3,5,6,8,17,54,56,60],
    '尖沙咀傍晚碼頭。下船出口左、登船入口右，兩路相隔十多米。第一鏡只有奶油蛋撻與林先生；阿晴栗棕阿華田尚在另一入口外，完全不在此鏡。兩犬尚未相遇。',
    [shot(0,8,'@林先生_深色眼鏡 隨下船人流由 @天星小輪_登船口與跳板 出來，右手握 @蛋撻_成年_導盲鞍項圈牽繩 的棕色鞍握柄，左手棕鬆繩；繞過 @天星碼頭_行李 往左出口。只有這一組人犬。','35mm左側下船通道中景，末端人流掠過。','船靠岸、腳步、金屬輕響，無对白無旁白。'),
     shot(8,16,'切右側往中環登船入口，只有 @阿晴 與 @阿華田_成年_橙色領巾項圈牽繩；犬聽金屬碰撞望船，不看見蛋撻。遊客擋遠側出口，阿晴帶犬入閘上船。林先生蛋撻完全不在此鏡。','40mm右側登船通道中景，視線朝船不是另一隻犬。','人流腳步、金屬碰響與海水，無对白。'),
     shot(16,24,'左出口跟拍只看林先生與奶油蛋撻離開碼頭。右側閘口已關，船員收跳板；阿晴阿華田已在船內不再出現。結尾保持走向出口，沒有犬的互嗅或回頭認人。','40mm左出口後側中景；兩路維持十多米，不拍兩對近距離同框。','腳步、閘門與跳板聲、遠引擎；無对白。')],
    '兩犬至少十多米相隔，整段不對望、不相認、不嗅、不碰鼻。第一與第三鏡只有Lam/Tart，第二鏡只有Ching/Tine；每鏡只有一犬。禁止四位主角站同一跳板或聚在一起。所有場景傍晚暮金，不提早入夜。')
revise(39,[5,8,37,54,59],
    '尖沙咀往中環下層船艙。阿晴坐木長椅畫面左，腳落绿色地板；阿華田只在她鞋旁地板右下方伏着，橙牽繩扣項圈在她手，狗身從不在木椅上。藍手機在阿晴另一手。窗右是暮金海面。',
    [shot(0,22,'@阿晴 收到 @阿晴_手機_藍色保護殼 震動，播放美姐語音；她低頭看脚旁地板上的 @阿華田_成年_橙色領巾項圈牽繩，說搭來回；收手機並看窗外。犬在地上伏着，再地上坐起看窗光，從不跳上椅。','40mm一段連續中遠景，同時看阿晴椅座、雙腳、绿色地板與犬全身；不裁掉地板。','1-12s 美姐電話 {陳伯頭先仲同我講緊張相。講到食飯都未講完。下次你得閒，再聽佢講。}；12-20s阿晴 {你識揀位坐喎。搭個來回，返尖沙咀再行陣。}；20-22s引擎海浪。')],
    '木椅上只能坐阿晴。阿華田四腳及身體一直在绿色船艙地板，位於她鞋旁，不坐人座、不伏木椅、不佔另一椅位。只有一位阿晴、一隻栗棕犬。')
revise(43,[2,5,6,8,15,35,55,56,60],
    '夜間尖沙咀返程下船出口，阿晴與栗棕阿華田剛下船；同一海旁長椅在遠方，林先生一直坐在長椅左端，奶油蛋撻無鞍在他脚前，折好的棕鞍在左側椅面。不能是空長椅。',
    [shot(0,6,'@阿晴 與 @阿華田_成年_橙色領巾項圈牽繩 從 @天星小輪_登船口與跳板 走出尖沙咀返程出口，保持橙鬆繩，朝海旁行。只有這一組近景主角。','35mm下船側後跟拍，先完整交代出口方向。','船岸腳步、海浪、夜間遠小輪引擎；無对白。'),
     shot(6,12,'跟拍阿晴與阿華田沿海旁靠近 @場10_11_12_尖沙咀海旁_長椅_夜；遠景明確看見 @林先生_深色眼鏡 仍左座，@蛋撻_成年_休息_項圈與牽繩 在他鞋前伏地，@蛋撻_棕色皮革導盲鞍_佩戴與卸下 折好左側椅面。阿晴與栗棕犬仍距十米，未打招呼；停在此狀態接第10場。','40mm後側中遠景，遠椅有人犬而非空椅；兩組暫不接觸。','腳步、微風與海聲，無对白。')],
    '林先生從未離開這張長椅，不能消失、站起走開或重返碼頭。蛋撻已卸鞍但棕項圈與棕繩仍扣好且在林先生手。阿晴阿華田只步行靠近，見面嗅聞留給下一場。')
revise(50,[1,4,10,11,18,19],
    '澳洲Victoria同一犬舍門。奶油Baby Tart坐草地左看工作人員手中舊皮球；栗棕Baby Tine從右跑來，右臀心形小毛斑，兩犬完全沒有成年裝備。這是幼犬回憶，暖心3D動畫。',
    [shot(0,8,'@阿華田_幼犬_Baby_Tine 從右跑來剎不住，碰歪空 @幼犬_金屬碗，碗在草地傾倒有金屬聲。@蛋撻_幼犬_Baby_Tart 轉頭看它，Baby Tine停面前搖尾，四腳不浮空。','35mm低機位連續幼犬中景，碗與小脚接觸可讀。','只有草風、幼犬脚步、金屬碗輕碰。沒有音樂、沒有旋律、沒有唱歌、沒有对白。'),
     shot(8,16,'工作人員手只入鏡把 @幼犬_舊皮球 輕滾草地，兩幼犬追幾步；奶油Tart先到，栗棕Tine貼在旁擠一下，保持軟毛、厚小腳與幼犬比例。最後兩犬留球旁，不新增成犬或人物臉。','40mm幼犬側向跟移到球旁，末秒穩住。','只有皮球滾草、幼犬腳步與呼吸；完全無配樂、無哼唱、無任何電影音樂、無对白。')],
    '全段聲音只有環境與動作，任何音樂都禁止。狗不能說話或唱歌。幼犬無領巾無鞍；奶油犬無心形，栗棕犬右臀心形；舊皮球與金屬碗嚴格用原設計。')

# The inspected solo bench take already has correct blocking. Restore the exact
# original prompt/bindings rather than falsely stamping old media with a new hash.
j=read(ROOT/'exports/task-journal.json')
t=j['takes']['chapter_041'];c=v['chapters'][40]
c['prompt']=t['prompt'];c['linked_asset_ids']=[b['asset_id'] for b in t['bindings']]
c['tagged_assets']=[b['tag'] for b in t['bindings']]
(ROOT/'chapters'/c['id']/'prompt.txt').write_text(c['prompt'],encoding='utf-8')
c['revision_reason']='Inspected original take already preserves solo bench blocking; restore exact submitted prompt and original approved bindings'
save(ROOT/'proposal-ferry-repairs.json',v)
print(helper.save(ROOT,p,v,'Repair ferry near-miss, floor position and occupied bench; retry flashback with Foley only; retain faithful solo bench take'))
