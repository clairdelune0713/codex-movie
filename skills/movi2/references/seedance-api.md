# Direct Seedance 2.5 generation

This authentication and task route produced six successful 10-second, native 480p clips with image references and audio on 2026-10-08. It describes the verified BytePlus regional route, not every Volcengine deployment. Recheck provider capabilities when the model, region or API version changes. Keep this guide free of credential values, account/project names and real endpoint IDs. Reference construction follows Movi2: text prompt plus selected assets, with no storyboard dependency or upload.

## Settings and source implementation

When authorized by the user, read these four settings from the specified environment file; the working workspace used `../aifx-studio/.env`:

- `VOLC_ACCESS_KEY`
- `VOLC_SECRET_KEY_RAW`
- `VOLC_PROJECT_NAME`
- `VOLC_ENDPOINT_SEEDANCE_25`

Resolve the environment path from the workspace, not by guessing relative to a deeply nested chapter. Parse quotes, comments, optional `export` and UTF-8 BOM correctly. Retain only the authorized settings in memory. Report presence and equality booleans for diagnostics, never their values. Do not print `.env`, request authorization headers, signed canonical requests or token responses.

If AIFX Studio is present, inspect `src/lib/volcengine.ts`, especially `makeSignedVolcRequest`, `getVolcCredentials`, `getTemporaryApiKeyForEndpoint` and the Ark auth headers. Read its environment loader only when parsing or overrides are in doubt. These source files are useful read-only implementation evidence; do not invoke application routes, API loggers, databases, credit accounting or storage services.

Model-specific routing matters: the observed AIFX helper selects `VOLC_ACCESS_KEY_M`, `VOLC_SECRET_KEY_RAW_M` and `VOLC_PROJECT_NAME_M` for Seedance 2.5 when available. App success alone therefore does not prove it used the base variables. Compare the effective route without logging values. If the user named the base variables, bind those explicitly; do not silently switch to `_M` or other credentials. This is a routing check, not an assertion that alternate credentials are needed.

## Authentication: two distinct hosts

Management/OpenAPI signing uses:

| Setting | Verified value |
| --- | --- |
| Host | `ark.ap-southeast-1.byteplusapi.com` |
| Region | `ap-southeast-1` |
| Service | `ark` |
| API version | `2024-01-01` |
| Path | `/` |

Sign a POST with query `Action=GetApiKey&Version=2024-01-01` and compact UTF-8 JSON body:

```json
{"DurationSeconds":3600,"ResourceType":"endpoint","ResourceIds":["<resolved-endpoint>"]}
```

The provider's V4 HMAC signing details are easy to mix up with other SDKs:

1. Serialize the body once; SHA-256 the exact bytes sent. Sort and RFC3986-encode query names/values, with spaces as `%20`.
2. Use UTC `X-Date` in `YYYYMMDDTHHMMSSZ` format and its first eight characters as the date.
3. Canonical headers, lowercase and in this order, each with a trailing newline: `content-type:application/json`, `host:<management-host>`, `x-content-sha256:<body-hash>`, `x-date:<timestamp>`. Signed headers are `content-type;host;x-content-sha256;x-date`.
4. Join with newlines: method, `/`, canonical query, canonical headers, signed-header names, body hash. Preserve the separator after the already newline-terminated canonical headers.
5. Scope is `<date>/ap-southeast-1/ark/request`. String to sign is `HMAC-SHA256`, timestamp, scope and SHA-256 of the canonical request, joined with newlines.
6. Starting with the raw UTF-8 secret key bytes, chain HMAC-SHA256 over date, region, service and `request`, retaining binary digest bytes at each stage. There is no `AWS4` prefix in the verified helper. HMAC the string to sign with the derived key to obtain the hexadecimal signature.
7. Send `Authorization: HMAC-SHA256 Credential=<access-key>/<scope>, SignedHeaders=<signed-headers>, Signature=<signature>` plus the four signed headers. Treat this header as secret.

Read the temporary key from `Result.ApiKey` or `ApiKey`; keep it only in memory. The working client requested 3,600 seconds and refreshed before 3,000 seconds. Prefer the provider's returned expiry when available.

Inference/tasks use a different host:

```text
https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks
```

Send `Authorization: Bearer <temporary-token>`, `Content-Type: application/json`, and `X-Project-Name` from the authorized `VOLC_PROJECT_NAME`. The endpoint used for token scope, payload `model` and project header must belong together. The access key is not the task API bearer token.

## Diagnose endpoint pairing before declaring bad credentials

A `403` mentioning `ark:GetApiKey` can result from an endpoint outside the named credentials' account/project. In the verified run, the named credentials were valid; resolving to their project's running Seedance 2.5 endpoint fixed authentication without changing AK/SK/project values.

Use the same authorized AK/SK signing route for read-only `Action=ListEndpoints`, with the same version and body:

```json
{"ProjectName":"<named-project>","PageNumber":1,"PageSize":100}
```

Inspect `Result.Items` and `Result.TotalCount`, fetching additional pages when needed. Check endpoint `Id`, `Status`, `ModelReference`, project membership and whether the configured endpoint is listed. Select only a running endpoint verified to host Seedance 2.5 in the authorized project. If there is one unambiguous matching endpoint, record a project-local endpoint resolution and use it for both token scope and task `model`; explain the correction. With multiple plausible choices, resolve ambiguity before paid submission. Do not create/start/change endpoints or edit the sibling `.env` just to troubleshoot.

Store only a sanitized resolution record: reason, model/version, verification time and endpoint mapping if needed by the movie client. Real endpoint identifiers may belong in that authorized project's operational state, but not this reusable skill. Revalidate when configuration changes; a cached endpoint mapping is not universal. If no accessible matching endpoint exists, preserve the prepared work and report the specific remaining authorization or configuration problem.

