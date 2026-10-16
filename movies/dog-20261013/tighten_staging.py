"""Repair observed staging failures using the same approved original assets."""
import json
from pathlib import Path
from render_movie import ROOT, helper, read, save

p=read(ROOT/'project.json');v=json.loads(json.dumps(p))
assets={int(a['id'].split('_')[1]):a for a in p['asset_list']}

def revise(index,refs,first,shots,locks):
    c=v['chapters'][index-1]
    duration=c['duration']
    assert shots[0]['start']==0 and shots[-1]['end']==duration
    tags=[assets[i]['tag'] for i in refs]
    roles=[]
    for i in refs:
        a=assets[i]
        role='身分、造型與指定裝備，單一角色，不複製角色表。' if a['category']=='character' else '原物件的外形、材質與空間設計，去除多視圖分格與標籤。'
        roles.append(a['tag']+'：'+role)
    lineparts=[]
    for i,s in enumerate(shots):
        s.update(end_state=s['action']+'；保留末端可剪接自然微動。')
        lineparts.append(f"Shot {i+1} ({s['start']}s-{s['end']}s): {s['action']} Camera: {s['camera']} Audio: {s['audio']}"+(' Hard cut.' if i+1<len(shots) else ''))
    new='''SCENE CONTEXT
依v7原劇本，此鏡修正動作與空間，不改故事、不加对白。親切、幽默、自然的Up式柔和細緻3D動畫，完全保留核准角色與原道具設計。
OUTPUT SETTINGS
'''+f'{duration} seconds, 1080p 1920x1080, 16:9, real-time. '+('Single continuous shot.' if len(shots)==1 else 'Only the explicitly timed hard cuts below.')+'''
ACTIVE REFERENCES
'''+ '\n'.join(roles)+'''
FIRST FRAME AND LOCATION MAP
'''+first+'''
TIMELINE AND SHOT SEQUENCE
'''+ '\n'.join(lineparts)+'''
LIGHTING AND PHYSICS
香港上午自然日光，室內窗光與柔和毛髮材質。人犬腳掌和鞋接地；手、握柄、鞍有實際接觸；皮帶和金屬把手保持連接，牽繩扣在項圈。所有動作有重量與因果順序。
PERFORMANCE AND AUDIO
逐字粵語对白，成年人物穩定聲線，開口者才動嘴。狗不說話，保持細緻耳尾、嗅覺、呼吸與小表情。環境聲與克制暖心原創音樂，音樂低於对白。完整音訊只包含所列对白與本場環境/動作聲，不新增旁白。
TARGETED STAGING LOCKS
'''+locks+'''
POSITIVE CONSTRAINTS
林先生同一藍綠外套、白襯衫、灰褲、棕鞋、深色眼鏡；蛋撻全身淡奶油色，成年拉布拉多非幼犬，無心形斑；工作棕色皮革鞍、銀把手棕握柄、棕項圈和棕牽繩。阿華田栗棕、右臀奶油心形、正確紅色圓章橙領巾、另戴橙項圈，橙牽繩只扣項圈。阿晴核准綠襯衣白內搭、深褲、斜袋。每張角色表只代表一位有正常頭部的角色。
No author, titles, subtitles, captions, credits, watermarks, reference grids, headless subjects or extra copies of the main cast. 店內物件上的文字只作自然道具，不是字幕。
'''
    c.update(prompt=new,shots=shots,tagged_assets=tags,linked_asset_ids=[assets[i]['id'] for i in refs],
        prompt_status='revised_after_visual_inspection',revision_reason='Repair observed staging failure in actual take, same approved images')
    (ROOT/'chapters'/c['id']/'prompt.txt').write_text(new,encoding='utf-8')
    save(ROOT/'chapters'/c['id']/'shots.json',shots)

def shot(a,b,action,camera,audio):return {'start':a,'end':b,'action':action,'camera':camera,'audio':audio}

grip='林先生在行走時右手必須包住棕皮握柄；銀鞍把手從犬背連至手，兩者清楚可見，不能只拉牽繩。左手另握鬆棕牽繩；鞍形與把手高度適合成人自然垂手。犬肩高近林先生膝部，人體與犬體比例固定。'
revise(9,[3,6,16,35],
    '住宅門外，林先生畫面右站定，蛋撻在他左前方；箱在前方左側部分阻路。右手已握住導盲鞍棕握柄，銀把手與犬背鞍連接；左手鬆繩。35mm側向全身構圖須看見握柄接觸。',
    [shot(0,12,'@林先生_深色眼鏡 右手保持握鞍棕握柄，@蛋撻_成年_導盲鞍項圈牽繩 帶他自然繞過 @住宅門外_貨物箱 後左行；到街口聞麵包香微抬頭，继续前行。','35mm固定侧向中遠景，輕跟移但始終包含人手、銀把手和犬。','0-6s脚步與城市早聲；6-10s 林先生 {今日間麵包舖咁早開爐。}；10-12s腳步。')],grip)
