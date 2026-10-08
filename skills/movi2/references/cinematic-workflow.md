# Cinematic planning and refinement

## Source behavior adapted from Movi2

This skill was derived from the local AIFX Studio Movi2 module on 2026-10-08. The source paths below explain provenance; they are not runtime dependencies:

- `src/ai/flows/prepare-movi2-script.ts`: idea-to-timed-script and script rearrangement, fixed/adaptive pacing.
- `src/ai/flows/generate-movi2-master-prompt.ts`, `expand-movi2-chapter-prompt.ts`: production plan, exhaustive chapter expansion, source-language continuity.
- `src/ai/flows/refine-movi2-chapter-prompt.ts`, `yolo*-movi2-chapter-prompt.ts`: instruction/reference-image refinement and three prompt formats.
- `src/ai/flows/fact-check-movi2-{master,chapter}-prompt.ts`: creative clarification and continuity audit, not a requirement to browse every fictional fact.
- `src/lib/movi2-types.ts`, `movi2-script-parser.ts`: assets, chapter links, takes, screenshots, runtime reconciliation.

The original model names and service limits are historical implementation details. This skill keeps the creative grammar without assuming that a named provider is available. Current tool constraints override historical render limits.

## Script and production plan

Retain the input verbatim in `source_text`. For an idea, develop a screenplay with absolute movie timestamp ranges, chapter title, mood, character identity/wardrobe anchors, environment, props, summary, actions, and timed dialogue. For a supplied script, preserve significant story and dialogue details while improving pacing only as requested.

Fixed duration: chapter durations sum exactly to the requested target. Adaptive duration: pace according to substantive actions and speakable dialogue; report the resulting runtime. Explicit user duration wins over embedded metadata. Only ignore embedded runtime when adaptive mode is requested. The original draft tolerated roughly two seconds of timing error; the committed production plan should reconcile exactly.

Movi2 used 4–30 second chapters for Seedance 2.5; use these as planning defaults, not verified current provider requirements. Configure `chapter_limits` if the chosen tool needs different lengths or the user requests a shorter clip. Split long scenes at sensible action boundaries; redistribute a too-short tail. Recalculate shot times after a duration change instead of changing only chapter metadata. Do not introduce disconnected scenes solely to meet a count.

Keep `high_level_idea` consistent across chapters. Include all explicitly listed characters/environments/props under their original tags. Weave requested narrative assets into appropriate action beats, rather than appending an unused-assets list. Supplied mood/reference media need not appear as physical objects in the story.

## Default chapter prompt

For Seedance generation, the user's `prompt-library/` is the golden writing standard. Read [seedance-prompts.md](seedance-prompts.md), then its template and relevant examples. The generic structure below remains useful for planning; adapt it to the library's explicit reference roles, blocking and performance grammar before submission.

Use labeled prose with these sections; keep body text in the user's language:

```text
GLOBAL STYLE: medium, palette, genre, optical look, aspect ratio, negative constraints.
SCENE: the action, location, and mood, using @tags.
LOCATION: spatial architecture, atmosphere, and relevant @location/@prop tags.
FIRST FRAME AND BLOCKING: starting positions at 0s, screen-left/right, facing directions, ownership of props.
SHOT-BY-SHOT BREAKDOWN:
Shot 1 (0.0s-3.0s): framing, movement, specific physical action, expression, dialogue, @tags. Hard cut.
Shot 2 (3.0s-8.0s): the next causal action and observable end state.
OPTICS and CAMERA: focal lengths, camera height, movement, focus/depth.
PHYSICS: relevant fabric, hair, smoke, rain, momentum or object mechanics.
LIGHTING: motivated sources, direction, contrast, shadows and highlights.
AUDIO: timed dialogue with speaker, atmosphere, Foley/SFX, music or silence.
CONTINUITY LOCKS: identity, costume, spatial axes, prop state/ownership, time and light.
```

Shot times are chapter-local, consecutive, non-overlapping, and span exactly 0 to chapter duration. Absolute movie time is the accumulated chapter duration. Use "Hard cut." where a cut occurs; omit it for intentional continuous movement. Keep the shot count feasible for the action and runtime. Do not squeeze long speeches into brief clips.

Ground appearance in selected reference sheets rather than repeating a separate CHARACTERS section. If images are missing, preserve identity anchors in the asset descriptions and record that visual grounding is pending. The original master prompt and storyboard sometimes hard-coded photorealism; this adaptation honors anime, illustration, clay, or any user-selected medium throughout.

## Refinement modes

Ordinary refinement preserves the full prompt structure and granular pacing while applying user text, composition sketches, or reference images. Expand sparse prompts with cinematic detail that serves existing beats, rather than changing the narrative.

**YOLO**: enhance cinematography with each shot containing framing, Lens/Camera, Camera Movement or Camera/Focus, Visuals, Mise-en-Scène when useful, Lighting/Tone, Audio, and Purpose. Preserve duration, plot and active tags; the source's action-heavy examples do not require turning a quiet scene into action.

**YOLO2**: the YOLO format with deeper camera/sensor/lens, framing/movement, color, photometry, and exposure reasoning. The source loaded five CBGA books (`pp1.pdf` through `pp5.pdf`) from a service. If the user supplies those locally, consult them; otherwise use available cinematographic knowledge and say the books were not consulted. Do not claim they are attached or recreate cloud file caches.

**YOLO3**: source Seedance-oriented grammar:

```text
【Generation Goal】
Subject + location + event + style + camera intent.
【Reference Asset Roles】
@person: identity and wardrobe, excluding sheet background.
@prop: shape, material and state. @place: layout and ambient light.
【Subjects and Spatial Relationships】
Blocking relative to stable anchors and foreground/midground/background planes.
【Timeline & Shot Sequence】
Shot 1 (0-3s): Camera; Visuals & Action; Lighting/Tone; Audio; End State.
Shot 2 (3-8s): ...
【Maintain Consistency】
Identity, costumes, prop ownership, axes, state and lighting.
【Strictly Exclude】
No subtitles, watermarks, duplicate characters, or unintended morphing, as appropriate.
```

Prefer integer-second stages for this format where compatible with runtime. Source audio notation: `{spoken dialogue}` with speaker/delivery, `<Foley or SFX>`, `(music cue)` or explicit no BGM. These are Movi2 conventions, not proof a current renderer supports the syntax. Preserve exact @tags, exclude phantom tags, and omit an Unused Assets section. Save the prior format so the user can revert.

## Continuity review

Check identity and wardrobe, causal timeline, geography and screen direction, motivated lighting, prop state transitions, ownership, dialogue timing, and chapter handoffs. For reference sketches inspect the image and describe observable blocking before changing it. Fix contradictions already resolved by the user's brief. Ask only the consequential unresolved creative questions; do not copy the source's mandatory 3–6 question modal into conversation.

Changes to timing or plot can affect later chapters; record those dependencies. A scoped lens, lighting, or phrasing edit should preserve unrelated assets and chapters. After tag changes reconcile prompts, shot records, tagged lists and explicit link/delink IDs together.
