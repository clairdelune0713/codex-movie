"""Give every required supplied App screen an explicit, timed phone insert."""
from pathlib import Path
definitions=(Path(__file__).parent/'tighten_staging.py').read_text(encoding='utf-8').split('\ngrip=')[0]
exec(compile(definitions,'local_staging_functions','exec'))
revise(49,[2,5,6,8,15,21,22,23,24,25,27,28,37,39],
    '尖沙咀同一夜椅。林先生左座、阿晴右座，奶油蛋撻左前地面、栗棕阿華田右前地面。林先生左手一直握棕鬆繩，右手抽胸袋卡；阿晴右腕與手掌一直握橙鬆繩，右指接卡，左手持藍手機。各繩只扣自己的犬項圈。',
    [shot(0,6,'@林先生_深色眼鏡 右手從胸袋 @林先生_卡套 抽出 @蛋撻_晶片認證卡，右手遞給 @阿晴，左手始終握棕鬆繩。阿晴右手接卡同時右掌握橙鬆繩，左手持 @阿晴_手機_藍色保護殼。','65mm手、卡與兩條鬆繩，夜色，清晰物理接触。','0-5.7s林先生 {蛋撻張卡喺度。你個程式讀唔讀到？}；5.7-6s阿晴開始下一鏡句。'),
     shot(6,9,'阿晴說可以並問同意，才用藍手機背面靠近手中卡片；@App_01_感應卡片 在手機屏幕，實體卡只在手機旁，不拿手機掃狗。','65mm藍手機與卡片接近的手特寫。','6-8.5s阿晴完整說 {可以。我幫你掃？}；8.5-9s開始下一句，環境聲低於对白。'),
     shot(9,12,'原 @App_02_蛋撻檔案 自然顯示在同一藍手機屏幕，奶油Tart、ID VIC-001、照顧者林先生；接著點入 @App_03_蛋撻來源，Victoria來源記錄。屏幕只在手機內，不滿畫面、不新增字卡。','65mm固定藍手機特寫，保持可辨認的原畫面版式和內容。','阿晴9-12s開始說 {唔止都係Victoria……連犬舍都係同一間。}，下一鏡同句續完。'),
     shot(12,15,'在同一手機明確切到 @App_04_阿華田檔案，栗棕Tine、ID VIC-002、照顧者阿晴，與奶油Tart不同個體；右手卡與橙繩保持可見，不卡上狗身。','65mm同手機同角度屏幕特寫，不重新設計介面。','阿晴上一句12-15s繼續 {唔止都係Victoria……連犬舍都係同一間。}，這是同一句聲音延續，不重複整句。'),
     shot(15,21,'手機顯示 @App_05_共同來源，兩隻犬來自同一間Victoria Meadow Kennels／維多利亞草原犬舍，原文字與版式保留，不另造假名。','65mm手机屏幕特寫後輕拉至阿晴臉，原屏仍在手機邊框內。','15-16.7s阿晴前句結尾；16.7-18.1s林先生 {同一間？}；18.1-20.9s阿晴 {係。我讀畀你聽。}。'),
     shot(21,30,'@阿晴 讀共同犬舍名後把實體卡還林先生右手；他右手收回胸袋卡套，左手仍棕鬆繩，阿晴右手仍橙鬆繩。兩犬地面嗅耳，蛋撻稍避但留下，阿華田徽章跟 @阿華田_橙色三角領巾 的白圓底紅圓紋。','50mm兩人中景轉犬地面反應；同夜椅軸線、林左晴右。','20.9-24.1s阿晴 {維多利亞草原犬舍。}；24.1-28s林先生輕聲 {咁你哋……以前見過㗎？}；28-30s夜海浪。')],
    '所有App畫面逐一出現在同一藍手機裡，至少各一個清楚插入鏡頭；禁止只有一張檔案而跳過VIC-002及共同来源。兩犬始終地面，蛋撻無鞍。阿華田領巾徽章是圓形，不是心形。兩人全程各握自己附著的牽繩。精確音訊連續只說原句一次，切鏡不得重複上一句或變成旁白。')
c=v['chapters'][48]
for s in c['shots']:
    old_audio=s['audio']
    s['audio']=f"{s['start']}-{s['end']}s聲音連續使用下方CONTINUOUS AUDIO SCHEDULE，此剪接不重啟或重複句子；背景夜海浪、物件和衣料聲低於对白。"
    c['prompt']=c['prompt'].replace(old_audio,s['audio'])
c['prompt']=c['prompt'].replace('香港上午自然日光，室內窗光與柔和毛髮材質。','同一尖沙咀深藍夜色，暖路燈、維港灯光与柔和毛髮材質。')
# State a continuous dialogue schedule once; shot-boundary references above
# describe continuation and must never induce repeated speech.
c['prompt']+='\nCONTINUOUS AUDIO SCHEDULE\n0-5.7s林先生 {蛋撻張卡喺度。你個程式讀唔讀到？}；5.7-8.5s阿晴 {可以。我幫你掃？}；8.5-16.7s阿晴 {唔止都係Victoria……連犬舍都係同一間。}；16.7-18.1s林先生 {同一間？}；18.1-20.9s阿晴 {係。我讀畀你聽。}；20.9-24.1s阿晴 {維多利亞草原犬舍。}；24.1-28s林先生 {咁你哋……以前見過㗎？}。每句只一次，聲音連續跨剪接。'
(ROOT/'chapters'/c['id']/'prompt.txt').write_text(c['prompt'],encoding='utf-8')
save(ROOT/'chapters'/c['id']/'shots.json',c['shots'])
save(ROOT/'proposal-scan-repair.json',v)
print(helper.save(ROOT,p,v,'Repair scan timing with all five supplied App screens, original card and held collar leads'))
