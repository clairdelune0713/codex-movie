# Local project state

`project.json` is canonical structured state. The helper uses Python's standard library and no network. Media, project JSON, history and exports live inside the user's chosen project directory, not inside the installed skill.

```text
movies/<project>/
  project.json
  history/revision-000000.json
  assets/<asset-id>/<candidate-id>.<ext>
  chapters/<chapter-id>/storyboards/<storyboard-id>.png
  chapters/<chapter-id>/takes/<take-id>.mp4
  chapters/<chapter-id>/screenshots/<screenshot-id>.png
  exports/render-package-r000001.json
```

All stored `path`, `*_path` and `*_paths` fields must refer to existing project-relative local files. Copy supplied references into the project before recording them. Absolute paths are used at tool invocation and for final clickable links, and appear in the generated render package. External URLs may be kept under `source_uri` as provenance; they do not replace saved media. Keep keys consistent with the local schema below rather than assuming original app `imageUrl`/`imageKey` fields work here.

## Helper commands

Resolve `HELPER` to this skill's `scripts/project.py` and `PYTHON` to an executable interpreter. `ROOT` is the movie directory. Examples are argument layouts, not literal environment variables:

```text
PYTHON HELPER init ROOT --name "Movie title"
PYTHON HELPER check ROOT
PYTHON HELPER status ROOT
PYTHON HELPER check ROOT --from proposal.json
PYTHON HELPER commit ROOT --from proposal.json --reason "Refine chapter 2 blocking"
PYTHON HELPER fingerprint ROOT --asset @Mira
PYTHON HELPER fingerprint ROOT --chapter chapter_02
PYTHON HELPER fingerprint ROOT --chapter chapter_02 --from proposal.json
PYTHON HELPER restore ROOT --revision 3 --reason "Return to previous visual style"
PYTHON HELPER export ROOT
```

After `init`, copy the latest `project.json` to a working proposal JSON, modify the proposal, check it, then commit. Do not hand-edit the live `project.json` or snapshots. A proposal must preserve project `id` and the current `revision`; a stale base revision is rejected. Commit writes the next snapshot and atomically replaces the live JSON. If writing live state fails after reserving a history revision, keep the snapshot and reconcile it with the live JSON; do not delete history and retry blindly. The helper rejects concurrent commits reserving the same revision. Restoring creates a new revision, leaving all earlier snapshots/media available.

`check` exits nonzero for errors: duplicate/invalid tags or IDs, unknown tags/links, selected IDs missing, selected failed takes, missing/escaping local paths, invalid duration, total mismatch, shot gaps/overlap, and detected prompt/structured-shot timing mismatch. Warnings include missing selected references and timing syntax requiring visual/manual review. Structural validation does not prove creative quality, correct prose, media type/decodability, or permission to render.

`status` also returns `current`, `stale`, or `unknown` freshness for candidates/storyboards/takes. `fingerprint` captures relevant current dependencies; save its returned string on an artifact **at generation/submission time**, not after later edits. Missing fingerprints yield `unknown`; never assign a current fingerprint to old media to conceal staleness. Chapter fingerprints include style, canonical prompt/shots/duration, aspect ratio, selected linked asset identity/file hash, and material files/roles. Unrelated unlinked asset edits do not stale a chapter. Candidate fingerprints cover style, description, category and supplied reference hashes. Original uploaded references can have unknown freshness because they were not generated from those definitions.

`export` prepares a versioned, tool-neutral render package; it does not generate video. Add renderer-specific bindings, settings and submission payload beside it when a renderer is chosen. Material paths in the package remain project-relative and resolve against ROOT; selected asset paths are absolute. Keep credentials outside project/history/exports.

## State conventions

The initializer creates common metadata, empty `asset_list`/`chapters`, a `style` object, 16:9 aspect ratio, adaptive timing, and historical Movi2 chapter limits `{ "min": 4, "max": 30 }`. Override them when user intent/current tools require it. Set `duration_mode` to `fixed` and `total_duration_target` to the requested seconds for an exact runtime. Chapter sums determine `total_estimated_duration` on commit.

