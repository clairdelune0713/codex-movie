"""Finalize approved-asset cinematic prompts, without rewriting screenplay dialogue."""
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
HELPER=Path('C:/Users/Admin 3/.codex/skills/movi2/scripts/project.py')
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
assert p['asset_review']['status']=='approved'
assets={int(a['id'].split('_')[1]):a for a in p['asset_list']}
specs=[]
def add(refs, first, action, lines='', camera='穩定的35mm中景與自然小幅移動；以角色行動帶動畫面', duration=None):
    specs.append(dict(refs=refs,first=first,action=action,lines=lines.split('\n') if lines else [],camera=camera,duration=duration))

# Scene 1. Do not reveal either puppy before the scripted later memory.
add([10,11,19],'低機位朝犬舍草地，近景露珠、遠景門口。','清晨風掠草葉；露珠發亮；遠處傳來金屬碗輕碰，工作人員靴子由右至左走過。幼犬仍在門後。',camera='50mm草葉近景，慢移焦到遠景靴子；低機位')
add([10,18,19],'同一犬舍門口，靴子停在門側，舊皮球仍在門內。','門向內開；不見門後幼犬，只聞幼犬叫聲與脚步；舊皮球滾出停草地，工作人員彎腰拾球。','工作人員（畫外英語）|Coming?',camera='35mm門檻低機位，跟隨球短移；球停下後穩定')
add([11,12,56,60],'風吹草葉的暖光，動態匹配下一鏡維港波光。','前6秒草葉被風吹，風聲接上海浪。Hard cut. 後10秒海面晨光，碼頭工人拉緊纜繩，閘門開第一批乘客走入；不加地名文字。',camera='50mm草地轉35mm港灣中遠景；光與聲音匹配剪接')
add([12,57,60],'綠奶油小輪已準備離岸，船岸間距逐步增加。','前6秒小輪慢慢離岸、纜繩收妥。Hard cut. 後8秒清晨下層船艙乘客打開早餐紙袋、另一乘客靠窗補眠，城市醒來；直接接下一場，不出片名。',camera='35mm外觀轉40mm船艙暖光中景')

# Scene 2.
add([2,6,27,28,30,31,32,33],'林先生在暖色小廚房桌旁，桌左水煲右杯，抽屜固定位置；休息蛋撻在右下方。','水煲跳掣；林先生沿桌摸到杯柄放固定位置；摸收音機轉小音量，從固定抽屜取卡套指腹確認，連卡放胸袋；此時不見卡面資料。','林先生|你張卡帶齊。鎖匙……喺度。',camera='40mm桌旁三分之四中景，手與道具近景切入')
add([2,3,6,29,30,35],'門旁林先生收鎖匙、折白手杖入側袋，握棕色牽繩；蛋撻坐起。','摸肩背，穿整副棕色導盲鞍，先扣胸帶再腹帶，觸摸金屬扣鉚釘確認；把銀把手提起、棕握柄在手，Click。蛋撻由休息裝備過渡工作裝備，不換狗。','林先生|頭先叫你起身就聽唔到。出街就咁精神？\n林先生|好，蛋撻。返工。',camera='50mm手與肩背動作近景，動作完整有順序')
add([3,6,36],'住宅走廊升降機前，鄰居推購物車卡在開門門檻；林先生和蛋撻左側等待。','蛋撻在購物車前停穩，林先生不催促；鄰居把車輪拉正，車退出門邊後兩者入升降機。','鄰居|等陣呀，架車唔知做乜——\n鄰居|得喇，唔好意思。\n林先生|唔緊要，慢慢嚟。',camera='35mm門檻與全身中景，保持阻擋與清空狀態可見')
add([3,6],'升降機內林先生站左、蛋撻近腳，右邊小朋友好奇望狗。','小朋友手伸到一半，聽林先生說狗工作便收手；向蛋撻道早晨，林先生温暖微笑。','小朋友|可唔可以摸吓佢？\n林先生|佢而家做緊嘢。等佢放工先，好唔好？\n小朋友|咁……早晨，蛋撻。\n林先生|呢個可以。',camera='40mm三分之四中景，視線保持狗與孩童之間')
add([3,6,16],'住宅門外右側貨物箱阻部分路，蛋撻在林先生左前方，向畫面左行。','蛋撻自然繞過箱子再走到熟悉街口，林先生微抬頭聞麵包香，不直視物品。','林先生|今日間麵包舖咁早開爐。',camera='35mm側向跟拍，繞箱後保持左行')

