import hashlib
import json
from decimal import Decimal
from pathlib import Path
from xml.sax.saxutils import escape

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    KeepTogether, LongTable, PageBreak, Paragraph, SimpleDocTemplate,
    Spacer, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parents[3]
THREAD = '01a142df-5816-7ba3-8bca-44fe99062e45'
INPUT = ROOT / 'outputs' / THREAD
MOVIE = ROOT / 'movies' / 'dog-20261014'
OUTPUT = ROOT / 'output' / 'pdf' / THREAD
OUTPUT.mkdir(parents=True, exist_ok=True)
FINAL = OUTPUT / 'dog-20261014-production-report.pdf'
DATA = json.loads((INPUT / 'report-data.json').read_text(encoding='utf-8'))
S, SEGMENTS, ATTEMPTS = DATA['summary'], DATA['segments'], DATA['attempts']
JOURNAL = json.loads((MOVIE / 'exports/task-journal.json').read_text(encoding='utf-8'))
ASSEMBLY = json.loads((MOVIE / 'exports/assembly-settings.json').read_text(encoding='utf-8'))
PROJECT = json.loads((MOVIE / 'project.json').read_text(encoding='utf-8'))
assert PROJECT['revision'] == S['revision'] == 57
assert all(hashlib.sha256((MOVIE / rel).read_bytes()).hexdigest() == expected
           for rel, expected in S['source_hashes_sha256'].items())

by_attempt = {}
for latest in JOURNAL['takes'].values():
    for take in latest.get('prior_takes', []) + [latest]:
        by_attempt[take['attempt_id']] = take
selected = {item['chapter']: item for item in ASSEMBLY['input_takes']}
final_movie = MOVIE / PROJECT['delivery']['path']
assert final_movie.is_file()
expected_files = set()
for a in ATTEMPTS:
    take = by_attempt[a['attempt_id']]
    if a['state'] == 'succeeded':
        assert take['path'] and (MOVIE / take['path']).is_file()
        a['video_file'] = take['path']
        expected_files.add(take['path'])
    else:
        a['video_file'] = ''
for s in SEGMENTS:
    s['selected_video_file'] = selected[s['segment']]['path']
    assert (MOVIE / s['selected_video_file']).is_file()
    expected_files.add(s['selected_video_file'])

NAVY = colors.HexColor('#253C59')
INK = colors.HexColor('#233044')
MUTED = colors.HexColor('#627084')
PALE = colors.HexColor('#F2F5F9')
LINE = colors.HexColor('#D5DDE7')
AMBER = colors.HexColor('#FFF0D3')
PAGE_W, PAGE_H = landscape(A4)
WIDTH = PAGE_W - 72
styles = {
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=22, leading=26, textColor=NAVY, spaceAfter=7),
    'h1': ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=15, leading=19, textColor=NAVY, spaceAfter=9),
    'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=10.5, leading=14, textColor=NAVY, spaceBefore=8, spaceAfter=6),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=12, textColor=INK, spaceAfter=6),
    'small': ParagraphStyle('small', fontName='Helvetica', fontSize=8, leading=10.5, textColor=MUTED, spaceAfter=5),
    'cell': ParagraphStyle('cell', fontName='Helvetica', fontSize=8.1, leading=10.2, textColor=INK),
    'file': ParagraphStyle('file', fontName='Courier', fontSize=8, leading=10, textColor=INK, wordWrap='CJK'),
    'head': ParagraphStyle('head', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=colors.white, alignment=TA_CENTER),
    'right': ParagraphStyle('right', fontName='Helvetica', fontSize=8.1, leading=10.2, textColor=INK, alignment=TA_RIGHT),
    'center': ParagraphStyle('center', fontName='Helvetica', fontSize=8.1, leading=10.2, textColor=INK, alignment=TA_CENTER),
    'value': ParagraphStyle('value', fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=INK),
    'coverfile': ParagraphStyle('coverfile', fontName='Courier-Bold', fontSize=12, leading=16, textColor=NAVY),
}


def para(text, style='body', markup=False):
    clean = str(text).replace('\u2011', '-').replace('\u2013', '-').replace('\u2014', '-')
    return Paragraph(clean if markup else escape(clean), styles[style])


def cell(text, style='cell'):
    return para(text, style)


def money(value, code='HK$'):
    return f'{code}{Decimal(str(value)):,.2f}'


