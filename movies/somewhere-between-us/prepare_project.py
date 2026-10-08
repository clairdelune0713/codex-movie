import json, shutil, importlib.util, hashlib
from pathlib import Path
from datetime import datetime, timezone
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
WORK = ROOT.parents[1]
HELPER = Path('C:/Users/admina/.codex/skills/movi2/scripts/project.py')
spec = importlib.util.spec_from_file_location('movi2', HELPER)
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)

# Each tuple is one twenty-second sequence with three causal performance beats.
# Dialogue is human speech in Cantonese; dog identity and source plot remain fixed.
SCENES = [
('同一個名字','farm','清晨草原，幼犬聲只在遠處，暫不揭示兩犬共同身世。',
 [('露水草葉沿左至右被風吹動；低鏡頭緩緩前進。','24mm 草地微距轉遠景','風、遠處幼犬叫聲'),('澳洲 Victoria 的草原在日出中展開，遠處犬舍仍朦朧。','35mm 固定大全景','獨奏鋼琴兩音主題'),('草浪的節奏接上維港水面的波紋；最後一秒穩定海面。','50mm 草浪特寫，明確 match cut 至海浪','草風轉海風，幼犬声淡出')]),
('另一個 Victoria','harbour','維多利亞港晨曦；同名兩地的旅程開始。',
 [('晨光照亮維港，天星小輪从右向左驶過。','24mm 海面橫向遠景','海浪、渡輪低鳴'),('小輪留下的波紋延伸至尖沙咀海旁，城市漸漸甦醒。','35mm 緩慢平移','鋼琴主題加柔弦'),('鏡頭在海旁步道停住，留下日後重逢的空間。','35mm 地面高度遠景','海鳥、低聲城市環境')]),
('Click：工作開始','street','@Owner 為 @Tart 裝上導盲鞍；專注由扣合聲開始。',
 [('早晨住宅門口，@Tart 坐在 @Owner 左腳側，橙背心保持附圖設計。','50mm 中景','日常室內環境'),('@Owner 在橙背心外扣上簡潔黑色導盲鞍，握起硬柄；@Tart 耳朵前傾。','65mm 手與肩部特寫','清晰一聲 Click'),('@Tart 穩定站起，帶 @Owner 朝右踏出門外；主人跟上步伐。','35mm 低位跟拍','爪步、衣物摩擦；鋼琴節奏規整')]),
('城市是方向','street','@Tart 與 @Owner 穿過行人道，以清楚路線建立信任。',
 [('@Tart 在 @Owner 左側朝右走，避過路邊固定路障，兩者一直在人行道。','35mm 平行跟拍','腳步、爪步、街聲'),('@Tart 在樓梯前停下，@Owner 感受鞍柄提示，放慢腳步。','50mm 低角度中景','節拍暫停、自然呼吸'),('二者有節奏地踏上兩級樓梯，@Tart 到平台停住等待。','35mm 側面完整動作','腳步有重量；短柔弦')]),
('不吃那一口','cafe','掉落食物測試 @Tart 的專注；幽默藏在一次鼻尖動作。',
 [('@Owner 坐在茶餐廳卡位，@Tart 安静伏在桌下，導盲鞍仍在身。','35mm 桌下低位中景','杯碟、茶餐廳低聲人語'),('一小塊麵包從鄰桌掉在 @Tart 鼻前；牠鼻尖輕動，眼睛仍望向主人。','65mm 鼻、麵包近景','麵包落地、一次輕嗅'),('@Tart 保持伏姿，不碰食物；@Owner 手輕放鞍柄，安然喝茶。','50mm 人犬同框','幽默單音鋼琴，杯碰碟')]),
('阿華田登場','centre','@Handler 與 @Tine 抵達社區中心；熱情是不同的節奏。',
 [('@Handler 牽 @Tine 從畫面左側進門，橙背心、心形斑位置跟附圖。','35mm 寬中景','門聲、歡迎人語'),('兩位老人與一位小朋友坐在房間另一側，向 @Tine 招手；不圍堵狗。','50mm 中景反打','街坊笑：{阿華田！}'),('@Tine 等 @Handler 鬆開短牽繩再靠近，尾巴輕拍空椅邊。','50mm 犬眼高度跟拍','椅邊輕拍、木管加入旋律')]),
('一張張面孔','centre','@Tine 對每個人作出不同反應，讓熱情有節制。',
 [('一位老人伸出手；@Tine 慢慢嗅聞，再在他腳旁坐下，@Handler 在旁。','50mm 雙主體中景','笑聲、鼻息'),('一位小朋友躲在成人腿後，@Tine 停在一米外，耳朵放鬆。','65mm 小朋友眼線及狗反打','室內環境，鋼琴放輕'),('小朋友伸手到成人手旁，@Tine 不追近，只眨眼等待。','65mm 手與狗頭特寫','一次笑氣，溫柔弦樂')]),
('角落的人','centre','@Elder 留在窗邊角落，拒絕與熱鬧連結。',
 [('@Elder 坐在畫面右側窗邊，其他訪客活動在模糊遠景左側。','65mm 老人近景','人語退遠，單音鋼琴'),('@Handler 禮貌問是否想見 @Tine，@Elder 目光仍向窗外。','50mm 斜側雙人鏡頭','老人低聲：{我不喜歡狗。}'),('@Tine 原本輕搖的尾巴停慢，望望老人後收住步伐。','85mm 狗表情特寫','呼吸、室內風聲')]),
('陪他停留','centre','@Tine 不催促，讓 @Elder 自己選擇靠近。',
 [('@Tine 在 @Elder 椅子前一米處緩緩伏下，@Handler 退到左側不打擾。','35mm 側面全景','只有室內環境和衣料聲'),('@Tine 下巴放前爪上，目光低而柔，老人手仍收在膝上。','65mm 低位近景','呼吸；保持幾秒空白'),('@Elder 側望 @Tine，肩膀稍放鬆，仍未觸碰牠。','85mm 老人反應近景','鋼琴兩音主題轻轻返回')]),
('第一次伸手','centre','細小的身體接觸成為整段故事的第一個轉折。',
 [('@Elder 的右手慢慢離開膝蓋；@Tine 仍然伏下、不主動伸頭。','85mm 手部特寫','布料、呼吸'),('老人手落在 @Tine 額頭，指尖轻轻撫過一次；狗的眼神放柔。','65mm 手與頭同一平面','輕撫毛聲、兩音鋼琴'),('人犬静静停留，@Handler 遠處微笑，不插話。','50mm 側面雙主體','弦樂微暖，無額外台詞')]),
('這麼快就走了','centre','@Tine 離開時，@Elder 第一次主動挽留。',
 [('@Handler 蹲下接回牽繩，@Tine 緩緩起身，老人手回到膝上。','50mm 中景','牽繩扣聲'),('@Tine 走兩步再停下，@Elder 望著門口，開口不夸張。','65mm 老人近景','老人：{這麼快就走了？}'),('@Handler 點頭微笑，@Tine 轉頭輕搖尾巴；留下回訪的期待。','50mm 門口反打','溫柔一聲犬鼻息、原創鋼琴')]),
('電車：差一點','street','@Tart 與 @Tine 首次擦身而過，觀眾同時看到兩條路。',
 [('@Tart 帶 @Owner 在中環行人路朝右走，二者守在路沿內。','35mm 平行中遠景','叮叮電車鈴'),('一辆雙層電車從前景向左行；上層窗內 @Tine 與 @Handler 正望向另一側。','50mm 一個有深度的層次構圖','車輪、叮聲'),('電車驶出畫面，@Tart 和 @Owner 繼續右行；沒有犬互望或相遇。','35mm 固定原軸線','兩種音樂節奏短暫疊合又分開')]),
('港鐵：差一扇門','mtr','關閉的列車門與打開的升降機門造成第二次錯過。',
 [('@Tart 與 @Owner 已在列車內，車門開始閉合，保持安全距離。','50mm 月台側面列車窗景','列車關門提示'),('列車離開向左；背景升降機門打開，@Handler 與 @Tine 走出來。','35mm 固定廣角，兩個門在不同深度','列車聲转升降机提示'),('@Tine 在 @Handler 腳旁停下，看向空月台，不知道剛錯過。','65mm 人犬中景','轻鼻息、短俏皮木管')]),
('同一條街','street','相隔數分鐘的兩段路，用同一構圖把牠們連起來。',
 [('@Handler 牽 @Tine 從社區中心門口向右離開，背景固定茶色店門。','35mm 固定寬景','腳步、城市環境'),('硬切到同一構圖；日光位置不變，@Tart 帶 @Owner 由左向右經過。','35mm 完全相同機位','規整爪步'),('店員望 @Tart 笑著叫錯名字；牠保持工作，只微微抬眉。','65mm 狗近景','店員：{阿華田！}；鋼琴幽默短音')]),
('叫誰都開心','street','同樣的錯認，兩隻狗有完全不同的反應。',
 [('硬切稍晚同街另一店外，店員看見 @Tine 與 @Handler。','50mm 中景','店員：{蛋撻！}'),('@Tine 興奮搖尾巴但留在牽繩可控範圍，向店員笑般眨眼。','65mm 狗表情近景','轻拍尾巴、短木管'),('@Handler 笑著說是阿華田，輕鬆牽牠往渡輪方向走。','35mm 跟拍','女 handler：{佢係阿華田呀。}')]),
('天星碼頭','pier','第三次錯過最接近：二犬只相距十多米。',
 [('@Tart 與 @Owner 從碼頭左側出口走出；@Tine 與 @Handler 在右側等候區。','24mm 全景顯示至少十米距離','港口、船笛、腳步'),('遊客群從前景左向右经过，短暫遮住犬的視線與鏡頭。','35mm 同一軸線，前景遮擋','人潮腳步、人語'),('人潮散去，@Tart 已離開左側出口；@Tine 随 @Handler 登船。','35mm 原構圖重新可見','小輪船身輕響')]),
('又差一點','pier','小輪離岸與空碼頭留下即將相遇的期待。',
 [('@Tine 在船舱入口與 @Handler 安穩坐下，仍有松牽繩。','50mm 人犬中景','船機低鳴'),('船窗外碼頭向右退後；遠處 @Tart 與 @Owner 沿街前行，彼此沒看見。','65mm 船窗前後層景','海浪、木管逐渐消失'),('碼頭空出的長椅迎向風，硬切準備進入各自最重要的工作。','35mm 寬景慢停','主題變沉穩，無新增相遇')]),
('綠燈不等於安全','street','@Tart 在行人燈允許前進時，察覺轉彎車仍接近。',
 [('@Tart 與 @Owner 停在路沿後，燈號轉綠，行人提示聲響起。','35mm 側面寬景看清路沿','行人提示聲、街聲'),('@Owner 輕握鞍柄說前進，@Tart 卻四腳穩穩停住。','50mm 人犬側面中景','主人：{前進。}'),('轉彎小型貨車在二者前方道路通過；鏡頭保持他們在人行道內。','35mm 一個連貫側面全景','車輪声；音樂收住，沒有撞擊')]),
('拒絕也是信任','street','@Tart 的判斷保護主人，讓信任有可見的重量。',
 [('貨車通過後 @Owner 感受鞍柄與狗的停留，鬆一口氣，沒有誇張跌倒。','65mm 主人表情近景','主人輕呼吸'),('@Owner 輕摸 @Tart 肩頭，说谢谢，狗抬眼再望回道路。','65mm 手與狗頭','主人：{多謝你，蛋撻。}'),('道路清空後 @Tart 主動穩定踏出，帶 @Owner 完整越過斑馬線到另一邊。','35mm 平行跟拍','正常行人提示、柔弦恢復')]),
('有人叫牠的名字','centre','第二次探訪，@Elder 主動連結世界。',
 [('@Handler 與 @Tine 再次進入同一社區中心；老人坐同一窗邊椅。','35mm 門口到窗邊寬景','門聲、安靜室內環境'),('@Elder 未等狗靠近便微微伸手，轻声叫名字。','65mm 老人近景','老人：{阿華田。}'),('@Tine 缓缓走到椅邊坐下，掌心落在狗頭，尾巴輕搖；@Handler 靜靜讓開。','50mm 人犬雙主體','掌心撫毛、鋼琴兩音，沒有奇蹟式歡呼')]),
('一天的終點','harbour','夜幕降下，@Owner 为 @Tart 解下導盲鞍。',
 [('藍調傍晚海旁，@Owner 坐左側長椅，@Tart 在左腿旁站穩。','35mm 人犬中景','海風、遠處渡輪'),('@Owner 放下鞍柄，解扣並完整取下黑色導盲鞍；橙背心仍在狗身上。','65mm 手與背部','清晰一聲 Click，呼應開場'),('@Tart 肩膀放鬆，耳朵垂軟，戴日常牽繩在主人腳旁坐下。','65mm 狗表情近景','鬆鼻息；音樂由規整变自由')]),
('不再工作','harbour','@Tart 安靜看海；@Tine 从同一海旁另一端走来。',
 [('@Tart 坐在长椅旁左側，看向維港；@Owner 在椅子上陪伴。','35mm 侧后人犬景','浪声，原創鋼琴'),('硬切 @Handler 帶 @Tine 從右側沿同一海旁步道向左走。','35mm 侧面跟拍','爪步、衣料、城市晚聲'),('@Tine 停步望左，@Handler 順著牠目光停下。','65mm 犬中近景','音樂停留兩音；狗不叫')]),
('真正看見','harbour','二犬第一次面对彼此，熟悉感比熱情更安靜。',
 [('@Tart 回頭朝畫面右側；遠處 @Tine 在右側望向左，保持同一軸線。','50mm 有距離的寬雙主體','海風、輕呼吸'),('@Handler 允许 @Tine 缓步向左靠近；@Owner 也給 @Tart 留出松牽繩。','35mm 犬眼高度側拍','緩慢爪步、柔弦'),('二犬停在鼻距一掌，互相嗅聞，不碰撞、不立刻追逐。','85mm 鼻與眼睛雙主體','輕嗅，最後兩秒停在互望')]),
('一下，兩下','harbour','尾巴節奏喚回被遺忘的童年。',
 [('@Tine 尾巴輕拍地面一次、兩次；身体仍安静坐下。','65mm 尾與右後腿，心形斑正确','一聲、兩聲柔尾拍'),('@Tart 先望尾巴再望對方，自己的尾巴缓缓回應一次。','65mm 表情到尾部輕移','尾拍回应，鋼琴兩音主題完整出現'),('@Owner 與 @Handler 在狗身後首次交談，狗仍坐在前景。','50mm 兩人與犬層次構圖','女 handler：{Tine 是從澳洲來的。}；主人：{Tart 也是。}')]),
('Victoria？','harbour','共同地名由一次问答露出，资料确认同一犬舍。',
 [('@Owner 朝 @Handler 轉頭，表情好奇；二犬保持画面下缘静坐。','65mm 雙人中景','主人：{澳洲哪裡？}；女 handler：{Victoria。}'),('@Owner 顿一下，轻声再問；@Handler 拿出手机打开既有资料。','65mm 人手与表情','主人：{……Victoria？}'),('二人对照两份记录，露出克制惊喜；具体信息在后期排字。','50mm 手機与双方反應，不要求模型生成可讀字','女 handler：{同一間犬舍。}；远处幼犬声预叠')]),
('很久以前','farm','短暫黑場之后回到开场草地，這次幼犬进入画面。',
 [('開頭十二幀黑畫面，再顯出與開場同一草原；幼犬聲清晰近來。','24mm 固定草原遠景；黑場属于本章內部剪輯','幼犬声、草風'),('三隻其他拉布拉多幼犬在遠景跑過，@BabyTart 安靜坐在前景左側，無背心。','50mm 低位前後層景','小爪步、柔鋼琴'),('@BabyTine 從右側小跑近，減速停在 @BabyTart 前，不撞上牠。','35mm 横向低位跟拍','短促开心鼻息、草叶摩擦')]),
('早就見過','farm','@BabyTart 与 @BabyTine 的性格和尾巴节奏呼應成年。',
 [('@BabyTine 在右側尾巴轻拍一次兩次，@BabyTart 在左側平静望著牠。','65mm 幼犬雙主體','轻尾拍、兩音钢琴'),('@BabyTine 緩緩挨近，@BabyTart 挪开半掌；前者又挨近。','50mm 低位雙犬景','小爪草地、俏皮木管'),('二犬肩并肩坐在草地，看向同一片光；共同过去直到此刻才揭示。','35mm 緩慢拉遠','暖弦扩展主题，沒有旁白解釋')]),
('不同的路','farm','幼犬走向不同訓練道路，随后match cut回成年香港。',
 [('犬舍草地，@BabyTart 跟隨左側遠處照顧者向左，@BabyTine 隨右側照顧者向右。','35mm 正面低位寬景','草風、温柔脚步'),('二犬各自回望一次，隨后继续前行，不暗示被遗弃或恐惧。','65mm 两个明确反打以hard cut连接','鋼琴旋律分成兩個聲部'),('Match cut 到夜間海旁：@Tart 從左走來，@Tine 從右走來，方向由離開變相聚。','35mm 正面宽景，成年身份和夜色在剪切时改变','幼犬脚步转成年爪步，海风接回')]),
('你又靠過來','harbour','成年人身边的犬像幼年一樣，保留含蓄幽默。',
 [('@Tart 與 @Tine 并肩坐下看海，@Owner 与 @Handler 在远景长椅安静谈话。','50mm 犬侧后雙主體','海浪、软钢琴'),('@Tine 挨近 @Tart，后者挪开半掌；@Tine 再靠近一次。','65mm 二犬中景，完整保留爪与肩接触','两次爪步，俏皮单音'),('@Tart 微微侧眼，終於不再挪開，讓 @Tine 靠在肩旁。','85mm 犬雙表情','轻叹鼻息、弦乐舒展')]),
('Some paths are meant to cross','harbour','兩隻狗一樣的睡姿與整個香港，收束不同天賦同樣溫度。',
 [('@Tart 與 @Tine 慢慢伏下，下巴放前爪，姿態幾乎相同；二者橙背心仍在。','50mm 低位兩犬同框','轻呼吸、海风'),('鏡頭从二犬緩慢拉遠，维港对岸城市灯火展開，二人仍在远处陪伴。','24mm 平穩後退升高，最後保持全景','原創主題最后回歸'),('最后七秒保持海港与二犬小小身影，後期加來源結語及來源署名，收在第600秒。','24mm 鎖定完整21:9構圖','鋼琴與弦樂自然收束，最后海風')]),
]

