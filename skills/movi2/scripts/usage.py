#!/usr/bin/env python3
"""Persist Movi2 production sessions and evidence-based Seedance usage locally."""
import argparse
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import re
import sys
from uuid import uuid4
from pathlib import Path

from project import read, atomic_write


def timestamp(value=None):
    result = datetime.fromisoformat(value.replace("Z", "+00:00")) if value else datetime.now(timezone.utc)
    if result.tzinfo is None:
        raise ValueError("Timestamps require a timezone offset")
    return result.astimezone(timezone.utc)


def elapsed(sessions, at):
    intervals = []
    for session in sessions:
        start = timestamp(session["started_at"])
        end = timestamp(session["ended_at"]) if session.get("ended_at") else at
        if end < start:
            raise ValueError("Session end/report time is earlier than its start")
        intervals.append((start, end))
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return sum((end - start).total_seconds() for start, end in merged)


def costs(jobs):
    currencies, unknown = {}, 0
    for job in jobs:
        cost = job.get("cost") or {"kind": "unknown"}
        kind = cost["kind"]
        if kind == "unknown":
            unknown += 1
            continue
        currency = cost["currency"]
        bucket = currencies.setdefault(currency, {"actual": Decimal(0), "estimated": Decimal(0)})
        bucket[kind] += Decimal(str(cost["amount"]))
    return {"currencies": {key: {kind: str(amount) for kind, amount in value.items()}
                           for key, value in sorted(currencies.items())},
            "unknown_charge_attempts": unknown, "attempts": len(jobs),
            "provisional": bool(unknown or any(job.get("cost", {}).get("kind") == "estimated" for job in jobs))}


def validate_job(record):
    allowed = {"attempt_id", "task_id", "chapter_id", "take_id", "state", "model", "resolution",
               "duration_seconds", "reference_video_seconds", "usage", "cost"}
    if set(record) - allowed:
        raise ValueError("Unsupported job fields; store only the documented sanitized usage record")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", record.get("attempt_id", "")):
        raise ValueError("A stable local attempt_id is required")
    cost = record.get("cost") or {"kind": "unknown", "basis": "Charge not yet known"}
    if cost.get("kind") not in ("actual", "estimated", "unknown"):
        raise ValueError("cost.kind must be actual, estimated or unknown")
    if cost["kind"] != "unknown":
        amount = Decimal(str(cost.get("amount")))
        if not amount.is_finite() or amount < 0:
            raise ValueError("Charge amount must be finite and nonnegative")
        if not re.fullmatch(r"[A-Z]{3}", cost.get("currency", "")) or not cost.get("basis"):
            raise ValueError("Known/estimated cost requires currency and evidence/formula in basis")
        cost["amount"] = str(amount)
    record["cost"] = cost


def summary(ledger, session_id, at):
    session = next(item for item in ledger["sessions"] if item["id"] == session_id)
    jobs = list(ledger["jobs"].values())
    return {"session_id": session_id, "session_reason": session["reason"],
            "session": {"seedance_cost": costs([job for job in jobs if job["session_id"] == session_id]),
                        "elapsed_seconds": elapsed([session], at), "outcome": session.get("outcome", "in_progress")},
            "project_total": {"seedance_cost": costs(jobs), "elapsed_seconds": elapsed(ledger["sessions"], at)},
            "coverage_started_at": min(item["started_at"] for item in ledger["sessions"]),
            "elapsed_basis": "Wall-clock production session time, including queues and approval waits; excludes gaps between sessions"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("start", "record", "finish", "report"))
    parser.add_argument("root", type=Path)
    parser.add_argument("--session")
    parser.add_argument("--reason", default="Movie production")
    parser.add_argument("--outcome", default="delivered", choices=("delivered", "failed", "cancelled", "edited"))
    parser.add_argument("--from", dest="source", type=Path)
    parser.add_argument("--at", help="Known actual UTC/offset timestamp; never invent historical timing")
    args = parser.parse_args()
    root = args.root.resolve()
    project_id = read(root / "project.json")["id"]
    path = root / "usage.json"
    ledger = read(path) if path.exists() else {"schema_version": 1, "project_id": project_id, "sessions": [], "jobs": {}}
    if ledger["project_id"] != project_id:
        raise ValueError("Usage ledger belongs to another project")
    at = timestamp(args.at)
    if args.command == "start":
        active = [session for session in ledger["sessions"] if not session.get("ended_at")]
        if active:
            return {"session_id": active[-1]["id"], "resumed": True, "started_at": active[-1]["started_at"]}
        session = {"id": "session_" + uuid4().hex, "reason": args.reason, "started_at": at.isoformat()}
        ledger["sessions"].append(session)
        atomic_write(path, ledger)
        return {"session_id": session["id"], "resumed": False, "started_at": session["started_at"]}
    if not args.session:
        raise ValueError("--session SESSION_ID is required")
    session = next(item for item in ledger["sessions"] if item["id"] == args.session)
    if args.command == "record":
        if not args.source:
            raise ValueError("record requires --from sanitized-job.json")
        job = read(args.source)
        validate_job(job)
        previous = ledger["jobs"].get(job["attempt_id"])
        if previous and previous["session_id"] != args.session:
            raise ValueError("An attempt cannot move to a different session")
        if previous and previous.get("task_id") and job.get("task_id") != previous["task_id"]:
            raise ValueError("An existing attempt's provider task ID cannot be changed or dropped")
        for key, other in ledger["jobs"].items():
            if key != job["attempt_id"] and job.get("task_id") and other.get("task_id") == job["task_id"]:
                raise ValueError("Provider task ID already belongs to another attempt; update that entry")
        job.update(session_id=args.session, updated_at=at.isoformat(),
                   recorded_at=previous["recorded_at"] if previous else at.isoformat())
        ledger["jobs"][job["attempt_id"]] = job
        atomic_write(path, ledger)
        return {"attempt_id": job["attempt_id"], "updated": bool(previous)}
    if args.command == "finish":
        if not session.get("ended_at"):
            if at < timestamp(session["started_at"]):
                raise ValueError("Session cannot end before it starts")
            session.update(ended_at=at.isoformat(), outcome=args.outcome)
            atomic_write(path, ledger)
        return {"session_id": args.session, "ended_at": session["ended_at"], "outcome": session["outcome"]}
    report = summary(ledger, args.session, at)
    atomic_write(root / "exports" / f"usage-report-{args.session}.json", report)
    return report


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    try:
        import json
        print(json.dumps(main(), ensure_ascii=False, indent=2, allow_nan=False))
    except (ValueError, KeyError, TypeError, OSError, StopIteration, InvalidOperation) as error:
        print(f"Movi2 usage: {error}", file=sys.stderr)
        sys.exit(1)
