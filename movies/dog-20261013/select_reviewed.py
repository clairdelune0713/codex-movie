"""Select only current successful takes that have actual recorded inspection."""
from render_movie import ROOT,read,save,sync
j=read(ROOT/'exports/task-journal.json');reviews=read(ROOT/'exports/visual-reviews.json')
for cid,t in j['takes'].items():
    review=reviews.get(cid)
    if review and review['take_id']==t['id']:t['visual_review']=review
save(ROOT/'exports/task-journal.json',j)
print(sync(j))
