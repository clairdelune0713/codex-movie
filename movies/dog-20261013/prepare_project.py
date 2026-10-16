"""Preserve the supplied v7 pack; prepare planning and an honest asset review."""
import hashlib
import json
import shutil
from pathlib import Path
from datetime import datetime, timezone
from PIL import Image, ImageDraw, ImageFont, ImageOps
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
PACK = ROOT.parents[1] / 'VIDEO_GENERATION_ASSET_PACK'
SOURCE = ROOT / 'source' / 'VIDEO_GENERATION_ASSET_PACK'

def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')

assert not SOURCE.exists(), 'Do not overwrite retained source media'
shutil.copytree(PACK, SOURCE)
hash_records = []
for p in sorted(PACK.rglob('*')):
    if p.is_file():
        rel = p.relative_to(PACK)
        original = hashlib.sha256(p.read_bytes()).hexdigest()
        copied = hashlib.sha256((SOURCE / rel).read_bytes()).hexdigest()
        assert original == copied
        hash_records.append({'file': rel.as_posix(), 'sha256': original, 'copy_verified': True})
save(ROOT / 'exports' / 'source-integrity.json', hash_records)

pdf = next((SOURCE / '00_SCRIPT').glob('*.pdf'))
pages = [p.extract_text().replace('\x00', ' ') for p in PdfReader(pdf).pages]
text = '\n\n'.join(f'--- PAGE {i+1} ---\n{p}' for i, p in enumerate(pages))
(ROOT / 'source' / 'screenplay-extracted.txt').write_text(text, encoding='utf-8')
mapping = json.loads((SOURCE / '99_PRODUCTION_NOTES' / 'SCRIPT_ASSET_MAP.json').read_text(encoding='utf-8-sig'))
by_file = {m['file']: m for m in mapping}
manifest = json.loads((SOURCE / '99_PRODUCTION_NOTES' / 'asset_manifest.json').read_text(encoding='utf-8-sig'))
expected = {m['file']: m for m in manifest['files']}
manifest_checks = []
for item in hash_records:
    spec = expected.get(item['file'])
    if spec:
        assert item['sha256'] == spec['sha256'], item['file']
        manifest_checks.append(item['file'])

project = json.loads((ROOT / 'project.json').read_text(encoding='utf-8'))
project.update(input_mode='script', language='zh-Hant', source_text=text,
    source_script_path=pdf.relative_to(ROOT).as_posix(),
    detailed_script='\n\n'.join(pages[2:15]),
    high_level_idea='蛋撻與阿華田在香港各展所長，溫暖陪伴不同的人；數度擦身後重逢，發現同出澳洲Victoria犬舍。',
    duration_mode='fixed', total_duration_target=1020,
    production_stage='asset_review',
    render_status='not_submitted',
    user_constraints={'project_name':'dog-20261013', 'runtime_seconds':1020,
        'follow_script':'Preserve v7 story, dialogue and scene order',
        'asset_policy':'Use every current supplied visual reference in its mapped role; no new or replacement reference images',
        'style_reference':'Pixar Up', 'vibe':'Fun and endearing',
        'no_author':True,'no_title':True,'no_subtitles':True},
    style={'medium':'溫暖細緻的立體動畫，參照《Up》的親切角色比例、自然喜劇表演、柔和圓潤造型與電影感光影；嚴格保留素材包角色設計。',
        'palette':'奶油金、栗棕、橙色點綴；清晨柔光、白日清亮、暮金與夜間維港深藍。',
        'lighting':'柔和主光、自然輪廓光、蓬鬆毛髮與有層次的景深。',
        'constraints':['No author or production credits','No opening or closing title','No subtitles, captions or narrative text overlays',
            'No copied reference-sheet panels, labels, borders or studio backdrop in video',
            'Dogs never speak; Cantonese dialogue preserved; opening worker speaks English',
            'Keep authored card and App text only as diegetic prop content, never subtitle overlays',
            'Every supplied design remains canonical; no outside image references']},
    script_changes=[{'reason':'Explicit user instructions override screenplay graphics',
        'change':'Omit opening place-name captions and film title; omit three final text overlays and all author/end credits. Preserve visual action and audio in their allocated time.'}],
    continuity_locks=['Tart is cream throughout, no heart patch; brown harness with silver handle and brown grip, never orange training vest.',
        'Tine is chestnut with cream heart marking on one fixed anatomical side; never mirror; orange bandana badge and collar lead use character/prop authority.',
        'Lam retains dark glasses throughout; cane stays folded in side pocket; card sleeve chest pocket.',
        'Scene 9 harness is removed and folded on bench; collar and brown lead remain attached.',
        'Scenes 10-12 handlers continuously hold their respective slack attached leads, including phone/card handling; never tie to bench.',
        'Hong Kong near-lane vehicles head left; teal car ahead of silver van; wait for next crossing cue after van clears; scene 7 has no heroic music.',
        'Ching round trip Tsim Sha Tsui -> Central -> Tsim Sha Tsui; Lam remains at the same bench during dusk-to-night montage.',
        'Phone senses record card, never implanted dog chip. Tart VIC-001/Lam, Tine VIC-002/Ching; same Victoria Meadow Kennels.',
        'Ah Wong only appears in old photograph, no eyebrows and narrow smiling slit eyes; no new flashback.',
        'Puppies have no adult equipment; old leather ball and metal bowl match opening and memory.'],
    source_coverage_limitations=['Source audit lists unpictured supporting cast, home/cafe/terminal geography and missing audio recordings.',
        'Stage screenplay supporting people and incidental settings directly during video generation using the existing design language; do not create new standalone reference assets.',
        'Vehicle multi-view/action plates and ending staging are reference guidance, never literal final frames.',
        'Timings are an unrendered production plan. No actual runtime, voice performance or video quality has been verified.'],
    tool_availability={'video_connector_found':False,'direct_seedance_route':'documented in Movi2; requires user authorization for named credential settings before access',
        'credentials_read':False,'jobs_submitted':0})

