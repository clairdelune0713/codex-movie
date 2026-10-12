import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import re
import shutil
from PIL import Image, ImageDraw, ImageFont, ImageOps
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'exports' / 'adaptive-review'
OUT.mkdir(parents=True, exist_ok=True)
project = json.loads((ROOT / 'project.json').read_text(encoding='utf-8'))
assert project['revision'] == 14, 'Review proposal must be regenerated against current state'
now = datetime.now(timezone.utc).isoformat()
records = json.loads((OUT / 'generated-assets.json').read_text(encoding='utf-8'))
by_key = {r['key']: r for r in records}

def save_candidate(key, asset_id, candidate_id):
    r = by_key[key]
    source = Path(re.search(r'as (C:\\[^\n]+?\.png) by default', r['output_hint']).group(1))
    dest = ROOT / 'assets' / asset_id / (candidate_id + '.png')
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        shutil.copy2(source, dest)
    else:
        assert hashlib.sha256(dest.read_bytes()).digest() == hashlib.sha256(source.read_bytes()).digest()
    im = Image.open(dest)
    return {'id': candidate_id, 'path': dest.relative_to(ROOT).as_posix(), 'prompt': r['prompt'],
            'source_revision': 14, 'created_at': now, 'width': im.width, 'height': im.height,
            'generation_method': 'built_in_imagegen', 'freshness_note': 'No dependency fingerprint captured at submission; never backfilled.'}

defs = [
    ('harness', 'asset_harness', '@GuideHarness', 'Guide harness', '黑色皮革導盲鞍，連接完整的身體帶、側扣與硬質金屬拱柄。只供Tart工作時穿於橙背心外；夜晚完整卸下。', 'harness_c01'),
    ('ferry', 'asset_ferry', '@Ferry', 'Harbour ferry', '單一綠白雙層維港小輪，木座椅、圓窗駕駛艙、黑色防撞輪胎；無文字或品牌。', 'ferry_c01'),
    ('phone_v2', 'asset_origin_phone', '@OriginPhone', 'Puppy photograph on phone', '黑色橫向手機，螢幕只有澳洲犬舍舊幼犬合照：米金BabyTart在左，棕色BabyTine在右靠向牠；無文字介面。此正面角度不顯示Tine右後臀心斑。由Handler持有；不讓視障Owner依靠看螢幕得知來歷。', 'origin_phone_c02'),
]
for key, aid, tag, name, desc, cid in defs:
    candidates = []
    if key == 'phone_v2':
        candidates.append(save_candidate('phone', aid, 'origin_phone_c01'))
    candidates.append(save_candidate(key, aid, cid))
    project['asset_list'].append({'id': aid, 'tag': tag, 'name': name, 'category': 'prop',
        'description': desc, 'source': 'generated', 'media_type': 'Image', 'status_variants': [],
        'reference_paths': [], 'candidates': candidates, 'selected_candidate_id': cid})
    if key == 'phone_v2':
        project['asset_list'][-1]['reference_paths'] = ['assets/asset_babytart/babytart_c01.png', 'assets/asset_babytine/babytine_c01.png']
pier = next(a for a in project['asset_list'] if a['tag'] == '@pier')
pier['candidates'].append(save_candidate('pier', 'asset_pier', 'pier_c02'))
pier['selected_candidate_id'] = 'pier_c02'
pier['reference_paths'] = ['assets/asset_pier/pier_c01.png']
pier['description'] = '天星碼頭空場：左側到埗出口、右側上船等候門；中央寬闊空地，後景海面與香港島天際線。奶白柱配綠色下半部、綠欄杆，日光由左。無人犬、無小輪；小輪由獨立道具參考提供。'

for a in project['asset_list']:
    for candidate in a.get('candidates', []):
        im = Image.open(ROOT / candidate['path'])
        candidate.setdefault('width', im.width)
        candidate.setdefault('height', im.height)

