import collections
import csv
import hashlib
import json
from decimal import Decimal
from pathlib import Path

BASE = Path(__file__).resolve().parent
PROJECT = BASE.parents[1] / 'movies' / 'dog-20261014'
FX = Decimal('7.847')
RATE = Decimal('10.70')
PRICE_URL = 'https://docs.byteplus.com/id/docs/modelark/model-pricing?redirect=1'
FX_URL = 'https://ycharts.com/indicators/us_dollar_to_hong_kong_dollar_exchange_rate'


def read(rel):
    return json.loads((PROJECT / rel).read_text(encoding='utf-8'))


p = read('project.json')
j = read('exports/task-journal.json')
u = read('usage.json')
assembly = read('exports/assembly-settings.json')
verification = read('exports/verification.json')
old_report = read('exports/usage-report-session_4c7e7838a5184bab82868c8ba6b1cbd8.json')
sources = ['project.json', 'usage.json', 'exports/task-journal.json',
           'exports/assembly-settings.json', 'exports/verification.json',
           'exports/usage-report-session_4c7e7838a5184bab82868c8ba6b1cbd8.json']
source_hashes = {rel: hashlib.sha256((PROJECT / rel).read_bytes()).hexdigest() for rel in sources}

by_attempt = {}
for latest in j['takes'].values():
    for take in latest.get('prior_takes', []) + [latest]:
        aid = take.get('attempt_id')
        assert aid and aid not in by_attempt, ('duplicate/missing attempt', aid)
        by_attempt[aid] = take
assert set(by_attempt) == set(u['jobs']), 'Ledger and journal attempt IDs differ'
assert len(u['sessions']) == 1

selected = {item['chapter']: item for item in assembly['input_takes']}
selected_sources = {}
local_edits = {}
for cid, item in selected.items():
    native_id = item['take']
    if native_id.count('_') > 1:
        edit = read(f'exports/local-edits/{cid}_{native_id}.json')
        native_id = edit['source_video_take_id']
        assert edit['local_edit']['additional_seedance_cost'] == '0'
        local_edits[cid] = {'selected_take': item['take'], 'source_take': native_id,
                            'type': edit['local_edit']['type'],
                            'reason': edit['local_edit']['reason']}
    selected_sources[cid] = native_id
assert len(selected) == len(p['chapters'])

notes = {
    's02_c03': 'Guide lead and floor staging revised. Take 03 failed output-audio policy.',
    's03_c01': 'Cantonese dialogue alignment revised.',
    's03_c02': 'Cantonese dialogue alignment revised.',
    's03_c03': 'Guide-handle continuity revised.',
    's03_c04': 'Guide-handle continuity revised.',
    's04_c01': 'Guide control and visiting-dog floor staging revised.',
    's04_c02': 'Guide control and visiting-dog floor staging revised.',
    's04_c04': 'Cafe departure staging and Cantonese dialogue revised.',
    's04_c06': 'Input privacy rejection, then guide-control revision.',
    's07_c03': 'Evening lighting continuity revised.',
    's08_c02': 'Walking direction and location continuity revised.',
    's09_c01': 'Local crop removes duplicate child. One Seedance output, no added generation fee.',
    's12_c02': 'One input privacy rejection and two output-video policy failures; take 04 succeeded.',
    's13_c01': 'Dogs separated across forecourt. Local ambience replacement after take 02.',
    's14_c02': 'May character identity revised.',
    's14_c03': 'Dog floor staging revised.',
    's15_c02': 'Open-air planter-gap geography revised twice.',
    's16_c02': 'Dogs on floor, lead ownership and toy invitation revised.',
    's16_c05': 'Dogs on floor and reunion coverage revised twice.',
    's16_c07': 'Character identity and group seating coverage revised.',
}

