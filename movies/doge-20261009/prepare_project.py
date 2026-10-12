import json
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
p = json.loads((ROOT / 'project.json').read_text(encoding='utf-8'))
p.update({
    'input_mode': 'script', 'language': 'zh-Hant-HK',
    'source_text': '\n\n'.join(page.extract_text() for page in PdfReader(ROOT / 'source/original-script.pdf').pages),
    'source_pdf_path': 'source/original-script.pdf',
    'high_level_idea': 'Tart 帶人前進；Tine 陪人停留。兩種天賦，兩條路，繞過半個世界後，在維港找回童年朋友。',
    'aspect_ratio': '21:9', 'resolution': '720p', 'duration_mode': 'adaptive',
    'total_duration_target': None,
    'production_stage': 'asset_creation',
    'output_spec': {'resolution': '720p', 'aspect_ratio': '21:9', 'fps': 30,
                    'audio': 'Cantonese dialogue, original instrumental score, ambience and Foley',
                    'in_video_titles': False, 'subtitles': False, 'credits': False,
                    'author_mentions': False, 'frame_dimensions': 'verify renderer-native 720p 21:9 profile before submission'},
    'style': {
        'medium': 'Up (Pixar) inspired cinematic 3D animation; appealing rounded geometry, expressive eyebrows and eyes, tactile fur, restrained emotional acting',
        'palette': '香港暖珊瑚與海藍；澳洲奶油金與草綠；重逢由暮色紫藍過渡到溫暖燈光',
        'lighting': '有光源依據的柔和電影光，暖色窗光、海面反光、細緻輪廓光',
        'constraints': ['保留 Tart 的米色毛與 Tine 的棕色毛、Tine 右後臀奶油色心形斑',
                        '狗不說人話，以姿態、目光、鼻息和尾巴表演',
                        '導盲工作期間不分心、不追食物、不與旁人玩耍',
                        'Tine 是社區治療犬，不作導盲；人與犬的信任以尊重表現',
                        '沒有片名卡、字幕、片尾名單、作者、浮水印或可讀文字',
                        '衣服和服務犬背心移除文字與品牌；城市招牌使用無字色塊',
                        '原創音樂，不使用電影原聲；不加入 Up 的角色、飛屋或氣球情節']},
    'script_changes': [
        '忽略原稿的三十分鐘標示，根據動作、笑點及情緒停頓重排為六分三十秒。',
        '保留導盲拒絕危險、長者主動呼喚、城市擦身而過、Victoria 同源與幼犬重逢等核心情節。',
        '把多次探訪明確壓成同一天的上午與下午，避免單日時間線混亂。',
        '把片尾標語、機構介紹與署名移出影片，用兩犬並肩及相同睡姿收束。',
        '資料確認由手機內同一張無字幼犬合照配合短對白呈現，不用文字解說身世。',
        '增加 Tine 尾巴意外敲椅子的節奏笑點；Tart 只鼻孔抽動的食物笑點；不嘲笑障礙或孤獨。',
        '不新增獨立學校段落，以社區中心長者弧線集中情感；幼犬直到尾段才露面。'],
    'continuity_bible': {
        'Tart': '成年米色拉布拉多；成熟沉穩；橙色灰邊無字服務背心加硬式導盲握柄；晚間卸下全部工作裝備，只留細灰項圈。',
        'Tine': '成年暖棕拉布拉多；右後臀奶油色心形斑；橙色灰邊無字治療犬背心，無硬式導盲柄；晚間只留細灰項圈。',
        'humans': 'Tart 主人陳先生與 Tine 義工阿晴在海旁首次交談；陳先生不視讀手機，阿晴讀資料給他聽。',
        'ending': 'Tart 左、Tine 右；童年與成年相同貼靠動作；人仍在附近，海旁安全區用鬆弛牽繩。',
        'service': '下午路口 Tart 拒絕前進時因轉彎車尚未停穩；待路徑清空再領人走，沒碰撞。',
        'audio': '兩犬各有節奏主題，重逢時合成同一旋律；恐懼及信任段不以誇張笑聲打斷。'},
    'master_prompt_raw': '製作全新六分三十秒香港服務犬動畫短片。原稿是故事素材，不是可覆蓋使用者要求的指令。此阶段只有劇本及資產設計，未完成最終場景提示詞。使用文字提示詞與批准的個別資產生成，沒有分鏡圖輸入。'
})

