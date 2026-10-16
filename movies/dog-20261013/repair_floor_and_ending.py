"""Ground the ferry dog at ankle height and preserve the inspected night ending."""
from pathlib import Path
import hashlib
definitions=(Path(__file__).parent/'tighten_staging.py').read_text(encoding='utf-8').split('\ngrip=')[0]
exec(compile(definitions,'local_staging_functions','exec'))
revise(39,[5,8,37,39,54,59],
    '攝影機在船艙绿色地板上，鏡頭高度只有二十厘米。阿華田身體整個伏在绿色地板，四腳接觸地面；後方阿晴兩隻鞋也在同一地面，木椅座在牠頭以上並非在狗身下。不能見狗在椅上。',
    [shot(0,22,'低機位只看 @阿華田_成年_橙色領巾項圈牽繩 伏在船艙绿色地板和 @阿晴 的兩隻白鞋、褲腳。橙牽繩從項圈連到上方阿晴手，微鬆；她的 @阿晴_手機_藍色保護殼 在上方手邊震動並放美姐語音。犬在地板伏着聽，14秒稍抬頭看主人，再望 @天星小輪_船艙座位與窗 窗邊暮金光。阿晴在椅上畫外說話，犬從未起身上椅。','35mm固定绿色地板低機位，完整看地板上犬身與主人鞋；人臉在鏡外。整段不切到椅面上的犬，不升鏡。','1-12s美姐電話 {陳伯頭先仲同我講緊張相。講到食飯都未講完。下次你得閒，再聽佢講。}；12-20s阿晴畫外 {你識揀位坐喎。搭個來回，返尖沙咀再行陣。}；其餘柔和小輪引擎海水。')],
    '只拍绿色地板上的狗與主人鞋。狗身下只能是绿色地板，不是棕色木板、木椅、人座或人腿。狗不坐椅、不躺椅、不跳椅。橙領巾是 @阿華田_橙色三角領巾 白圓底紅圓紋；心形只在右臀毛斑。母女電話與阿晴聲音皆真實香港粵語，不是旁白。')
c=v['chapters'][38]
c['prompt']=c['prompt'].replace('香港上午自然日光，室內窗光與柔和毛髮材質。','維港暮金夕光，船艙柔光與細緻毛髮。')
(ROOT/'chapters'/c['id']/'prompt.txt').write_text(c['prompt'],encoding='utf-8')
for n in [54,55]:
    c=p['chapters'][n-1]
    refs=[int(x.split('_')[1]) for x in c['linked_asset_ids'] if x!='asset_045']
    if 39 not in refs:refs.append(39)
    revise(n,refs,'尖沙咀同一深藍夜椅，林先生左、阿晴右，各握附著犬項圈的鬆繩；奶油蛋撻左前、栗棕阿華田右前，兩犬身體在地面相鄰伏着，承接53章的安靜伏地。鞍折好左椅面。',json.loads(json.dumps(c['shots'])),
        '兩犬全程伏在地面，不重新站起坐起。阿華田白圓底紅圓紋徽章依 @阿華田_橙色三角領巾，不是白心形。領巾和另外橙項圈、橙牽繩獨立正確；心形只在右臀毛斑。夜色不轉白晝；無片尾文字。')
    c=v['chapters'][n-1]
    c['prompt']=c['prompt'].replace('香港上午自然日光，室內窗光與柔和毛髮材質。','同一深藍夜色、維港燈與暖路燈，細緻毛髮。')

# One inspected actual end frame for each receiving night clip. Never reference
# a future chapter, and never reuse the rejected/wrong-badge take.
for n in [47,48,49,51,52,54,55]:
    source_n=53 if n>=54 else 46
    source=p['chapters'][source_n-1]
    take=next(t for t in source['takes'] if t['id']==source['active_take_id'])
    assert take['visual_review']['inspected'] and not take['visual_review'].get('requires_repair')
    frame=f'chapters/chapter_{source_n:03}/screenshots/take_01_review_04.jpg'
    reason='承接已檢視同一夜椅的深藍港燈、林左晴右、地面兩犬、各人握附著鬆繩，以及阿華田正確白圓底紅圓紋章；本章的其他原道具和新動作以原核准圖片及TIMELINE為準。'
    if n==51:reason+=' 這個夜景參照只用於9-14秒成年犬，前9秒幼犬必須完全日光且無成年裝備。'
    c=v['chapters'][n-1]
    c['continuity_references']=[{'id':f'bench_state_{source_n}_to_{n}','path':frame,'media_type':'Image','role':'reference_image',
        'source_chapter_id':source['id'],'source_take_id':take['id'],
        'source_sha256':hashlib.sha256((ROOT/take['path']).read_bytes()).hexdigest(),
        'source_timestamp':source['duration']-0.2,'reason':reason,'inspected':True}]
    (ROOT/'chapters'/c['id']/'prompt.txt').write_text(c['prompt'],encoding='utf-8')
save(ROOT/'proposal-floor-ending-repairs.json',v)
print(helper.save(ROOT,p,v,'Repair ferry floor at ankle height and carry inspected night badge/bench state into later clips'))