attempts = []
segments = []
for chapter in p['chapters']:
    cid = chapter['id']
    jobs = [v for v in u['jobs'].values() if v['chapter_id'] == cid]
    jobs.sort(key=lambda v: by_attempt[v['attempt_id']]['take_number'])
    assert jobs
    successes = [v for v in jobs if v['state'] == 'succeeded']
    assert successes
    first_success = next(i + 1 for i, v in enumerate(jobs) if v['state'] == 'succeeded')
    assert any(v['take_id'] == selected_sources[cid] for v in successes)
    for ordinal, job in enumerate(jobs, 1):
        take = by_attempt[job['attempt_id']]
        assert job['take_id'] == take['id']
        assert job['chapter_id'] == take['chapter_id']
        assert job.get('task_id') == take.get('task_id')
        assert job['resolution'] == '480p'
        assert job['model'] == 'dreamina-seedance-2-5-260628'
        assert job['reference_video_seconds'] == 0
        assert job['cost']['currency'] == 'USD'
        assert job['cost']['kind'] == 'estimated'
        cost = Decimal(job['cost']['amount'])
        usage = job.get('usage', {})
        token_count = usage.get('completion_tokens')
        ok = job['state'] == 'succeeded'
        native = take.get('verification', {})
        if ok:
            assert isinstance(token_count, int) and token_count > 0
            assert cost == Decimal(token_count) * RATE / Decimal(1000000)
            assert (native['width'], native['height'], native['fps']) == (854, 480, 24.0)
            assert (PROJECT / take['path']).is_file()
        else:
            assert job['state'] in ('failed', 'rejected') and cost == 0
        err = take.get('error') or {}
        use = ('Selected source' if job['take_id'] == selected_sources[cid]
               else 'Superseded video') if ok else 'No video'
        attempts.append({
            'number': len(attempts) + 1, 'segment': cid, 'take': job['take_id'],
            'state': job['state'], 'use': use,
            'recorded_at_utc': job['recorded_at'],
            'model': job['model'], 'resolution': job['resolution'],
            'requested_seconds': job['duration_seconds'],
            'native_container_seconds': native.get('duration') if ok else None,
            'completion_tokens': token_count,
            'successful_output_seconds': job['duration_seconds'] if ok else 0,
            'reference_video_seconds': job['reference_video_seconds'],
            'ledger_usd': float(cost), 'estimated_usd': float(cost),
            'estimated_hkd': float(cost * FX),
            'error_code': err.get('code', ''), 'task_id': job.get('task_id', ''),
            'attempt_id': job['attempt_id'], 'request_number_in_segment': ordinal,
        })
    usd = sum((Decimal(job['cost']['amount']) for job in jobs), Decimal(0))
    selected_cost = next(Decimal(job['cost']['amount']) for job in jobs
                         if job['take_id'] == selected_sources[cid])
    segments.append({
        'number': chapter['chapter_index'], 'segment': cid, 'scene': chapter['source_scene'],
        'description': chapter['title'], 'timeline_start_seconds': chapter['absolute_start'],
        'duration_seconds': chapter['duration'], 'requests': len(jobs),
        'videos_generated': len(successes),
        'failed_after_acceptance': sum(job['state'] == 'failed' for job in jobs),
        'rejected_before_generation': sum(job['state'] == 'rejected' for job in jobs),
        'requests_to_first_success': first_success,
        'first_successful_take': jobs[first_success - 1]['take_id'],
        'final_selected_take': selected[cid]['take'], 'source_video_take': selected_sources[cid],
        'successful_output_seconds': sum(job['duration_seconds'] for job in successes),
        'all_request_seconds': sum(job['duration_seconds'] for job in jobs),
        'completion_tokens': sum(job.get('usage', {}).get('completion_tokens', 0) for job in jobs),
        'estimated_usd': float(usd), 'estimated_hkd': float(usd * FX),
        'selected_source_usd': float(selected_cost),
        'superseded_usd': float(usd - selected_cost),
        'model': 'dreamina-seedance-2-5-260628', 'resolution': '480p (854x480)',
        'aspect_ratio': '16:9', 'notes': notes.get(cid, ''),
    })

usd_total = sum((Decimal(v['cost']['amount']) for v in u['jobs'].values()), Decimal(0))
assert str(usd_total) == old_report['project_total']['seedance_cost']['currencies']['USD']['estimated']
assert len(attempts) == 96 and sum(v['videos_generated'] for v in segments) == 91
assert len({a['task_id'] for a in attempts if a['task_id']}) == 94
assert sum(s['duration_seconds'] for s in segments) == 1200
selected_usd = sum((Decimal(u['jobs'][a['attempt_id']]['cost']['amount']) for a in attempts
                    if a['use'] == 'Selected source'), Decimal(0))
