# Assets, storyboards, takes and delivery

Adapted from Movi2 `generate-asset-image`, `save-asset-candidates`, `select-asset-image`, `generate-storyboard`, `generate`, `status/[taskId]`, `select-chapter-take`, `upload-screenshot`, and screenshot/playblast UI behavior. Do not run those routes; use Codex tools and local files.

## Asset generation and edits

Use the imagegen skill and tool actually present in the session. Before editing a local reference, inspect it with the image-viewing tool. Use local reference paths for edits when supported; use recent conversation images only according to the tool's rules. If an image tool returns an in-chat image without a local path, follow its documented save/export behavior; do not pretend a file was saved. Never create a fake path or replace a failed image with text-only success.

Save the exact submitted prompt, requested style, input reference paths and source revision beside the candidate metadata. Copy a returned local file into a unique project candidate path. Keep all successful candidates, including those not selected. Honor the number of variations requested; a single request does not imply a large batch.

Default Movi2 asset composition, overridable by the user:

- **Character:** horizontal 16:9, three side-by-side panels on a clean neutral studio background. Left is front wardrobe from neck/collar to shoes with no head; middle is back wardrobe with no head; right is the only face/head, a detailed portrait. Keep costume, materials, identity, and lighting coherent across panels. Use the project's medium, including stylized rendering.
- **Environment:** a wide establishing plate of architecture/landscape/layout, ambient dressing, lighting and weather. No people, silhouettes or crowds; no featured story props or hero objects. Environment descriptions should separate setting from people and props so later composition remains controllable.
- **Prop:** a clear hero view on a neutral backdrop, belonging to the story's design language, with readable shape/material/scale and wear. For state variants use consistent multi-view/state sheets or distinct tagged candidates, as requested.
- **Reference:** preserve user-provided Image/Video/Audio and its intended role. A reference is not automatically a character or prop sheet.

Image tool aspect ratios may differ from requested composition. Record actual dimensions; do not claim exact 16:9 if the returned raster differs. Use normal local cropping/padding only when suitable and authorized; use the image tool for semantic visual edits.

Inspect image results for requested panel structure, identity and wardrobe, empty environment constraints, prop state, style, and obvious defects. Refine with the selected reference rather than generating unrelated identities. A selection updates `selected_candidate_id`; leave old candidates and their files intact.

## Storyboard previews

Choose 2x2 for a simple short sequence, 3x3 for more progression, or 4x4 for dense coverage; let content and user choice determine layout. Write the panel action list in local metadata, ordered left-to-right/top-to-bottom. Generate one continuous canvas of equal rectangular panels with no outer frame, gutters, divider lines, text, labels, watermarks, subtitles, or speech bubbles. Use the same style as the movie.

Resolve reference assets with exact-tag matching and explicit link/delink precedence (see local-project.md). Use their selected candidates; list which reference supplies face/wardrobe, prop shape/state, or environment geometry. Only pass relevant chapter references within the tool's limit. If a reference is unavailable, record it and avoid claiming fully grounded identity. Use separate storyboard images or a locally prepared contact sheet if reference limits require a smaller set, without silently dropping critical subjects.

Capture the chapter `fingerprint` before rendering. Save each storyboard with that `dependency_fingerprint`, its grid, panel descriptions, prompt, media path and created time. A newer prompt or selected asset can make it stale; do not automatically delete it.

## Video and audio tools

Discover callable video/audio tools and inspect their schemas. The source app submitted asynchronous Seedance jobs, with image/video/audio references, optional first/last frames, and per-chapter takes. This skill includes no credentials. When the user authorizes direct Seedance generation using named environment settings, follow [seedance-api.md](seedance-api.md); consult [seedance-prompts.md](seedance-prompts.md) before writing the submitted prompt. If neither a suitable tool nor an authorized direct API route is available, write `exports/render-package.json` with chapter prompts, durations, aspect ratio, selected local references, media roles, intended audio, and output goals. State that rendering is pending. Do not silently use AIFX secrets or its application services.

For an available renderer:

1. Resolve actual supported duration, resolution, aspect ratio, reference formats/count and first/last-frame mode. Repartition or clarify conflicts before submission; do not silently clamp duration or omit references. A filesystem path is not a public provider URL; use the tool's documented local-file mechanism or explicitly supported transient upload.
2. Compile stable @tags into the tool's documented bindings. When it uses numbered references, save a deterministic binding table and translated prompt separate from the canonical @tag prompt. Match complete tags, so @Tom does not capture @Tom-hat. Delinked assets are excluded. If an active tag has no render reference, surface the missing grounding rather than stripping the @ sign to conceal it.
3. Keep first-frame/last-frame inputs distinct from identity/environment references. Movi2's source first-frame branch discarded other reference types; preserve only inputs actually supported by the current tool and disclose consequential exclusions.
4. Save a pending take with provider task ID, source revision, exact submitted prompt, settings and fingerprint. Poll that same job using the tool's documented status mechanism; timeouts are pending, not grounds for submitting a duplicate paid job. Record failures and stop retries that risk duplicate jobs until submission state is known.
5. On success retain the returned local clip (or save via documented export), actual metadata, last-frame image if available, and separate take ID. Update selection after success; a failed render must not replace a working selected take. Store any output URL as provenance, with local media as the durable result.

A raster image generation result is never a video take. If a still-image animatic is requested, build it locally from storyboards with honest labeling; do not present it as generated character motion.

## Screenshots, assembly and verification

When local video tools are available, use ffmpeg or an equivalent installed processor to extract the requested timestamps and final decodable frame. Record timestamps and source take IDs; an extracted frame can become a local reference/first-frame candidate for later work. Keep generated/edit semantics with imagegen when the screenshot needs visual changes.

Assemble only the selected successful takes in chapter order. Inspect dimensions, fps, audio streams and timestamps before concatenation; normalize to a common output profile when needed. Preserve intentional dialogue/sound; do not indiscriminately drop audio. Save assembly settings and input take IDs in `exports/`. Crossfades change runtime, so use cuts for an exact duration unless the user requests transitions.

Probe duration/resolution/fps and ensure video decodes. Inspect sample frames across each clip for identity/style/blocking and obvious discontinuities. Compare actual runtime to the requested plan and report any remaining mismatch; record technical checks in local verification metadata. With no local processing executable, preserve original results and state which assembly or checks remain unavailable.

Show useful generated images or local previews in Codex and link final files with absolute paths. Report completed candidates, selected versions, outdated dependent media, and pending render stages succinctly. Do not start a web server or build a UI for this workflow.
