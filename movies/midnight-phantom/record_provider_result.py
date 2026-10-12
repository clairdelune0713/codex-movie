from project_ops import ROOT,helper,write_json,commit
p=helper.read(ROOT/'project.json')
records=[{'chapter':c['id'],'status':c['takes'][-1]['status'],'provider_reason':'Copyright restrictions' if 'copyright' in c['takes'][-1].get('error','').lower() else c['takes'][-1].get('error','')} for c in p['chapters']]
if not all(item['status']=='failed' for item in records):raise RuntimeError('Some jobs are still active or succeeded; reconcile before closing attempt')
summary={'submitted_chapters':len(records),'successful_clips':0,'failed_chapters':len(records),'reason':'Provider rejected generated outputs for copyright restrictions.','jobs':records,'next_action':'User authorized original detective character recast; new project is midnight-phantom-original and awaits revised visual approval.','credential_values_saved':False}
write_json(ROOT/'exports/provider-result.json',summary)
p.update(production_status='provider_rejected',production_stage='retained_for_reference',render_status='failed',provider_result=summary)
commit(p,'Record 13 confirmed provider copyright rejections and retain original-cast adaptation separately')
print('Original named-character attempt closed: 13 failed, no successful video clips.')