assets = []
groups = {}
for i, p in enumerate(sorted(SOURCE.rglob('*.png')),1):
    rel = p.relative_to(SOURCE).as_posix()
    m = by_file[rel]
    assert m['status'] != 'reference_only_do_not_use', rel
    aid = f'asset_{i:03}'
    group = rel.split('/')[0]
    category = {'01_CHARACTERS':'character','02_LOCATIONS':'environment','03_PROPS':'prop',
                '04_STAGING_REFERENCES':'reference','05_VEHICLES':'prop'}[group]
    if p.stem.startswith('App_'):
        category = 'reference'
    tag = '@' + p.stem
    with Image.open(p) as img:
        img.verify()
    with Image.open(p) as img:
        dimensions = list(img.size)
    item = {'id':aid,'tag':tag,'name':p.stem,'category':category,
        'description':p.stem+'。依v7素材包原圖；'+m['note'],
        'source':'supplied','media_type':'Image','reference_paths':[],
        'source_pack_file':rel,'script_scenes':m['scenes'],'reference_role':m['status'],
        'candidates':[{'id':'reference_v7','path':p.relative_to(ROOT).as_posix(),
            'created_at':datetime.now(timezone.utc).isoformat(),'source_revision':0,
            'dimensions':dimensions,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
            'prompt':'Supplied v7 image, copied without modification; not generated for this project'}],
        'selected_candidate_id':'reference_v7'}
    assets.append(item)
    groups.setdefault(group,[]).append(item)
project['asset_list'] = assets

