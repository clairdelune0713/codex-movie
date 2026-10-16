import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {createRequire} from 'node:module';
const bundledRequire = createRequire('C:/Users/Admin 3/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/loader.cjs');
const {Workbook, SpreadsheetFile} = await import(pathToFileURL(bundledRequire.resolve('@oai/artifact-tool')).href);

const dir = path.dirname(fileURLToPath(import.meta.url));
const data = JSON.parse(await fs.readFile(path.join(dir, 'report-data.json'), 'utf8'));
const {summary: s, segments, attempts} = data;
const wb = Workbook.create();
const summary = wb.worksheets.add('Summary');
const seg = wb.worksheets.add('Segments');
const att = wb.worksheets.add('Attempts');
const segStart = 7, segEnd = segStart + segments.length - 1;
const attStart = 7, attEnd = attStart + attempts.length - 1;
const navy = '#253C59', muted = '#627084', pale = '#F1F4F8';
const usd = '"US$"#,##0.000000', hkd = '"HK$"#,##0.00';
const sRange = col => `'Segments'!$${col}$${segStart}:$${col}$${segEnd}`;
const aRange = col => `'Attempts'!$${col}$${attStart}:$${col}$${attEnd}`;
const set = (sheet, cell, value) => sheet.getRange(cell).values = [[value]];
const formula = (sheet, cell, value) => sheet.getRange(cell).formulas = [[value]];
function base(sheet, extent) {
  sheet.showGridLines = false;
  const r = sheet.getRange(extent);
  r.format.font = {name: 'Arial', size: 10, color: '#233044'};
  r.format.rowHeight = 22;
  r.format.verticalAlignment = 'center';
}
function title(sheet, text, note) {
  set(sheet, 'A2', text);
  sheet.getRange('A2').format.font = {name: 'Arial', size: 14, bold: true, color: navy};
  sheet.getRange('A2').format.rowHeight = 28;
  if (note) {
    set(sheet, 'A4', note);
    sheet.getRange('A4').format.font = {name: 'Arial', size: 10, italic: true, color: muted};
  }
}
function header(sheet, range) {
  sheet.getRange(range).format = {
    fill: navy, font: {name: 'Arial', size: 10, bold: true, color: '#FFFFFF'},
    horizontalAlignment: 'center', verticalAlignment: 'center', wrapText: true,
  };
}
function width(sheet, column, size) {sheet.getRange(`${column}:${column}`).format.columnWidth = size;}
function stripe(sheet, start, end, last) {
  for (let row=start; row<=end; row++) if ((row-start)%2) sheet.getRange(`A${row}:${last}${row}`).format.fill = '#F5F7FA';
}
base(summary, 'A1:H59'); base(seg, `A1:W${segEnd+2}`); base(att, `A1:S${attEnd+2}`);
summary.tabColor = navy; seg.tabColor = '#557396';

