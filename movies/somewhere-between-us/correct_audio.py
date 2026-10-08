"""Replace only confirmed audio-filter failures with original location ambience."""
import importlib.util,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('h','C:/Users/admina/.codex/skills/movi2/scripts/project.py');h=importlib.util.module_from_spec(s);s.loader.exec_module(h)
p=h.read(ROOT/'project.json');q=json.loads(json.dumps(p));j=h.read(ROOT/'exports/seedance-journal.json')
for index in [13,21]:
    c=q['chapters'][index-1];t=j['takes'][c['id']]
    assert t['status']=='failed' and t['provider_status']=='failed' and 'OutputAudioSensitiveContentDetected' in str(t.get('error'))
    c['prompt']=c['prompt'].replace('Up般圓潤有重量的3D視覺語言','溫暖圓潤有重量的原創3D視覺語言').replace('原創角色與原創配樂','原創角色；本章沒有配樂')
    replacements={'轻鼻息、短俏皮木管':'輕鼻息、空月台的通風環境聲','鬆鼻息；音樂由規整变自由':'鬆鼻息、海浪與海風'}
    for old,new in replacements.items():
        c['prompt']=c['prompt'].replace(old,new)
        for shot in c['shots']:shot['audio']=shot['audio'].replace(old,new)
    c['prompt']=re.sub(r'AUDIO\n.*?\nCONTINUITY LOCKS','AUDIO\n只有上文逐鏡頭的自然環境聲與動作Foley：海浪、海風、通風、車門、列車與犬呼吸依地點使用。無音樂、無旋律、無人類或犬台詞、無字幕。扣具聲為單聲原創Click。\nCONTINUITY LOCKS',c['prompt'],flags=re.S)
    c['audio']='Location ambience and Foley only; no score or dialogue. Replaces confirmed failed generated-audio take.'
r=h.save(ROOT,p,q,'Replace confirmed audio-filter failures in chapters 13 and 21 with original location ambience and Foley')
print('Revision',r['revision'],'chapters13,21 audio revised')