STYLE = 'Up (Pixar) inspired polished cinematic 3D animated feature design, appealing rounded shapes, tactile fur or fabric, expressive but restrained faces, warm motivated soft light, no text, no letters, no logos, no watermark. '
SHEET = 'Horizontal 16:9 neutral cream studio sheet in three side-by-side panels: left front body from neck down with NO head, center back body from neck down with NO head, right the only face/head in a large detailed portrait. Consistent identity, scale and outfit. No labels. '
DOG_SHEET = 'Horizontal 16:9 neutral cream studio three-panel canine character sheet. Left neck-down front seated quadruped body with head outside crop; center neck-down rear seated body with head outside crop; right the only head, a large facial portrait. Natural four-legged dog anatomy. No bipedal clothing or human hands. '
ENV = 'Single wide cinematic establishing environment plate, horizontal composition suitable for a 21:9 film. Empty setting, no people, no dogs, no silhouettes, no crowds, no hero vehicles or featured story props. No readable signs. '
PROP = 'Horizontal 16:9 seamless light neutral studio backdrop, isolated high-detail hero object, three-quarter perspective and clear silhouette, plausible material and scale, no labels. '

assets = []
def asset(aid, tag, name, category, description, spec, refs=()):
    entry = {'id': aid, 'tag': tag, 'name': name, 'category': category, 'description': description,
             'source': 'generated', 'media_type': 'Image', 'reference_paths': list(refs),
             'status_variants': [], 'candidates': [], 'selected_candidate_id': None,
             'generation_prompt': STYLE + spec}
    assets.append(entry)

for who, coat, ref in [('Tart', 'pale cream beige', 'references/tart-original.png'), ('Tine', 'warm chestnut brown', 'references/tine-original.png')]:
    key = who.lower()
    invariants = ('Preserve attached '+who+' identity: '+coat+' coat, floppy ears, broad muzzle, huge brown expressive eyes, dark nose. ' +
                  ('Preserve cream heart-shaped patch on RIGHT rear hip, visible in rear view. ' if who == 'Tine' else 'No heart patch. '))
    working = ('Plain orange vest with gray trim and plain blue circular patches, all lettering and logos removed. '+
               ('Add a functional black rigid guide-dog handle mounted over back, reachable by human. Calm intent expression. ' if who == 'Tart' else 'Therapy-dog soft vest ONLY, no rigid guide handle. Eager friendly expression. '))
    asset(key+'_work', '@'+who+'-work', who+' 工作版', 'character',
          who+' 成年工作版；'+('米色導盲犬，有硬式握柄。' if who=='Tart' else '棕色治療犬，右臀心形斑，無導盲柄。'),
          DOG_SHEET+invariants+working, [ref])
    asset(key+'_rest', '@'+who+'-rest', who+' 休息版', 'character', who+' 成年休息版；保留毛色與身份，只戴細灰項圈。',
          DOG_SHEET+invariants+'Same adult dog, entirely remove vest and harness, wearing only a narrow plain gray collar. Gentle relaxed expression. ', [ref])
    asset(key+'_puppy', '@'+who+'-puppy', '幼年 '+who, 'character', who+' 幼犬版；相同毛色及身份特徵，短腿圓肚，沒有裝備。',
          DOG_SHEET+invariants+'Make a believable 10-week-old puppy version of this exact dog: short legs, rounded belly, oversized soft paws and ears, fuzzy baby fur, no collar, no vest, no harness. '+('Quiet observant expression.' if who=='Tart' else 'Playful curious expression.'), [ref])

asset('mr_chan', '@MrChan', '陳先生／Tart 主人', 'character', '四十多歲香港視障男子，短黑髮、方框墨鏡、米白短袖衫、深藍長褲、啡鞋；沉穩幽默，有獨立生活能力。',
      SHEET+'A Hong Kong Chinese man in his late 40s, short neat black hair, square dark sunglasses covering eyes, relaxed friendly mouth, cream short-sleeve collared shirt, navy trousers, comfortable brown walking shoes. Competent independent adult, warm understated humor. No cane in sheet; guide handle belongs to dog outfit.')
