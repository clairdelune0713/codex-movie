"""Narrow director repairs after actual Chan-take inspection; source unchanged."""
import copy
from render_movie import ROOT, read, helper

p = read(ROOT / 'project.json')
q = copy.deepcopy(p)
c = q['chapters'][21]
old = '阿華田下巴前腳上，阿晴不催，陳伯報紙漸放低。'
new = ('阿晴坐在椅上，雙手留在自己膝上並握住連接犬項圈的鬆牽繩。'
       '阿華田從第一幀至最後一幀全身伏在阿晴椅前的地板，四爪、胸口、腹部和後腿都在地板上，'
       '下巴枕在地板上的兩隻前爪；椅座只坐阿晴。陳伯報紙漸放低。')
if old not in c['prompt']:
    raise RuntimeError('Expected original floor-blocking paragraph missing; do not reapply')
c['prompt'] = c['prompt'].replace(old, new)
c['prompt'] = c['prompt'].replace('阿華田換舒適姿勢',
    '阿華田全身保持伏在地板，只輕輕調整地板上的前爪與後腿，再把下巴放回前爪')
c['prompt'] += ('\nSHOT-SPECIFIC FLOOR CONTINUITY\n'
    '這是一隻成年犬，完整身體一直在椅前地板上休息。'
    '犬近景只拍地板上的頭與前爪，阿晴坐姿、膝頭和椅座保持清楚可見且空於犬身；'
    '所有對話與切鏡都延續同一地板位置。犬不跳椅、不上膝、不被抱起。\n')
c['active_take_id'] = None
c = q['chapters'][23]
c['prompt'] = c['prompt'].replace('AUDIO AND EXACT DIALOGUE\n',
    'AUDIO AND EXACT DIALOGUE\n'
    '使用香港粵語口音與粵語詞彙，原文逐字說，保持原生香港日常語氣。'
    '這兩句的粵拼發音只供聲音導演參考，不另讀拼音：'
    '陳伯一句 gam3 faai3 zau6 zau2；阿晴一句 haa6 sing1 kei4 zoi3 lai4。'
    '特別清楚說出「咁」gam3 及「嚟」lai4，保留自然疑問和溫暖道別語調。\n', 1)
c['active_take_id'] = None
print(helper.save(ROOT, p, q,
    'Repair observed chapter 22 floor-resting continuity and clarify chapter 24 exact Cantonese pronunciation'))