# Rough narrative segmentation only. Final cinematic prompts await review approval.
plans = [
('同一個名字，兩個地方',[(12,'草葉水珠、犬舍金屬碗聲與靴子'),(18,'門開、幼犬聲、舊皮球滾出及英語Coming?'),(16,'風聲接海浪，草地光轉海面光，碼頭開閘'),(14,'小輪離岸、清晨船艙早餐與補眠；無地名字幕或片名')]),
('蛋撻，返工',[(18,'水煲跳掣、杯子固定位置、收音機與卡套入胸袋'),(24,'備用白手杖與鎖匙、穿鞍扣帶提把手；好，蛋撻，返工'),(20,'走廊與升降機，購物車卡門，等待鄰居拉正'),(16,'小朋友詢問摸狗；工作時等放工，向蛋撻道早晨'),(12,'繞過貨物箱，麵包舖氣味，繼續前行')]),
('阿華田，早晨',[(16,'橙色項圈領巾與牽繩、玻璃門倒影、阿晴等候回神'),(16,'美姐呼喚入室，長者輪候與互相打趣'),(22,'婆婆手掌與阿華田安靜親近'),(22,'怕被舔的小女孩觀察，尾巴拍椅腳，風扇笑話'),(14,'窗邊陳伯背向大家整齊折報紙，不望過來')]),
('各有各忙',[(18,'收窄行人路，蛋撻引導，急步途人讓路'),(16,'茶餐廳阿強拉椅，林先生準時早餐笑話'),(24,'桌下蛋撻面前掉多士、不起身；阿強拾起提醒勿餵'),(18,'巴士遮窗，阿華田對葉子有興趣，兩犬再次錯過'),(14,'巴士與阿華田離去，早餐很香，蛋撻安靜工作')]),
('唔使過嚟',[(18,'活動後陳伯拒接近，阿晴尊重距離坐下'),(20,'水瓶倒水入水碗、阿華田喝水伏下、報紙被風吹'),(24,'休息亦重要、名字叫阿華田、陳伯放低報紙'),(18,'先問同意、指尖摸頭，美姐遠處提醒時間'),(10,'收碗離開、陳伯問咁快就走，下星期再嚟')]),
('又認錯',[(22,'第一天報紙檔誤叫奶油色蛋撻阿華田，早餐笑話'),(24,'另一天誤叫阿華田蛋撻；靚仔也會回應'),(26,'再一天港鐵門關，對面升降機開，反光人影中擦身，等下一班'),(18,'一星期後陳伯問星期四，把袋子移到腳邊空出椅位')]),
('唔行，係有原因',[(14,'街口約友、茶餐廳聲、首輪過路提示'),(22,'蛋撻停步不行，林先生確認；客貨車被前車阻擋'),(18,'途人認清阻擋停下、車輛駛離時提示已改變'),(24,'等下一轉、摸肩收到；正常街聲，茶凍可以再叫，無英雄配樂'),(12,'下一輪提示確認路況過街，安全位置摸狗道好狗')]),
('今日，我叫你',[(18,'陳伯主動呼阿華田，安靜接近與古怪名字笑話'),(22,'舊相片阿黃、全巷養狗、下雨來陳伯家'),(26,'妻子留毛巾，停頓與杯聲；美姐問年輕樣貌，幽默回應'),(24,'相片轉給美姐談深水埗，阿華田伏兩椅間，談話延續')]),
('最近的一次',[(24,'尖沙咀小輪靠岸，林先生下船阿晴登船，行李與人群造成擦身'),(22,'往中環下層船艙、美姐語音、阿晴明說搭來回'),(18,'尖沙咀朋友與林先生船笛準時笑話、道別'),(26,'同一長椅卸完整導盲鞍折好，保留項圈牽繩，放工嗅乾葉'),(18,'中環下船離出口再登返程，暮金至深藍，切回仍在長椅的林先生'),(12,'尖沙咀返程出口下船，阿晴沿海旁朝同一長椅走')]),
('今次，見到你',[(14,'阿華田見休息蛋撻放慢、蛋撻站起不拉扯，林先生問有朋友'),(20,'阿晴詢問休息與可否打招呼，雙方同意慢慢嚟'),(16,'雙犬嗅聞側身回頭，海風尾巴輕動，身體放鬆'),(10,'兩人耐性與斯文笑話、阿華田坐下，兩條鬆繩仍由各自領犬者握住')]),
('Victoria？',[(18,'阿晴介紹名字，蛋撻阿華田早餐認錯真相，澳洲Victoria來源'),(26,'林先生取卡套交卡，手機感應卡片，依序蛋撻來源與阿華田檔案比對'),(24,'讀共同犬舍名稱、交還收卡，幼犬腳步先行；同門、碰金屬碗、滾球追逐'),(22,'兩工作人員各自呼喚，幼犬分開與回頭；回到夜間成年犬對望')]),
('我們之間',[(16,'歷史紀錄幼犬照片放大，阿晴描述，蛋撻幼時趕返工笑話'),(18,'阿華田再挨近、蛋撻諗緊、終於伏下；批准咗'),(16,'今日辛苦晒、手機收起、兩人沉默與拉遠，小輪船笛呼應開場'),(10,'兩犬鬆繩並肩伏着，尾巴碰蛋撻不挪開；無文字，切黑至17:00')])]
chapters=[]
scene_plan=[]
cursor=0
for scene, (title, beats) in enumerate(plans,1):
    start=cursor
    planned=[a['id'] for a in assets if scene in a['script_scenes']]
    for duration, summary in beats:
        num=len(chapters)+1
        chapters.append({'id':f'chapter_{num:03}','chapter_index':num,'title':summary,
            'source_scene':scene,'absolute_start':cursor,'absolute_end':cursor+duration,
            'duration':duration,'scene_summary':summary,'prompt':'','shots':[],
            'tagged_assets':[],'linked_asset_ids':[],'delinked_asset_ids':[],
            'planned_asset_ids':planned,
            'pacing_reason':'依原劇本此行動、對白與反應分配初步時間；完整表演與鏡位於素材審閱後定稿。',
            'materials':[],'takes':[],'active_take_id':None,'storyboards':[],
            'selected_storyboard_id':None,'screenshots':[],'prompt_status':'rough_plan_awaiting_asset_approval'})
        cursor+=duration
    scene_plan.append({'scene':scene,'title':title,'start_seconds':start,'end_seconds':cursor,'duration_seconds':cursor-start})
