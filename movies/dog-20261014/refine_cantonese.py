"""Promote the existing Cantonese requirement, without rewriting a source line."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as h
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=json.loads(json.dumps(p))
voice='''配音硬要求 / HONG KONG CANTONESE ONLY
所有人物對白只講自然香港廣東話（粵語），逐字跟隨 TIMELINE 入面「」內嘅原句。保留香港口語嘅唔、佢、冇、嚟、喎、㗎、陣、返工，唔好翻譯、改寫或讀成普通話／國語。香港人物用自然粵語聲調和語氣助詞，唔用普通話配音。蛋撻讀粵語 daan6 taat3；阿華田讀 aa3 waa4 tin4；呢啲羅馬字只係發音提示，唔係要讀出嚟嘅台詞。沒有列出對白嘅鏡頭只保留環境聲、動作聲和配樂，唔加旁白或者人聲。狗永遠唔講嘢。
'''
changed=[]
for c in q['chapters']:
    if c['chapter_index']<14 and c['id'] not in ('s03_c01','s03_c02'):continue
    if not any(b['type']=='dialogue' for b in c['planning_source_blocks']):continue
    if c['prompt'].startswith('配音硬要求'):continue
    c['prompt']=voice+'\n'+c['prompt'];changed.append(c['id'])
    if c['id'] in ('s03_c01','s03_c02'):
        c.setdefault('prompt_refinements',[]).append({'reason':'Local speech audit flags paraphrased wording in first take; foreground exact colloquial Cantonese and name pronunciation. Language classification alone is not conclusive.'})
q.setdefault('production_quality_notes',[]).append('Whisper forced-Cantonese and automatic-Chinese transcripts differ; automatic language ID can label Cantonese as Chinese. Treat ASR as review evidence, not proof of accent. Foregrounded the existing Cantonese-only requirement for future dialogue and two flagged morning takes; original 107 lines unchanged.')
print(h.save(ROOT,p,q,'Strengthen exact colloquial Cantonese delivery without changing source dialogue'))
print('Dialogue prompts refined:',len(changed))