// Per-request source records and the owning cost calculation.
title(att, 'dog-20261014 request log', 'All requests, including failed and rejected submissions. Times shown in Hong Kong time (UTC+8).');
const aHeaders = ['#','Segment','Take','API result','Use in final movie','Recorded (HKT)','Seedance model','Resolution','Requested duration (s)','Native MP4 duration (s)','Completion tokens','Successful output (s)','Reference video (s)','Ledger estimate (USD)','Calculated estimate (USD)','Calculated estimate (HKD)','Provider error code','Provider task ID','Attempt ID'];
att.getRange('A6:S6').values = [aHeaders];
att.getRange(`A${attStart}:S${attEnd}`).values = attempts.map(a => [
  a.number, a.segment, a.take, a.state, a.use,
  new Date(Date.parse(a.recorded_at_utc) + 8*3600*1000), a.model, a.resolution,
  a.requested_seconds, a.native_container_seconds, a.completion_tokens, null,
  a.reference_video_seconds, a.ledger_usd, null, null, a.error_code,
  a.task_id || null, a.attempt_id,
]);
formula(att, 'L7', '=IF(D7="succeeded",I7,0)');
att.getRange(`L7:L${attEnd}`).fillDown();
formula(att, 'O7', '=IF(D7="succeeded",K7*\'Summary\'!$F$5/\'Summary\'!$F$6,0)');
att.getRange(`O7:O${attEnd}`).fillDown();
formula(att, 'P7', '=O7*\'Summary\'!$F$7');
att.getRange(`P7:P${attEnd}`).fillDown();
header(att, 'A6:S6'); att.getRange('A6:S6').format.rowHeight = 50;
stripe(att, 7, attEnd, 'S');
for (const [c,w] of Object.entries({A:5,B:13,C:12,D:12,E:21,F:22,G:41,H:12,I:15,J:15,K:17,L:15,M:15,N:21,O:22,P:21,Q:57,R:32,S:46})) width(att,c,w);
att.getRange(`F7:F${attEnd}`).setNumberFormat('yyyy-mm-dd hh:mm:ss');
att.getRange(`I7:I${attEnd}`).setNumberFormat('0');
att.getRange(`J7:J${attEnd}`).setNumberFormat('0.00');
att.getRange(`K7:M${attEnd}`).setNumberFormat('#,##0');
att.getRange(`N7:O${attEnd}`).setNumberFormat(usd);
att.getRange(`P7:P${attEnd}`).setNumberFormat(hkd);
att.getRange(`D7:D${attEnd}`).conditionalFormats.add('containsText', {text:'failed',format:{fill:'#FCE9E6',font:{color:'#9C3028'}}});
att.getRange(`D7:D${attEnd}`).conditionalFormats.add('containsText', {text:'rejected',format:{fill:'#FFF1DB',font:{color:'#805000'}}});
att.freezePanes.freezeRows(6); att.freezePanes.freezeColumns(3);

// One row for each planned generation segment.
title(seg, 'dog-20261014 segment breakdown', 'First success = request number returning the first video. All requests include later quality revisions.');
const headers = ['#','Segment','Scene','Description','Timeline start (s)','Duration (s)','All requests','Videos generated','Failed after acceptance','Rejected before generation','Requests to first success','First successful take','Final selected take','Native source take','Successful output (s)','All requested duration (s)','Completion tokens','Estimated cost (USD)','Estimated cost (HKD)','Seedance model','Native resolution','Aspect ratio','Revision / edit notes'];
seg.getRange('A6:W6').values = [headers];
seg.getRange(`A7:W${segEnd}`).values = segments.map(x => [
  x.number,x.segment,x.scene,x.description,x.timeline_start_seconds,x.duration_seconds,
  null,null,null,null,x.requests_to_first_success,x.first_successful_take,
  x.final_selected_take,x.source_video_take,null,null,null,null,null,x.model,x.resolution,x.aspect_ratio,x.notes,
]);
const formulas = {
  G:`=COUNTIFS(${aRange('B')},$B7)`,
  H:`=COUNTIFS(${aRange('B')},$B7,${aRange('D')},"succeeded")`,
  I:`=COUNTIFS(${aRange('B')},$B7,${aRange('D')},"failed")`,
  J:`=COUNTIFS(${aRange('B')},$B7,${aRange('D')},"rejected")`,
  O:`=SUMIFS(${aRange('L')},${aRange('B')},$B7)`,
  P:`=SUMIFS(${aRange('I')},${aRange('B')},$B7)`,
  Q:`=SUMIFS(${aRange('K')},${aRange('B')},$B7)`,
  R:`=SUMIFS(${aRange('O')},${aRange('B')},$B7)`,
  S:`=SUMIFS(${aRange('P')},${aRange('B')},$B7)`,
};
for (const [col,f] of Object.entries(formulas)) {formula(seg,`${col}7`,f);seg.getRange(`${col}7:${col}${segEnd}`).fillDown();}
header(seg,'A6:W6'); seg.getRange('A6:W6').format.rowHeight = 58;
stripe(seg,7,segEnd,'W'); seg.getRange(`A7:W${segEnd}`).format.rowHeight = 32;
for(const [c,w] of Object.entries({A:5,B:13,C:7,D:61,E:15,F:12,G:12,H:13,I:15,J:16,K:15,L:16,M:21,N:17,O:17,P:18,Q:18,R:22,S:21,T:41,U:21,V:12,W:105}))width(seg,c,w);
seg.getRange(`D7:D${segEnd}`).format.wrapText = true;
seg.getRange(`E7:K${segEnd}`).setNumberFormat('#,##0');
seg.getRange(`O7:Q${segEnd}`).setNumberFormat('#,##0');
seg.getRange(`R7:R${segEnd}`).setNumberFormat(usd);
seg.getRange(`S7:S${segEnd}`).setNumberFormat(hkd);
seg.getRange(`G7:G${segEnd}`).conditionalFormats.add('cellIs',{operator:'greaterThan',formula:1,format:{fill:'#FFF1DB',font:{bold:true}}});
seg.freezePanes.freezeRows(6); seg.freezePanes.freezeColumns(3);