def table_style(header=True, font_size=8.1):
    result = [
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1 if header else 0), (-1, -1), [colors.white, PALE]),
        ('LINEBELOW', (0, -1), (-1, -1), 0.5, LINE),
    ]
    if header:
        result += [('BACKGROUND', (0, 0), (-1, 0), NAVY),
                   ('LINEBELOW', (0, 0), (-1, 0), 0.5, NAVY)]
    return TableStyle(result)


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setTitle('dog-20261014 production and cost report')
    canvas.setAuthor('')
    canvas.setStrokeColor(LINE)
    canvas.line(36, PAGE_H - 27, PAGE_W - 36, PAGE_H - 27)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(36, PAGE_H - 20, 'dog-20261014 - generation and cost report')
    canvas.line(36, 28, PAGE_W - 36, 28)
    canvas.drawString(36, 17, 'Report date: 16 October 2026 | Seedance list-price estimates')
    canvas.drawRightString(PAGE_W - 36, 17, f'Page {doc.page}')
    canvas.restoreState()


story = [para('dog-20261014 production report', 'title'),
         para('Generation audit for the 20-minute Tart and Tine movie. Project revision 57.', 'small'),
         Spacer(1, 4), para('Final movie video filename', 'h2')]
file_box = Table([[para(final_movie.name, 'coverfile')]], colWidths=[WIDTH])
file_box.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), PALE),
                             ('LEFTPADDING', (0, 0), (-1, -1), 10),
                             ('TOPPADDING', (0, 0), (-1, -1), 8),
                             ('BOTTOMPADDING', (0, 0), (-1, -1), 8)]))
story += [file_box, Spacer(1, 5), para(f'Movie file location: {final_movie}', 'small'),
          para(f'Clip paths below are relative to the movie project folder: {MOVIE}', 'small'), Spacer(1, 8)]

left = [
    ('Production', 'Result'),
    ('Planned segments / screenplay scenes', '70 / 16'),
    ('Total API requests / accepted tasks', '96 / 94'),
    ('Successful returned videos', '91'),
    ('Selected / superseded video sources', '70 / 21'),
    ('Failed after acceptance / rejected', '3 / 2'),
    ('Final timeline duration', '20:00 (1,200 seconds)'),
    ('Total successful output duration', '26:04 (1,564 nominal seconds)'),
]
right = [
    ('Generation and cost', 'Result'),
    ('Model', 'Dreamina Seedance 2.5'),
    ('Model identifier', 'dreamina-seedance-2-5-260628'),
    ('Native resolution / format', '480p, 854x480, 16:9, 24 fps'),
    ('Duration per segment', '8-24 seconds'),
    ('Returned completion tokens', '15,062,518'),
    ('Estimated Seedance cost (USD)', 'US$161.1689426'),
    ('Estimated Seedance cost (HKD)', 'HK$1,264.69'),
]


def stat_table(rows, widths):
    t = Table([[cell(a, 'head' if i == 0 else 'cell'),
                cell(b, 'head' if i == 0 else 'value')] for i, (a, b) in enumerate(rows)],
              colWidths=widths, hAlign='LEFT')
    t.setStyle(table_style())
    return t


stats = Table([[stat_table(left, [207, 173]), '', stat_table(right, [155, WIDTH-547])]],
              colWidths=[380, 12, WIDTH-392])
stats.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'),
                          ('LEFTPADDING', (0, 0), (-1, -1), 0),
                          ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                          ('TOPPADDING', (0, 0), (-1, -1), 0),
                          ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
story += [stats, Spacer(1, 10), para('Requests used through final selection', 'h2')]
dist = Table([[cell(x, 'head') for x in ['Requests per segment', '1', '2', '3', '4']],
              [cell(x, 'center') for x in ['Number of segments', '51', '14', '3', '2']]],
             colWidths=[190, 80, 80, 80, 80], hAlign='LEFT')
dist.setStyle(table_style())
story += [dist, Spacer(1, 7),
          para('68 segments returned a video on request 1. s04_c06 first returned a video on request 2; s12_c02 first returned one on request 4. Later successful takes could still replace earlier videos after quality review.', 'small'),
          para('The cost includes HK$294.33 for 21 superseded successful videos. Five failed or rejected requests are estimated at zero under the provider billing policy. Account invoices, discounts, tax and card FX fees were not available.', 'small'),
          PageBreak()]

story += [para('All 70 planned segments', 'h1'),
          para('Every row uses Dreamina Seedance 2.5 at native 480p (854x480), 16:9 and 24 fps. Duration is the timeline / nominal duration for one take. Costs include all successful takes for that segment.', 'small'),
          para('First video = request number returning the first successful video. Failed / rejected shows those two counts separately. Selected video filenames are unique paths relative to the movie project folder printed on page 1.', 'small')]
