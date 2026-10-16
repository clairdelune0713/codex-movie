"""Restore the original Australian worker's single English line."""
import json
from render_movie import ROOT,helper,read,save
p=read(ROOT/'project.json');v=json.loads(json.dumps(p));c=v['chapters'][1]
c['prompt']+='''
SCENE-SPECIFIC SPOKEN LANGUAGE OVERRIDE
這是澳洲犬舍工作人員，不是香港人物。本章唯一人物对白是原劇本的英語 {Coming?}，必須實際說出 English "Coming?"，自然親切澳洲英語口音、短問句上揚，且只一次。絕不翻成中文「出發」「嚟唔嚟」「過來」，也不新增任何字句。上方的粵語要求只適用香港人物，對這個澳洲工作人員不適用。本章仍只用原工作人員手與鞋、舊皮球、犬舍晨光，動作與秒數原樣。
'''
c.update(prompt_status='revised_after_audio_audit',revision_reason='Local ASR heard Chinese paraphrase of the sole English worker line; restore original Coming?')
(ROOT/'chapters'/c['id']/'prompt.txt').write_text(c['prompt'],encoding='utf-8')
save(ROOT/'proposal-english-line.json',v)
print(helper.save(ROOT,p,v,'Restore the screenplay Australian worker line to English Coming?'))
