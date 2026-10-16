"""Read immutable movie records and create a separate, filename-complete PDF audit."""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from collections import Counter
import json, hashlib, math, sys
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

BASE=Path(__file__).resolve().parents[2]
ROOT=BASE/'movies/dog-20261015'
OUT=BASE/'output/pdf/dog-20261015-generation-cost-report.pdf'
TMP=BASE/'tmp/pdfs/dog-generation-report'
OUT.parent.mkdir(parents=True,exist_ok=True);TMP.mkdir(parents=True,exist_ok=True)
assert not OUT.exists() or '--refine' in sys.argv,'Preserve an existing report; use --refine only for this new report draft.'
read=lambda f:json.loads(f.read_text(encoding='utf-8-sig'))
p=read(ROOT/'project.json');u=read(ROOT/'usage.json');j=read(ROOT/'exports/task-journal.json')
verification=read(ROOT/'exports/verification.json')
jobs=list(u['jobs'].values());FX=Decimal('7.80');RATE=Decimal('11.70')
cash=lambda v:f'{v.quantize(Decimal("0.01"),rounding=ROUND_HALF_UP):,.2f}'
all_takes={}
for latest in j['takes'].values():
 for t in latest.get('prior_takes',[])+[latest]:all_takes[(t['chapter_id'],t['id'])]=t
assert len(jobs)==82 and Counter(x['state'] for x in jobs)=={'succeeded':77,'failed':5}
assert {x['model'] for x in jobs}=={'dreamina-seedance-2-5-260628'}
assert {x['resolution'] for x in jobs}=={'1080p'}
rows=[]
for c in p['chapters']:
 attempts=sorted([x for x in jobs if x['chapter_id']==c['id']],key=lambda x:int(x['take_id'].split('_')[-1]))
 generated=[]
 for a in attempts:
  assert a['duration_seconds']==c['duration']
  t=all_takes[(c['id'],a['take_id'])]
  if a['state']=='succeeded':
   assert (ROOT/t['path']).is_file()
   v=t['verification'];assert (v['width'],v['height'],v['fps'])==(1920,1080,24)
   generated.append(t['path'])
  else:assert not t.get('path')
 selected=next(t for t in c['takes'] if t['id']==c['active_take_id'])
 assert (ROOT/selected['path']).is_file()
 usd=sum(Decimal(a['cost']['amount']) for a in attempts)
 rows.append({'number':c['chapter_index'],'id':c['id'],'title':c['title'],'seconds':c['duration'],
  'attempts':len(attempts),'videos':len(generated),'history':''.join('S' if a['state']=='succeeded' else 'F' for a in attempts),
  'files':generated,'selected':selected['path'],'usd':str(usd),'hkd':str(usd*FX),
  'first_success_attempt':next(i+1 for i,a in enumerate(attempts) if a['state']=='succeeded')})
