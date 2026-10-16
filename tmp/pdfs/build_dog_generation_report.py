import json
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from collections import Counter
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader

ROOT = Path.cwd()
MOVIE = ROOT / 'movies/dog-20261013'
OUT = ROOT / 'output/pdf/dog-20261013-generation-cost-report.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
project = json.loads((MOVIE / 'project.json').read_text(encoding='utf-8'))
usage = json.loads((MOVIE / 'usage.json').read_text(encoding='utf-8'))
chapters = sorted(project['chapters'], key=lambda c: c['chapter_index'])
jobs = list(usage['jobs'].values())
FX = Decimal('7.80')
USD = sum(Decimal(j['cost']['amount']) for j in jobs)
NAVY = colors.HexColor('#153448')
TEAL = colors.HexColor('#147D83')
MUTED = colors.HexColor('#526775')
LIGHT = colors.HexColor('#EEF4F6')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleCustom', fontName='Helvetica-Bold', fontSize=27, leading=31, textColor=NAVY, spaceAfter=12))
styles.add(ParagraphStyle(name='SectionCustom', fontName='Helvetica-Bold', fontSize=16, leading=20, textColor=NAVY, spaceAfter=12))
styles.add(ParagraphStyle(name='BodyCustom', fontName='Helvetica', fontSize=9.3, leading=14, textColor=NAVY, spaceAfter=9))
styles.add(ParagraphStyle(name='SmallCustom', fontName='Helvetica', fontSize=8, leading=11, textColor=MUTED, spaceAfter=7))
styles.add(ParagraphStyle(name='CellCustom', fontName='Helvetica', fontSize=7.6, leading=10, textColor=NAVY))
styles.add(ParagraphStyle(name='FileCustom', fontName='Courier', fontSize=6.8, leading=9, textColor=NAVY, wordWrap='CJK'))
styles.add(ParagraphStyle(name='HeaderCustom', fontName='Helvetica-Bold', fontSize=7.5, leading=10, textColor=colors.white))
styles.add(ParagraphStyle(name='MoneyCustom', fontName='Helvetica', fontSize=7.6, leading=10, textColor=NAVY, alignment=TA_RIGHT))

def p(s, style='BodyCustom'):
    return Paragraph(s, styles[style])

def money(n):
    return f'{n.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP):,.2f}'

def table(headers, rows, widths, fontcols=(), rightcols=()):
    data = [[p(escape(h).replace('\n','<br/>'), 'HeaderCustom') for h in headers]]
    for row in rows:
        data.append([p(escape(str(v)).replace('\n','<br/>'), 'FileCustom' if i in fontcols else 'MoneyCustom' if i in rightcols else 'CellCustom') for i, v in enumerate(row)])
    t = Table(data, colWidths=widths, repeatRows=1, hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),NAVY),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
        ('TOPPADDING',(0,0),(-1,0),7),('BOTTOMPADDING',(0,0),(-1,0),7),
        ('TOPPADDING',(0,1),(-1,-1),4.4),('BOTTOMPADDING',(0,1),(-1,-1),4.4),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,LIGHT]),
        ('LINEBELOW',(0,0),(-1,0),1,TEAL),
    ]))
    return t

def selected(c):
    return next(t for t in c['takes'] if t['id']==c['active_take_id'])

def compact_path(path):
    path = str(path).replace('\\','/')
    if path.startswith('chapters/'):
        return path.replace('chapters/','',1).replace('/takes/','/')
    return Path(path).name

by_chapter = {c['id']: sorted([j for j in jobs if j['chapter_id']==c['id']],key=lambda j:int(j['take_id'].split('_')[-1])) for c in chapters}
total_ok = sum(j['state']=='succeeded' for j in jobs)
total_sec = sum(c['duration'] for c in chapters)
assert len(chapters)==55 and len(jobs)==85 and total_ok==82 and total_sec==1020
assert USD==Decimal('865.1079450')
assert {j['model'] for j in jobs}=={'dreamina-seedance-2-5-260628'}
assert {j['resolution'] for j in jobs}=={'1080p'}
all_generated_paths=[]
for c in chapters:
    for t in c['takes']:
        if t.get('path'):
            assert (MOVIE/t['path']).is_file()
            if not t.get('local_edit'): all_generated_paths.append(compact_path(t['path']))

