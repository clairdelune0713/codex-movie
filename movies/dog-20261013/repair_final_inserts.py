"""Ground the return ferry dog and retain Ching's ownership of the phone."""
from pathlib import Path
import hashlib
definitions=(Path(__file__).parent/'tighten_staging.py').read_text(encoding='utf-8').split('\ngrip=')[0]
exec(compile(definitions,'local_staging_functions','exec'))
c=v['chapters'][41];s=c['shots'][1]
s['action']='返程船艙低機位，只有 @阿華田_成年_橙色領巾項圈牽繩 全身伏在绿色地板，身下不是木板或綠色椅座。@阿晴 只有白鞋及褲脚入鏡，鞋和犬身同一地板水平。橙鬆繩向上連到她手；她坐在鏡外椅上。窗光從暮金轉深藍，城市燈亮；林先生與奶油蛋撻留在尖沙咀，完全不在此鏡。'
s['camera']='35mm攝影機離绿色地板二十厘米，只拍地上的犬與主人鞋，完全不拍椅座；不升鏡，不能把狗放窗邊椅上。'
c['prompt']=c['prompt'].replace(p['chapters'][41]['shots'][1]['action'],s['action']).replace(p['chapters'][41]['shots'][1]['camera'],s['camera'])
s['end_state']=s['action']+'；保持暮色到夜的時間進展。'
src=p['chapters'][38];take=next(t for t in src['takes'] if t['id']==src['active_take_id'])
assert take['id']=='edit_01'
c['continuity_references']=[{'id':'return_ferry_floor','path':'chapters/chapter_039/screenshots/take_03_review_01.jpg','media_type':'Image','role':'reference_image',
    'source_chapter_id':src['id'],'source_take_id':take['id'],'source_sha256':hashlib.sha256((ROOT/take['path']).read_bytes()).hexdigest(),
    'source_timestamp':.2,'reason':'只給第二鏡6-12秒沿用同一犬伏在绿色船艙地板、主人鞋在地面的空間，不沿用手機位置；第一鏡及第三鏡完全按各自TIMELINE，不出現其他犬或人物。','inspected':True}]
c['revision_reason']='Return ferry shot uses inspected floor geometry; other two shots retain original correct cast separation'
(ROOT/'chapters'/c['id']/'prompt.txt').write_text(c['prompt'],encoding='utf-8');save(ROOT/'chapters'/c['id']/'shots.json',c['shots'])
revise(52,[6,8,15,20,26,28,37],
    '尖沙咀同一深藍夜椅，上半身近景只看林先生左、阿晴右。兩犬一直在兩人脚前地面、畫面下方之外，絕不拍上椅的狗。阿晴左手持藍手機，右手握鏡外橙鬆繩；林先生左手握鏡外棕鬆繩，右手在自己胸袋卡套。',
    [shot(0,4,'@阿晴 左手持 @阿晴_手機_藍色保護殼，手機裡 @App_06_幼犬歷史照片 的同一 @幼犬歷史照片_蛋撻與阿華田 輕放大，原照片內容保持，不畫新照片、不把成年犬放椅上。手機一直在阿晴手。','65mm手機手特寫，只看阿晴袖口，手機邊框和原照片。','0-3.6s阿晴 {細個都係咁，成日黐住其他狗。}；3.6-4s開始林先生下一句，連續聲音跨剪接。'),
     shot(4,10,'@林先生_深色眼鏡 左座，右指腹按胸袋收好的 @林先生_卡套 笑；@阿晴 右座左手仍持手機、右手仍握橙鬆繩，不遞手機。鏡頭只拍兩人胸口以上和手機，兩隻成年犬在畫面下方的地面，不入鏡。','50mm兩人上半身近景，最低只到腰上，禁止拉成全身或拍犬在椅面。','4-8.3s林先生 {蛋撻細個張相，個樣已經好似趕住返工。}；8.3-10s阿晴開始 {佢坐喺草地度。其他狗都郁緊，得佢望住前面……}，下一鏡聲音繼續同一句、不重說。'),
     shot(10,16,'@阿晴 同一左手手機裡同一幼犬原照片，指腹輕移放大奶油BabyTart端坐草地的部分，其他幼犬原樣保留。林先生右手按卡套，左棕鬆繩仍握；阿晴右橙鬆繩仍握。狗不入鏡但始終脚前地面。','65mm同一阿晴左手藍手機特寫，夜光，不把手機交林先生。','10-14s阿晴前句續完，14-16s海風與安靜微笑，不加对白。')],
    '手機從未離開阿晴左手；林先生完全不接、不拿、不看手機，不把手機放犬前。兩犬只在脚前地面且整段畫面外；不在椅上，不跳上椅，不在兩人腿上。原App照片不能替換為新畫、其他成年犬或新犬舍。每句只一次，香港粵語，自然微笑。')
c=v['chapters'][51];c.pop('continuity_references',None)
c['prompt']=c['prompt'].replace('香港上午自然日光，室內窗光與柔和毛髮材質。','同一尖沙咀深藍夜色、維港灯與暖路燈，手機反光自然。')
(ROOT/'chapters'/c['id']/'prompt.txt').write_text(c['prompt'],encoding='utf-8')
save(ROOT/'proposal-final-inserts.json',v)
print(helper.save(ROOT,p,v,'Repair return ferry floor and phone ownership with restrained inserts and original photos'))