assert len(rows)==70 and sum(r['seconds'] for r in rows)==600
usd=sum(Decimal(x['cost']['amount']) for x in jobs);hkd=usd*FX
tokens=sum(x.get('usage',{}).get('completion_tokens',0) for x in jobs)
assert Decimal(tokens)*RATE/Decimal(1000000)==usd==Decimal('371.4273225')
assert sum(r['videos'] for r in rows)==77
final=ROOT/verification['file'];assert final.is_file()
manifest={'project_revision':p['revision'],'report_date':'2026-10-16','report_timezone':'Asia/Taipei',
 'usd_hkd_reporting_assumption':str(FX),'completion_tokens':tokens,'usd':str(usd),'hkd':str(hkd),
 'rows':rows,'source_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['project.json','usage.json','exports/task-journal.json','exports/verification.json']}}
(TMP/'report-inputs.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')

pdfmetrics.registerFont(TTFont('Arial','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold','C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFont(TTFont('Consolas','C:/Windows/Fonts/consola.ttf'))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold',italic='Arial',boldItalic='Arial-Bold')
PAGE=landscape(A4);W=PAGE[0]-72
INK=colors.HexColor('#183832');TEAL=colors.HexColor('#087F78');MUTED=colors.HexColor('#536861')
LIGHT=colors.HexColor('#EEF5F2');LINE=colors.HexColor('#D7E3DD');WHITE=colors.white
styles={
 'title':ParagraphStyle('title',fontName='Arial-Bold',fontSize=23,leading=28,textColor=INK,spaceAfter=7),
 'h':ParagraphStyle('h',fontName='Arial-Bold',fontSize=15,leading=20,textColor=INK,spaceAfter=7),
 'body':ParagraphStyle('body',fontName='Arial',fontSize=9,leading=13,textColor=INK,spaceAfter=6),
 'small':ParagraphStyle('small',fontName='Arial',fontSize=8,leading=11,textColor=MUTED,spaceAfter=5),
 'cell':ParagraphStyle('cell',fontName='Arial',fontSize=8.1,leading=10.7,textColor=INK),
 'mono':ParagraphStyle('mono',fontName='Consolas',fontSize=7.8,leading=10.5,textColor=INK),
 'th':ParagraphStyle('th',fontName='Arial-Bold',fontSize=8,leading=10,textColor=WHITE),
 'stat':ParagraphStyle('stat',fontName='Arial-Bold',fontSize=25,leading=29,textColor=TEAL),
 'cost':ParagraphStyle('cost',fontName='Arial-Bold',fontSize=24,leading=28,textColor=TEAL),
}
P=lambda s,kind='body':Paragraph(s,styles[kind])
def table_style(header=True):
 commands=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
 ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),('LINEBELOW',(0,-1),(-1,-1),0.6,LINE)]
 if header:commands += [('BACKGROUND',(0,0),(-1,0),INK),('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE,LIGHT])]
 return TableStyle(commands)
def footer(c,doc):
 c.saveState();c.setStrokeColor(LINE);c.line(36,PAGE[1]-34,PAGE[0]-36,PAGE[1]-34)
 c.setFont('Arial-Bold',8);c.setFillColor(TEAL);c.drawString(36,PAGE[1]-24,'DOG-20261015  /  SEEDANCE GENERATION AUDIT')
 c.setFont('Arial',8);c.setFillColor(MUTED);c.drawRightString(PAGE[0]-36,PAGE[1]-24,'16 OCT 2026  |  PROJECT SNAPSHOT r32')
 c.line(36,31,PAGE[0]-36,31);c.setFont('Arial',7.5)
 c.drawString(36,19,'HKD uses assumed USD/HKD 7.80. All API costs are estimates, not an invoice.')
 c.drawRightString(PAGE[0]-36,19,f'{doc.page} / 6');c.restoreState()

story=[P('Generation and cost report','title'),P('Complete 70-segment register with generated filenames, selected edit filenames and retry outcomes.','body'),Spacer(1,6)]
cards=[]
for value,label in [('70','planned segments'),('82','API requests'),('77','returned videos'),('5','failed requests')]:
 cards.append([P(value,'stat'),P(label,'small')])
metrics=Table([cards],colWidths=[W/4]*4);metrics.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),LIGHT),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),6),('LEFTPADDING',(0,0),(-1,-1),12)]))
story += [metrics,Spacer(1,12)]
cost=Table([[P('HK$'+cash(hkd),'cost'),P('<b>Estimated total Seedance API cost</b><br/>US$'+cash(usd)+' converted at the explicit reporting assumption of US$1 = HK$7.80.','body')]],colWidths=[W*.31,W*.69]);cost.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),0)]));story += [cost,Spacer(1,7)]
settings=[('Model - every request','Seedance 2.5 / dreamina-seedance-2-5-260628'),('Resolution / frame format','1080p / 1920 x 1080 / 16:9 / 24 fps. All 77 returned videos match.'),
 ('Planned duration','16 scenes; 70 segments; 600 seconds (10:00). Per-request clips range from 4 to 19 seconds.'),
 ('Request totals','60 segments used 1 request; 8 used 2; 2 used 3. All attempts requested 684 seconds in total.'),
 ('Successful request duration','650 seconds, including discarded takes. Raw files can contain a few extra frames; final cut is exactly 600 seconds.'),
 ('Usage / price basis',f'{tokens:,} completion tokens x US$11.70 per million = US$371.4273225.')]
t=Table([[P(escape(a),'cell'),P(escape(b),'cell')] for a,b in settings],colWidths=[140,W-140]);t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]));story += [t,Spacer(1,9)]
story += [P('<b>Final movie filename</b>  dog-20261015-1080p.mp4','body'),P(escape(str(final).replace('\\','/')),'mono'),Spacer(1,8),
 P('Cost scope: this new movie only, including discarded successful retakes. Previously created dog-20261014 assets/audio are reused; their historical production costs are not included. Local edits and assembly add no Seedance calls. No account invoice, tax or card FX charge has been verified.','small'),
 P('FX context: HKMA describes a HK$7.75-7.85 per US dollar linked-rate band. The 7.80 used here is a reporting assumption, not a spot or settlement quote. <link href="https://www.hkma.gov.hk/eng/key-functions/money/linked-exchange-rate-system/" color="#087F78">HKMA reference</link>.','small')]