story=[]
story += [p('PRODUCTION &amp; COST REPORT','SmallCustom'),p('dog-20261013','TitleCustom'),
          p('Seedance generation breakdown | Prepared 16 October 2026','SmallCustom'),Spacer(1,12)]
metrics=[['Planned segments','55'],['Script scenes','12'],['API attempts','85'],['Completed video outputs','82'],['Final movie duration','17:00 (1,020 seconds)'],['Estimated Seedance cost',f'HK$ {money(USD*FX)}']]
story.append(table(['Production measure','Recorded total'],metrics,[245,266]))
story += [Spacer(1,20),p('Final movie','SectionCustom'),p('<b>dog-20261013-1080p.mp4</b>'),
          p('Location: movies/dog-20261013/exports/dog-20261013-1080p.mp4','SmallCustom'),
          p('1920 x 1080 | 16:9 | 24 fps | Stereo audio | 55 selected segments'),
          Spacer(1,9),p('Generation settings','SectionCustom'),
          p('<b>Model:</b> Dreamina Seedance 2.5<br/><b>Model ID:</b> dreamina-seedance-2-5-260628<br/><b>Resolution:</b> 1080p (1920 x 1080), 16:9, across all attempts.<br/><b>Segment durations:</b> 10-30 seconds, as recorded per segment.'),
          Spacer(1,8),p('How to read this report','SectionCustom'),
          p('An <b>attempt</b> is one API submission. A <b>completed output</b> is a technically successful generation; it may still have needed a creative revision. The <b>selected file</b> is the clip used to assemble the delivered movie, including five local edits.'),
          p(f'Costs include every recorded generation, including earlier takes. Total: US$ {money(USD)}, converted at the reporting assumption <b>US$1 = HK$7.80</b>. These are ledger-based list-price estimates, not an inspected invoice. Discounts, tax, fees and actual settlement FX are unverified.','SmallCustom')]

overview=[]
for c in chapters:
    js=by_chapter[c['id']]
    first=next(i+1 for i,j in enumerate(js) if j['state']=='succeeded')
    sel=selected(c)
    cost=sum(Decimal(j['cost']['amount']) for j in js)*FX
    overview.append([f"{c['chapter_index']:02}",str(c['source_scene']),str(c['duration']),len(js),sum(j['state']=='succeeded' for j in js),first,compact_path(sel['path']),money(cost)])

for a,b in [(0,28),(28,55)]:
    story += [PageBreak(),p(f'Segment breakdown | {a+1:02}-{b:02}','SectionCustom'),
              p('All rows: Seedance 2.5 / 1080p / 16:9. Duration is the planned clip length in seconds. First OK is the attempt number that first produced a completed output.','SmallCustom'),
              table(['Seg.','Scene','Sec.','API\ntries','Videos\nOK','First\nOK','Selected video file','Est. HKD'],overview[a:b],[29,32,30,36,39,35,240-20,90-20],fontcols=(6,),rightcols=(7,)),
              Spacer(1,10),p('Filename key: chapter_NNN/take_NN.mp4 or chapter_NNN/edit_01.mp4 maps to chapters/chapter_NNN/takes/ under the movie folder. Badge files map to exports/badge-correction/. Full local-edit paths and source details appear on the final page.','SmallCustom')]

attemptrows=[]
for c in chapters:
    sel=selected(c)
    base=sel.get('source_video_take_id',sel['id'])
    for j in by_chapter[c['id']]:
        take=next(t for t in c['takes'] if t['id']==j['take_id'])
        tokens=j.get('usage',{}).get('completion_tokens')
        if j['state']!='succeeded': role='No output'
        elif j['take_id']==base: role='Final base' if sel.get('local_edit') else 'Selected'
        elif c['chapter_index']==39 and j['take_id']=='take_01':role='Audio reused'
        else:role='Earlier take'
        attemptrows.append([f"{c['chapter_index']:02}",j['take_id'].replace('take_',''),j['state'].capitalize(),j['duration_seconds'],f'{tokens:,}' if tokens is not None else '-',money(Decimal(j['cost']['amount'])*FX),compact_path(take['path']) if take.get('path') else '(no video file)',role])