revise(15,[3,6,35],
    '窄行人路圍欄左牆右，人犬從右向左通過。林先生右手已包住棕皮鞍握柄，左手牽繩，蛋撻在左前方。後方途人只跟随，不阻擋鏡頭。',
    [shot(0,18,'@蛋撻_成年_導盲鞍項圈牽繩 放慢帶 @林先生_深色眼鏡 通過欄牆間；手始終握鞍而非僅牽繩。後方途人喊借借，看見鞍改從另一側走；人犬到店門聽收音機停下。','35mm側前方跟拍，人手到銀把手全程可見；最後停在店門外。','3-5s途人 {借借——}；12-16s林先生 {阿強，今日有冇位？}；腳步與店內收音機聲。')],grip)
revise(16,[3,6,47],
    '茶餐廳入口在左，窗口右；空早餐桌在窗口內側。林先生剛入門，蛋撻四腳始終在地板。阿強是未戴眼鏡的短黑髮年輕店員、綠圍裙，站空椅旁。林先生桌上尚無早餐。',
    [shot(0,16,'店員阿強拉開椅子讓通道，@林先生_深色眼鏡 安全坐下，@蛋撻_成年_導盲鞍項圈牽繩 直接走入桌下伏地，四腳不上椅、不碰桌沿。兩人說原对白，桌上保持空，早餐到下一段才供應。','40mm桌旁中景，前11秒坐下對話；後5秒攝影機略降看桌下犬與林先生鞋。','1-6s阿強 {有。你個朋友又未到呀？}；6-13s林先生 {今日冇約佢。畀自己食餐準時嘅早餐。}；椅脚聲。')],
    '工作犬從頭到尾只在地面。絕不立起、不把前腳放椅或桌、不對食物要求接觸。阿強和林先生是兩位不同的人，店員無深色眼鏡；林先生不蹲到桌下。')
revise(17,[3,6,34],
    '固定低機位只拍桌下地板。蛋撻伏下，頭在中間，下巴接地。林先生坐桌旁，只可見黑灰褲腳與棕鞋，頭與上身永遠在畫面外、桌面上方。隔壁小孩只見鞋與短暫手；阿強只有手入鏡，無臉進桌下。',
    [shot(0,24,'@蛋撻_成年_導盲鞍項圈牽繩 安靜伏地，@茶餐廳_早餐餐具與多士 的一小塊多士在4秒由旁桌掉到鼻前。犬鼻子稍動，四腳與身體不移，不吃食物。8秒孩子手欲推多士；10秒店員阿強另一隻手先拾起並帶走多士，孩子手收回。林先生聽到事件，在桌上方說多謝，只有鞋可見。最後犬安靜呼吸，地上已無多士。','65mm固定低機位，一段連續桌下特寫；禁止抬鏡看臉。','落地小聲、衣料；11-16s阿強畫外低聲 {佢做緊嘢，唔好餵佢。}；17-19s林先生畫外 {多謝。}；其餘安靜。')],
    '林先生從不俯身、下桌、爬桌下或伸手拾多士，僅畫外聲。沒有任何成人臉出現在桌下。拾多士者只能是阿強的手。犬不吃不舔。小孩不是坐在狗旁的新主角。')
revise(18,[3,5,6,8,46,47],
    '茶餐廳內側看玻璃窗，蛋撻在前景桌下朝室內，林先生在內部椅上僅腿可見。黃色巴士在窗外近車道朝左停靠遮窗；阿晴阿華田在巴士遠側人行道，從未在餐廳內。',
    [shot(0,5,'@蛋撻_成年_導盲鞍項圈牽繩 在窗內桌下朝室內，@林先生_深色眼鏡 仍室內座椅上，窗外 @場04_巴士_外觀 停著完全遮住遠側人行道。','50mm窗內低中景，窗框是明確內外分隔。','茶餐廳杯碟、巴士低引擎；無对白。'),
     shot(5,12,'切巴士遠側人行道，只出現 @阿晴 與 @阿華田_成年_橙色領巾項圈牽繩；栗棕犬停看風吹葉子，阿晴不拉、等一下再左行。這一鏡絕無林先生或蛋撻；他們留在餐廳內。','40mm外側中景，巴士是遮擋背景；人犬左行。','海港城市聲、葉子細聲、橙繩衣料；無对白。'),
     shot(12,18,'切回原窗內鏡位，@場04_巴士_外觀 朝左開走，遠側路已空。蛋撻仍桌下朝另一方向，兩犬沒有看見對方。','與第一鏡相同50mm機位；玻璃與窗框保持原樣。','引擎遠離、餐廳聲；無对白。')],
    '奶油蛋撻與林先生只在窗內，栗棕阿華田與阿晴只在窗外。四者不站同一人行道。兩犬不相遇、不互望、不嗅聞。巴士左行、鏡位軸線固定。')

save(ROOT/'proposal-staging-repairs.json',v)
print(helper.save(ROOT,p,v,'Repair inspected working-hand contact and café staging with the approved original references'))