# Scene 3.
add([5,8,13,39,41],'社區中心玻璃入口阿晴左、阿華田右，橙繩扣項圈而非領巾。','阿華田看倒影停一下、挪一步倒影同步；阿晴等牠回神不拉扯；美姐門內呼喚，尾巴立即搖，進門。','阿晴|係你嚟㗎。日日都要認一次？\n美姐（門內）|阿華田！',camera='40mm玻璃側視；倒影是真實鏡像而非另一隻狗')
add([5,7,8,13],'社區中心桌椅中間通道，阿晴與阿華田停桌旁，長者甲乙分坐兩侧。','長者轉椅輪候，互相打趣，阿晴讓阿華田安定再逐一接觸；眾人自然笑。','長者甲|今日到我先，上次你淨係掛住隔籬嗰個。\n長者乙|因為你講嘢太長氣呀。\n阿晴|一個一個嚟，佢先知望邊個。',camera='35mm群體中景，輕橫移看甲乙反應')
add([5,8,13],'婆婆桌側，阿華田在阿晴身旁停穩，婆婆手緊握在膝上。','婆婆慢慢伸手；阿華田先觀察再頭靠近掌心；手指逐漸放鬆，婆婆微笑、輕摸毛；阿晴保持鬆繩不催。',camera='65mm手與犬頭近景，接婆婆柔和反應，最後呼吸小動作')
add([5,8,13],'小女孩在婆婆椅背後，阿華田仍在鬆繩範圍，尾巴靠近椅腳。','女孩保持可選距離觀察，阿晴蹲低陪她；女孩看尾巴，尾巴自然拍椅腳嗒嗒嗒，長者講風扇笑話。','小女孩|佢會唔會舔我？\n阿晴|我陪住你。你想離遠睇都得。\n小女孩|佢條尾冇停過。\n長者甲|開咗風扇咁。',camera='50mm女孩視點與犬尾中近景')
add([5,9,13,42],'相同活動室，窗口在畫面右，陳伯靠窗背向群體，報紙在手。','前景大家笑聲自然漸低；阿華田轉頭望窗邊；陳伯只把報紙折整齊，不望過來；鏡頭看見距離與安靜。',camera='50mm阿華田視線接70mm窗邊陳伯，緩慢移焦')

# Scene 4.
add([3,6],'上午窄行人路，圍欄左、牆右、前方人停走；林先生與蛋撻往左前行。','蛋撻減速帶林先生在欄牆間通過，後方途人準備擠，見導盲鞍改走另一邊；熟悉店收音機聲傳來，林先生停店門。','途人|借借——\n林先生|阿強，今日有冇位？',camera='35mm側前向跟拍，明確留出人犬通道')
add([3,6,34,47],'茶餐廳窗口在右、店門左，林先生入門蛋撻在左前方；早餐桌靠窗。','阿強拉椅讓通道，林先生坐下，蛋撻伏桌下保持鞍；两人說早餐笑話。','阿強|有。你個朋友又未到呀？\n林先生|今日冇約佢。畀自己食餐準時嘅早餐。',camera='40mm桌旁中景到低機位桌下犬，保持窗位')
add([3,6,34],'同桌下蛋撻已伏下，旁桌孩子掉一小塊多士到牠鼻前。','多士落地，蛋撻鼻子動一下仍不起；孩子彎腰想推食物，阿強先拾起；林先生聽出發生何事道謝。','阿強（輕聲）|佢做緊嘢，唔好餵佢。\n林先生|多謝。',camera='65mm低機位犬鼻與多士，再切40mm阿強與林先生')
add([3,5,6,8,46,47],'從茶餐廳同一窗口看近側道路，巴士向左停靠遮窗；阿華田與阿晴在外側人行道。','黃色雙層巴士遮住窗外兩者；阿華田被風吹葉吸引停，阿晴等；窗內蛋撻面朝另一邊，彼此未看見；巴士開始向左離開。',camera='50mm固定窗内視點；左行車輛與窗外人物地理清晰')
add([3,6,34,46,47],'巴士左行離畫，阿晴阿華田亦已走遠；林先生桌上接過早餐。','早餐放桌、熱氣升起，林先生朝蛋撻說香；蛋撻仍安靜伏下工作。結尾用溫暖小反應，不令犬去吃多士。','林先生|蛋撻，今日好香喎。',camera='50mm林先生與早餐轉65mm桌下蛋撻安靜眨眼')