// Summary, with the two cost inputs kept close to the answer.
title(summary,'dog-20261014 production report');
for(const [c,w] of Object.entries({A:43,B:24,C:4,D:34,E:3,F:26,G:21,H:19}))width(summary,c,w);
set(summary,'A4','Production totals');header(summary,'A4:B4');
const metrics = [
  ['Planned generation segments',`=COUNTA(${sRange('B')})`],
  ['Screenplay scenes','=COUNTA(A31:A46)'],
  ['API requests',`=SUM(${sRange('G')})`],
  ['Successful returned videos',`=SUM(${sRange('H')})`],
  ['Failed after acceptance',`=SUM(${sRange('I')})`],
  ['Rejected before generation',`=SUM(${sRange('J')})`],
  ['Selected video sources',`=COUNTIFS(${aRange('E')},"Selected source")`],
  ['Final timeline duration (seconds)',`=SUM(${sRange('F')})`],
  ['Successful output duration (seconds)',`=SUM(${aRange('L')})`],
  ['Superseded successful videos','=B8-B11'],
  ['Estimated Seedance cost (USD)',`=SUM(${aRange('O')})`],
  ['Estimated Seedance cost (HKD)',`=SUM(${aRange('P')})`],
  ['Average requests per segment','=B7/B5'],
  ['Segments using one request in total',`=COUNTIFS(${sRange('G')},1)`],
  ['Segments first returning a video on request 1',`=COUNTIFS(${sRange('K')},1)`],
  ['Production elapsed time',s.production_elapsed_seconds/86400],
];
for(let i=0;i<metrics.length;i++){
  const [label,value]=metrics[i],r=i+5;set(summary,`A${r}`,label);
  typeof value==='string' ? formula(summary,`B${r}`,value) : set(summary,`B${r}`,value);
}
summary.getRange('B5:B14').setNumberFormat('#,##0');
summary.getRange('B15').setNumberFormat('"US$"#,##0.00000000');
summary.getRange('B16').setNumberFormat(hkd);
summary.getRange('B17').setNumberFormat('0.00');
summary.getRange('B18:B19').setNumberFormat('#,##0');
summary.getRange('B20').setNumberFormat('[h]:mm:ss');
summary.getRange('A15:B16').format.fill = '#E7EEF7';
summary.getRange('A15:B16').format.font.bold = true;
summary.getRange('B16').format.font.size = 14;
summary.getRange('A19').format.font.size = 9;
set(summary,'D4','Pricing and generation settings');header(summary,'D4:H4');
const rates = [
  [5,'USD per million completion tokens',s.rate_usd_per_million_tokens],
  [6,'Tokens per pricing unit',1000000],
  [7,'HKD per USD',s.hkd_per_usd],
  [8,'FX observation date',new Date('2026-10-15T00:00:00Z')],
  [10,'Model','Dreamina Seedance 2.5'],
  [11,'Model identifier',s.model],
  [12,'Native resolution','480p (854x480)'],
  [13,'Frame rate / aspect ratio','24 fps / 16:9'],
  [14,'Input type','Image references; zero video input'],
  [15,'Duration per segment','8–24 seconds'],
  [16,'Final timeline','20:00'],
  [18,'Unknown charge attempts',s.unknown_charge_attempts],
  [19,'Report date',new Date('2026-10-16T00:00:00Z')],
  [20,'Production dates (HKT)','14–15 October 2026'],
];
for(const [row,label,val] of rates){set(summary,`D${row}`,label);set(summary,`F${row}`,val);}
summary.getRange('F5').setNumberFormat('"US$"0.00');
summary.getRange('F6').setNumberFormat('#,##0');
summary.getRange('F7').setNumberFormat('0.000');
summary.getRange('F7').format.fill = '#FFF1C9';
summary.getRange('F8').setNumberFormat('yyyy-mm-dd');
summary.getRange('F19').setNumberFormat('yyyy-mm-dd');
const context = [
  'Costs include 91 successful generations. This includes 21 videos replaced during quality review.',
  'Five failed or rejected requests have an estimated zero generation fee under the provider policy.',
  'Local crops, audio edits and final assembly add no Seedance generation fee.',
  'API success means a returned video. Final selection also required visual review.',
  'List-price estimates exclude image generation, Codex subscription, discounts, tax and card FX fees.',
  '70 segments cover 16 screenplay scenes and 169 planned camera shots. Native output totals 26:04 before selection.',
];
for(let i=0;i<context.length;i++){set(summary,`A${22+i}`,context[i]);summary.getRange(`A${22+i}`).format.font.color=muted;}
set(summary,'A29','By screenplay scene');summary.getRange('A29').format.font.bold=true;
summary.getRange('A30:H30').values=[['Scene','Segments','Duration (s)','Requests','Videos','Failed / rejected','Estimated USD','Estimated HKD']];
header(summary,'A30:H30');summary.getRange('A30:H30').format.rowHeight=34;
for(let scene=1;scene<=16;scene++){
  const r=scene+30;set(summary,`A${r}`,scene);
  formula(summary,`B${r}`,`=COUNTIFS(${sRange('C')},$A${r})`);
  formula(summary,`C${r}`,`=SUMIFS(${sRange('F')},${sRange('C')},$A${r})`);
  formula(summary,`D${r}`,`=SUMIFS(${sRange('G')},${sRange('C')},$A${r})`);
  formula(summary,`E${r}`,`=SUMIFS(${sRange('H')},${sRange('C')},$A${r})`);
  formula(summary,`F${r}`,`=SUMIFS(${sRange('I')},${sRange('C')},$A${r})+SUMIFS(${sRange('J')},${sRange('C')},$A${r})`);
  formula(summary,`G${r}`,`=SUMIFS(${sRange('R')},${sRange('C')},$A${r})`);
  formula(summary,`H${r}`,`=SUMIFS(${sRange('S')},${sRange('C')},$A${r})`);
}
stripe(summary,31,46,'H');
set(summary,'A47','Total');for(const c of ['B','C','D','E','F','G','H'])formula(summary,`${c}47`,`=SUM(${c}31:${c}46)`);
summary.getRange('A47:H47').format.font.bold=true;summary.getRange('A47:H47').format.fill=pale;
summary.getRange('A31:F47').setNumberFormat('#,##0');
summary.getRange('G31:G47').setNumberFormat('"US$"#,##0.00');summary.getRange('H31:H47').setNumberFormat(hkd);
// The leading gutter is not used in this operational report; C is narrow above but must fit duration here.
width(summary,'C',16);
width(summary,'E',12);
set(summary,'A50','Sources and calculation method');summary.getRange('A50').format.font.bold=true;
const sourceNotes = [
  'USD = returned completion tokens x published USD rate / 1,000,000. HKD = USD x HKD-per-USD input F7.',
  'BytePlus Seedance 2.5 pricing and successful-generation billing policy, checked 16 October 2026:',
  s.pricing_source,
  'USD/HKD: YCharts ECB-derived observation for 15 October 2026. Conversion input F7 can be changed.',
  s.fx_source,
  'Records: project revision 57, usage ledger, full take journal, assembly settings and selected local-edit records.',
  'Reconciled 96 unique attempts and 94 task IDs. All 91 generated files exist. All 70 segments have selected sources.',
  'Every successful job has returned completion-token usage. No duration-based token estimates were needed.',
];
for(let i=0;i<sourceNotes.length;i++){set(summary,`A${51+i}`,sourceNotes[i]);summary.getRange(`A${51+i}`).format.font.color=muted;}