widths=[26,70,34,43,37,48,220,220,W-698]
assert abs(sum(widths)-W)<.01
for offset in range(0,70,18):
 subset=rows[offset:offset+18];story.append(PageBreak())
 story += [P(f'Segment register  |  {offset+1:02}-{offset+len(subset):02}','h'),
 P('S = returned video; F = failed request with no video file. History is chronological. Costs include all takes for the segment.','small'),
 P('Files below are inside <b>chapters/&lt;segment ID&gt;/takes/</b> under the project folder. The selected file may be a local edit of a returned video.','small'),Spacer(1,3)]
 headers=['#','Segment','Sec /<br/>try','API<br/>tries','Video<br/>files','History','Generated video filename(s)','Selected source / local-edit filename','Est.<br/>HK$']
 data=[[P(x,'th') for x in headers]]
 for r in subset:
  data.append([P(str(r['number']),'cell'),P(r['id'],'mono'),P(str(r['seconds']),'cell'),P(str(r['attempts']),'cell'),P(str(r['videos']),'cell'),P(r['history'],'mono'),
   P('<br/>'.join(escape(Path(f).name) for f in r['files']),'mono'),P(escape(Path(r['selected']).name),'mono'),P(cash(Decimal(r['hkd'])),'cell')])
 t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT');t.setStyle(table_style());story += [t,Spacer(1,8),
 P('Project folder: C:/Users/Admin 3/Downloads/codex-movie/movies/dog-20261015/','small'),
 P('Example: s02_c04 + take_03.mp4 resolves to chapters/s02_c04/takes/take_03.mp4. Failed requests have no invented filename. Totals use unrounded values; rounding the 70 rows independently creates a HK$0.04 difference.','small')]

story += [PageBreak(),P('Retakes, failures and audit notes','h')]
reasons={
 's02_c01':'Rural-geography correction; both requests returned videos.',
 's02_c04':'Two output-audio rejections. Third request returned silent picture; local training-room ambience supplied.',
 's03_c01':'Dialogue-performance retake; both requests returned videos.',
 's03_c02':'Dialogue-performance retake; both requests returned videos.',
 's04_c03':'Correct dog/table and floor-toast placement; both requests returned videos.',
 's04_c06':'Correct dog placement on the floor; both requests returned videos.',
 's06_c02':'Correct dog/mat placement beside Chan; both requests returned videos.',
 's07_c02':'One output-audio rejection, then one output-video rejection. Third request returned silent picture; finalized original local audio supplied.',
 's16_c06':'Output-audio rejection. Second request returned silent picture; finalized original local audio supplied.',
 's16_c08':'First output put dogs on the bench. Second output corrected the ground-level ending.'}
data=[[P('Segment','th'),P('History','th'),P('Reason / resolution','th')]]
for r in rows:
 if r['attempts']>1:data.append([P(r['id'],'mono'),P(r['history'],'mono'),P(escape(reasons[r['id']]),'cell')])
t=Table(data,colWidths=[85,62,W-147]);t.setStyle(table_style());story += [t,Spacer(1,9)]
story += [P('<b>API success vs. final selection.</b> 67 segments returned a video on their first request; one first returned on request 2 and two on request 3. Seven returned videos were subsequently replaced for creative review. A returned video is not a guarantee of perfect continuity or dialogue.','small'),
 P('<b>Local selected edits.</b> s06_c03 uses take_01_detailcrop03.mp4 (hand/eye reframing); s07_c03 uses take_01_roomtone01.mp4 (local audio edit). These are derivatives, not extra API generations. Picture-only selected takes are s02_c04/take_03.mp4, s07_c02/take_03.mp4 and s16_c06/take_02.mp4; local audio is attached during assembly.','small'),
 P('<b>Failure accounting.</b> The five failed requests comprise four output-audio rejections and one output-video rejection. They have no returned video files and are recorded at estimated zero cost under the ledger pricing assumption. All 82 attempts are resolved; none have pending/unknown usage charges in the report. Actual billing remains unverified.','small'),
 P('<b>Sources and reproducibility.</b> Read from project snapshot r32: project.json (plan and selected files), usage.json (82 attempts, measured tokens and cost estimates), exports/task-journal.json (take histories and real generated paths), exports/verification.json (600-second final technical profile), and exports/assembly-settings.json (movie inputs). All source movie records were read only.','small'),
 P('<b>Pricing reference recorded in the ledger:</b> <link href="https://ai.byteplus.com/ark/region:ap-southeast-1/docs/model-pricing" color="#087F78">BytePlus model pricing</link>, checked during production on 15 October 2026. The recorded rate is a list-price estimate; it is not an account invoice.','small')]
doc=SimpleDocTemplate(str(OUT),pagesize=PAGE,rightMargin=36,leftMargin=36,topMargin=47,bottomMargin=43,title='dog-20261015 - Generation and Cost Report',author='',subject='70-segment Seedance generation register with video filenames and HKD cost estimates')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(json.dumps({'pdf':str(OUT),'segments':70,'requests':82,'returned_videos':77,'failures':5,'estimated_hkd':str(hkd),'expected_pages':6},indent=2))