# Scene 5.
add([5,8,9,13,42],'活動後房間安靜，陳伯靠右窗口，阿晴與阿華田遠側通道。','陳伯抬報紙拒絕，阿晴停在有距離位置答應，坐另一椅留通道；阿華田站一下再伏，不接近陳伯。','陳伯|唔使過嚟。我唔鍾意狗。\n阿晴|好。我哋喺呢邊坐陣，唔過嚟。',camera='40mm两區域同框，尊重距離')
add([5,8,9,13,38,40,42],'阿晴椅旁地上展開水碗，陳伯仍隔通道讀報。','阿晴開水瓶倒水，阿華田喝幾口重新伏下呼吸；陳伯從報紙上方看一下；窗風吹報翻頁他壓回。水碗位置固定。',camera='65mm倒水犬喝水插入，50mm陳伯視線反應')
add([5,8,9,13,42],'阿華田下巴前腳上，阿晴不催，陳伯報紙漸放低。','對話在安靜房間自然進行，陳伯像想反駁卻收住；阿華田換舒適姿勢；陳伯終於問名字，手放膝旁。','陳伯|佢唔使周圍走㗎？\n阿晴|頭先見咗好多人，佢都要休息。\n陳伯|咁都叫返工？\n阿晴|識得休息，都幾重要。\n陳伯|佢叫咩話？\n阿晴|阿華田。\n陳伯|狗都叫阿華田。\n阿晴|所以個個都記得佢。',camera='50mm兩人過肩反打，阿華田偶爾近景')
add([5,7,8,9,13],'陳伯手在膝邊，阿晴先問；犬尚未跨通道。','陳伯遲疑後點頭，阿晴引導阿華田近一點停，陳伯先伸手指碰頭停一下才摸；美姐遠側提醒，不打斷接觸。','阿晴|想摸吓佢？\n美姐（遠處）|阿晴，差唔多喇。',camera='65mm手指接觸與毛髮受壓、陳伯面部小反應')
add([5,8,9,13,40,42],'阿晴收水碗準備離開，陳伯手慢慢收回。','陳伯問咁快走，阿晴答下星期；陳伯重新拿報紙却不舉遮臉，望狗離開。','陳伯|……咁快就走？\n阿晴|下星期再嚟。',camera='50mm固定窗側中景，留出望門口的眼線')

# Scene 6, three complete comic near-miss vignettes and the chair setup.
add([3,6,42],'第一個早上站外報紙檔，老闆低頭摺報，林先生蛋撻向左經過。','老闆只見餘光先誤叫名字，再看見奶油色糾正；林先生早餐笑話令老闆笑，道別前行。','報紙檔老闆|阿華田！今日咁早？\n林先生|呢個蛋撻。\n報紙檔老闆|啊，淺色嗰隻係蛋撻。我又叫錯名。\n林先生|你係咪未食早餐？',camera='40mm檔口固定中景與蛋撻色澤清楚')
add([5,8,42],'另一天相同報紙檔視角，阿晴與栗棕阿華田經過。','老闆叫蛋撻，阿華田立即轉頭搖尾；阿晴糾正，再試叫靚仔犬再次回頭；阿晴笑，身分沒有交換。','報紙檔老闆|蛋撻！\n阿晴|阿華田先啱。啡色呢隻呀。\n報紙檔老闆|但係佢應我喎。\n阿晴|你叫靚仔，佢都會應。\n報紙檔老闆|靚仔？',camera='50mm檔主犬阿晴反應構圖，重複動作喜劇節奏')
add([3,5,6,8,48,49,50],'再一天站月台，銀列車紅門框在左，對面升降機右，站屏門與列車門對齊。','前8秒林先生蛋撻入車廂、提示聲、車門與屏門關。Hard cut. 後18秒對面升降機開阿晴阿華田出，列車向左移；犬透反光人影挪一步，阿晴停等，列車離去帶風。','阿晴|等下一班。',camera='35mm門邊中景轉50mm月台過肩，列車左行與屏門安全不跨越')
add([7,9,13,42,44],'一星期後同社區中心右窗椅，袋子在陳伯旁椅上，美姐整理椅。','陳伯望門口問星期，聽星期四點頭，把旁椅袋子移脚邊，空出位置，報紙留膝上。','陳伯|今日星期幾？\n美姐|星期四。',camera='50mm窗側中景，袋子手到地面動作完整')