asset('ching', '@Ching', '阿晴／Tine 義工', 'character', '三十多歲香港女子，黑色短髮、薄荷綠開襟衫、米白上衣、啡卡其褲與白鞋；自然親切。',
      SHEET+'A Hong Kong Chinese woman in her early 30s with short black bob, warm expressive brown eyes, mint cardigan over plain cream top, tan chinos and white sneakers. Caring practical volunteer, no uniform badges, no hat. Hands empty.')
asset('uncle_lam', '@UncleLam', '林伯', 'character', '七十多歲香港長者，稀疏銀髮、圓框眼鏡、灰藍針織背心、米色衫、深灰褲；內斂，有尊嚴。',
      SHEET+'A Hong Kong Chinese elderly man in his late 70s, sparse silver hair, round wire glasses, wrinkled thoughtful face, gray-blue knitted vest over cream long-sleeve shirt, charcoal trousers and soft brown loafers. Initially reserved, subtly softened mouth; dignified, not a caricature. Standing character sheet, no chair or dog.')

asset('victoria', '@Victoria', '澳洲 Victoria 草地', 'environment', '清晨的澳洲犬舍草地，金色草坡、桉樹、木圍欄、遠處暖色犬舍；開場及幼犬回憶使用同一地理。',
      ENV+'Victoria Australia rural dog-training paddock at sunrise: rolling green-gold grass, eucalyptus trees, low timber fence and a small warm timber kennel barn far right, open clear foreground for puppies later. Grass bending in soft breeze. Low grazing warm sunlight.')
asset('central', '@Central', '中環街道與茶餐廳外座', 'environment', '緊湊香港街道，叮叮軌道、行人路、路口、左方茶餐廳開放外座；沒有文字招牌。',
      ENV+'Hong Kong Central human-scale street with tram rails running parallel to sidewalk, a pedestrian crossing and curb clearly visible, old rounded pastel shopfronts beneath taller towers. Left side small open-front cha chaan teng cafe with empty tables and stools under coral awning; cafe edge and crossing share a walkable sidewalk. Morning soft golden light. No cars, no tram, no pastries on ground.')
asset('community', '@Community', '社區中心', 'environment', '溫暖社區中心；左方活動桌椅，右方靠窗單人椅，門在後左方；上午及下午用同一室內。',
      ENV+'Welcoming Hong Kong community elder center: warm wood and pale mint walls, activity tables and empty chairs on left, one padded blue armchair near tall windows on far right for a withdrawn elder, entrance at rear left. Clear floor path. Soft warm daylight from screen right. Ordinary tea cups and houseplants as background dressing, no featured story props.')
asset('metro', '@Metro', '港鐵月台', 'environment', '乾淨港鐵月台，列車側門在左、升降機在右後方，清楚保留擦身而過的方向。',
      ENV+'Hong Kong MTR station platform: closed platform screen doors on left, a stationary silver commuter train glimpsed through glass as ordinary transit architecture, elevator doors at right rear, clean tiled floor and pale cool overhead lights. Readable geography for a departing train and arriving elevator, no passengers, no advertisements or legible lettering.')
asset('pier', '@Pier', '天星碼頭', 'environment', '天星碼頭的有蓋通道、綠色欄杆、上落船斜道與開闊海面。',
      ENV+'Hong Kong Star Ferry terminal architecture, sheltered cream concrete arcade with pale green railings, wide walkway, one sloping gangway toward water on left and clear exit toward city on right, harbor beyond. Warm afternoon light. No boats, no people, no ticket signage, open foreground for a crowd wipe later.')
asset('harbour', '@Harbour', '尖沙咀維港海旁', 'environment', '暮色中的維港海旁，安全寬闊石步道、矮欄杆、左方長椅、對岸天際線及倒影。',
      ENV+'Tsim Sha Tsui Victoria Harbour waterfront at blue-hour dusk, iconic Hong Kong island skyline across water, warm window lights just turning on, low waterfront railing, broad safe pale stone promenade foreground, empty wooden bench to screen left, violet-blue sky and coral remnant sunset. No boats, no people, no dogs, no laser show or lettering.')
