# SOMEWHERE BETWEEN US｜我們之間

Completed Movi2 adaptation of the supplied plot, with adult Tart and Tine as the two leads: exactly 10:00, Seedance's native 720p profile at 1470×630, 21:9, 30fps, 18,000 frames, stereo audio. The user expressly accepted retaining the native resolution.

[Watch the finished movie](exports/somewhere-between-us-10min-720p-21x9.mp4) — 185,917,374 bytes. All thirty selected video takes and the complete movie passed full decode. Final measured sound: -22.92 LUFS integrated, -1.39 dBTP true peak, stereo 48kHz. Project validation: zero errors and zero warnings. The author's name is excluded from the video titles and generation directions.

The story follows two different gifts: Tart guides a visually impaired man through Hong Kong; Tine gives an isolated elderly man patient companionship. Tram, train, street and ferry near misses lead to a quiet Victoria Harbour reunion. Their handlers discover that both came from the same Victoria dog farm in Australia. A late puppy flashback reveals that the dogs met long before their adult lives took different paths.

The PDF's 30-minute label is overridden by the user's 10-minute request. The adult dogs follow the attached identity sheets. Baby variants retain their identity without work vests. Human characters and locations use original generated reference assets in a warm, expressive 3D animated feature style inspired by Up. The dogs do not speak; human dialogue is directed in Cantonese. Original generated score, atmosphere, Foley and dialogue are retained in the edit.

## Files

- `project.json`: canonical Movi2 project with immutable revisions in `history/`.
- `screenplay.md`: complete 600-second adaptation, 30 chapters, 90 timed shot directions.
- `source/`: unchanged source PDF, extracted text, and direct user request.
- `assets/`: original adult dog sheets and selected generated puppy, human and environment references. Earlier human candidates are retained.
- `chapters/`: chapter prompts, recorded payload plans, real video takes, and actual extracted review frames.
- `exports/submission-plan.json`: deterministic reference bindings, file hashes, translated prompts and settings. No secrets or inline image bytes are exported.
- `exports/seedance-journal.json`: task IDs and resumable state. Accepted or uncertain requests are never resubmitted blindly.
- `exports/adaptation-audit.json`: plot preservation and duration override.
- `exports/assembly-manifest.json`: final input order and editing decisions, created at assembly.
- `exports/video-verification.json`: actual final duration, dimensions, FPS, frames and full decode, created after delivery.

## Timeline

| Time | Story |
| --- | --- |
| 00:00–00:40 | Victoria meadow to Victoria Harbour; shared name remains a mystery. |
| 00:40–01:40 | Tart's work harness, careful route and restraint at a cafe. |
| 01:40–03:40 | Tine's community visit, patient pause and the elderly man's first touch. |
| 03:40–05:40 | Tram, MTR, street and ferry near misses. |
| 05:40–06:40 | Tart refuses an unsafe forward command; trust is rewarded. |
| 06:40–07:00 | The elderly man calls Tine's name on the next visit. |
| 07:00–08:20 | Harness release, harbour recognition and shared-origin discovery. |
| 08:20–09:20 | Puppyhood and their different paths; match cut to adult Hong Kong. |
| 09:20–10:00 | Gentle reunion humour, shared posture and the source's closing lines. |

## Production notes

Generation inputs are cinematic text plus selected identity and empty-location assets. No storyboard was generated, required or uploaded. Multi-view identity sheets represent one subject per sheet.

The direct Seedance route uses only the four base environment settings expressly authorized in the earlier Tart/Tine chat: `VOLC_ACCESS_KEY`, `VOLC_SECRET_KEY_RAW`, `VOLC_PROJECT_NAME`, `VOLC_ENDPOINT_SEEDANCE_25`. Credential values remain in memory, outside project state. The endpoint was rechecked live in the authorized project before submission. No application services or cloud buckets are used.

The API's 720p profile produced all selected takes at 1470×630. The user accepted this output, so delivery keeps these dimensions with no resizing.

One first pilot request was rejected before acceptance because a generated human reference was classified as possibly a real person. The human assets were revised to more clearly stylized animated characters, and the new pilot was accepted. The rejected request and its references remain in history.

Native generated audio is kept, with hard cuts, 40ms audio edge fades and final loudness normalization. Readable title, shared-origin record and closing source lines are composited after generation. Three confirmed audio-filter failures were replaced with location ambience and Foley. A ferry take that prematurely reunited the dogs was replaced with Tine and her handler alone on the boat. Unwanted generated closing-footer lettering is covered by a dark lower band; the native frame dimensions are retained.

Review frames from the final file are in `exports/final-review/`; `exports/poster.jpg` is an actual movie frame. Costume lettering, harness shape, heart-patch placement and minor body details vary in some shots. The opening city montage shifts from morning to night before the daytime work scenes. Exact spoken wording was not independently transcribed, and native music varies across some cuts. The detailed review and its scope are recorded in `exports/visual-review.json`.
