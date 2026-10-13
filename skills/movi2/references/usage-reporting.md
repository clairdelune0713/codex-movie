# Seedance cost and elapsed-time reporting

Use `scripts/usage.py` for a project-local `usage.json` ledger. It is separate from creative snapshots: reverting a prompt or deleting/replacing a take never erases API spending or elapsed production history. The helper is standard-library-only and makes no network calls. It records evidence supplied by Codex/the adapter; it cannot discover provider charges itself.

## Session and total meanings

A production session is one initial movie-delivery run or one user-requested revision run. Start it when work on that request begins, finish it immediately before delivering the verified full video, and resume the same ID across asset approvals, interruptions or chat continuations. A later revision after delivery starts a new session even in the same chat. A prompt-only update not delivering a movie may be closed as a separate editing session; record its outcome. A cancelled/failed run still keeps its incurred costs and elapsed time.

Elapsed time means **wall-clock production session time**, including rendering queues, local processing and user approval waits inside that session. It is not video runtime, GPU compute time or billed generation seconds. State this briefly in the delivery table. Project total is the sum of recorded production sessions, excluding idle time between deliveries; overlapping recorded intervals are merged instead of counted twice. Store UTC timestamps, display dates/times in the user's timezone, and show durations in minutes/seconds or hours/minutes. Do not infer unrecorded historical session times or silently present incomplete history as all-time total.

## Commands and ledger use

Resolve `USAGE_HELPER` to the installed skill's `scripts/usage.py`; ROOT is an existing local movie project.

```text
PYTHON USAGE_HELPER start ROOT --reason "Initial full video"
PYTHON USAGE_HELPER record ROOT --session SESSION_ID --from sanitized-job.json
PYTHON USAGE_HELPER finish ROOT --session SESSION_ID --outcome delivered
PYTHON USAGE_HELPER report ROOT --session SESSION_ID
```

`start` returns an existing unfinished session instead of resetting it; use that ID when resuming. Finish before starting a new revision session. Capture the request's actual start timestamp using `--at ISO_TIMESTAMP` when known; otherwise start immediately and disclose any earlier untracked work. `finish` persists the end time; subsequent reporting must not keep growing a delivered session. If work is resumed for a later request, start a new session.

Before each generation POST, create a unique stable local `attempt_id`, record the session and pending cost evidence, and write the submission journal. Once a task ID exists, update **the same attempt** with it, then update that entry after completion/billing reconciliation. Polling repeatedly updates one entry and does not multiply the cost. An explicitly resubmitted generation gets a new attempt ID. Record all successful, failed, cancelled, discarded and uncertain jobs; chargeability follows provider evidence, not whether the take was selected. Reusing or assembling old clips incurs zero new Seedance generation calls; retain their original costs in project total.

Sanitized record example:

```json
{
  "attempt_id": "attempt_02",
  "task_id": "provider-returned-task-id",
  "chapter_id": "chapter_02",
  "take_id": "take_03",
  "state": "succeeded",
  "model": "actual model/version",
  "resolution": "requested profile",
  "duration_seconds": 6,
  "reference_video_seconds": 0,
  "usage": {"provider_reported_units": 123},
  "cost": {
    "kind": "actual",
    "currency": "USD",
    "amount": "0.12",
    "basis": "Provider billing record for this task"
  }
}
```

The numbers above illustrate storage only, not Seedance pricing. Prefer provider-confirmed task charges or billing records attributable to the jobs. Usage tokens alone are not a currency charge. If only usage/rates are available, verify current primary provider pricing for the actual model, region, resolution, audio mode and reference-video mode; record the measured billing units, rate, formula, currency and source/date under `basis`/`usage`, and label `cost.kind: estimated`. Do not assume output seconds are always the billing unit or ignore reference-video charges, rounding, discounts or taxes. Avoid converting currencies without a stated verified conversion. Group different currencies separately.

For unknown/pending charges use `{ "kind": "unknown", "basis": "Awaiting provider billing" }`, not a made-up zero. Zero is valid when provider evidence confirms no charge, or when the session has no generation attempts. Final session and cumulative costs include every recorded attempt, even if the resulting video was discarded. The helper rejects duplicate provider task IDs across attempt entries and requires complete records when updating an attempt; copy the old entry and change only newly known fields to avoid dropping billing evidence. A correction replaces an entry rather than adding its amount a second time.

Record only non-secret identifiers/settings, bounded usage facts, money and evidence; exclude authorization headers, tokens, signed URLs and image/video base64. Track generation usage, not Codex subscriptions/imagegen costs or AIFX app credits. Credential/auth/status calls are not generation attempts unless provider evidence identifies a relevant charge.

## Final delivery requirement

Finish the session, run `report`, and save its result under `exports/usage-report-SESSION_ID.json`. Include a compact table with rows `Seedance API cost` and `Elapsed time` and columns `This session` and `Project total`, on every initial or revised **full-video delivery**. For costs, separate confirmed amounts, estimates and jobs with unknown/pending charges; if any are unresolved, label the total partial/provisional. Include failed/uncertain jobs as pending until reconciled. Never claim an actual total from estimates or from only selected takes.

For old projects, import historical attempts only from retained submission/billing evidence and known times; list any coverage gap. The reporting period begins with the earliest ledger session, not automatically the movie's creation date. Do not backfill invented prices/timestamps. The project total covers this movie across its revision sessions, not all account spending or all movies. When a revision only reassembles cached clips, explicitly show this session's Seedance cost as zero new generation cost and retain cumulative spending.
