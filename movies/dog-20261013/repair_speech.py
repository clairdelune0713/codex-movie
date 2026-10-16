"""Target possible Mandarin paraphrasing found by the local audio audit."""
import json
from render_movie import ROOT,helper,read,save
p=read(ROOT/'project.json');v=json.loads(json.dumps(p))
for n in [7,25,26]:
    c=v['chapters'][n-1]
    c['prompt']+='''
MANDATORY SPOKEN LANGUAGE
所有人物真正發出香港粵語 Cantonese / yue 的口語聲音，逐字說TIMELINE中的原句。不得翻成普通話、國語、中文書面語或英語；不能把「等陣」「架車」「唔緊要」「今日咁早」「呢個」「淺色嗰隻」「先啱」「你係咪」「靚仔」變成普通話對應詞。保留粵語聲調與自然香港口音、語尾，成年男女聲線穩定。每句只一次，無旁白、無唱歌，音樂極低不遮字。
名稱發音：蛋撻 = daan6 taat1，阿華田 = aa3 waa4 tin4，靚仔 = leng3 zai2。名字不改成其他飲品或狗名。主角造型、動作、鏡頭、逐秒時間及原字句完全跟上方，這個修正只確保說話語言和名稱。
'''
    c.update(prompt_status='revised_after_audio_audit',revision_reason='ASR suggests possible Mandarin paraphrase; require literal Cantonese phonology and supplied names')
    (ROOT/'chapters'/c['id']/'prompt.txt').write_text(c['prompt'],encoding='utf-8')
save(ROOT/'proposal-speech-repair.json',v)
print(helper.save(ROOT,p,v,'Tighten literal Cantonese and names in three flagged audio clips'))