for tag, supplied in [('@Tart', 'tart.png'), ('@Tine', 'tine.png')]:
    a = next(a for a in project['asset_list'] if a['tag'] == tag)
    c = next(c for c in a['candidates'] if c['id'] == a['selected_candidate_id'])
    incoming = Path('C:/Users/admina/Downloads/project/dog-test') / supplied
    assert hashlib.sha256(incoming.read_bytes()).digest() == hashlib.sha256((ROOT / c['path']).read_bytes()).digest(), 'Supplied adult design changed'

src = Path('C:/Users/admina/Downloads/doge-original-script.pdf')
archived = ROOT / 'source' / 'doge-original-script.pdf'
if hashlib.sha256(src.read_bytes()).digest() != hashlib.sha256(archived.read_bytes()).digest():
    archived = ROOT / 'source' / 'doge-original-script-request20261009.pdf'
    shutil.copy2(src, archived)
project['source_pdf_path'] = archived.relative_to(ROOT).as_posix()
project['source_text'] = '\n\n'.join(p.extract_text() or '' for p in PdfReader(src).pages)
project['duration_mode'] = 'adaptive'
project['total_duration_target'] = None
project['aspect_ratio'] = '21:9'
project['language'] = '繁體中文；少量人類對白用廣東話；狗沒有擬人對白'
project['output_profile'] = {'resolution': '720p', 'aspect_ratio': '21:9', 'final_width': 1680, 'final_height': 720,
    'fps': 30, 'audio': 'stereo', 'format': 'mp4', 'titles': False, 'subtitles': False, 'credits': False,
    'resolution_note': 'Request 720p from renderer; verify actual dimensions before assembly. Final 1680x720 is exact 21:9. Record any resize of provider native output explicitly.'}
project['style']['medium'] = 'Up般溫暖、圓潤有重量、表情細膩的電影級3D動畫；原創人物與原創配樂'
project['style']['constraints'] = [
    '成年Tart米金、成年Tine焦糖棕，身份與成年比例完全依照使用者附圖',
    'Tine心形斑只在解剖右後臀；角度看不到時不另加一個斑',
    '幼犬只在結尾回憶與手機舊照片中出現；無制服',
    '人類表演自然有尊嚴；笑點来自犬的個性、節奏與錯過',
    '多視角參考只代表同一個角色；四足重量接觸、牽繩與導盲鞍連接完整',
    '全片無片頭字卡、片中標題、字幕、片尾字卡、作者署名或其他署名',
    '服飾上的既有圖案是造型參考，禁止新增可讀姓名、標語或說明文字',
    '結尾以犬的相同睡姿、海港與音樂完成主題，不用文字總結',
]
project['script_changes'] = [
    '忽略PDF內30分鐘及既有10分鐘版本；按每個動作與情緒節點重排為352秒，不平均分配章長。',
    '保留澳洲到香港、兩種天賦、多次擦身、交通危險判斷、老人伸手、同犬舍與童年重逢的核心。',
    'PDF內宣言、組織資料與片尾句子不變成字卡；共同犬舍由少量廣東話和無字的舊幼犬照片交代。',
    '主人不能靠觀看手機得知結果：領犬員讀出犬舍來歷，主人用觸摸與回應參與重逢。',
    '以Tart的克制鼻尖和眼神、Tine尾巴輕拍椅子、錯名和最後挨近作幽默；不用羞辱弱勢角色作笑點。',
]
project['adaptation_notes'] = project['script_changes']
project['master_prompt_raw'] = ''
project['asset_review'] = None
project['render_state'] = {'status': 'awaiting_asset_approval', 'final_prompts': 'pending_after_approval',
    'video_generation': 'not_submitted_for_adaptive_cut', 'delivery': 'not_rendered',
    'prior_delivery_note': 'Earlier 600-second output belongs to revision 14 and is not the requested new cut.'}