assert cursor==1020
project['chapters']=chapters
project['source_scene_plan']=scene_plan
save(ROOT/'proposal.json',project)
save(ROOT/'exports'/'rough-timeline.json',{'status':'unrendered rough plan','total_seconds':cursor,'scenes':scene_plan,'chapters':chapters})

fontpath='C:/Windows/Fonts/msyh.ttc'
font=ImageFont.truetype(fontpath,18)
small=ImageFont.truetype(fontpath,15)
heading=ImageFont.truetype(fontpath,28)
gallery=ROOT/'exports'/'asset-review'
gallery.mkdir(parents=True,exist_ok=True)
gallery_index=[]
for group,items in groups.items():
    for offset in range(0,len(items),8):
        subset=items[offset:offset+8]
        rows=(len(subset)+1)//2
        sheet=Image.new('RGB',(1560,90+rows*490),'#f3f0e9')
        d=ImageDraw.Draw(sheet)
        d.text((24,18),f'{group} | {offset+1}-{offset+len(subset)} | original v7 references',font=heading,fill='#242624')
        for k,a in enumerate(subset):
            x=20+(k%2)*780;y=86+(k//2)*490
            img=Image.open(ROOT/a['candidates'][0]['path']).convert('RGB')
            img=ImageOps.contain(img,(740,410))
            sheet.paste(img,(x+(740-img.width)//2,y+(410-img.height)//2))
            d.text((x,y+412),a['tag'],font=font,fill='#1d2524')
            d.text((x,y+441),f"{a['id']} / reference_v7 | scenes "+','.join(map(str,a['script_scenes'])),font=small,fill='#465652')
        target=gallery/f'{group}_{offset//8+1:02}.jpg'
        sheet.save(target,quality=94)
        gallery_index.append({'group':group,'path':target.relative_to(ROOT).as_posix(),'assets':[a['id'] for a in subset]})
save(gallery/'gallery-index.json',gallery_index)
lines=['# dog-20261013: supplied asset review','',
    'All thumbnails preserve source image bytes in the linked originals. Every candidate is `reference_v7`.',
    'Review sheets are for human review only and must never enter video payloads.','']
for a in assets:
    lines.append(f"- {a['tag']} | {a['id']} | reference_v7 | [full-size original](../../{a['candidates'][0]['path']}) | scenes {a['script_scenes']}")
(gallery/'originals.md').write_text('\n'.join(lines),encoding='utf-8')
save(ROOT/'exports'/'preparation-report.json',{'copied_files':len(hash_records),'manifest_hashes_verified':len(manifest_checks),
    'supplied_images':len(assets),'rough_chapters':len(chapters),'runtime_plan_seconds':cursor,
    'missing_retired_map_entries':[m['file'] for m in mapping if not (SOURCE/m['file']).exists()],
    'gallery_sheets':gallery_index,'video_generated':False})
print(json.dumps({'copied_files':len(hash_records),'images':len(assets),'chapters':len(chapters),'seconds':cursor,'gallery_sheets':len(gallery_index)},ensure_ascii=False))