DEFS = {
'Tart':('character','成年米金色拉布拉多蛋撻；柔軟垂耳、黑棕鼻、深色大眼、橙色灰邊背心與藍圓章；工作時在背心外穿黑色導盲鞍，夜晚解除。成年比例照使用者附圖，冷靜專注。'),
'Tine':('character','成年焦糖棕色拉布拉多阿華田；右後臀淡色心形斑，橙色灰邊背心、藍圓章，成年的體格照附圖。熱情但能讀懂別人的界線；從不在工作情境猛衝人。'),
'BabyTart':('character','Tart 幼年：同一米金毛色、耳、鼻、眼身份，幼犬短腿圓頭；無橙背心、無導盲鞍、沒有成人工作裝備。'),
'BabyTine':('character','Tine 幼年：同一焦糖棕毛色、右後臀淡色心形斑、耳鼻眼身份；幼犬短腿圓頭；無背心、無成人工作裝備。'),
'Owner':('character','38歲香港華裔視障男士；整齊短黑髮、透明矩形眼鏡、青綠polo、米色長褲、海軍藍運動鞋。生活獨立、與Tart互信，尊嚴自然。'),
'Handler':('character','32歲香港華裔女治療犬領犬員；下巴長黑bob髮、珊瑚色針織外套、米白T恤、海軍藍長褲、白運動鞋、棕色小斜肩包。尊重人犬界線。'),
'Elder':('character','78歲香港華裔老人；稀疏銀髮、銀細框眼鏡、灰藍開襟衫、米色有領襯衣、炭色長褲、深色鞋。從疏離到微小主動，沒有誇張奇蹟式表演。'),
'farm':('environment','澳洲Victoria犬舍草原：晨曦從左側、露水草葉、低木籬笆、遠處淺色木犬舍、柔弧山丘。開場和回憶同一幾何；沒有幼犬在空場參考圖中。'),
'harbour':('environment','尖沙咀維港海旁：石鋪地、右側水平金屬護欄、左側長椅、遠處香港島天際線、開放海面。參考圖幾何一致；早晨暖光，重逢藍調入夜。空場無狗無人。'),
'street':('environment','中環香港街道：寬行人道、行人路沿、斑馬線、雙軌電車、低層店面、遠處高樓；道路與行人區有清楚邊界、街道由左至右。空場無人犬車；交通由提示生成。'),
'cafe':('environment','香港茶餐廳：薄荷綠牆、左側窗、米色卡位、棕色桌面、棋盤地磚，窗光從左側。完整桌下空間可見，無人犬食物英雄道具。'),
'centre':('environment','社區長者中心：米白牆、右側大窗與安靜角落椅、左侧入口、中間分散椅子、低書架，右側暖窗光；空場無人狗。'),
'mtr':('environment','簡化香港港鐵月台：前景安全黃線、左側軌道列車位置、右後景升降機、暖灰牆、藍綠玻璃與頂燈。空場無人犬列車。'),
'pier':('environment','天星碼頭：左側到埗出口、右側上船等候門、海面與小輪泊位在後景、中央寬闊人行空間；日光從左。空場無人犬小輪。'),
}