# Each row is a story beat chosen before submission prompts. No downstream render prompt is finalized here.
rows = [
 (8, '草地、風與遠處幼犬聲建立未知的共同起點；草浪的形狀接到下一段海浪。', '八秒足以讀懂空場與聽見隱約幼犬，避免開場拖長。', [], ''),
 (8, '維港晨光中小輪駛過，香港甦醒；不顯示地名字幕。', '短大全景建立香港，靠剪接呼應澳洲。', ['@Ferry'], ''),
 (12, '主人摸到鞍扣，為Tart扣妥導盲鞍；Click之後Tart停止小動作、望向前路。', '扣合動作、專注反應和起步各有可讀的時間。', ['@GuideHarness'], 'Owner：{好，蛋撻，出發。}'),
 (12, 'Tart引導主人繞過行人道障礙；主人配合轉向，二者步伐逐漸一致。', '讓觀眾看懂安全路線與彼此信任。', ['@GuideHarness'], ''),
 (8, '茶餐廳一小口食物落在附近，Tart鼻尖動一下、偷瞄、最後端正抬頭；主人微笑。', '喜劇採誘惑、微反應、端正三拍，笑點後即剪。', ['@GuideHarness'], ''),
 (12, 'Tine與領犬員踏入中心，聽到呼喚尾巴連拍空椅腳；牠回頭像自己也被聲音嚇了一下。', '尾巴喜劇需要期待、聲音、反應，但不延長進門。', [], '背景長者：{阿華田嚟喇！}'),
 (10, 'Tine輕嗅老人伸出的手，隨後伏低讓一個緊張的小朋友自行靠近；領犬員始終看顧。', '用兩個很短的可見回應呈現牠懂得不同界線。', [], ''),
 (8, '窗邊老人不參與熱鬧，把身體轉向窗；Tine注意到他的退縮，熱鬧聲漸遠。', '對比热鬧與孤單，只留必要的拒絕和Tine注意。', [], 'Elder：{我唔鍾意狗。}'),
 (20, 'Tine在老人一臂之外伏下，把下巴放在前爪，目光轉開；老人偷看牠，手指鬆開。', '最長的安靜等待讓陪伴有重量；呼吸、目光與手指仍然推進情緒。', [], ''),
 (14, '老人慢慢伸手，停一下；Tine不搶先，直到手碰上額頭才輕輕閉眼；老人嘴角第一次放鬆。', '伸手猶豫、同意接觸、微笑都不能被快剪。', [], ''),
 (10, '领犬員收拾準備走，老人抬頭挽留；Tine回望，尾巴輕輕掃地。', '短對白後保留回望，使情緒轉折自然落地。', [], 'Elder：{咁快就走喇？} Handler：{我哋會再嚟。}'),
 (12, '中環街口Tart陪主人向前走；電車經過，上層Tine偏偏回頭望另一邊，視線剛好錯開。', '同一地理軸線交代二者距離，保留一拍「差一點」。', ['@GuideHarness'], ''),
 (10, 'Tart與主人所在列車門關上，列車離開；對面升降機門才打開，Tine與領犬員步出。', '一扇關、一扇開形成清楚的機械喜劇節拍。', ['@GuideHarness'], ''),
 (6, '同一固定街角先見Tine離去，明確時間剪接後Tart從同一角落經過；都沒有看見彼此。', '最短的錯過作節奏變化，避免重複同一場景。', ['@GuideHarness'], ''),
 (12, '一個街坊對Tart叫阿華田，Tart停一個眼神；剪到Tine被叫蛋撻，牠立即歡喜搖尾。', '相同觸發配兩個相反反應，建立完整笑點。', ['@GuideHarness'], '背景街坊分兩鏡：{阿華田！}／{蛋撻！}'),
 (12, '碼頭Tart與主人從左側到埗出口步出；右側Tine與領犬員準備登上小輪，僅相隔十餘米。', '這次最近的錯過必須先讓觀眾讀懂左右與距離。', ['@Ferry', '@GuideHarness'], ''),
 (8, '一小群遊客暫時遮住兩犬；人群散去Tart已離開，小輪載Tine與領犬員離岸，Tine才轉頭。', '遮擋、揭露、晚一拍回頭構成失之交臂的收束。', ['@Ferry'], ''),
 (14, '行人提示聲響起，主人示意前進；Tart察覺轉彎車仍逼近，穩穩停在路沿內。', '讓危險位置和拒絕動作明白可見，不用誇張追車。', ['@GuideHarness'], 'Owner：{前進。}'),
 (16, '車輛擦過斑馬線後停下，Tart仍等安全空隙；主人感到停頓，鬆下肩膀輕碰牠，二者安全過路。', '等待、理解和安全前進讓信任成為實際選擇。', ['@GuideHarness'], 'Owner，低聲：{好彩有你。}'),
 (16, '第二次探訪老人先叫Tine名字；牠回頭，控制興奮慢步走近；老人主動伸手，椅腳這次只被尾巴輕拍一下。', '呼應早前尾巴笑點，並讓老人主動的改變有停頓。', [], 'Elder，輕聲：{阿華田，過嚟吖。}'),
 (10, '傍晚主人完整解下Tart工作鞍，握在身邊；扣聲Click後Tart鬆肩，仍穿橙背心，以普通牽繩散步。', '一次完整卸鞍和身體放鬆清楚標誌下班。', ['@GuideHarness'], 'Owner：{收工喇。}'),
 (10, '夜色維港前Tart坐看水面；Tine與領犬員從另一端走來，牠忽然慢下腳步。', '以海風和安靜姿態轉入重逢，不加入多餘事件。', [], ''),
 (12, 'Tine停下；Tart回頭，兩犬對視後慢慢靠近，在鬆牽繩下輕嗅彼此，不猛衝。', '認出與嗅聞需要可見的觀察時間。', [], ''),
 (14, 'Tine尾巴輕拍地面一下、兩下；Tart望牠，片刻後也輕輕搖一下；主人聽見節奏微笑。', '把尾巴由笑點轉成記憶線索，保留回應前的停頓。', [], ''),
 (22, '兩人聊到澳洲Victoria；領犬員從犬舍舊資料中找出手機幼犬合照，讀出同一犬舍；主人驚喜地摸Tart背。', '三個短問答、查資料、讀出確認、反應需要較長時間；手機不出現可讀文字。', ['@OriginPhone', '@Tart', '@Tine'], 'Handler：{佢由澳洲嚟。} Owner：{蛋撻都係。邊度呀？} Handler：{Victoria。} Owner：{Victoria？} Handler，查證後：{同一個犬舍……原來佢哋細個已經一齊。} Owner：{原來你哋識咗咁耐。}'),
 (8, '短暫黑場只聽幼犬聲；回到開場草地，這次幼犬踏入；先見安靜BabyTart。', '回憶需要簡潔的聲音橋與同一場景辨認。', [], ''),
 (12, 'BabyTine急步跑來，刹住腳差點撞上BabyTart；尾巴一拍、兩拍；BabyTart側眼後搖一下。', '童年尾巴節奏解答熟悉感，保留小刹車的喜劇。', [], ''),
 (10, '兩幼犬望向不同的畫外呼喚，分向草場兩邊走；各自回望；方向匹配剪回兩隻成年犬靠近。', '分離與回望各有一拍，成年匹配剪接不拉長。', ['@harbour'], ''),
 (16, '成年Tine慢慢挨向Tart；Tart移開一小步，Tine又挨近；第二次後Tart嘆息般鼻呼氣，終於讓牠靠著。', '三拍身體喜劇以接受和依偎落地，笑和感動同時成立。', [], ''),
 (10, '兩犬並排伏下成幾乎相同睡姿，Tart輕靠回Tine；鏡頭拉遠，香港夜光與海面圍住牠們，音樂安靜結束。', '留足最後依偎和拉遠，畫面直接完成主題，不加片尾字卡。', [], ''),
]
assert len(rows) == len(project['chapters']) == 30
cursor = 0
script = []
for c, (duration, action, reason, extras, dialogue) in zip(project['chapters'], rows):
    c['duration'] = duration
    c['pacing_reason'] = reason
    c['scene_summary'] = action
    c['absolute_start'] = cursor
    c['absolute_end'] = cursor + duration
    c['draft_screenplay'] = action + ('\n' + dialogue if dialogue else '')
    c['draft_dialogue'] = dialogue
    c['prompt'] = ''
    c['prompt_status'] = 'awaiting_asset_approval_before_director_prompt'
    c['shots'] = []
    c['active_take_id'] = None
    c['selected_storyboard_id'] = None
    c['tagged_assets'] = list(dict.fromkeys(c['tagged_assets'] + extras))
    c['resolution'] = '720p'
    c['handoff'] = {'draft_only': True, 'next_beat': project['chapters'][c['chapter_index']]['id'] if c['chapter_index'] < 30 else None}
    if c['chapter_index'] == 30:
        c['title'] = '同一個睡姿'
    script.append(f"{cursor//60:02d}:{cursor%60:02d}–{(cursor+duration)//60:02d}:{(cursor+duration)%60:02d}　{c['title']}（{duration}秒）\n{c['draft_screenplay']}\n節奏：{reason}\n")
    cursor += duration