seg_widths = [56, 191, 38, 44, 44, 48, 50, 228, WIDTH-699]
seg_headers = ['Segment', 'Description', 'Sec.', 'All requests', 'Videos', 'Failed / rejected', 'First video', 'Selected video filename / path', 'Est. HKD']
rows = [[cell(h, 'head') for h in seg_headers]]
for s in SEGMENTS:
    rows.append([
        cell(s['segment']), cell(s['description']), cell(s['duration_seconds'], 'right'),
        cell(s['requests'], 'right'), cell(s['videos_generated'], 'right'),
        cell(f'{s["failed_after_acceptance"]} / {s["rejected_before_generation"]}', 'center'),
        cell(s['requests_to_first_success'], 'right'), cell(s['selected_video_file'], 'file'),
        cell(money(s['estimated_hkd']), 'right'),
    ])
rows.append([cell('TOTAL', 'value'), cell('70 segments'), cell('1,200', 'right'), cell('96', 'right'),
             cell('91', 'right'), cell('3 / 2', 'center'), cell(''), cell(''), cell('HK$1,264.69', 'value')])
segments_table = LongTable(rows, colWidths=seg_widths, repeatRows=1, hAlign='LEFT')
segments_table.setStyle(table_style())
segments_table.setStyle(TableStyle([('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#E5EDF7')),
                                    ('LINEABOVE', (0, -1), (-1, -1), 0.7, NAVY)]))
story += [segments_table, Spacer(1, 8),
          para('Row costs are rounded to cents. The total uses unrounded amounts. take_01_crop02.mp4 and take_02_mix01.mp4 are local edits of existing generated sources, with no additional Seedance generation fee.', 'small'),
          PageBreak()]

story += [para('All 96 generation requests and video filenames', 'h1'),
          para('Each successful request has its actual video filename and project-relative path. Failed / rejected requests did not return a video file. Use identifies the source selected for the final movie; selected local edits are listed after this log.', 'small'),
          para('Duration is the requested nominal generation duration. MP4 container durations can include a small audio or frame padding difference. Requests are grouped in segment order, matching the spreadsheet audit.', 'small')]
att_widths = [26, 56, 54, 62, 252, 48, 84, 86, WIDTH-668]
att_headers = ['#', 'Segment', 'Take', 'API result', 'Generated video filename / path', 'Duration (s)', 'Completion tokens', 'Est. HKD', 'Use']
rows = [[cell(h, 'head') for h in att_headers]]
for a in ATTEMPTS:
    rows.append([
        cell(a['number'], 'right'), cell(a['segment']), cell(a['take']), cell(a['state']),
        cell(a['video_file'], 'file') if a['video_file'] else cell('No file - ' + a['state']),
        cell(a['requested_seconds'], 'right'),
        cell(f'{a["completion_tokens"]:,}' if a['completion_tokens'] is not None else 'Not returned', 'right'),
        cell(money(a['estimated_hkd']), 'right'), cell(a['use']),
    ])
rows.append([cell(''), cell('TOTAL', 'value'), cell(''), cell('91 videos'),
             cell('96 requests; 5 returned no video file'), cell('1,656', 'right'),
             cell('15,062,518', 'right'), cell('HK$1,264.69', 'value'), cell('70 selected sources')])
attempts_table = LongTable(rows, colWidths=att_widths, repeatRows=1, hAlign='LEFT')
attempts_table.setStyle(table_style())
attempts_table.setStyle(TableStyle([('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#E5EDF7')),
                                    ('LINEABOVE', (0, -1), (-1, -1), 0.7, NAVY)]))
for idx, a in enumerate(ATTEMPTS, 1):
    if a['state'] != 'succeeded':
        attempts_table.setStyle(TableStyle([('BACKGROUND', (3, idx), (4, idx), AMBER)]))
story += [attempts_table, PageBreak()]

story += [para('Cost method, local edits and evidence', 'h1'),
          para('Estimated USD = returned completion_tokens x US$10.70 / 1,000,000. Estimated HKD = USD x 7.847. The FX observation is dated 15 October 2026, checked on 16 October 2026. All generation requests used image references, with zero reference-video input.', 'body'),
          para(f'Selected video sources: {money(S["selected_usd"], "US$")} / {money(S["selected_hkd"])}. Superseded successful videos: {money(S["superseded_usd"], "US$")} / {money(S["superseded_hkd"])}. Local assembly and conventional edits add no Seedance generation cost.', 'body'),
          para('These are list-price estimates derived from recorded provider usage. They exclude image generation, Codex subscription costs, account discounts or credits, taxes and card exchange fees. There are no unresolved charge attempts in the ledger.', 'small'),
          para('Selected local edits and source filenames', 'h2')]