// Verify linked costs respond to the FX driver, then restore the recorded observation.
const near = (a,b) => Math.abs(a-b)<1e-7;
const before = summary.getRange('B16').values[0][0];
if(!near(before,s.hkd_total))throw new Error(`Initial HKD mismatch: ${before}`);
set(summary,'F7',8);
const changed = summary.getRange('B16').values[0][0];
if(!near(changed,s.usd_total*8))throw new Error(`FX recalculation failed: ${changed}`);
set(summary,'F7',s.hkd_per_usd);
wb.recalculate();
const expected={B5:70,B6:16,B7:96,B8:91,B9:3,B10:2,B11:70,B12:1200,B13:1564,B14:21,B15:s.usd_total,B16:s.hkd_total,B18:51,B19:68};
for(const [cell,want] of Object.entries(expected)){
  const got=summary.getRange(cell).values[0][0];
  if(!near(got,want))throw new Error(`${cell}: expected ${want}, got ${got}`);
}
for(let i=0;i<segments.length;i++){
  const got=seg.getRange(`G${i+7}:S${i+7}`).values[0],x=segments[i];
  for(const [idx,want] of [[0,x.requests],[1,x.videos_generated],[2,x.failed_after_acceptance],[3,x.rejected_before_generation],[8,x.successful_output_seconds],[9,x.all_request_seconds],[10,x.completion_tokens],[11,x.estimated_usd],[12,x.estimated_hkd]]){
    if(!near(got[idx],want))throw new Error(`Segment ${x.segment} reconciliation failed in column ${idx}`);
  }
}
const scan=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},summary:'Formula error scan'});
const overview=await wb.inspect({kind:'region',sheetId:'Summary',range:'A4:B20',maxChars:4500,tableMaxRows:20,tableMaxCols:2});
await fs.writeFile(path.join(dir,'workbook-inspection.json'),JSON.stringify({scan,overview,fxTest:{before,changed,restored:summary.getRange('B16').values[0][0]},all70SegmentRowsReconciled:true},null,2));
console.log(overview.ndjson);console.log(scan.ndjson);
const views = [
  ['Summary','A1:H27','summary-preview.png'],
  ['Summary','A29:H58','summary-detail-preview.png'],
  ['Segments','A1:N15','segments-preview.png'],
  ['Segments','O5:W15','segment-cost-preview.png'],
  ['Attempts','A1:F16','attempts-preview.png'],
  ['Attempts','G5:S12','attempt-cost-preview.png'],
];
for(const [sheetName,range,name] of views){
  const blob=await wb.render({sheetName,range,scale:1.4,format:'png'});
  await fs.writeFile(path.join(dir,name),new Uint8Array(await blob.arrayBuffer()));
}
const output=await SpreadsheetFile.exportXlsx(wb);
await output.save(path.join(dir,'dog-20261014-production-report.xlsx'));
console.log('EXPORTED dog-20261014-production-report.xlsx');