assert cursor == 352
project['detailed_script'] = '\n'.join(script)
project['runtime_rationale'] = '352秒（5分52秒）：建立兩個日常與笑點2分02秒；城市錯過1分鐘；信任與老人轉變46秒；下班、重逢、來歷、童年與依偎2分04秒。逐章由動作和可讀反應決定，沒有平均分段。'
(OUT / 'adaptive-screenplay.txt').write_text(project['detailed_script'], encoding='utf-8')
(OUT / 'proposal.json').write_text(json.dumps(project, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

fonts = Path('C:/Windows/Fonts')
font = ImageFont.truetype(str(fonts / 'segoeui.ttf'), 21)
small = ImageFont.truetype(str(fonts / 'segoeui.ttf'), 17)
categories = [('characters', 'character'), ('locations', 'environment'), ('props', 'prop')]
catalog = ['# Adaptive movie asset review', '', 'Planned runtime: 5:52 (352 seconds). 720p / 21:9. No titles, subtitles or credits.', '',
    'Every image below is a proposed selected reference. Awaiting explicit asset approval; no new video submitted.', '']
manifest = []
for filename, category in categories:
    assets = [a for a in project['asset_list'] if a['category'] == category]
    columns = 2 if category != 'prop' else 3
    cell_width, cell_height = (610, 390) if category != 'prop' else (570, 390)
    height = ((len(assets) + columns - 1) // columns) * cell_height
    canvas = Image.new('RGB', (columns * cell_width, height), '#eeeae3')
    draw = ImageDraw.Draw(canvas)
    catalog += [f'## {filename.capitalize()}', '']
    for i, a in enumerate(assets):
        cand = next(c for c in a['candidates'] if c['id'] == a['selected_candidate_id'])
        full = ROOT / cand['path']
        im = Image.open(full).convert('RGB')
        im.thumbnail((cell_width - 24, cell_height - 76), Image.Resampling.LANCZOS)
        x, y = (i % columns) * cell_width, (i // columns) * cell_height
        draw.text((x+14, y+9), a['name'] + '  ' + a['tag'], font=font, fill='#282828')
        draw.text((x+14, y+38), cand['id'], font=small, fill='#555555')
        canvas.paste(im, (x + (cell_width-im.width)//2, y+70 + (cell_height-76-im.height)//2))
        catalog += [f"- [{a['name']} {a['tag']} — {cand['id']}]({full.as_posix()}) ({cand['width']} × {cand['height']})"]
        manifest.append({'name':a['name'], 'tag':a['tag'], 'candidate_id':cand['id'], 'category':category,
                         'path':cand['path'], 'dimensions':[cand['width'],cand['height']]})
    canvas.save(OUT / (filename + '-gallery.jpg'), quality=94)
    catalog += ['']
(OUT / 'asset-catalog.md').write_text('\n'.join(catalog), encoding='utf-8')
(OUT / 'selected-assets.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'planned_runtime':cursor,'assets':len(manifest),'proposal':str(OUT/'proposal.json'),'galleries':[str(OUT/(n+'-gallery.jpg')) for n,_ in categories]},indent=2))
