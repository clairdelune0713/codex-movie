import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
project = json.loads((root / 'project.json').read_text(encoding='utf-8'))
package = json.loads((root / 'exports' / f"render-package-r{project['revision']:06d}.json").read_text(encoding='utf-8'))
delivery = json.loads((root / 'exports/delivery-specification.json').read_text(encoding='utf-8'))
package.update(project_name=project['project_name'], project_root=str(root), status='prepared_awaiting_video_renderer', total_duration_target=60, output_goals=delivery['output_goals'], desired_output_filename=delivery['desired_output_filename'], actual_video=None, pending_stages=delivery['pending_stages'], storyboard_note=delivery['storyboard_note'])
package['status'] = delivery['status']
package['actual_video'] = delivery['actual_video']
for exported, chapter in zip(package['chapters'], project['chapters']):
    selected = next(s for s in chapter['storyboards'] if s['id'] == chapter['selected_storyboard_id'])
    exported['title'] = chapter['title']
    exported['movie_start_seconds'] = chapter['movie_start']
    exported['movie_end_seconds'] = chapter['movie_end']
    exported['handoff'] = chapter['handoff']
    exported['audio'] = chapter['audio']
    exported['selected_storyboard'] = {'id': selected['id'], 'path': str(root / selected['path']), 'grid': selected['grid'], 'panel_descriptions': selected['panel_descriptions'], 'inspection': selected['inspection'], 'dependency_fingerprint': selected['dependency_fingerprint']}
assert len(package['chapters']) == 6 and sum(c['duration'] for c in package['chapters']) == 60
assert all(Path(reference['path']).is_file() for c in package['chapters'] for reference in c['references'])
assert all(Path(c['selected_storyboard']['path']).is_file() for c in package['chapters'])
(root / 'exports/render-package.json').write_text(json.dumps(package, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print('Expanded render-package.json: six chapters, verified references and storyboards; delivery status ' + delivery['status'])