edit_rows = [[cell(h, 'head') for h in ['Segment', 'Selected video file', 'Generated source file', 'Additional Seedance cost']]]
for cid, edit in S['selected_local_edits'].items():
    native = next(a['video_file'] for a in ATTEMPTS if a['segment'] == cid and a['take'] == edit['source_take'])
    edit_rows.append([cell(cid), cell(selected[cid]['path'], 'file'), cell(native, 'file'), cell('HK$0.00', 'right')])
t = Table(edit_rows, colWidths=[65, 285, 285, WIDTH-635], hAlign='LEFT')
t.setStyle(table_style()); story += [t, Spacer(1, 6),
          para('s09_c01 uses a local crop to remove a duplicate child. s13_c01 uses a local ambience replacement with existing project audio. An unused crop trial and assembly trial are not new Seedance generations.', 'small'),
          para('Failed and rejected requests', 'h2')]
failure_rows = [[cell(h, 'head') for h in ['Segment', 'Take', 'Result', 'Provider error code', 'Est. HKD']]]
for a in ATTEMPTS:
    if a['state'] != 'succeeded':
        failure_rows.append([cell(a['segment']), cell(a['take']), cell(a['state']),
                             cell(a['error_code'], 'file'), cell('HK$0.00', 'right')])
t = Table(failure_rows, colWidths=[65, 65, 65, WIDTH-275, 80], hAlign='LEFT')
t.setStyle(table_style());story += [t, Spacer(1, 7)]
references = [
    ('Published price and successful-generation billing policy', S['pricing_source']),
    ('YCharts ECB-derived USD/HKD observation for 15 October 2026', S['fx_source']),
]
for label, url in references:
    story.append(para(f'<b>{escape(label)}</b>: <link href="{escape(url)}" color="#244E80">{escape(url)}</link>', 'small', markup=True))
story += [
    para('Project evidence: revision 57, usage.json, exports/task-journal.json including all prior takes, assembly settings, selected local-edit records and exports/verification.json. All 96 attempt IDs match between the ledger and journal. All 91 generated files and all 70 selected clip files exist.', 'small'),
    para('Final movie verification: dog-20261014-480p.mp4 has 28,800 video frames at 24 fps, giving an exact 1,200-second video timeline. The MP4 container is 1,200.02 seconds, with stereo AAC audio at 48 kHz. These are the recorded production verification results.', 'small'),
    para('Production session: 14 October 2026 19:32:52 to 15 October 2026 14:45:23 Hong Kong time. Elapsed time was 19:12:31, including preparation, queues, reviews and approval waits. It is not model processing time.', 'small'),
]

doc = SimpleDocTemplate(str(FINAL), pagesize=(PAGE_W, PAGE_H),
                        leftMargin=36, rightMargin=36, topMargin=40, bottomMargin=39,
                        title='dog-20261014 production and cost report', author='')
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
reader = PdfReader(FINAL)
text = '\n'.join(page.extract_text(extraction_mode='plain') or '' for page in reader.pages)
compact = ''.join(text.split())
missing = [f for f in sorted(expected_files) if ''.join(f.split()) not in compact]
assert not missing, f'Filenames missing from PDF: {missing}'
assert final_movie.name in text
assert all(s['segment'] in text for s in SEGMENTS)
assert all(a['error_code'] in text for a in ATTEMPTS if a['error_code'])
assert '1,264.69' in text and '15,062,518' in text
assert len(ATTEMPTS) == 96 and len(SEGMENTS) == 70
assert sum(bool(a['video_file']) for a in ATTEMPTS) == 91
assert all(hashlib.sha256((MOVIE / rel).read_bytes()).hexdigest() == expected
           for rel, expected in S['source_hashes_sha256'].items())
qa = {'pdf': str(FINAL), 'pages': len(reader.pages), 'final_movie_filename': final_movie.name,
      'planned_segments': len(SEGMENTS), 'requests': len(ATTEMPTS),
      'generated_video_filenames': 91, 'unique_selected_or_generated_paths': len(expected_files),
      'all_video_paths_present_in_pdf': not missing, 'production_sources_unchanged': True,
      'page_text_lengths': [len(page.extract_text() or '') for page in reader.pages]}
(Path(__file__).parent / 'pdf-qa.json').write_text(json.dumps(qa, indent=2), encoding='utf-8')
print(json.dumps(qa, indent=2))
