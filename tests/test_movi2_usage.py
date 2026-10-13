"""Verify usage accounting without calling any provider."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "skills/movi2/scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("movi2_usage", SCRIPTS / "usage.py")
usage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(usage)


class UsageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=SCRIPTS.parents[2] / "tests")
        self.root = Path(self.temp.name) / "movie"
        result = subprocess.run([sys.executable, str(SCRIPTS / "project.py"), "init", str(self.root)], capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def tearDown(self):
        self.temp.cleanup()

    def command(self, command, *args, at="2026-10-13T01:00:00Z", expected=0):
        result = subprocess.run([sys.executable, str(SCRIPTS / "usage.py"), command, str(self.root), "--at", at, *args],
                                capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, expected, result.stderr + result.stdout)
        return json.loads(result.stdout) if expected == 0 else result.stderr

    def record(self, session, record, expected=0):
        path = Path(self.temp.name) / "record.json"
        path.write_text(json.dumps(record), encoding="utf-8")
        return self.command("record", "--session", session, "--from", str(path), expected=expected)

    def test_resume_does_not_reset_start_and_finished_time_stops_growing(self):
        session = self.command("start")["session_id"]
        resumed = self.command("start", at="2026-10-13T01:02:00Z")
        self.assertTrue(resumed["resumed"])
        self.assertEqual(resumed["session_id"], session)
        self.command("finish", "--session", session, at="2026-10-13T01:03:00Z")
        self.command("finish", "--session", session, at="2026-10-13T01:10:00Z")
        result = self.command("report", "--session", session, at="2026-10-13T02:00:00Z")
        self.assertEqual(result["session"]["elapsed_seconds"], 180)
        self.assertEqual(result["session"]["seedance_cost"]["attempts"], 0)

    def test_updates_do_not_double_count_and_unknown_is_not_zero(self):
        session = self.command("start")["session_id"]
        self.record(session, {"attempt_id": "one", "state": "submitting"})
        pending = self.command("report", "--session", session)
        self.assertEqual(pending["session"]["seedance_cost"]["unknown_charge_attempts"], 1)
        for _ in range(2):
            self.record(session, {"attempt_id": "one", "task_id": "task_one", "state": "succeeded",
                                  "cost": {"kind": "actual", "amount": "0.10", "currency": "USD", "basis": "Fixture charge"}})
        result = self.command("report", "--session", session)["session"]["seedance_cost"]
        self.assertEqual(result["currencies"]["USD"]["actual"], "0.10")
        self.assertEqual(result["attempts"], 1)
        self.record(session, {"attempt_id": "duplicate", "task_id": "task_one"}, expected=1)

    def test_revision_counts_old_and_failed_jobs_and_excludes_gap_time(self):
        first = self.command("start")["session_id"]
        self.record(first, {"attempt_id": "failed_attempt", "state": "failed",
                            "cost": {"kind": "actual", "amount": "0.20", "currency": "USD", "basis": "Billable failed job fixture"}})
        self.command("finish", "--session", first, at="2026-10-13T01:02:00Z")
        second = self.command("start", "--reason", "Revision", at="2026-10-13T02:00:00Z")["session_id"]
        self.command("finish", "--session", second, at="2026-10-13T02:01:00Z")
        # Creative restore must not reset the independent accounting ledger.
        restored = subprocess.run([sys.executable, str(SCRIPTS / "project.py"), "restore", str(self.root), "--revision", "0"], capture_output=True)
        self.assertEqual(restored.returncode, 0, restored.stderr)
        result = self.command("report", "--session", second, at="2026-10-13T02:02:00Z")
        self.assertEqual(result["session"]["seedance_cost"]["attempts"], 0)
        self.assertEqual(result["project_total"]["seedance_cost"]["currencies"]["USD"]["actual"], "0.20")
        self.assertEqual(result["session"]["elapsed_seconds"], 60)
        self.assertEqual(result["project_total"]["elapsed_seconds"], 180)

    def test_estimates_currencies_and_unknown_charges_remain_distinct(self):
        session = self.command("start")["session_id"]
        for ident, kind, currency, amount in (("a", "actual", "USD", "0.1"), ("b", "estimated", "USD", "0.2"), ("c", "actual", "TWD", "4")):
            self.record(session, {"attempt_id": ident, "cost": {"kind": kind, "amount": amount, "currency": currency, "basis": "Test evidence"}})
        self.record(session, {"attempt_id": "d", "state": "uncertain"})
        result = self.command("report", "--session", session)["project_total"]["seedance_cost"]
        self.assertEqual(result["currencies"]["USD"], {"actual": "0.1", "estimated": "0.2"})
        self.assertEqual(result["currencies"]["TWD"]["actual"], "4")
        self.assertTrue(result["provisional"])
        self.assertEqual(result["unknown_charge_attempts"], 1)

    def test_overlapping_sessions_are_not_double_counted(self):
        sessions = [{"started_at": "2026-10-13T01:00:00Z", "ended_at": "2026-10-13T01:05:00Z"},
                    {"started_at": "2026-10-13T01:03:00Z", "ended_at": "2026-10-13T01:06:00Z"}]
        self.assertEqual(usage.elapsed(sessions, usage.timestamp("2026-10-13T02:00:00Z")), 360)

    def test_invalid_cost_and_time_evidence_rejected(self):
        session = self.command("start")["session_id"]
        for amount in ("NaN", "Infinity", "-1"):
            self.record(session, {"attempt_id": "bad", "cost": {"kind": "actual", "amount": amount, "currency": "USD", "basis": "test"}}, expected=1)
        self.command("finish", "--session", session, at="2026-10-13T00:00:00Z", expected=1)
        self.command("start", at="2026-10-13T01:00:00", expected=1)


if __name__ == "__main__":
    unittest.main()
