from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
archive=ROOT/'source'/f"full-screenplay-plan-r{p['revision']:06d}.json"
if len(p['chapters'])==51:
    archive.write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
    selected=copy.deepcopy(p['chapters'][36:51]);offset=0
    for i,c in enumerate(selected,1):
        c['source_scene_number']=c['chapter_index'];c['chapter_index']=i
        c['source_absolute_start']=c['absolute_start'];c['source_absolute_end']=c['absolute_end']
        c['absolute_start']=offset;c['absolute_end']=offset+c['duration'];offset+=c['duration']
    p['chapters']=selected
    p['full_screenplay_plan_path']=archive.relative_to(ROOT).as_posix()
    p['original_full_duration_seconds']=1045
    p['total_duration_target']=305
    p['production_notes'].append('Active timeline narrowed to source scenes37-51 only, with consecutive local chapter indices1-15 and stable IDs scene_37 through scene_51. Complete51-scene plan archived unchanged; source scene numbers/timings retained. No earlier scene may be submitted.')
(ROOT/'proposal.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'active_scenes':len(p['chapters']),'seconds':sum(c['duration'] for c in p['chapters']),'source_numbers':[c['source_scene_number'] for c in p['chapters']]}))