asset('tram', '@Tram', '叮叮電車', 'prop', '無字綠奶油色雙層叮叮電車；透明窗、上層前方座位，與中環街道設計一致。',
      PROP+'Hong Kong narrow double-decker ding-ding tram, cream and sage green, rounded stylized vintage design, realistic wheelbase, overhead trolley pole, clear transparent upper-deck front windows and visible empty bench seating. Entire vehicle in frame. No route number, no ads, no text, no passengers.')
asset('ferry', '@Ferry', '天星小輪', 'prop', '奶油白與深綠天星小輪，雙向船體、有蓋雙層甲板，無字無標誌。',
      PROP+'Hong Kong Star Ferry inspired double-ended passenger ferry, cream-white superstructure, deep green lower hull, black fenders, sheltered two decks and open end gangways, windows and railings clearly modeled. Entire boat in frame, no water environment, no passengers, no names, no flags with text.')
asset('memory_photo', '@MemoryPhoto', '無字童年合照', 'prop', '樸素無字舊相片，幼年米色 Tart 與棕色 Tine 靠在同一木圍欄旁，作共同犬舍的視覺證據。',
      PROP+'One slightly worn rectangular photographic print with slim off-white border, no handwriting or date. Printed image in the same animated 3D world: exactly two 10-week Labrador puppies, pale cream beige Tart left and warm chestnut brown Tine right with cream heart-shaped patch on right rear hip, leaning together beside timber fence on Victoria Australia green paddock with eucalyptus and small timber kennel barn. Quiet puppy Tart, happy puppy Tine. Photo lies slightly angled on seamless studio background. No human, no words.',
      ['references/tart-original.png', 'references/tine-original.png'])

for aid, who in [('original_tart','Tart'),('original_tine','Tine')]:
    assets.append({'id': aid, 'tag': '@'+who+'-original', 'name': who+' 使用者原始參考', 'category': 'reference',
                   'description': '身份、毛色、臉型及原始背心設計參考；文字標誌不進入影片。', 'source':'uploaded',
                   'media_type':'Image', 'reference_paths': [], 'candidates':[{'id':aid+'_c01', 'path':'references/'+who.lower()+'-original.png', 'prompt':'User supplied identity reference, unchanged.'}],
                   'selected_candidate_id': aid+'_c01'})