# Scene 7. No heroic music; crossing happens only on the next cue.
add([3,6,14],'近側路緣林先生與蛋撻向橫向道路前行，黃過路線連近與對岸，對岸茶餐廳有碗聲。','林先生提遲到朋友茶無味微笑，停話留意車流；首輪行人提示響，蛋撻帶到路邊停，林先生確認方向。','林先生|今日唔知佢到咗未呢。上次杯茶飲到冇味，佢先出現。',camera='35mm中遠景交代過路線，50mm林先生聆聽')
add([3,6,14,51,52,53],'林先生蛋撻在近側路緣，銀客貨車擋黄過路線，深藍綠前車在其左前。','林先生叫向前，蛋撻保持原位不移。切前方阻擋，車只挪一點仍未清線；林先生不再催，聽周圍。','林先生|好，向前。\n林先生|蛋撻？',camera='50mm人犬中景轉35mm阻擋遠景，車頭向左')
add([3,6,14,51,52,53],'途人在林先生後右準備超前，客貨車還阻路。','途人說行得後看清阻擋停下；前車先左行，客貨車跟隨完全清線；這時行人提示聲改變，人犬仍在路緣不動。','途人|行得喇——\n途人|啊，等陣，前面仲有架車。',camera='40mm含路緣與車通道，動作前後順序不能互換')
add([3,6,14],'車已離開，人犬仍在同一路緣，普通車流掠過，途人也等。','林先生蹲低觸蛋撻肩背輕聲收到，再站穩握鞍；與途人聊茶可以再叫。完整等待一輪，有街流、人聲、無英雄音樂。','林先生|唔趕。等下一轉。\n林先生（輕聲）|收到。\n途人|頭先真係差啲睇唔到。\n林先生|等多個燈啫。杯茶凍咗，可以再叫。',camera='50mm路緣人物近中景與犬肩手接觸，固定軸線')
add([3,6,14],'下一輪行人提示才響，人犬仍路緣先聽後動，車道完全無阻。','重新確認後蛋撻帶林先生沿黃線由近岸過對岸；到安全位置摸背道好狗，轉向茶餐廳繼續前行。','林先生|好狗。',camera='35mm側向全身跟拍跨線，不穿車，對岸接50mm')

# Scene 8.
add([5,8,9,13,42,44],'同下午活動室，陳伯右窗、旁椅空位、袋脚邊，阿晴阿華田入口。','長者照常呼喚犬，但犬先停阿晴旁；陳伯輕叫名字再呢邊，阿晴帶犬靠近，陳伯摸額頭；名字古怪笑話。','陳伯|阿華田。\n陳伯|呢邊。\n阿晴|今日記得佢個名喇。\n陳伯|咁古怪，想唔記得都難。',camera='40mm入門視線到50mm窗側兩人犬')
add([5,8,9,13,43,44],'阿晴坐空椅，陳伯取舊相片，阿華田旁边安靜；相片必須用原圖。','相片近景年輕陳伯與唐狗阿黃，陳伯講全巷養狗與下雨到家；阿晴回應知他會開門。阿黃只有照片沒有新活體回憶。','陳伯|以前屋企嗰隻，叫阿黃。\n阿晴|你養㗎？\n陳伯|成條巷養嘅。邊間有飯食，就去邊間。\n陳伯|但係落雨，就淨係識嚟我屋企。\n阿晴|知你會開門。',camera='65mm手持舊照插入，50mm兩人溫暖中景')
add([5,7,8,9,13,43],'陳伯手停犬額頭片刻，相片拿近，美姐經過停在左邊。','妻子毛巾一句後留空氣，杯輕放聲與犬呼氣；美姐問年輕樣貌，陳伯幽默笑，兩人都笑，美姐不急離去。','陳伯|我太太會喺門口留條毛巾。\n美姐|呢個係你？好後生喎。\n陳伯|唔通一出世就咁老咩。',camera='65mm陳伯情緒微表情，50mm美姐中景，留自然停頓')
add([5,7,8,9,13,43,44],'美姐留窗側，陳伯轉相片給她，阿晴安靜聽，犬在兩椅間。','問以前住處，陳伯指相片談深水埗舊巷；視角慢移阿華田伏兩椅間，談話在犬頭頂延續，不另編明確對白。','美姐|以前住邊度？\n陳伯|深水埗。嗰條巷而家冇咗喇。嗱，呢度以前有間——',camera='50mm相片與人轉40mm低機位犬，輕緩移動')