for a,b in [(0,30),(30,60),(60,85)]:
    story += [PageBreak(),p(f'Generated take register | {a+1}-{b} of 85','SectionCustom'),
              p('One row per API attempt. All use dreamina-seedance-2-5-260628 at 1080p / 16:9. File identifiers include their chapter folder so repeated take names remain unambiguous.','SmallCustom'),
              table(['Seg.','Take','API result','Sec.','Output\ntokens','Est. HKD','Generated video file','Use in final'],attemptrows[a:b],[30,31,53,28,57,55,170,87],fontcols=(6,),rightcols=(4,5)),
              Spacer(1,9),p('Succeeded means a file was generated; it does not imply final creative acceptance. Failed and rejected submissions have no output file. Local edits are listed separately and are not additional Seedance generations.','SmallCustom')]

story += [PageBreak(),p('Accounting notes &amp; file locations','SectionCustom')]
dist=Counter(len(by_chapter[c['id']]) for c in chapters)
story += [table(['API attempts per segment','Number of segments'],[[i,dist[i]] for i in sorted(dist)],[245,266]),Spacer(1,12),
          p('52 segments produced their first completed video on attempt 1. Segments 14, 21 and 50 first completed on attempt 2. Segment 14 had a rejected submission; segments 21 and 50 had failed jobs. Further completed takes reflect revisions and final selection.'),
          p('Completed generations total 1,518 requested seconds (25:18). All submissions, including the three unsuccessful ones, total 1,568 requested seconds (26:08). The final edit uses 1,020 seconds (17:00). Container padding is excluded from these duration totals.'),
          p('Five selected files were edited locally','SectionCustom')]
editrows=[]
for c in chapters:
    sel=selected(c)
    if sel.get('local_edit'):
        editrows.append([f"{c['chapter_index']:02}",sel['path'],sel['source_video_take_id'].replace('_',' ')+' video / '+sel['source_audio_take_id'].replace('_',' ')+' audio'])
story += [table(['Seg.','Selected file, relative to movie folder','Source takes'],editrows,[30,300,181],fontcols=(1,)),Spacer(1,10),
          p('These edits did not add a Seedance generation charge. Segment 39 uses take 3 video with take 1 audio; the other four edited segments use take 2 as their source.'),
          p('Cost method and source records','SectionCustom'),
          p(f'The saved ledger applies measured provider completion tokens x US$11.70 per million tokens for Seedance 2.5 / 1080p / image-only references. Its recorded USD total is <b>{USD}</b>. The ledger records a zero estimate for the three unsuccessful attempts, citing the provider success-only billing policy. Pricing and that policy were recorded on 13-14 October 2026; no account invoice was inspected.'),
          p(f'HKD = USD x 7.80. Total HK$ {money(USD*FX)} is calculated before rounding. Individually rounded segment rows sum to HK$ {money(sum(Decimal(r[-1].replace(",","")) for r in overview))}; the HK$0.04 difference is rounding. No labor, local compute, asset storage, tax or payment charges are added.'),
          p('Project snapshot: revision 36. Sources within the movie folder: project.json (plan, takes, selection); usage.json (attempts, tokens, estimated costs); exports/verification.json (delivered video checks). All registered video paths were checked to exist when preparing this report.','SmallCustom'),
          p('Movie folder: '+escape(str(MOVIE).replace('\\','/')),'SmallCustom'),
          p('Provider pricing source recorded in the ledger: <link href="https://docs.byteplus.com/id/docs/modelark/model-pricing?redirect=1" color="#147D83">BytePlus ModelArk model pricing</link>.','SmallCustom')]

def footer(canvas,doc):
    w,h=A4
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#D8E3E8'));canvas.line(42,36,w-42,36)
    canvas.setFont('Helvetica',7.5);canvas.setFillColor(MUTED)
    canvas.drawString(42,24,'dog-20261013 | Generation and estimated cost report | 16 Oct 2026')
    canvas.drawRightString(w-42,24,str(doc.page))
    canvas.restoreState()

doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=38,bottomMargin=48,title='dog-20261013 - Generation and Cost Report',author='')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
reader=PdfReader(OUT)
text='\n'.join(page.extract_text() for page in reader.pages)
assert len(reader.pages)==7, len(reader.pages)
for s in ['6,747.84','865.1079450','dog-20261013-1080p.mp4','dreamina-seedance-2-5-260628']:
    assert s in text,s
for filename in all_generated_paths: assert filename in text,filename
print(json.dumps({'pdf':str(OUT),'pages':len(reader.pages),'bytes':OUT.stat().st_size,'attempt_rows':len(attemptrows),'generated_filenames_checked':len(all_generated_paths),'USD':str(USD),'HKD':money(USD*FX)},indent=2))
