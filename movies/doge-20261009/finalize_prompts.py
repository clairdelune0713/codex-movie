"""Finalize approved-asset chapter direction; no media calls and no credential access."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
assert p['asset_review']['status']=='approved'
assets={a['tag']:a for a in p['asset_list']}

# Each row is (end second, observable action, framing/camera, sound, ending state).
sequences=[
 [(4,'@Victoria 空草地的晨風吹過，同一木圍欄及右方犬舍清楚可見；遠處只聞幼犬聲，不見犬。',
     '24mm 廣角低位，緩慢向右滑移，草浪由左至右。','清風、草葉、遠處兩聲細小幼犬叫；原創鋼琴三音 D-F#-A。','草浪佔畫面下半。'),
  (10,'Hard cut：草浪的弧線匹配為 @Harbour 海面水紋；@Ferry 從左向右劃過中景，城市在晨光甦醒。只使用海旁參考的地理，改為清晨。',
     '24mm 海面高度慢滑移，延續向右方向，終點輕停。','草風交接成海水、小輪低鳴，鋼琴主題帶弦樂。','小輪向右離開，水紋仍在。')],
 [(4,'@MrChan 坐在 @Central 左方茶餐廳外座，右手替身旁 @Tart-work 扣緊灰色背心扣具，黑導盲柄已固定在犬背。',
     '65mm 手與扣具近鏡，避免頭像或身體複製。','布料、扣具 Click；街頭輕環境音。','扣具完全閉合，手離開。'),
  (8,'Hard cut：@Tart-work 兩耳微抬，嘴閉，目光由主人轉向安全行人路，身體只一次穩定坐直。',
     '65mm 犬眼高度臉部近鏡，細微推近後停住。','短鼻息；鋼琴以規整節奏回應。','犬眼看向畫右的路。'),
  (14,'Hard cut：@MrChan 站起穩握導盲柄，輕說「蛋撻，出發。」@Tart-work 在主人左前方帶路，沿行人路向右走。',
     '35mm 側面兩人犬中廣景，平順跟移，四足與人腳都接地。','@MrChan 平靜粵語：「蛋撻，出發。」鞋步、爪步、輕車聲。','兩者以相同方向走出右側。')],
 [(4,'@MrChan 已坐在 @Central 外座，@Tart-work 在椅左側靠腳邊工作。畫外普通麵包碎掉到犬鼻前三十厘米，犬不移動。',
     '50mm 犬眼高度中近鏡，畫左是犬，主人小腿在畫右。','一聲小小麵包落地；音樂暫空一拍。','碎屑靜止於地面。'),
  (8,'Hard cut：@Tart-work 鼻孔抽動一次，眼睛偷偷瞥碎屑半秒，立即回到主人前方；嘴閉，前爪不動。',
     '85mm 鼻與眼的近鏡，固定鏡頭，微表情是唯一笑點。','很輕的吸鼻聲，一粒撥弦回應；沒有舔嘴或咀嚼。','目光重新集中前路。'),
  (12,'Hard cut：@MrChan 手指輕碰導盲柄確認犬位置，安心拿起茶杯；@Tart-work 保持崗位，碎屑仍在原處。',
     '50mm 中景，主人上身及犬完整一同可見，末尾保持呼吸。','茶杯輕碰碟、城市音，鋼琴恢復規整節奏。','安穩的主人與專注的犬。')],
 [(5,'@Ching 牽著 @Tine-work 由 @Community 後左門口進入。左方活動桌只有兩位普通風格一致的背景長者，不具名、不搶鏡。',
     '28mm 正向中廣景，鏡頭自活動區看向門口。','門聲、爪步；背景兩人自然說「阿華田嚟喇！」。','Tine 停在中央空地。'),
  (10,'Hard cut：@Tine-work 尾巴快搖，眼睛亮起，前腳短短一小步但沒有撲人；@Ching 彎腰提示慢下來。',
     '50mm 犬與義工中景，右方窗光，輕推近。','@Ching 溫柔粵語：「阿華田，慢慢嚟。」輕撥弦節奏。','犬停住，四足踏地。'),
  (14,'Hard cut：@Tine-work 乖乖坐下，尾巴仍歡快；@Ching 露出會心微笑，鬆牽繩在她手上而非飄空。',
     '65mm 犬胸以上與義工近景，末尾停兩秒。','犬鼻息、房間自然聲，笑意只在臉上。','犬已坐好、尾巴還搖。')],
 [(4,'@Tine-work 已坐在 @Community 活動桌旁；尾巴以固定節奏敲一隻木椅腳，犬表情認真，好像努力當好學生。',
     '50mm 側面犬全身中景，椅腳及尾巴接觸可見。','尾巴「咚、咚、咚」，撥弦剛好跟著三下。','犬仍坐直。'),
  (7,'Hard cut：@Ching 忍笑把空椅輕輕移開十厘米，讓尾巴避開椅腳。椅子重量、四腳滑動合理。',
     '50mm 義工手、椅脚及犬尾近鏡，固定。','椅脚細擦聲，敲擊突然停一拍。','椅移到新位置。'),
  (10,'Hard cut：下一個尾巴擺動剛好敲到另一隻椅腳。@Ching 終於輕笑；@Tine-work 一臉無辜地抬眼，沒有說話。',
     '65mm 犬與義工的反應近景，最後一秒停在無辜表情。','又一聲「咚」；義工自然小笑，撥弦收尾。','犬坐姿不變，義工笑容留下。')],
 [(6,'@UncleLam 在 @Community 右方窗邊藍椅，身體微向窗；@Ching 與 @Tine-work 在畫左停下。林伯輕說「我唔係好鍾意狗。」義工點頭尊重。',
     '35mm 固定中廣景，清楚看到一米半空白距離。','@UncleLam 低、略沙啞粵語：「我唔係好鍾意狗。」房間聲低，音樂退下。','犬與人沒有侵入林伯空間。'),
  (14,'Hard cut：@Tine-work 先看林伯低垂的手，再慢慢收起前腳，趴在一米半外；尾巴停成細小擺動。@Ching 安靜坐在犬左後方。',
     '50mm 低位中景，林伯膝與手佔右邊，犬在左邊；不推近。','布料、犬落地小鼻息；一個稀疏暖鋼琴和弦。','犬趴好，頭未靠近人。'),
  (24,'Hard cut：@UncleLam 從窗轉看犬；握緊的手指一點一點鬆開。他沒有摸犬，只在最後輕輕呼氣。@Tine-work 安靜陪伴。',
     '65mm 林伯中近鏡，犬頭在左下柔焦，鏡頭固定讓變化可見。','一聲慢呼氣、很低房間聲；沒有奇蹟音效，沒有催促。','林伯手已攤鬆，眼睛仍看犬。')],
 [(5,'@Tart-work 正在 @Central 帶著 @MrChan 向右安全走；畫外街坊友善叫「阿華田！」，犬耳朵一下動了，但脚步不中斷。',
     '35mm 側向穩定跟移，犬左前，主人右後。','畫外粵語：「阿華田！」；鞋步、爪步。','兩者繼續同速前進。'),
  (8,'Hard cut：@Tart-work 給一個極短無奈側眼，立即望回前路；只此一次，不停下找聲音來源。',
     '65mm 犬臉側面近鏡，背景緩慢向左流動。','一粒低撥弦；犬不吠。','眼睛回前路。'),
  (12,'Hard cut：@MrChan 聽到錯叫，嘴角上揚，自然說「佢今日唔接藝名。」他保持握柄，Tart 引導路線不變。',
     '50mm 主人上身中近鏡帶犬背前景，跟移後以穩定畫面結束。','@MrChan 乾爽幽默粵語：「佢今日唔接藝名。」沒有罐頭笑聲。','主人的小笑與工作犬專注並存。')],
 [(4,'@Ching 與 @Tine-work 在 @Central 外座旁沿行人路向右走；畫外有人叫「蛋撻！」，Tine 高興轉耳、尾巴開始搖。',
     '35mm 行人路中景，義工與犬同框，不走到軌道。','畫外粵語：「蛋撻！」；輕街聲、撥弦。','犬原地停半步等待義工。'),
  (7,'Hard cut：@Ching 彎一點腰，帶笑提醒「你係阿華田呀。」@Tine-work 抬眼，頭只歪一次，好像名字都可以。',
     '65mm 兩者中近鏡，義工右、犬左。','@Ching 粵語：「你係阿華田呀。」犬不回話。','犬歪頭而尾巴不停。'),
  (10,'Hard cut：@Tine-work 步伐輕快地繼續跟著 @Ching；開心來自被叫，不是食物。',
     '50mm 犬眼高度側移，最後保持同行。','義工小笑，兩下爪步加原創撥弦尾音。','犬和義工同向出畫。')],
 [(4,'@Central 行人路上 @Tart-work 左前、@MrChan 右後向右走；@Tram 已在中景軌道由左向右緩過。先清楚見車及街。',
     '28mm 固定廣景，鏡頭在行人路對面，交通與人行區分離。','電車叮叮、慢輪軌聲、爪步。','兩犬的近距離路徑已建立。'),
  (9,'Hard cut：@Tine-work 和 @Ching 已坐在 @Tram 上層前方，犬在內側安全座位。Tine 正看向另一邊玻璃，錯過下方 Tart。',
     '50mm 上層窗內側中景，外面街道向左移；不讓狗跳窗。','電車鈴、義工小聲「望吓嗰邊。」；Tine 興奮鼻息。','犬仍望向另一側。'),
  (14,'Hard cut：回 @Central 原固定廣景，@Tram 過去後 @Tart-work 與 @MrChan 還在行人路，向右離開；互不回頭。',
     '28mm 同軸固定廣景，不突然變到鏡像另一街。','電車聲漸遠，音樂做一個沒落下的半終止。','行人路空出，仍沒有相遇。')],
 [(4,'@Metro 左側列車即將離站，@Tart-work 與 @MrChan 已安全在車內並遠離門縫；月台玻璃門及車門一起關妥。',
     '35mm 固定中廣景，月台視角，右後方升降機同框。','車門提示音、門合聲，沒有文字字幕。','兩層門完全關上。'),
  (7,'同一連續鏡頭：列車平穩向左離開，透過窗看见 @Tart-work 穩坐主人身邊。',
     '35mm 三腳架鎖定，不追列車，電梯仍在右後景。','列車低鳴漸遠，音樂懸一拍。','列車離開此窗位。'),
  (10,'同一連續鏡頭：右後升降機門開，@Ching 與 @Tine-work 步出，見到剛空出的月台，繼續往通道。',
     '35mm 固定，不切鏡；電梯出來後保持一秒。','升降機一聲叮、爪步；小小撥弦嘆號。','義工與犬向畫右通道走。')],
 [(6,'@Pier 的 @Ferry 停在左方斜道旁；@Tart-work 領 @MrChan 安全踏上碼頭，從左前往右側出口。@Ching 與 @Tine-work 在右後方走向上船區。',
     '28mm 廣景，先保留兩組相隔十米的實際空間。','船纜、水聲、爪步，人群低聲。','兩組路線即將靠近。'),
  (11,'Hard cut：@Tart-work 只看主人安全路線；@Tine-work 被旁邊普通旅行箱輪聲吸引，轉頭半秒，尚未看見 Tart。',
     '50mm 碼頭低位中景，把犬距離保留在同一深度軸。','箱輪聲、犬鼻息；音樂輕輕期待。','兩犬即將擦身但未認出。'),
  (17,'Hard cut：六位普通動畫遊客在前景向左自然走過，短暫遮住兩組；不變成真人、不複製主角。',
     '35mm 固定廣景，以人群實際走動作遮擋，沒有黑屏或假轉場。','步聲、普通人群模糊談話，不加可辨台詞。','前景遮擋正在散開。'),
  (22,'同一鏡頭人群散開：@Tart-work 與 @MrChan 已離開右側出口；@Ching 及 @Tine-work 已在 @Ferry 安全船艙，小輪慢慢向左離岸。',
     '35mm 同軸固定廣景，兩組按實際時間走位，不瞬移。','船鳴與水聲，音樂小小落空。','碼頭通道空出，船與岸分離。')],
 [(5,'下午 @Central 路口，@Tart-work 左前、@MrChan 右後停在路緣內，不在車道。行人聲響開始；陳先生說「前進。」',
     '35mm 側面中廣景，清楚見路緣、斑馬線與右方轉彎車道。','行人提示聲；@MrChan 粵語：「前進。」背景音樂退下。','指令已出，犬仍四足穩立。'),
  (10,'Hard cut：@Tart-work 重心穩定、握柄未前移，耳朵對準右方尚未停穩的普通轉彎車。沒有拉扯主人，只清楚拒絕前進。',
     '50mm 犬與主人手的近中景；車仍在道路內，遠離犬。','車胎、引擎聲；犬一次輕鼻息。','主人感到柄沒動，腳也停住。'),
  (17,'Hard cut：普通轉彎車以慢而可讀的速度從畫右至左經過斑馬線，沒有碰撞。@MrChan 從犬的停頓理解，放鬆呼氣，耐心等。',
     '35mm 回側面廣景，完整看見安全邊界，固定鏡頭。','車聲消退，行人提示持續；不加尖叫、爆炸或煞車戲劇音。','車完全離開，路徑已空。'),
  (24,'Hard cut：@Tart-work 確認兩側路清空，才穩穩走向畫右；@MrChan 跟隨過斑馬線，最後雙雙踏上對面安全行人路。',
     '35mm 平滑跟移，全身與脚掌落地可見，末尾停穩。','規律鞋步爪步、城市音；溫暖鋼琴主題輕回。','兩者在對岸安全地面。')],
 [(5,'剛安全過街後，@Tart-work 與 @MrChan 在 @Central 寬行人路停好，主人右手輕摸犬肩側，不干擾前路判斷。',
     '50mm 腰以下與犬同框，穩定中景。','掌摸毛、衣料、自然街音。','主人手輕貼犬肩。'),
  (9,'Hard cut：@MrChan 面向犬位置，輕聲說「多謝你。我信你。」語氣自然、有力量，不把犬或人當可憐對象。',
     '65mm 主人上身中近鏡，犬頭在左下。','@MrChan 低暖粵語：「多謝你。我信你。」稀疏鋼琴和弦。','主人微笑，手回握柄。'),
  (12,'Hard cut：@Tart-work 抬眼看主人，尾巴只輕動一下，再回望前路；二者重新向右走。',
     '65mm 犬臉近鏡轉為50mm同行中景，以自然可用終態收尾。','一聲細鼻息、恢復鞋步。','犬眼回前路。')],
 [(6,'下午 @Community 同一布局。@UncleLam 在右方藍椅，看見 @Ching 帶 @Tine-work 由後左門進來，先輕叫「阿華田。」',
     '35mm 固定中廣景，光比上午稍暖，地理不變。','@UncleLam 低沙啞粵語：「阿華田。」輕房間声，沒有大音樂。','犬在原來一米半位置停下。'),
  (12,'Hard cut：@UncleLam 右手從膝上慢慢伸出，指尖放鬆；@Tine-work 先看手，再看林伯。@Ching 只安靜守在犬後。',
     '65mm 手與犬目光中近鏡，慢節奏，沒有突然推鏡。','老人衣料、呼吸、犬鼻息；鋼琴單音不催促。','伸出的手成為邀請。'),
  (18,'Hard cut：@Tine-work 用四個小步慢慢跨過距離，鼻尖先輕嗅手背，不舔或跳起；林伯第一下輕摸犬頭。',
     '50mm 犬眼高度側面中景，手、頭接觸及爪落地清楚。','四下小爪步、皮膚與毛輕接觸；溫暖弦樂很低。','手真實貼住犬頭。'),
  (24,'Hard cut：@UncleLam 手停在犬頭上，長呼一口氣，嘴角只一點點上揚；@Tine-work 安心坐好，尾巴輕掃地一次。',
     '65mm 林伯與犬的雙近景，最後兩秒安靜。','長呼氣，尾巴掃地；音樂含蓄，不加奇蹟鐘聲。','雙方舒適停留，不宣稱孤獨已治好。')],
 [(5,'@Community 同一下午，@Ching 正把鬆牽繩輕收，@Tine-work 已離開林伯膝旁一步。@UncleLam 主動問「咁快就走？」',
     '50mm 中景，林伯右、義工犬左，留距離。','@UncleLam 粵語：「咁快就走？」帶一點捨不得。','義工和犬都回看林伯。'),
  (10,'Hard cut：@Ching 溫柔回答「我哋會再嚟。」不是空泛說教；@Tine-work 用安靜的目光望林伯。',
     '65mm 義工中近鏡，犬頭前景，陽光維持。','@Ching 溫柔粵語：「我哋會再嚟。」原創鋼琴主題柔和。','義工向林伯輕點頭。'),
  (14,'Hard cut：@UncleLam 回一個小笑；@Tine-work 只搖一下尾巴，跟 @Ching 往後左门離開，沒有狂跳或哀鳴。',
     '50mm 林伯近鏡含犬離開的柔焦輪廓，最後留他的笑。','爪步漸遠，老人的慢呼氣，溫柔弦樂。','林伯看著門口，眼神已多一點連結。')],
 [(5,'@Harbour 暮色安全步道左方長椅，@MrChan 坐著，@Tart-work 面向他。主人解扣並把完整橙背心連導盲柄移離犬身，放到椅上，細灰項圈留著。',
     '50mm 近中景，完整看見裝備被手拿走；動作後才成為 @Tart-rest。','扣具 Click、衣料；街音轉成平靜海水，音樂鬆開。','@Tart-rest 已無背心與握柄，裝備確實在椅上。'),
  (10,'Hard cut：步道另一端 @Ching 從 @Tine-work 身上卸下軟背心收进手提袋，留細灰項圈及鬆牽繩，成為 @Tine-rest；犬輕伸前腿。',
     '50mm 近中景；只呈現同一隻犬的前後裝備狀態，不同時複製兩隻。','一聲細扣具 Click、袋布、舒展鼻息。','@Tine-rest 裝備已收起，義工準備散步。')],
 [(6,'@Tine-rest 隨 @Ching 由 @Harbour 右側沿寬步道走向左側長椅；牽繩鬆，人在旁，與水邊有欄杆隔開。犬忽然停下。',
     '35mm 中廣景，海在後景、長椅左、兩犬實際距離約六米。','犬步聲停、海水、原創鋼琴留下懸念單音。','犬望向左方 Tart。'),
  (11,'Hard cut：@Tart-rest 本來在長椅前坐看海，聽到腳步後緩緩回頭，看見 Tine；@MrChan 坐在椅上手持鬆牽繩。',
     '65mm Tart 犬眼高度近鏡，沒有突然驚叫表情。','項圈微聲、犬短鼻息、海水。','Tart 視線落在右方 Tine。'),
  (16,'Hard cut：@Tine-rest 表情從好奇變得安靜，沒有立刻衝過去；@Ching 輕停腳步，順著牠目光看向 Tart。',
     '65mm Tine 臉部近鏡，背景燈光溫暖。','很低鋼琴與一聲短呼氣；沒有對白。','Tine 安靜等待，尾巴由快變慢。')],
 [(6,'@MrChan 與 @Ching 在 @Harbour 安全步道允許兩犬慢慢走近，鬆牽繩仍握在手；@Tart-rest 左、@Tine-rest 右，互嗅肩頸，不拉扯。',
     '50mm 低位雙犬中景，兩人下半身在後景，不跨軸。','鼻嗅、爪步、海水，音樂只一個稀疏鋼琴和弦。','兩犬近距離平靜並立。'),
  (13,'Hard cut：@Tine-rest 坐下，尾巴在石地輕拍一下、停一拍、再一下，望著 Tart；笑意含在小鼻息。',
     '65mm Tine 側面中近景，尾巴與臉都可見，固定。','兩聲相隔的尾巴拍地；沒有說話或擬人笑声。','Tine 坐定等回應。'),
  (20,'Hard cut：@Tart-rest 看一眼 Tine 的尾巴再看臉，停頓後自己的尾巴輕動一下；兩犬鼻尖緩近，不碰撞。',
     '65mm Tart 與 Tine 雙近景，慢微推後停住，末尾保持兩秒。','第三聲很輕拍地；兩個主題首次共享三音。','兩犬相望，熟悉先於解釋。')],
 [(7,'@Harbour 長椅旁 @Ching 在右、@MrChan 在左，兩犬坐在前景。阿晴自然開口「Tine 係澳洲嚟嘅。」',
     '50mm 平視雙人中景，兩犬輪廓在下方；不讓人盯鏡頭。','@Ching 粵語：「Tine 係澳洲嚟嘅。」海水及溫暖低鋼琴。','陳先生聆聽，輕轉向她。'),
  (13,'Hard cut：@MrChan 露意外的小笑，回「Tart 都係。邊度？」話後留一個自然空拍。',
     '65mm 陳先生中近鏡，墨鏡保持，視線方向不假裝視讀。','@MrChan 粵語：「Tart 都係。邊度？」自然低暖男性聲。','他等待回答。'),
  (17,'Hard cut：@Ching 答「Victoria。」再看一眼兩犬，沒有搶著解釋。',
     '65mm 阿晴中近鏡，保持與前場同軸。','@Ching 以自然粵語語境說：「Victoria。」海聲。','她注意到對方反應。'),
  (22,'Hard cut：@MrChan 稍頓，笑說「咁啱？Tart 都係嗰度。」兩犬在下方仍坐著，身世轉折由人自然交談帶出。',
     '50mm 回雙人中景，末尾停在二人的相似驚喜。','@MrChan 粵語：「咁啱？Tart 都係嗰度。」原創鋼琴小小開闊。','兩人想確認紀錄。')],
 [(5,'@Ching 在 @Harbour 取出普通無品牌手機，手指翻到犬舍舊紀錄。手機屏幕只有 @MemoryPhoto 的兩隻幼犬合照內容，無界面字、日期或通知。',
     '65mm 手機近鏡，照片内容填滿屏幕，排除參考相片外的棚拍背景。','指尖碰屏小聲、海水；音樂降低。','兩犬同一圍欄旁的合照清楚可讀。'),
  (11,'Hard cut：@Ching 看屏幕，向聆聽的 @MrChan 說「同一間犬舍。睇，細個已經一齊。」他不看或視讀屏幕，笑容慢慢擴開。',
     '50mm 雙人中近鏡，手機在阿晴手中，她向他解釋；犬在腳邊。','@Ching 粵語：「同一間犬舍。睇，細個已經一齊。」聲音清楚、不含字幕。','共同來源已被人聲確認。'),
  (14,'Hard cut：@MrChan 回「原來係老朋友。」@Tart-rest 左與 @Tine-rest 右安靜相靠；幼犬叫聲先從聲軌輕入，為回憶搭橋。',
     '65mm 雙犬近景，人聲畫外；末尾兩秒在熟悉的靠近姿勢。','@MrChan 畫外粵語：「原來係老朋友。」遠處幼犬聲橋接，鋼琴回到開場三音。','相靠姿勢準備匹配童年。')],
 [(6,'回到開場同一 @Victoria 草地、右方木犬舍、相同圍欄。@Tart-puppy 安靜坐在畫左，沒有項圈背心；只有這兩位幼犬主角。',
     '35mm 幼犬眼高度中廣景，暖晨光、草在腳邊，有實際短腿比例。','草風、小幼犬鼻息，開場鋼琴三音。','Tart 看向畫右。'),
  (13,'Hard cut：@Tine-puppy 從右方奔向 Tart，圓小爪交替落地，耳朵跟隨跑動；到兩步外才開始减速。',
     '50mm 低位橫跟移，保留身體重量，不能漂浮或腳滑到前方。','四拍幼犬爪步、短興奮吠一声、輕撥弦。','Tine 正準備急停。'),
  (18,'Hard cut：@Tine-puppy 在乾草上短短煞停，後腳滑出小半圓，身體安全一晃，没有摔傷或撞 Tart。Tart 只抬一邊眉。',
     '50mm 雙幼犬全身中景，固定，滑動有摩擦與重量。','草擦聲、一粒撥弦停頓；不加卡通撞擊或痛叫。','Tine 尷尬地坐正。'),
  (24,'同一鏡頭：@Tine-puppy 尾巴拍一下、兩下，慢慢靠向 @Tart-puppy；Tart 小挪一下又接受。',
     '50mm 固定中景，最後兩秒保持兩犬靠著的姿勢。','兩下幼犬尾巴掃草，鋼琴和弦溫暖回應。','幼犬姿勢與成年相片呼應。')],
 [(6,'@Victoria 同一圍欄前，@Tart-puppy 在左、@Tine-puppy 在右。畫外輕柔無字呼喚提示各自跟人走；兩犬回望彼此一次。',
     '35mm 固定中廣景，幼犬之間的視線清楚，不出現飛機或地圖字幕。','草風、遠處普通人無字輕喚、音樂轉柔。','兩犬開始向相反方向迈步。'),
  (10,'同一鏡頭：@Tart-puppy 往左、@Tine-puppy 往右小步離開，回頭只一次，不悲傷哭喊。',
     '35mm 固定，讓左右運動充足但不拖長。','兩組幼犬爪步向不同方向漸遠，弦樂轉位。','草地中央空出。'),
  (16,'Hard cut：@Harbour 成年的 @Tart-rest 從左往中間、@Tine-rest 從右往中間走來，左右路線反轉為相遇；他們在同一安全石地並肩坐下。',
     '35mm 相同水平构圖與犬眼高度，成年較大比例；以剪接呈現年月，不用變形。','海水、兩組成年爪步，開場主題合流。','Tart 左、Tine 右，坐定看海。')],
 [(7,'@Harbour 的 @Tart-rest 坐左、@Tine-rest 坐右，@MrChan 與 @Ching 在長椅附近保持鬆牽繩。Tine 以肩輕靠 Tart；Tart 用半個屁股挪左。',
     '50mm 低位雙犬中景，鏡頭固定，欄杆海面在後。','毛接觸、石地小爪聲，撥弦玩笑節奏。','兩犬間開了一點縫。'),
  (13,'同一鏡頭：@Tine-rest 只再往左挪同樣距離，重新靠上；@Tart-rest 給側眼，再小挪半步。動作有重量與停頓。',
     '50mm 固定，不加第三隻犬、不拉長腿或變形尾巴。','兩次小腳步，音樂先停一拍，再一粒撥弦。','Tart 已無意繼續挪。'),
  (22,'同一鏡頭：@Tine-rest 最後靠近；@Tart-rest 鼻子長呼一口氣，終於接受。兩犬肩貼肩；背景兩人聽到鼻息，輕笑，不打斷。',
     '50mm 最後微推到溫柔雙近景，末尾留兩秒真實呼吸。','Tart 長鼻息；兩人很小自然笑，鋼琴由喜劇和弦回溫暖。','兩犬安穩相靠，不再挪動。')],
 [(6,'@Harbour 安全寬石步道，@Tart-rest 左、@Tine-rest 右同時慢慢伏下，前爪伸直、頭輕放，姿勢幾乎相同；兩人仍在後方長椅旁。',
     '50mm 低位雙犬中近景，地面接觸可信，緩慢開始後拉。','身體落地、安穩鼻息、海水；原創鋼琴與弦樂兩主題合為D大調。','兩犬同姿勢休息。'),
  (18,'同一連續鏡頭：鏡頭從犬眼高度平滑後拉稍升，看到 @MrChan 與 @Ching 在長椅旁以及整個亮燈維港。犬自然微呼吸，不變成靜止照片。',
     '由50mm自然視角平滑後拉至廣景，沒有突然變焦，沒有無人機急飛。','海水與遠遠城市音，鋼琴弦樂完成溫暖終止，不用 Up 原聲。','兩小小身影並肩，人在身旁，整座城市在後。'),
  (20,'同一鏡頭溫柔保持後自然淡黑，最後不出現任何片名、標語、字幕、機構字樣、作者或片尾名單。',
     '廣景固定，最後兩秒自然淡黑，沒有黑卡文字。','最後一個原創和弦及海水自然消退。','黑畫面且無文字，聲音完成。')]
]
assert len(sequences)==len(p['chapters'])==24

maps={
 'central':'@Central 茶餐廳在畫左，行人路在前中景，車道及叮叮軌道在後中景；一般同行時犬在主人的左前方、向畫右走。轉彎車道在畫右；安全路緣始終分隔犬與車。',
 'community':'@Community 左方活動桌，右方窗及藍椅，後左入口；@UncleLam 在右，@Tine-work 起初在左距離一米半，@Ching 在犬左後；窗光從右進。',
 'harbour':'@Harbour 左方長椅，後景欄杆海水及香港島天際線，前景寬步道；@Tart-rest 通常在左、@Tine-rest 在右；@MrChan 及 @Ching 位於安全步道，鬆牽繩由人握住。',
 'victoria':'@Victoria 畫右遠處木犬舍，水平木圍欄在中後景，前景乾草；@Tart-puppy 左、@Tine-puppy 右。清晨暖光從左，開場及回憶保持同一地理。',
 'metro':'@Metro 列車及玻璃月台門在畫左，升降機在右後方；鏡頭在月台安全區。Tart 先在車內，Tine 後從電梯到月台，不能交換兩組角色。',
 'pier':'@Pier 左方上落船斜道，右方城市出口，@Ferry 停在斜道外；Tart 從船往右出口、Tine 往左斜道上船，六位普通動畫遊客只在前景自然遮擋。'}
voice='@MrChan：四十多歲香港男性，低暖、乾爽幽默、自然粵語。@Ching：三十多歲香港女性，溫暖清晰自然粵語。@UncleLam：七十多歲男性，略沙啞、有氣息但有力量的自然粵語。全片各人物維持同一聲線，狗不說人話。'
common=('保持已批准的 Up (Pixar) inspired 精緻3D動畫語言：圓潤造型、觸感毛髮、細膩表情、真實重量、溫暖有依據的光。'
        '角色參考圖的多視角只是一位角色，不是多人或多犬；影片中狗永遠完整四足與頭，不複製裁切身體、展示圖面板、棚拍背景或印字。'
        'Tart 米色，Tine 暖棕且右後臀心形奶油斑，任何時間不可交換毛色、工作身份或臉型。'
        '只在明確卸下裝備後使用休息版；幼犬只在回憶。狗的思考用眼、耳、鼻息、尾巴及停頓呈現。'
        '沒有片名、字幕、標語、署名、片尾名單、浮水印、可讀招牌、衣服字或品牌。'
        '普通背景市民是同風格動畫造型，不用真人臉；服務犬工作時不追食物、不衝向陌生人。'
        '原創音樂，不重製 Up 配樂；剪接照具體時間執行，不把全片變成蒙太奇。')

for i,(ch,sequence) in enumerate(zip(p['chapters'],sequences),1):
    declared=ch['tagged_assets']
    # Role descriptions refer only to the chapter's active assets.
    roles=[]
    for tag in declared:
        a=assets[tag]
        if a['category']=='character':
            role='身份、臉型、毛色或衣服、工作裝備及年龄；排除棚拍背景，單一角色的多視圖不能成為重複角色。'
        elif a['category']=='environment':
            role='地理、建築比例、擺設和材質；場景時間及天氣依本場指示，沒有參考板文字或固定空鏡構圖限制。'
        else:
            role='物件造型、材質、比例及狀態，排除棚拍底色。'
        if tag=='@MemoryPhoto':
            role='只取無字幼犬合照的影像內容作手機屏幕上的照片；不複製圖片的棚拍背景，不把印刷相片變成第三隻實體犬。'
        roles.append(tag+'：'+a['description']+' 用途：'+role)
    if '@Metro' in declared: key='metro'
    elif '@Pier' in declared: key='pier'
    elif '@Community' in declared: key='community'
    elif '@Central' in declared: key='central'
    elif '@Victoria' in declared and i in (1,21,22): key='victoria'
    else: key='harbour'
    location=maps[key]
    # Prune globally described tags absent in this scene while retaining names in plain prose.
    for tag in assets:
        if tag not in declared:
            location=location.replace(tag,assets[tag]['name'])
    voice_local=voice
    for tag in ('@MrChan','@Ching','@UncleLam'):
        if tag not in declared: voice_local=voice_local.replace(tag,assets[tag]['name'])
    first=sequence[0][1]
    shots=[]
    cursor=0
    lines=[]
    for n,(end,action,camera,audio,end_state) in enumerate(sequence,1):
        shots.append({'start':cursor,'end':end,'action':action,'camera':camera,'audio':audio,'end_state':end_state})
        lines.append(f'Shot {n} ({cursor}s-{end}s):\n畫面及表演：{action}\n鏡頭：{camera}\n音訊：{audio}\n終態：{end_state}')
        cursor=end
    assert cursor==ch['duration']
    prompt='\n\n'.join([
        'SCENE CONTEXT\n'+ch['scene_summary']+' 本段情緒目的：'+ch['pacing_reason'],
        f"OUTPUT SETTINGS\n{ch['duration']} 秒，720p 原生1470×630，21:9，MP4。有聲，原創音樂及粵語對白。動作正常速度；依下面明確鏡頭指示剪接或連續，不加慢動作、速度變化或額外片名。",
        'ACTIVE REFERENCES\n'+'\n'.join(roles),
        'LOCATION MAP\n'+location,
        'FIRST FRAME AND SPATIAL BLOCKING\n'+first+' 所有可見角色在開場已具有指定位置，沒有先展示角色參考圖。相鄰鏡頭保留動作軸與毛色。',
        'FORMAT MODE\n依下列鏡頭時間，明確 Hard cut 才切鏡；標示同一鏡頭的段落保持連續。時間總和等於本段秒數。沒有額外建立鏡頭或片尾卡。',
        'ACTION TIMING\n'+'\n\n'.join(lines),
        'OPTICS AND CAMERA\n按每鏡指示使用24、28、35、50、65或85mm等效視角。狗視角鏡頭通常約地面0.5至0.7米；人對話在眼高。直線不彎，面部不因廣角變形；對焦在當前說話者或犬的近眼，不無故跳焦。',
        'PHYSICS\n每隻犬四條腿、兩耳一尾，爪掌與地面接觸；行走有重心，毛及耳跟隨運動後再停。人手五指、扣具真實開合、裝備不穿過身體，牽繩與握柄與手相連。物件接觸要有重量、摩擦及先後，不漂浮瞬移。',
        'LIGHTING\n保持本場所需晨光、下午窗光或暮色維港的明確光源。街道及草地暖低陽光，中心右窗柔光，月台頂燈，海旁夕光加城市燈及水面反光。此場內光向、曝光、膚色與毛色穩定，無突然閃光。',
        'AUDIO\n'+voice_local+'\n只使用每鏡列出的對白、環境音、Foley 及原創配樂。音樂在對白下保持低音量；重逢使用稀疏鋼琴三音D-F#-A及輕弦樂，喜劇以撥弦短節奏回應，不加罐頭笑聲。最後可用停頓保留呼吸，不把犬叫當人說話，不增加敘述者或字幕。',
        'POSITIVE CONSTRAINTS\n'+common+' 本段結束狀態：'+shots[-1]['end_state']])
    ch['prompt']=prompt
    ch['initial_prompt']=prompt
    ch['prompt_status']='final'
    ch['shots']=shots
    ch['resolution']='720p'
    ch['audio']={'language':'Cantonese','generate_audio':True,'score':'original sparse piano and light strings; restrained pizzicato for comedy'}
    ch['handoff']={'first_frame':first,'end_state':shots[-1]['end_state'],'screen_axis':'preserve specified scene axis; Tart left and Tine right at reunion'}
    ch['linked_asset_ids']=[assets[tag]['id'] for tag in declared]
    folder=ROOT/'chapters'/ch['id']
    folder.mkdir(parents=True,exist_ok=True)
    (folder/'prompt.txt').write_text(prompt,encoding='utf-8')
    (folder/'shots.json').write_text(json.dumps(shots,ensure_ascii=False,indent=2),encoding='utf-8')

p['production_stage']='ready_for_video_render'
p['output_spec']['frame_dimensions']='1470x630 (provider native 720p 21:9 profile)'
p['direct_render_authorization']={'confirmation':'Yes, use those four settings and render',
    'settings':list(('VOLC_ACCESS_KEY','VOLC_SECRET_KEY_RAW','VOLC_PROJECT_NAME','VOLC_ENDPOINT_SEEDANCE_25')),
    'environment_source':'C:/Users/admina/Downloads/project/aifx-studio/.env',
    'scope':'24 Seedance 2.5 video jobs; 390 seconds; 720p; 21:9; approved image assets'}
p['renderer_capabilities_verified']={'model':'Seedance 2.5','date':'2026-10-09','duration_range':[4,30],
    'reference_image_limit':30,'request_byte_limit':64*1024*1024,'native_720p_21_9':[1470,630],
    'documentation':'https://docs.byteplus.com/zh-TW/docs/modelark/seedance-2-5'}
p['detailed_script']='\n\n'.join(f"{c['absolute_start']}s–{c['absolute_end']}s | {c['title']}\n{c['scene_summary']}" for c in p['chapters'])
(ROOT/'proposal.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'final-scene-prompts.md').write_text('# doge-20261009 最終場景提示詞\n\n'+
    '\n\n'.join(f"## {c['chapter_index']:02d} {c['title']} · {c['duration']}秒\n\n{c['prompt']}" for c in p['chapters']),encoding='utf-8')
print(json.dumps({'finalized_chapters':24,'duration':390,'shots':sum(len(c['shots']) for c in p['chapters'])}))