# Scene 9, retain round-trip and elapsed time logic.
add([3,5,6,8,17,54,56,60],'尖沙咀暮色碼頭下船出口在左、往中環入口右；小輪靠岸，兩路線十多米相隔。','林先生蛋撻下船繞行李，阿晴阿華田走登船口；犬聽金屬看碼頭，遊客與乘客短遮；散開時前者已走出口，後者入閘，船員收跳板。',camera='35mm有地理深度的碼頭中遠景，兩路保持十多米不接觸')
add([5,8,37,54,59],'尖沙咀往中環下層船艙，阿晴木椅坐、阿華田脚邊，夕陽窗右，手機手內。','手機震動美姐語音，阿晴低頭對犬說來回路線；收手機，犬望晃動窗光，安靜同行。','美姐（電話）|陳伯頭先仲同我講緊張相。講到食飯都未講完。下次你得閒，再聽佢講。\n阿晴|你識揀位坐喎。搭個來回，返尖沙咀再行陣。',camera='50mm座椅中景，手持手機插入不顯新訊息字幕')
add([3,6,15,54,60],'尖沙咀海旁暮色，林先生與朋友并行，蛋撻導盲鞍仍穿，碼頭後景。','船鳴笛、海拍岸、遠處樂手調音；林先生叫聽、準時笑話，朋友笑搖頭道別分路。','林先生|聽吓。\n朋友|架架船都咁響，有咩特別？\n林先生|呢架唔同。呢架準時。\n朋友|仲記住我遲到。好喇，我行呢邊。你慢慢坐。\n林先生|下次早啲。',camera='40mm三分之四并行到固定分路構圖；將夜景板光改暮金')
add([2,3,6,15,35,45],'同一海旁長椅，林先生坐畫面左，蛋撻脚前站，完整鞍仍在身，右座空。','林先生坐下，棕牽繩持續在左手扣項圈；右手摸扣解胸腹帶，取下整副鞍，銀把手向後折平，放左側椅面帶垂。Click後蛋撻伸前腿、抖身嗅椅下乾葉，胸背露奶油毛，從此無鞍。','林先生|一放工就查環境。得喇，坐陣先。',camera='50mm肩背手扣帶完整過程到35mm椅面鞍和狗同框')
add([2,5,6,8,15,55,56,58,60],'中環暮色碼頭，阿晴阿華田下船到出口；林先生仍尖沙咀長椅。','前6秒阿晴中環下船離出口再由登船入口候返尖沙咀。Hard cut. 中6秒返程船艙由暮金變深藍兩岸亮燈。Hard cut. 後6秒同長椅林先生棕鬆繩在手、蛋撻脚邊伏、鞍左椅面，交代時間過去。',camera='35mm入口地理、50mm返程窗光、40mm同椅cutaway')
add([5,8,15,55,56,60],'夜間尖沙咀返程出口，阿晴阿華田从下船方向走出，海旁長椅在前方。','阿晴带阿華田出尖沙咀碼頭沿海旁朝原長椅步行；同時夜小輪離岸；不直接從中環跳到長椅，不重演見面。',camera='35mm後侧跟拍朝同長椅，夜藍燈光')

# Scene 10.
add([2,5,6,8,15,35,39,41,45],'林先生左座、鞍左椅面，休息蛋撻左前；阿晴阿華田由畫面右走近仍有距離。','阿華田先看蛋撻慢腳耳稍抬；阿晴顺视线，蛋撻转头站起但不拉；林先生感受棕繩變化。','林先生|有朋友？',camera='50mm犬高度視線、两条繩在各人手中可追踪')
add([2,5,6,8,15,35,45],'阿晴在長椅右側適當距離停，林先生面向聲音，犬暂不接觸。','阿晴先詢問休息，再問可打招呼，林先生答放工并同意慢慢來；雙方保留鬆繩，犬等候同意后才接近。','阿晴|唔好意思，我隻狗望住佢。佢而家休息緊？\n林先生|係呀，放咗工。\n阿晴|可以畀佢哋打個招呼？\n林先生|可以，慢慢嚟。',camera='50mm過肩兩人交流，兩犬前景分開')
add([2,5,6,8,15,39,41,45],'兩犬在兩領犬人各自鬆繩範圍，蛋撻畫面左，阿華田右。','阿華田先停，蛋撻嗅牠，阿華田稍側身再回頭；海風吹毛，阿華田尾輕拍，蛋撻身體渐放鬆；細小動作自然，不急撲。',camera='65mm狗頭與肩距近景，保持真實嗅聞接觸')
add([2,5,6,8,15,35,45],'阿華田坐右，蛋撻左没有走開；林先生与阿晴相視方向说話。','兩人说狗今日異常斯文耐心，一起笑；犬坐定；兩繩各扣項圈由各人握，不綁椅、無消失。','阿晴|佢平時識朋友，冇咁斯文㗎。\n林先生|我呢隻平時都冇咁有耐性。',camera='40mm四者同框温暖中景')

