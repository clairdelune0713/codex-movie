from project_ops import ROOT,helper,commit,write_json
from PIL import Image,ImageDraw,ImageFont
p=helper.read(ROOT/'project.json')
a=next(a for a in p['asset_list'] if a['tag']=='@ScaleReference')
for c in a['candidates']:c['inspection_status']='rejected_scale_measurement_mismatch'
a['description']='Mathematically constructed standing-height dimension diagram. Riff, Pip and Guard each occupy exactly one equal height unit; Crow exactly four units from shared sole baseline. Bounding rectangles are size guides only, not character designs. Separate approved character sheets supply all anatomy and identity. No measurement labels appear in movie.'
a['reference_paths']=[]
fp=helper.asset_fingerprint(ROOT,p,a)
path=ROOT/'assets/asset_scale_v02/scale_c06.png'
if path.exists():raise RuntimeError('Preserve prior candidate')
im=Image.new('RGB',(1600,900),'#faf4df');d=ImageDraw.Draw(im)
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',27);title=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',35)
d.text((44,23),'Standing height: 1 : 1 : 1 : 4',font=title,fill='#25252d')
floor=780;unit=165
for n in range(5):
 y=floor-unit*n;d.line((100,y,1545,y),fill='#9b998d',width=2);d.text((32,y-17),f'{n}H',font=font,fill='#414145')
for name,x,h,w,color in [('Riff',230,1,112,'#a94727'),('Pip',480,1,112,'#216376'),('Guard',730,1,112,'#273e60'),('Crow',1080,4,330,'#353b43')]:
 top=floor-unit*h;d.rectangle((x,top,x+w,floor),fill=color,outline='#17191d',width=4)
 d.text((x,802),name+f' {h}x',font=font,fill='#22222b')
d.text((160,853),'Dimensions only. Character identity and anatomy come from the separate character sheets.',font=font,fill='#414145')
path.parent.mkdir(parents=True,exist_ok=True);im.save(path)
a['candidates'].append({'id':'scale_c06','path':'assets/asset_scale_v02/scale_c06.png','prompt':'Measured technical dimension diagram constructed from exact numeric geometry; no existing raster image modified. Three 165px standing-height bounds and one 660px standing-height bound on shared y780 baseline. Not character artwork or storyboard.','source_revision':p['revision']+1,'dependency_fingerprint':fp,'dimensions':[1600,900],'generation_tool':'numeric technical diagram','inspection_status':'verified_geometry_165_165_165_660'})
a['selected_candidate_id']='scale_c06'
t=next(a for a in p['asset_list'] if a['tag']=='@TowerLayout');t['reference_paths']=['assets/reference/continuity-v02/user-tower-layout.png','assets/asset_scale_v02/scale_c06.png','assets/asset_tower/tower_c03.png','assets/asset_machine/machine_c01.png']
r=commit(p,'Replace drifting illustrated scale charts with exact numeric 1:1:1:4 diagram and bind tower layout sources')
write_json(ROOT/'exports/continuity-v02-tower-layout-meta.json',{'source_revision':r['revision'],'dependency_fingerprint':helper.asset_fingerprint(ROOT,r,t),'reference_paths':t['reference_paths']})
print('Measured diagram created; tower layout sources registered at revision',r['revision'])