Use `source_text`, `input_mode` (`idea` or `script`), `language`, `high_level_idea`, `detailed_script`, `master_prompt_raw`, and `style` for the production bible. Preserve source wording and user instructions. The helper retains additional fields, so narrative decisions, continuity notes and verified output metadata may be recorded without a database migration.

Asset example:

```json
{
  "id": "asset_mira",
  "tag": "@Mira",
  "name": "Mira",
  "category": "character",
  "description": "Short black bob, indigo raincoat; preserve identity in watercolor.",
  "source": "generated",
  "media_type": "Image",
  "status_variants": [],
  "reference_paths": [],
  "candidates": [
    {
      "id": "mira_c01",
      "path": "assets/asset_mira/mira_c01.png",
      "prompt": "Exact image tool prompt",
      "source_revision": 2,
      "dependency_fingerprint": "returned SHA-256 string",
      "created_at": "ISO timestamp"
    }
  ],
  "selected_candidate_id": "mira_c01"
}
```

Supported categories: `character`, `environment`, `prop`, `reference`. IDs are safe ASCII letters/digits/underscores/hyphens; tags support Unicode letters/numbers/underscores/hyphens with a leading @. Tags are unique case-insensitively and match whole tokens: @Mira and @Mira-hat are distinct. Filenames/IDs remain stable when display names change. Candidate files and their prompts are immutable once generated.

Chapter example (descriptive prompt abridged here only to show storage):

```json
{
  "id": "chapter_01",
  "chapter_index": 1,
  "title": "The arrival",
  "duration": 8,
  "high_level_idea": "The project's shared thematic idea",
  "scene_summary": "Mira finds a message at the station.",
  "prompt": "GLOBAL STYLE: watercolor. SCENE: @Mira at @station. Shot 1 (0-3s): @Mira enters @station. Hard cut. Shot 2 (3-8s): @Mira discovers the message.",
  "initial_prompt": "Preserved first expanded prompt",
  "tagged_assets": ["@Mira", "@station"],
  "linked_asset_ids": [],
  "delinked_asset_ids": [],
  "shots": [
    {"start": 0, "end": 3, "action": "@Mira enters @station", "camera": "Wide tracking", "audio": "Rain and footsteps", "end_state": "Mira pauses inside"},
    {"start": 3, "end": 8, "action": "@Mira discovers the message", "camera": "Slow close-up", "audio": "No dialogue", "end_state": "Mira holds the message"}
  ],
  "materials": [],
  "storyboards": [],
  "selected_storyboard_id": null,
  "takes": [],
  "active_take_id": null,
  "screenshots": []
}
```

Link resolution: explicit delink wins; then explicit asset ID link; then exact case-insensitive tag membership or prompt reference. Reconcile delinked tags out of prompts, shots and `tagged_assets` before committing. The source app used a substring check in one linking helper; this local implementation deliberately avoids prefix collisions. Direct shot actions must use known tags; keep those tags in the prompt/tagged list so renderer binding covers them.

Reference `materials` use `{ "id": "ref_01", "path": "assets/reference/frame.png", "media_type": "Image", "role": "first_frame", "tag": "@reference-frame" }`. Supported role meanings depend on the renderer; record `first_frame`, `last_frame`, `reference_image`, `reference_video` or `reference_audio` deliberately. Material tags used in a prompt must also be registered as `reference` assets.

Storyboards use `{ "id", "path", "grid", "panel_descriptions", "prompt", "source_revision", "dependency_fingerprint", "created_at" }`. Grid is `2x2`, `3x3` or `4x4`.

Takes use `{ "id", "take_number", "status", "task_id", "prompt", "submitted_prompt", "bindings", "duration", "resolution", "model", "source_revision", "dependency_fingerprint", "created_at" }`, plus `path` after success, optional `last_frame_path`, `error`, and `verification`. Status is `pending`, `processing`, `succeeded` or `failed`; only succeeded takes can be selected. Record actual generation facts, not invented model/task identifiers. Screenshots use `{ "id", "path", "timestamp", "source_take_id" }`.

For selective reverts, copy the desired older prompt/asset choice from a snapshot into a current-base proposal and commit; use `restore` for a whole-project revert. Changing selection retains the old candidate/take records. Removing a reference from a chapter should delink it instead of deleting its media.