# Scene 11. Allocate enough time for all original dialogue before the memory.
add([2,5,6,8,15,35,45],'阿晴在長椅右端坐下，林先生左，兩犬下前景，鞍左椅面。','介紹名字，發現早餐叫錯真相，两人笑；阿晴說澳洲，林先生答Victoria，阿晴驚訝轉頭問；兩人各握鬆繩。','阿晴|我叫阿晴。佢叫Tine，阿華田。\n林先生|原來就係你。\n林先生|成日有人叫我隻狗阿華田。\n阿晴|你嗰隻係蛋撻？\n林先生|係。Tart。\n阿晴|一隻奶油色，一隻紅棕色。報紙檔個叔叔都可以叫錯名。\n林先生|連早餐都幫我哋配埋。\n阿晴|阿華田係澳洲嚟㗎。\n林先生|蛋撻都係。Victoria。\n阿晴|Victoria？',camera='50mm兩人中景与狗反應，說話節奏自然',duration=30)
add([2,5,6,8,15,21,22,23,24,25,27,28,37,45],'林先生棕繩圈留左腕且左手握、右手取胸袋卡套；阿晴橙繩圈留右腕且右手握、藍手機左手。','林先生抽卡右手遞，阿晴右指接卡但仍握繩，先問掃卡后手機左靠感應卡。App依序掃卡、蛋撻VIC-001林先生檔案、來源紀錄、阿華田VIC-002阿晴檔案、共同犬舍。阿晴核對讀名稱，把卡交還林先生右手收卡套；兩繩持續實體連接。犬嗅耳蛋撻稍避但留下。','林先生|蛋撻張卡喺度。你個程式讀唔讀到？\n阿晴|可以。我幫你掃？\n阿晴|唔止都係Victoria……連犬舍都係同一間。\n林先生|同一間？\n阿晴|係。我讀畀你聽。\n阿晴|維多利亞草原犬舍。\n林先生（輕聲）|咁你哋……以前見過㗎？',camera='50mm手與卡手機特寫、原App內容追蹤入手機屏幕，不做全屏字卡',duration=30)
add([1,4,10,11,18,19],'幼犬脚步聲先行；回到開場同一犬舍門，門後這次可見幼犬。','幼犬跑草地。奶油Baby Tart坐看工作人員手裏舊皮球，栗棕Baby Tine跑來剎不住碰歪空金屬碗，心形毛斑右臀一閃；Baby Tart回頭，Baby Tine停面前搖尾；工作人員輕滾球，兩犬追幾步，Tart先到Tine貼身擠。',camera='35mm低機位全身犬、65mm碗與球插入；有可愛重量与笨拙感',duration=16)
add([1,2,4,5,10,15,18,45],'草地同球旁兩幼犬貼近，两工作人員分站左右；無成年裝備。','前9秒兩工作人員各自呼喚，幼犬分向不同方向，Baby Tine走幾步回頭。Hard cut. 後5秒成年栗棕阿華田同方向回頭看奶油蛋撻，維港燈光回來，毛色一一對應，右臀心形保持。',camera='50mm幼犬離開與回頭，匹配成年回頭；夜bench轴线原樣',duration=14)

# Scene 12, no closing slogan or credits; preserve quiet visual ending.
add([2,5,6,8,15,20,26,28,37,45],'夜椅原位置，卡已收好，阿晴打開App歷史幼犬照片，兩條鬆繩仍在手。','手機照片放大阿晴描述，林先生指腹按收好的卡套；兩人說幼時性格笑話，阿晴描述聲渐退背景；原照片與App一致。','阿晴|細個都係咁，成日黐住其他狗。\n林先生|蛋撻細個張相，個樣已經好似趕住返工。\n阿晴|佢坐喺草地度。其他狗都郁緊，得佢望住前面……',camera='65mm藍手機照片插入轉50mm兩人')
add([2,5,6,8,15,39,41,45],'犬在同椅前蛋撻左阿華田右，橙領巾正确白底紅圓章，鞍仍左椅面。','阿華田挨近，蛋撻挪少許，阿華田再挨；蛋撻轉頭，阿華田坐定裝無事；林先生感動靜問，阿晴答；蛋撻終伏，阿華田伏并輕靠，阿晴批准咗。','林先生|而家做緊咩？\n阿晴|阿華田想坐埋啲。蛋撻諗緊。\n阿晴|……批准咗。',camera='65mm犬高度喜劇中近景，動作停頓給反應')
add([2,5,6,8,15,35,37,45,55,60],'两犬并伏，林先生左手鬆繩、右手可摸背，阿晴橙繩仍握手機尚在左手。','林先生笑摸蛋撻背一次說今日辛苦晒；阿晴收手機，两人不再說話；鏡頭慢拉遠，原椅與兩犬仍可見，遠小輪駛過笛聲呼應開場。','林先生|今日辛苦晒。',camera='40mm全组中景渐拉遠；夜藍金點光，柔和毛髮')
add([2,5,6,8,15,35,39,41,45,55,60],'從原海旁距離看兩犬肩靠并伏，兩人安靜各握鬆繩，鞍折左椅面。','留在兩犬温暖安静状态，阿華田尾輕動碰蛋撻，蛋撻不挪開；只有風、海、小輪遠笛與柔和結尾樂句，最後0.5秒切黑，準時17:00；無文字無片尾字幕。',camera='65mm最後犬近景，末尾黑場0.5秒')