For signing uncertainty, compare against the actual AIFX helper using synthetic keys and a fixed timestamp before making another live call. Stub external logging/services if executing the helper in isolation. If loading `.env` is suspected, compare parsed values in memory with the app loader and emit equality booleans only. Repeated identical failing requests do not establish a fix.

## Reference mode and request configuration

Write the prompt using [seedance-prompts.md](seedance-prompts.md). Build the content list from one text item and the selected active assets, plus any explicitly supplied supported reference materials. Save a deterministic ordered asset-to-reference binding table. Do not read `selected_storyboard_id` to construct a request, append chapter storyboard files, or require a storyboard to exist. Do not copy an earlier project-specific adapter's automatic storyboard append behavior. Supported inline image inputs avoid unnecessary buckets and app uploads:

```json
{
  "model": "<resolved-endpoint>",
  "content": [
    {"type": "text", "text": "<compiled prompt with @Image1 and matching reference roles>"},
    {"type": "image_url", "image_url": {"url": "data:image/png;base64,<image-bytes>"}, "role": "reference_image"}
  ],
  "duration": 10,
  "ratio": "16:9",
  "resolution": "480p",
  "generate_audio": true,
  "watermark": false,
  "return_last_frame": true,
  "output_format": "mp4",
  "omni_reference_task_type": "reference",
  "seed": 18426
}
```

This is an example, not a fixed project recipe. Honor requested duration, ratio, resolution and audio; omit unsupported optional fields for other provider modes. Use the actual image MIME type. Preserve complete-tag matching so `@Tom` cannot capture `@Tom-hat`. Canonical project tags remain unchanged; save the translated prompt separately. Do not log or store base64 payloads just to record reference provenance: local paths, SHA-256 hashes, roles and bindings suffice.

The documented Seedance 2.5 profile consulted for this run allowed 4–30 seconds and 1–30 reference images, with 30 MB per image and 64 MB for the whole request. Check current documentation before assuming these limits; count serialized base64 JSON bytes, not just raw image sizes. Reference count follows the chapter's actual linked assets and supplied materials; do not add a fifth image or any fixed-count filler. At `16:9`, `480p` produced actual `854×480` video. Resolution is a structured API field, not merely prompt text.

Omni `reference_image` inputs guide asset identity and applicable geometry/composition; they are not exact first frames. First/last-frame generation is a separate supported mode and must not be mixed with omni roles when the current API excludes that combination. Use deliberately supplied frame assets for that mode, not storyboard previews. `return_last_frame` requests an output image and is distinct from supplying an input last frame. Character sheets represent one subject. Shot sequence and composition direction come from the cinematic text prompt.

## Submit once, poll, retain takes

Before a paid POST, save a pending take with a unique ID, source revision, dependency fingerprint, exact submitted prompt, bindings/hashes and non-secret settings. Atomically journal submission state as `submitting`; after acceptance immediately save the real returned task `id` as `accepted`. Never print request headers or token-bearing response bodies.

Poll `GET /contents/generations/tasks/<task-id>` using the same auth route. Typical states are `queued`, `running`, `succeeded`, `failed`, `cancelled` and `expired`. The verified watcher polled every 30 seconds and only printed changes. A render timeout or interrupted poll does not authorize another POST. If submission times out before an ID is received, mark it uncertain and reconcile with documented task listing/provider state before any retry. A confirmed rejected request and an accepted job are different states.

On success, save `content.video_url` through the provider's supported export/download mechanism into a unique local take file, and retain `content.last_frame_url` when supplied. Use temporary partial downloads and atomic rename. Avoid persisting expiring signed URLs unnecessarily. Keep originals immutable; register them through the Movi2 helper, and select only successful inspected takes. A failed new take does not replace a good selection.

## Assembly and actual verification

The requested 10-second jobs returned native `854×480`, 24 fps videos of roughly 10.08 container seconds, with AAC stereo at 32 kHz. These are observed properties, not delivery guarantees. Probe every actual take; trim/normalize for a requested exact runtime while preserving native sound. The verified 60-second delivery used six ten-second clips, 30 fps video and stereo AAC at 48 kHz.

FFmpeg concat plus AAC priming can shift video timestamps by about 21 ms or report an average frame rate slightly above 30. In the working assembly, each clip was normalized to ten seconds; the final concat was re-encoded with `setpts=N/(30*TB)`, `-r 30 -fps_mode cfr`, audio `atrim=duration=60,asetpts=PTS-STARTPTS`, and `-t 60`. The result was exactly 60.00 seconds, 1,800 frames and 30 fps. Adapt those numbers to the target movie instead of copying 60 seconds everywhere. Optional short audio edge fades can reduce clicks at hard cuts; they do not establish score continuity.

Fully decode original takes and final output. Verify duration, dimensions, frame count/FPS, audio presence and signal levels. Inspect multiple actual frames per chapter for identity, anatomy, style, subject count, reference artifacts, geography and handoffs. Technical audio checks do not prove musical/dialogue fidelity. Save observed verification results and limitations; update canonical take selection/render state through `scripts/project.py`, export the current revision, and distinguish the final verified file from earlier assembly candidates.

Primary API references: [Seedance 2.5 tutorial](https://docs.byteplus.com/es/docs/modelark/seedance-2-5), [GetApiKey](https://docs.byteplus.com/de/docs/ModelArk/1262825), [ListEndpoints](https://docs.byteplus.com/pt/docs/ModelArk/1262430). Use the provider's current create/retrieve-task documentation for new modes or changed fields.