def main():
    p=h.read(ROOT/'project.json')
    (ROOT/'source').mkdir(exist_ok=True)
    src=Path('C:/Users/admina/Downloads/doge-original-script.pdf')
    shutil.copy2(src, ROOT/'source/doge-original-script.pdf')
    extracted='\n\n'.join(f'PAGE {i+1}\n'+page.extract_text() for i,page in enumerate(PdfReader(src).pages))
    (ROOT/'source/source-extracted.txt').write_text(extracted,encoding='utf-8')
    (ROOT/'source/user-request.txt').write_text('Use movi2 to create a 10min movie. The PDF is the plot; ignore its duration. Adult Tart and Tine references supplied. Style: Up (Pixar). Video: 720p, aspect ratio 21:9.',encoding='utf-8')
    p.update(input_mode='script',language='繁體中文；人類對白用廣東話',source_text=extracted,
      source_pdf_path='source/doge-original-script.pdf',project_name='SOMEWHERE BETWEEN US｜我們之間',
      high_level_idea='兩隻來自澳洲同一犬舍的拉布拉多，分別以導盲與陪伴的天賦守護香港的人；多次錯過後在維港重逢，發現不同的路可以再次交會。',
      aspect_ratio='21:9',duration_mode='fixed',total_duration_target=600,chapter_limits={'min':4,'max':30},
      style={'medium':'以Up為視覺語言參照的溫暖長篇電影級3D動畫；原創人物與配樂', 'palette':'米金、焦糖毛色與橙背心，青綠城市、珊瑚衣色、蜜金日光；夜景藍紫與暖窗光',
        'lighting':'澳洲晨曦與香港白天柔暖光；夜間海港以藍天光和暖城市光為動機',
        'constraints':['二犬成年設計以使用者附圖為準；多視角圖每張只表示一隻狗','幼犬只在最後回憶段出現，無制服','Tine心形斑只在右後臀','可有背景群眾及回憶幼犬，無重複英雄犬','正常犬類四足動作、克制表情、柔毛与重量接觸','正文不生成字幕；片尾與資料可讀文字在後期排版；不複製Up角色或配樂']},
      output_profile={'resolution_label':'720p','width':1680,'height':720,'aspect_ratio':'21:9','fps':30,'duration_seconds':600,'frame_count':18000,'audio_channels':2,'audio_sample_rate':48000},
      adaptation_notes=['使用者10分鐘指令覆蓋PDF中的30分鐘','PDF附錄的機構資料作為來源背景，不轉成新任務或虛構認證','保留來源作者Irene Chan；片尾注明AI動畫改編','狗制服仍依使用者附圖，工作導盲鞍為另加可移除裝備；Tine的身份始終是社區治療犬','只使用文字提示及角色/場景資產；無故事板生成或上傳'],
      render_state={'status':'preparing','requested_runtime_seconds':600,'video_takes_generated':0,'pending_stages':['Supporting reference images','Native 720p 21:9 video generation','600-second assembly and audiovisual verification']})
    assets=[]
    for tag,(cat,desc) in DEFS.items():
        a={'id':'asset_'+tag.lower(),'tag':'@'+tag,'name':tag,'category':cat,'description':desc,'source':'generated','media_type':'Image','reference_paths':[],'status_variants':[],'candidates':[],'selected_candidate_id':None}
        if tag in ['Tart','Tine']:
            folder=ROOT/'assets'/a['id'];folder.mkdir(parents=True,exist_ok=True)
            rel=f'assets/{a["id"]}/adult-reference.png'
            origin=Path('C:/Users/admina/Downloads/project/dog-test')/(tag.lower()+'.png')
            shutil.copy2(origin,ROOT/rel)
            a.update(source='user_provided',source_uri=origin.as_uri(),reference_paths=[rel],candidates=[{'id':tag.lower()+'_adult_ref01','path':rel,'prompt':'使用者提供的成年身份圖；一張圖的三個角度代表同一隻犬。','source_revision':0}],selected_candidate_id=tag.lower()+'_adult_ref01')
        assets.append(a)
    p['asset_list']=assets
    chapters=[]; script=['# SOMEWHERE BETWEEN US｜我們之間\n','10:00｜720p｜21:9｜1680×720｜30fps\n','改編來源：Irene Chan 的劇情PDF。狗不說話；人類使用廣東話。\n']
    for i,(title,loc,summary,beats) in enumerate(SCENES,1):
        cid=f'chapter_{i:02d}'; start=(i-1)*20
        scene_tags=h.tags(summary+' '.join(b[0] for b in beats))|{'@'+loc}
        selected=[a for a in assets if a['tag'].casefold() in {t.casefold() for t in scene_tags}]
        setup={'farm':'草原前景左與右，中間留空；晨光左側。','harbour':'犬坐海旁前景，左側長椅、右側護欄、後景海面與香港島；不跳進水。','street':'犬與主人在行人路後方；道路和轉彎車在前景；人犬活動不越過未確認安全的路沿。','cafe':'主人卡位左上，狗伏桌下下中，食物落在狗鼻前。','centre':'入口左、活動人群中、窗與老人椅右；犬靠近时留下可選擇距離。','mtr':'列車前景左，升降機後景右；兩組人犬不在軌道內。','pier':'Tart由到埗出口左離開，Tine由右側候船門登船；中間十多米人行空間。'}[loc]
        light='藍調夜色、左側暖城市窗光、海面微反射' if (loc=='harbour' and i>=21) or i==28 else '左側蜜金柔光、溫暖反射與柔影'
        shots=[]; cursor=0
        ranges=[(0,6),(6,13),(13,20)]
        for j,((act,cam,aud),(a,b)) in enumerate(zip(beats,ranges),1):
            shots.append({'start':a,'end':b,'action':act,'camera':cam,'audio':aud,'end_state':act+'；最後一秒保留自然呼吸的穩定剪接姿態。'})
        roles='\n'.join(a['tag']+'：'+a['description']+' 參考圖只提供該單一資產身份/材質/幾何，不複製白底、多視角排列或額外主體。' for a in selected)
        timeline='\n'.join(f'Shot {j} ({s["start"]}s-{s["end"]}s): {s["action"]}\n鏡頭：{s["camera"]}。聲音：{s["audio"]}。結束：{s["end_state"]}。'+(' Hard cut.' if j<3 else '') for j,s in enumerate(shots,1))
        prompt=f'''SCENE CONTEXT\n{summary}\n本章是600秒電影中的第{i}段，電影絕對時間{start}-{start+20}秒。\nOUTPUT SETTINGS\n20秒；原生720p；21:9。三個連續計時鏡頭，明確hard cut。真實節奏的細緻3D動畫，無慢動作填時。\nGLOBAL STYLE\nUp般圓潤有重量的3D視覺語言，柔毛、表情眼神與有質感的服飾；原創角色與原創配樂。成年犬保持附圖身材；幼犬只在回憶使用幼犬專用圖。\nACTIVE REFERENCES\n{roles}\nLOCATION MAP\n@{loc}：{setup}\nFIRST FRAME AND SPATIAL BLOCKING\n直接以鏡頭一的構圖開始：{shots[0]['action']}。沿用本章地圖及前章的具體結束狀態；地點或時間改变只发生在明確剪輯。\nACTION TIMING\n{timeline}\nOPTICS AND CAMERA\n每鏡頭依上述焦段與機位。頭、鼻、眼與動作接觸可見；犬近景視線高度約0.55米。保持180度軸線，動作不因鏡頭改變位置。\nPHYSICS\n四爪與地面有重量，尾巴根部位置固定；牽繩有鬆度與接觸、鞍柄不穿過手掌。犬不具人手，不說人語。自然眨眼、呼吸和微姿態维持生命感。\nLIGHTING\n{light}；同章曝光與光向稳定，保持柔和動畫反射光。\nAUDIO\n逐鏡頭聲音按上文；人類引用花括號內的原句為廣東話對白，合理速度，無字幕。其他角色不即興台詞。原創鋼琴兩音主题，Tart規整節奏、Tine溫暖木管；海港重逢弦樂會合。犬只有呼吸、嗅聞與來源指定犬叫聲，沒有擬人對白。\nCONTINUITY LOCKS\n每個角色只有一個身份；衣服、毛色、身材、Tine右後臀心形斑固定；多視角參考不變成多隻犬。Tart工作鞍從第3章扣上至第21章完整卸下，其後只有橙背心和日常牽繩；沒有佩戴鞍而自由追逐。背景群眾只在敘述指明時出现。\nPOSITIVE CONSTRAINTS\n完整20秒全屏角色動畫；無圖格、參考圖白底、姓名標籤、水印、片中字幕；聲畫有一致時序，最後留自然穩定剪接狀態。'''
        c={'id':cid,'chapter_index':i,'title':title,'duration':20,'resolution':'720p','high_level_idea':p['high_level_idea'],'scene_summary':summary,'prompt':prompt,'initial_prompt':prompt,'tagged_assets':[a['tag'] for a in selected],'linked_asset_ids':[],'delinked_asset_ids':[],'shots':shots,'materials':[],'storyboards':[],'selected_storyboard_id':None,'takes':[],'active_take_id':None,'screenshots':[],'movie_start':start,'movie_end':start+20,'handoff':{'in':shots[0]['action'],'out':shots[-1]['end_state']},'source_pages': [1] if i<=2 else [2] if i<=15 else [3] if i<=23 else [4] if i<=25 else [5] if i<=29 else [6]}
        chapters.append(c)
        folder=ROOT/'chapters'/cid;folder.mkdir(parents=True,exist_ok=True)
        (folder/'prompt-r000001.txt').write_text(prompt,encoding='utf-8')
        script.append(f'\n## {start//60:02d}:{start%60:02d}-{(start+20)//60:02d}:{(start+20)%60:02d}　{title}\n\n{summary}\n')
        for s in shots:script.append(f'\n- {start+s["start"]:03d}-{start+s["end"]:03d}秒：{s["action"]}\n  鏡頭：{s["camera"]}。聲音：{s["audio"]}。\n')
    p['chapters']=chapters;p['detailed_script']='\n'.join(script);p['master_prompt_raw']=p['high_level_idea']+'\n'+'\n'.join(c['scene_summary'] for c in chapters)
    (ROOT/'screenplay.md').write_text(p['detailed_script'],encoding='utf-8')
    proposal=ROOT/'proposal-r000001.json';h.atomic_write(proposal,p)
    errors,warnings=h.validate(ROOT,p)
    if errors:raise ValueError(errors)
    print(json.dumps(h.save(ROOT,h.read(ROOT/'project.json'),p,'Adapt source PDF into exactly 600 seconds with adult identity references and 30 cinematic text chapters'),ensure_ascii=False))
    (ROOT/'exports').mkdir(exist_ok=True)
    h.atomic_write(ROOT/'exports/adaptation-audit.json',{'duration':600,'chapters':30,'shots':90,'story_events_preserved':['Victoria to Victoria Harbour','Tart guide-dog harness','cafe food restraint','Tine elderly connection and exact source dialogue','tram/MTR/street/ferry near misses','intelligent refusal at crossing','elder calls Tine','harness click release','quiet mutual recognition','same Victoria dog farm revelation','puppy flashback','different paths match cut','shared final posture'],'source_author':'Irene Chan 09092026','runtime_override':'User 10 minutes replaces source 30 minutes','supporting_sources_are_plot_only':True,'storyboard_inputs':0,'readable_text_strategy':'Composite title, provenance records and source closing lines in postproduction','output_goal':p['output_profile']})
    h.atomic_write(ROOT/'exports/end-titles.json',{'record_overlay':{'start':493,'end':498,'lines':['Tart — Victoria, Australia','Tine — Victoria, Australia','同一間犬舍 · Same dog farm']},'closing_overlay':{'start':593,'end':600,'lines':['From Victoria to Victoria Harbour.','Different paths. Different gifts.','Some paths are meant to cross.','我們之間 · AI動畫改編 · 原故事 Irene Chan']}})
    print('Prepared: 600 seconds; 30 chapters; 90 shots. Pending selected references:',len(warnings))

if __name__=='__main__': main()