summary = {
    'project': p['id'], 'revision': p['revision'], 'report_date': '2026-10-16',
    'planned_segments': len(segments), 'screenplay_scenes': len(set(s['scene'] for s in segments)),
    'planned_camera_shots': sum(len(c['shots']) for c in p['chapters']),
    'api_requests': len(attempts), 'accepted_tasks': 94,
    'videos_generated': sum(a['state'] == 'succeeded' for a in attempts),
    'failed_after_acceptance': sum(a['state'] == 'failed' for a in attempts),
    'rejected_before_generation': sum(a['state'] == 'rejected' for a in attempts),
    'selected_sources': sum(a['use'] == 'Selected source' for a in attempts),
    'superseded_videos': sum(a['use'] == 'Superseded video' for a in attempts),
    'final_timeline_seconds': sum(s['duration_seconds'] for s in segments),
    'requested_seconds_all_attempts': sum(a['requested_seconds'] for a in attempts),
    'successful_output_seconds': sum(a['successful_output_seconds'] for a in attempts),
    'completion_tokens': sum(a['completion_tokens'] or 0 for a in attempts),
    'usd_total': float(usd_total), 'hkd_total': float(usd_total * FX),
    'usd_exact': str(usd_total), 'hkd_exact': str(usd_total * FX),
    'selected_usd': float(selected_usd), 'selected_hkd': float(selected_usd * FX),
    'superseded_usd': float(usd_total - selected_usd),
    'superseded_hkd': float((usd_total - selected_usd) * FX),
    'unknown_charge_attempts': old_report['project_total']['seedance_cost']['unknown_charge_attempts'],
    'request_distribution': dict(sorted(collections.Counter(s['requests'] for s in segments).items())),
    'first_success_distribution': dict(sorted(collections.Counter(s['requests_to_first_success'] for s in segments).items())),
    'production_session': u['sessions'][0],
    'production_elapsed_seconds': old_report['session']['elapsed_seconds'],
    'model': 'dreamina-seedance-2-5-260628',
    'resolution': '480p', 'width': 854, 'height': 480, 'fps': 24, 'aspect_ratio': '16:9',
    'minimum_segment_seconds': min(s['duration_seconds'] for s in segments),
    'maximum_segment_seconds': max(s['duration_seconds'] for s in segments),
    'rate_usd_per_million_tokens': float(RATE), 'hkd_per_usd': float(FX),
    'fx_date': '2026-10-15', 'pricing_checked': '2026-10-16',
    'pricing_source': PRICE_URL, 'fx_source': FX_URL,
    'source_hashes_sha256': source_hashes, 'selected_local_edits': local_edits,
    'final_verification': verification,
}
report = {'summary': summary, 'segments': segments, 'attempts': attempts}
(BASE / 'report-data.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')

segment_columns = ['number', 'segment', 'scene', 'description', 'timeline_start_seconds',
                   'duration_seconds', 'requests', 'videos_generated', 'failed_after_acceptance',
                   'rejected_before_generation', 'requests_to_first_success', 'first_successful_take',
                   'final_selected_take', 'source_video_take', 'successful_output_seconds',
                   'all_request_seconds', 'completion_tokens', 'estimated_usd', 'estimated_hkd',
                   'model', 'resolution', 'aspect_ratio', 'notes']
