# Selective continuity references between clips

Use these decisions for same-environment clips and revisions, alongside the prompt library. The goal is a believable, editable sequence with minimal conflicting input, not automatic chaining of every render.

## Choose the lightest effective handoff

- **Approved environment + text only:** usually sufficient for a new camera angle, time jump or independent moment in the same location. Reuse the selected environment image and describe stable landmarks, axis, motivated lights and subject/prop positions. Repeating the environment does not itself require the previous video.
- **One inspected end frame as an omni image reference:** useful for layout, wardrobe, lighting or prop-state continuity when the next clip changes framing. State precisely which features to carry forward; do not imply the new frame must match exactly. Use a clean actual frame, not a storyboard/contact sheet.
- **Previous end frame as a first-frame input:** useful for a direct motion/action continuation or matched cut where frame-zero alignment matters. Check that the provider mode supports it and the other identity/image/video inputs needed. Do not mix first-frame and omni modes if the current API disallows it. Do not choose this mode if its locked composition conflicts with the next shot.
- **One short prior video reference:** useful when gait, motion direction, choreography, camera trajectory or evolving spatial action cannot be conveyed by a still. Use the smallest usable segment near the relevant handoff, within current provider limits; use the full clip only when required by that mode or the continuity genuinely needs it. Extract locally without overwriting the original take. Reference video is guidance, not a promise of frame-perfect continuation.

Prefer at most one derived continuity input for a handoff. Add more only for distinct necessary roles that cannot be combined. Keep essential approved identity/environment/prop references; remove optional redundant inputs rather than dropping grounding silently. Avoid both an end frame and its source clip unless they supply different necessary information. Do not carry a prior clip's dialogue, music, camera angle, obsolete action or incorrect visual details into the new clip merely because they appear in the reference. Explicitly separate spatial/motion reference from audio reference, using documented audio controls or a locally muted derivative when appropriate.

## Inspect before referring

Use the successful **selected** take, not merely the most recent submission. Inspect actual frames and, when relevant, motion/audio near its end. Reject references containing malformed identities, wrong prop states, bad anatomy, inconsistent lighting/geography or an unusable ending. Check the source take's dependency freshness against current project state. If it is unsuitable, use the approved environment and corrected written blocking, or repair the source within the user's requested scope. Do not propagate defects through a chain.

Record a short `handoff`/continuity decision on the receiving chapter: the shared environment, previous end state, next start state, screen direction/axis, props/ownership, lighting/time, cut type, audio boundary, and why a media reference is useful or unnecessary. In the submitted prompt bind the derived reference to its narrow role, distinguish reference footage from the new desired action, and specify the receiving clip's own duration. Provider count/size/duration limits and cost may depend on reference media; consult current primary docs before a new input mode and record reference usage in the cost ledger. No app route, cloud bucket or undocumented public-file URL is needed.

## Local representation and submission

Store derived inputs separately from the approved image inventory:

```json
{
  "id": "handoff_02",
  "path": "chapters/chapter_02/references/end-of-take01.png",
  "media_type": "Image",
  "role": "reference_image",
  "source_chapter_id": "chapter_01",
  "source_take_id": "take_01",
  "source_sha256": "SHA-256 of the original source take file",
  "reason": "Carry doorway geometry and prop ownership into a new angle",
  "inspected": true
}
```

Use `role: first_frame` only for the chosen first-frame mode, or `media_type: Video`, `role: reference_video` for video guidance. For an excerpt record `source_start` and `source_end` in source-clip seconds; for an extracted image record `source_timestamp`. These metadata fields are provenance, not guessed provider fields. Mark `inspected` only after actually inspecting it. Reference files and source clips remain local; use the renderer's documented input mechanism. The source file hash ensures later file changes are detected; the receiving chapter fingerprint also incorporates its actual reference bytes.

The helper reports invalid/superseded/stale sources and `render-ready --chapter ID` blocks a new submission using them. Include selected `continuity_references` in the final binding table and request alongside necessary approved assets/materials, subject to provider mode rules. They do not become a new cast/prop/environment asset, and do not require reapproval merely because an already approved scene now has generated motion. Existing image approval still applies to the underlying asset set; any creative change to it must be reviewed.

## Sequential dependencies and revisions

Generate and inspect the source before a clip that uses it; independent scenes can render independently. Never reference a future chapter or a chapter's own output as a new source for itself. Freeze source take IDs and hashes for each submitted job; do not switch references while a job is queued.

If an earlier take is replaced, inspect the affected handoffs. A later clip which actually depends on its footage/frame may need a refreshed reference, revised prompt or regeneration. A later clip that shares only the unchanged environment does not automatically need regeneration. Propagate changes only until the new handoff is compatible with existing selected clips; avoid rerendering an entire location by default. Keep prior takes and their costs, update assembly selections, and verify actual cuts and audio boundaries in the new full video.