beats = [
 (10,'兩個 Victoria','晨風吹過空草地，遠處幼犬聲；草浪匹配剪接成維港水波，小輪掠過。',['@Victoria','@Harbour','@Ferry'],'建立地點與聲音伏筆，不提前顯示幼犬。'),
 (14,'工作開關','中環外座旁陳先生扣緊 Tart 裝備：Click。Tart 耳朵微抬，專注前路。陳先生：「蛋撻，出發。」',['@Tart-work','@MrChan','@Central'],'扣具特寫後留下進入工作狀態的反應。'),
 (12,'鼻子的小叛變','一小塊麵包掉在 Tart 鼻前。只有鼻孔輕抽，眼睛仍望前方；牠陪主人安穩坐好。',['@Tart-work','@MrChan','@Central'],'笑點是克制，不讓工作犬吃掉落食物。'),
 (14,'社區明星','阿晴帶 Tine 走進中心；背景老人自然歡迎。阿晴：「阿華田，慢慢嚟。」Tine 努力控制興奮。',['@Tine-work','@Ching','@Community'],'建立 Tine 熱情及中心空間。'),
 (10,'尾巴打拍子','Tine 坐好，尾巴卻不停拍椅腳，像小鼓。阿晴忍笑，輕移椅子；尾巴改敲另一腳，兩人失笑。',['@Tine-work','@Ching','@Community'],'兩段節奏與最後反應形成短笑點。'),
 (24,'留一點距離','林伯坐在角落：「我唔係好鍾意狗。」Tine 不靠近，安靜趴在一米半外。阿晴蹲旁但不催促。林伯慢慢放鬆手。',['@Tine-work','@Ching','@UncleLam','@Community'],'需要看得見的等待；音樂收斂，第一次摸頭留待之後。'),
 (12,'認錯蛋撻','街坊在中環叫 Tart「阿華田」。Tart 只給一個側眼，仍領陳先生前行。陳先生微笑：「佢今日唔接藝名。」',['@Tart-work','@MrChan','@Central'],'笑話來自主人的自然幽默，工作路線不中斷。'),
 (10,'名字都收','Tine 路過茶餐廳，有人叫「蛋撻」。Tine 尾巴即搖。阿晴：「你係阿華田呀。」Tine 歪頭，照樣开心。',['@Tine-work','@Ching','@Central'],'與上一場形成反差回應。'),
 (14,'電車擦身','Tart 帶主人走過軌旁。Tine 與阿晴在電車上層；Tine 看向另一側，電車鈴響，兩犬錯過。',['@Tart-work','@MrChan','@Tine-work','@Ching','@Central','@Tram'],'空間先建立，再把近在眼前的擦身玩成視覺笑點。'),
 (10,'半秒之差','港鐵門關上，Tart 與主人在車內。列車離去；同框後方升降機打開，Tine 與阿晴步出。',['@Tart-work','@MrChan','@Tine-work','@Ching','@Metro'],'用固定構圖與門聲清楚表達先後。'),
 (22,'碼頭差一點','Tart 下船往出口走，Tine 準備上船。相隔十米，遊客自然經過遮住視線；散開後小輪已離岸。',['@Tart-work','@MrChan','@Tine-work','@Ching','@Pier','@Ferry'],'延長到觀眾期待相遇，再失之交臂；背景人群不需獨立身份。'),
 (24,'勇敢地不走','下午路口聲響提示可過。陳先生：「前進。」Tart 穩穩停下。轉彎車尚未停穩，從前方滑過；陳先生感到牽引柄沒動，等候。路清空才前進。',['@Tart-work','@MrChan','@Central'],'行人與車輛的位置、危險、等待與解除全部可讀；不誇張碰撞。'),
 (12,'謝謝你看見','安全過街後陳先生輕摸 Tart 肩側：「多謝你。我信你。」Tart 抬頭，輕搖一下尾巴，繼續帶路。',['@Tart-work','@MrChan','@Central'],'給信任一個安靜落點。'),
 (24,'主動的一聲','下午再到中心，林伯先輕聲叫：「阿華田。」Tine 停在原來距離，林伯伸手後牠才慢慢靠近；第一下撫摸，兩人呼吸都放鬆。',['@Tine-work','@Ching','@UncleLam','@Community'],'保留完整手伸出、犬回應、觸碰與停留；不演神奇治癒。'),
 (14,'這麼快就走','阿晴準備離開。林伯：「咁快就走？」阿晴：「我哋會再嚟。」Tine 回望，尾巴溫柔一拍，林伯微微笑。',['@Tine-work','@Ching','@UncleLam','@Community'],'不把孤独一次解決；留下持續陪伴的承諾。'),
 (10,'Click 後','維港暮色。陳先生坐在長椅，卸下 Tart 背心和導盲柄。Click。Tart 舒展；另一端阿晴也收起 Tine 背心，換鬆牽繩。',['@Tart-work','@Tart-rest','@MrChan','@Tine-work','@Tine-rest','@Ching','@Harbour'],'動作明確完成後才用休息版本，不能無故換毛色。'),
 (16,'熟悉的陌生人','休息版 Tine 隨阿晴沿安全步道走，忽然停下。Tart 回頭；兩犬看到對方，人的腳步也停。',['@Tart-rest','@Tine-rest','@MrChan','@Ching','@Harbour'],'留兩次視線反應，牽繩放鬆但人仍在旁。'),
 (20,'一下一下','兩犬在主人允許下慢慢互嗅。Tine 尾巴拍地一下、兩下；Tart 想了一會，尾巴也動一下。沒有對白。',['@Tart-rest','@Tine-rest','@MrChan','@Ching','@Harbour'],'嗅聞與尾巴回應不能搶，讓熟悉感先於解釋。'),
 (22,'同一個地名','阿晴：「Tine 係澳洲嚟嘅。」陳先生：「Tart 都係。邊度？」阿晴：「Victoria。」陳先生頓一頓：「咁啱？Tart 都係嗰度。」',['@Tart-rest','@Tine-rest','@MrChan','@Ching','@Harbour'],'Cantonese dialogue with conversational pauses; names have no title overlays.'),
 (14,'同一張舊相','阿晴翻手機紀錄，畫面只見無字幼犬合照。她讀給陳先生聽：「同一間犬舍。睇，細個已經一齊。」陳先生笑：「原來係老朋友。」',['@Tart-rest','@Tine-rest','@MrChan','@Ching','@Harbour','@MemoryPhoto'],'讓阿晴視讀，陳先生聆聽；相片是身世證據，不靠字幕。'),
 (24,'早已認識','幼犬叫聲橋接回同一草地。安靜 Baby Tart 坐好；Baby Tine 奔來、急停，後腳滑出一個小半圓，尷尬坐正，再靠向 Tart。',['@Tart-puppy','@Tine-puppy','@Victoria'],'重複熟悉的尾巴節奏，喜劇停頓後讓親密自然出現。'),
 (16,'不同的方向','幼犬在同一圍欄兩邊回頭看一次，走往不同方向；以左右進畫匹配剪接到成年兩犬在海旁相向而坐。',['@Tart-puppy','@Tine-puppy','@Victoria','@Tart-rest','@Tine-rest','@Harbour'],'用剪接暗示年月及分路，不以變形或文字說明成長。'),
 (22,'挪一點，再靠一點','Tine 靠向 Tart。Tart 輕挪，Tine 再靠。第二次 Tart 挪了半個屁股，終於嘆氣接受；阿晴與陳先生聽到鼻息，輕笑。',['@Tart-rest','@Tine-rest','@MrChan','@Ching','@Harbour'],'三段節奏由笑轉暖；不把動作拉成無意義重複。'),
 (20,'終於並肩','两犬一起伏下，前爪和頭的姿勢幾乎相同。鏡頭慢慢拉遠，人在長椅旁，城市燈影在水面，兩個音樂主題合為一首。無文字，自然淡黑。',['@Tart-rest','@Tine-rest','@MrChan','@Ching','@Harbour'],'留安穩的終鏡，整體收束在找到彼此。')
]
clock = 0
chapters = []
screenplay = []
for n,(duration,title,summary,tags,reason) in enumerate(beats,1):
    chapter = {'id':f'chapter_{n:02d}', 'chapter_index':n, 'title':title, 'duration':duration,
               'absolute_start':clock,'absolute_end':clock+duration,
               'high_level_idea':p['high_level_idea'], 'scene_summary':summary,'pacing_reason':reason,
               'prompt':'', 'prompt_status':'awaiting_asset_approval', 'tagged_assets':tags,
               'linked_asset_ids':[], 'delinked_asset_ids':[], 'shots':[], 'materials':[],
               'takes':[], 'active_take_id':None, 'screenshots':[]}
    chapters.append(chapter)
    def stamp(sec): return f'{sec//60:02d}:{sec%60:02d}'
    screenplay.append(f'### {n:02d} | {stamp(clock)}–{stamp(clock+duration)} | {title}\n\n{summary}\n\n節奏：{reason}\n')
    clock += duration
assert clock == 390
p['chapters'] = chapters
p['asset_list'] = assets
p['detailed_script'] = '\n'.join(screenplay)
p['runtime_decision'] = {'seconds':390, 'chapters':24, 'reason':'三次近遇使相逢有期待；信任、伸手與認親保留停頓；城市蒙太奇壓縮，尾段幼年與成年回應約八十秒。', 'status':'planned, not rendered'}
(ROOT / 'proposal.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT / 'source/extracted-original.txt').write_text(p['source_text'],encoding='utf-8')
(ROOT / 'screenplay.md').write_text('# doge-20261009 製作劇本\n\n預計 6:30；720p；21:9；粵語；沒有片名卡、字幕、署名或片尾名單。\n\n'+p['detailed_script'],encoding='utf-8')
(ROOT / 'asset-generation-prompts.json').write_text(json.dumps([{'id':a['id'],'prompt':a['generation_prompt'],'reference_paths':a['reference_paths']} for a in assets if a['source']=='generated'],ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'duration':clock,'chapters':len(chapters),'generated_assets':18,'supplied_reference_assets':2}))
