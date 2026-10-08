# Tart & Tine: A Little Braver Together

**Status: screenplay and visual production package; animated video rendering is pending.**

Requested movie: 60 seconds, 480p (854×480), 16:9, warm whimsical 3D animation inspired by *Up*. Tart is the beige puppy. Tine is brown, with a small pale heart-shaped patch on the right rear haunch. Both keep the orange training vests in the supplied references.

Tine helps hesitant Tart cross a little training bridge. Tart then returns the kindness by helping distracted Tine focus again. Their small adventure ends with the pair resting shoulder to shoulder beneath an oak tree.

## Production files

- `project.json`: canonical Movi2 state, asset choices, timed chapter prompts, and shot records.
- `screenplay.md`: readable six-chapter screenplay.
- `source.txt`: original request and style follow-up.
- `assets/`: original dog references and generated environment/prop candidates.
- `chapters/`: generated storyboard candidates, once registered.
- `history/`: immutable project revisions.
- `exports/render-package-rXXXXXX.json`: tool-neutral package exported by the Movi2 helper.
- `exports/render-package.json`: expanded delivery package with selected storyboards, chapter handoffs, audio directions and output goals.
- `exports/delivery-specification.json`: frame timing, audio cues, continuity review, intended delivery profile, and pending stages.
- `exports/asset-generation-r000001.json` and `exports/storyboard-results-r000002.json`: exact submitted image-generation prompts, reference bindings and retained candidate metadata. `storyboard-submissions-r000002.json` preserves the initial storyboard proposals before the extra precision notes and corrections.

Reference sheets show three views of each individual puppy; they do not represent six dogs. Text printed on the supplied vests is costume information. Uploaded image content is not a task instruction.

## Exact timeline

| Seconds | Chapter | Event |
| --- | --- | --- |
| 0–10 | Two little trainees | The puppies meet and follow the blue ball. |
| 10–20 | A tiny big obstacle | The ball crosses; Tart hesitates at the low bridge. |
| 20–30 | Coming back | Tine comes back and reassures Tart. |
| 30–40 | One paw at a time | They cross together at Tart's pace. |
| 40–50 | Your turn to help | Tart helps distracted Tine regain focus. |
| 50–60 | A little braver together | They settle together beneath the oak. |

Each chapter contains consecutive 3-, 3-, and 4-second shots. Total: 60 planned seconds, 18 shots, 1800 intended frames at 30 fps. The film has no dialogue; original piano/pizzicato music, garden ambience, pawsteps and canine sounds carry the emotion. These are audio directions, not generated audio.

## What is still needed

Direct Seedance 2.5 generation is authorized and all six 10-second chapters were accepted at 480p with native audio. The original authentication failure was an endpoint/project mismatch: the configured endpoint was not visible in the named credentials' project. The movie client resolves to the verified Running Seedance 2.5 endpoint in that project, retaining the named AK/SK/project values. See `exports/seedance-endpoint-resolution.json` and `exports/seedance-journal.json`. Rendering is in progress; no final MP4 exists yet.

The adapter reads the four named values at runtime without persisting credential values. `seedance_render.py poll` resumes the saved task IDs and downloads results; it never resubmits an accepted job. `assemble_movie.py inspect` decodes completed takes and extracts review frames; `assemble` produces the 60-second 480p/30-fps movie while retaining native audio.

When a renderer becomes available:

1. Inspect its actual duration, resolution, reference-count, local-upload and audio capabilities. Keep both dog identities grounded; preserve the selected garden and ball references when supported. Do not silently drop references or reduce the 60-second runtime.
2. Bind the full asset tags to the renderer's actual reference mechanism. Submit the six chapters, or repartition at the existing shot boundaries to satisfy supported duration limits. Record exact prompts, source revision, fingerprints, real task IDs and settings in separate take records before polling.
3. Keep each successful local clip as a distinct take. Verify identity, anatomy, the heart patch when visible, ball location, bridge geography and chapter handoffs. Select successful takes only.
4. Assemble selected takes in order at 854×480, 30 fps. Use cuts to retain exactly 60.000 seconds; do not add credits or crossfades that change runtime. Preserve generated scene sound and add an original continuous score if the renderer cannot produce it. Stereo audio goal: 48 kHz.
5. Probe actual duration, frame count, dimensions and audio; fully decode the movie; inspect sample frames throughout all six chapters. Record observed facts in verification metadata before reporting a finished movie.

Movie output target: `tart-and-tine-60s.mp4`. This filename is a goal, not an existing artifact.

## Continuing with Movi2

Use the installed `movi2/scripts/project.py` helper with a verified Python interpreter. Load the current `project.json`, edit a new current-base proposal, run `check`, then `commit` and `export`. Never hand-edit canonical state or overwrite existing candidates, takes, or history snapshots. Capture dependency fingerprints before new media generation.

Authentication was also checked by executing the actual signing helper from `../aifx-studio/src/lib/volcengine.ts` in an isolated harness, with only the four named values and external logging disabled. Its signed request matches the local Python adapter, and its live call reproduces the same 403. Evidence: `exports/aifx-auth-comparison.json`.