assert len(specs)==len(p['chapters'])==55
roles=[]
covered=set()
dialogue_inventory=[]
for c,s in zip(p['chapters'],specs):
    if s['duration'] is not None:c['duration']=s['duration']
    refs=[assets[n] for n in s['refs']]
    covered.update(s['refs'])
    tags=[a['tag'] for a in refs]
    ref_text=[]
    for a in refs:
        role={'character':'只鎖定一位角色身分、面貌、毛色、體型與適用裝備。多視圖代表同一位角色，不生成多人或無頭犬。',
              'environment':'鎖定場地布局、建築、材質與鏡位軸線；光照時間依本鏡。',
              'prop':'鎖定物件外形、材質與指定狀態；多視圖或前後狀態分別理解，去除標籤。',
              'reference':'只按指定參考角色使用；不作獨立人物、不作片頭或字幕。'}[a['category']]
        if a['id']=='asset_045':role='只鎖定長椅、人犬相對位置、鞍擺放與兩條牽繩路徑；角色身分与正確圓章以角色和領巾圖優先。'
        if a['name'].startswith('App_'):role='僅作手機屏幕內精確App美術，原文字與照片追蹤到藍手機；勿當全屏字幕卡。'
        ref_text.append(a['tag']+'：'+role)
    subjects='、'.join(a['tag'] for a in refs if a['category']=='character')
    d=c['duration']
    # Each clip is one directed dramatic beat with its own action sequence.
    # Explicit montage cuts remain in the action, synchronized as subshots below.
    if '前6秒' in s['action'] and '中6秒' in s['action']:
        spans=[(0,6),(6,12),(12,18)]
    elif '前6秒' in s['action'] and '後10秒' in s['action']:spans=[(0,6),(6,16)]
    elif '前6秒' in s['action'] and '後8秒' in s['action']:spans=[(0,6),(6,14)]
    elif '前8秒' in s['action'] and '後18秒' in s['action']:spans=[(0,8),(8,26)]
    elif '前9秒' in s['action'] and '後5秒' in s['action']:spans=[(0,9),(9,14)]
    else:spans=[(0,d)]
    split_actions=s['action'].split('Hard cut. ')
    assert len(spans)==len(split_actions),(c['id'],spans,s['action'])
    shots=[]
    cursor=0
    speechchars=sum(len(line.split('|',1)[1]) for line in s['lines'])
    available=d-2
    speech=[]
    for line in s['lines']:
        who,words=line.split('|',1)
        length=available*len(words)/max(speechchars,1)
        speech.append(f'{cursor:.1f}s-{cursor+length:.1f}s {who}：{{{words}}}')
        dialogue_inventory.append({'chapter':c['id'],'speaker':who,'text':words})
        cursor+=length
    audio='\n'.join(speech) if speech else '不加明确对白，只有指定环境声与动作声。'
    audio+='\n聲音：'+ ('正常車流、腳步、行人提示聲、衣料、鞍；完全無英雄配樂，無旁白。' if c['source_scene']==7 else '本場環境聲、真實脚步、衣料、牽繩与物件接觸；海旁加海風海浪遠船聲，犬舍加草風幼犬脚步，室內保持安靜層次。溫暖細緻且克制的原創木管/撥弦配樂可低於对白，保留情緒停頓；不引用現成電影音樂。')
    for (a,b),action in zip(spans,split_actions):
        shots.append({'start':a,'end':b,'action':(subjects+'。' if subjects else '')+action,
            'camera':s['camera'],'audio':audio if a==0 else '承接本鏡指定聲音、無新增台詞。',
            'end_state':action+'；末端保留1秒可剪接微呼吸與眨眼，不突然跳位。'})
    shottext='\n'.join(f"Shot {i+1} ({v['start']}s-{v['end']}s): {v['action']} Camera: {v['camera']} End state: {v['end_state']}"+(' Hard cut.' if i<len(shots)-1 else '') for i,v in enumerate(shots))
    # Film settings do not change approved style definitions.
    prompt=f'''SCENE CONTEXT
第{c['source_scene']:02}場；{c['scene_summary']}。嚴格沿用v7故事，暖心、輕微幽默、可愛而不誇張。狗只以動作表達，不說話。
OUTPUT SETTINGS
{d} seconds, 1080p, 1920x1080, 16:9. 原速动作；{('明確剪接的分鏡' if len(shots)>1 else '一段連續表演，可依描述插入道具及反應近景')}。生成完整電影鏡頭，不拍設計圖。
GLOBAL STYLE
{p['style']['medium']} {p['style']['palette']} {p['style']['lighting']}
ACTIVE REFERENCES
{chr(10).join(ref_text)}
LOCATION MAP AND FIRST FRAME
{s['first']} 初幀立即進入這個狀態。尚未出場者不提前露面。物件所有者與位置固定，左到右軸線不越。
TIMELINE AND SHOT SEQUENCE
{shottext}
OPTICS AND CAMERA
{s['camera']} 自然景深，動作和表情可讀，短插入與反打沿同一軸線，不卡頓，不任意快慢速。
PHYSICS
腳掌落地有重量，毛與耳有自然跟隨，尾巴碰物件要有接觸，皮帶扣合與牽繩扣項圈清晰。人手不穿物，不多指。倒水量、紙張重量、球与碗惯性符合動作。
LIGHTING
照原場次時間與情緒：開場澳洲及維港清晨，家中早上，社區日間；第09場暮金逐步到夜藍，第10至12場維港夜景。主光方向和背景燈位稳定，柔和毛髮轮廓不過曝。
AUDIO AND EXACT DIALOGUE
{audio}
粤語原文逐字說，不改成普通話，不加字幕。人物聲音全片一致：林先生中年低柔幽默；阿晴年輕清晰自然；陳伯年長低沉含蓄；美姐成熟温和。只说列出对白，嘴形隨說話，反應者不抢話。開場Coming?例外為英語。
CONTINUITY AND POSITIVE CONSTRAINTS
{chr(10).join(p['continuity_locks'])}
所有角色表只代表單一角色。原圖工作与休息版本只用於指定状态切換，同一隻犬不複製。阿黃只在舊相片。幼犬無鞍無領巾。兩牽繩全程附於項圈，各自領犬者保持握住，卡與手機操作也不丟繩。從同一核准素材及文字地理構圖，不需要先前clip作冗餘參考。
STRICTLY EXCLUDE
No author names, credits, titles, subtitles, captions, location labels, closing slogans, watermarks, reference-sheet grids, panel borders, reference annotations, duplicate characters, headless dogs or talking dogs. 保留手機、卡與報紙本身設計文字，僅作世界內道具，絕不是旁白字幕。
'''
    c.update(prompt=prompt,initial_prompt=prompt,shots=shots,tagged_assets=tags,
        linked_asset_ids=[a['id'] for a in refs],prompt_status='finalized',
        pacing_reason='保留原場次配額，依此完整動作與逐句粵語對白及反應時間分配；第11場調整為30/30/16/14秒以保護對白與幼犬回憶。' if c['source_scene']==11 else c['pacing_reason'],
        handoff={'strategy':'approved references plus written geography','derived_media_needed':False,
            'reason':'獨立鏡位或反應；場景、軸線、道具與裝備由核准圖與連戲鎖延續，避免自動鏈接舊片段。'})
    folder=ROOT/'chapters'/c['id'];folder.mkdir(parents=True,exist_ok=True)
    (folder/'prompt.txt').write_text(prompt,encoding='utf-8')
    (folder/'shots.json').write_text(json.dumps(shots,ensure_ascii=False,indent=2),encoding='utf-8')