for filename, records, columns in [
    ('dog-20261014-segments.csv', segments, segment_columns),
    ('dog-20261014-attempts.csv', attempts, list(attempts[0])),
]:
    with (BASE / filename).open('w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(records)


def mtime(seconds):
    return f'{int(seconds) // 60}:{int(seconds) % 60:02d}'


lines = [
    '# dog-20261014 generation and cost report', '',
    'Report date: 16 October 2026. Project revision: 57. Scope: recorded Seedance video generation for this project.', '',
    '| Metric | Result |', '|---|---:|',
    f'| Planned generation segments | {summary["planned_segments"]} |',
    f'| Screenplay scenes / planned camera shots | {summary["screenplay_scenes"]} / {summary["planned_camera_shots"]} |',
    '| Final timeline | 20:00 (1,200 seconds) |',
    '| Model | Dreamina Seedance 2.5 (`dreamina-seedance-2-5-260628`) |',
    '| Native video format | 480p, 854×480, 16:9, 24 fps |',
    '| Segment durations | 8–24 seconds |',
    '| Total API requests | 96 |', '| Accepted provider tasks | 94 |',
    '| Successful returned videos | 91 |', '| Failed after acceptance | 3 |',
    '| Rejected before generation | 2 |', '| Selected video sources | 70 |',
    '| Successful superseded videos | 21 |',
    '| Successful output duration, before selection | 26:04 (1,564 nominal seconds) |',
    '| Requested duration across all requests | 27:36 (1,656 seconds, including requests that failed) |',
    f'| Returned completion tokens | {summary["completion_tokens"]:,} |',
    f'| Estimated Seedance cost (USD) | US${usd_total:.8f} |',
    f'| Estimated Seedance cost (HKD) | HK${usd_total * FX:,.2f} |',
    '| Unresolved charge attempts | 0 |', '',
    'The ledger and the full take history match on all 96 unique attempt IDs. All 91 successful source files exist and their recorded verification is 854×480 at 24 fps. Every planned segment has a selected source.', '',
    '## What “successful” means', '',
    'A successful API request returned a video. Some returned videos still needed revisions for dialogue, character identity, guide-dog handling, staging or continuity. The report therefore shows both requests to the first API success and all requests used to reach the selected final take.', '',
    '| Requests per segment, including rejections | Number of segments |', '|---:|---:|',
] + [f'| {k} | {v} |' for k, v in summary['request_distribution'].items()] + [
    '', '68 segments returned a video on their first request. s04_c06 first succeeded on request 2. s12_c02 first succeeded on request 4. A total of 51 segments used just one request through final selection; 19 segments had multiple requests.', '',
    '## Cost calculation', '',
    f'Estimated USD = returned completion_tokens × US${RATE} / 1,000,000. This uses the published no-video-input rate. All requests used image references, with zero reference-video seconds. Still images extracted from prior clips remain image input.', '',
    f'Estimated HKD = estimated USD × {FX}. The conversion uses the [YCharts ECB-derived USD/HKD value for 15 October 2026]({FX_URL}), checked on 16 October 2026.', '',
    f'The [BytePlus pricing page]({PRICE_URL}) lists the rate and states that unsuccessful video generations are not charged. The five confirmed failed/rejected requests are therefore estimated at zero. The successful replaced takes remain included.', '',
    f'Selected video sources account for US${selected_usd:.8f} (HK${selected_usd * FX:,.2f}). Superseded successful videos account for US${usd_total - selected_usd:.8f} (HK${(usd_total - selected_usd) * FX:,.2f}).', '',
    'These are usage-based list-price estimates. The account invoice, discounts, credits, taxes and card exchange fees were not available. Image generation and Codex subscription costs are outside this Seedance video total.', '',
    '## All planned segments', '',
    'Model and native format above apply to every row. Duration is the planned timeline / nominal generated duration for one take. “Videos” counts successful outputs only. “First success” is the request number that first returned a video. “HKD” includes every successful take for that segment, including superseded takes.', '',
    '| # | Segment | Description | Duration (s) | Requests | Videos | Failed / rejected | First success | Selected take | Est. HKD |',
    '|---:|---|---|---:|---:|---:|---:|---:|---|---:|',
]
for s in segments:
    lines.append(f'| {s["number"]} | {s["segment"]} | {s["description"].replace("|", "/")} | {s["duration_seconds"]} | {s["requests"]} | {s["videos_generated"]} | {s["failed_after_acceptance"]}/{s["rejected_before_generation"]} | {s["requests_to_first_success"]} | {s["final_selected_take"]} | {s["estimated_hkd"]:.2f} |')
lines += [
    '', 'Per-row amounts are shown to cents. The total is calculated from unrounded amounts, so displayed cents can have a small rounding difference.', '',
    '## Revision notes', '', '| Segment | Reason / local edit |', '|---|---|',
] + [f'| {cid} | {note} |' for cid, note in notes.items()] + [
    '', 'The selected local edits are s09_c01 take_01_crop02 (one generated source) and s13_c01 take_02_mix01 (two generated sources for that segment). These edits do not count as new Seedance generations. An unused crop trial and final assembly exports are also excluded from API request counts.', '',
    '## Failed and rejected requests', '',
    '| Segment | Take | Result | Provider code | Est. HKD |', '|---|---|---|---|---:|',
] + [f'| {a["segment"]} | {a["take"]} | {a["state"]} | {a["error_code"]} | 0.00 |' for a in attempts if a['state'] != 'succeeded'] + [
    '', '## Evidence and timing', '',
    'Sources: canonical project revision 57, usage.json, exports/task-journal.json including all prior_takes, exports/assembly-settings.json, selected local-edit records, exports/verification.json and the production-session usage report. The accompanying workbook includes all 96 attempt IDs and 94 provider task IDs for reconciliation.', '',
    'Production session: 14 October 2026 19:32:52 to 15 October 2026 14:45:23 Hong Kong time. Elapsed time: 19 hours 12 minutes 31 seconds, including preparation, queues, review and approval waits. It is not model processing time.', '',
]
(BASE / 'dog-20261014-report.md').write_text('\n'.join(lines), encoding='utf-8')
print(json.dumps({k: v for k, v in summary.items() if k not in ('source_hashes_sha256', 'final_verification', 'selected_local_edits')}, ensure_ascii=False, indent=2))