assert covered==set(assets), sorted(set(assets)-covered)
cursor=0
for c in p['chapters']:
    c['absolute_start']=cursor;cursor+=c['duration'];c['absolute_end']=cursor
assert cursor==1020
p['requested_output']={'resolution':'1080p','width':1920,'height':1080,'aspect_ratio':'16:9','audio':True,'duration_seconds':1020}
p['production_stage']='render_ready'
p['tool_availability'].update(credentials_read=True,direct_seedance_route='User authorized workspace .env; four named base settings only; endpoint authenticated live')
p['generation_authorization']={'confirmation':'proceed. video res: 1080p. aspect ratio: 16:9.','credential_source':'.env','settings':['VOLC_ACCESS_KEY','VOLC_SECRET_KEY_RAW','VOLC_PROJECT_NAME','VOLC_ENDPOINT_SEEDANCE_25']}
p['prompt_library_sources']=['TEMPLATE.md','shots/scene-12/09_a-man-seated-at-a-table-in-a-pale-mint-green-room.md']
out=ROOT/'proposal-directed.json';out.write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'exports'/'dialogue-inventory.json').write_text(json.dumps(dialogue_inventory,ensure_ascii=False,indent=2),encoding='utf-8')
subprocess.run([sys.executable,'-X','utf8',str(HELPER),'commit',str(ROOT),'--from',str(out),'--reason','Finalize 55 cinematic clips, preserve Cantonese dialogue, bind every supplied image and set 1080p 16:9'],check=True)
print(f'{len(specs)} finalized chapters, {len(dialogue_inventory)} dialogue lines, {cursor}s; all {len(covered)} images bound')
