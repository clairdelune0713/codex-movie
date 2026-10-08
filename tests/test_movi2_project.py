"""Exercise persistent editing and reference behavior without generating media."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


HELPER = Path(__file__).resolve().parents[1] / "skills" / "movi2" / "scripts" / "project.py"
spec = importlib.util.spec_from_file_location("movi2_project", HELPER)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=HELPER.parents[3] / "tests")
        self.root = Path(self.temp.name) / "movie"
        self.command("init", "--name", "Rain / 雨")
        self.project = module.read(self.root / "project.json")
        for name in ("tom", "hat", "station"):
            path = self.root / "assets" / f"{name}.bin"
            path.write_bytes((name + "test fixture").encode())
        self.project["asset_list"] = [
            {"id": "tom", "tag": "@Tom", "category": "character", "description": "Blue coat",
             "candidates": [{"id": "tom_1", "path": "assets/tom.bin"}], "selected_candidate_id": "tom_1"},
            {"id": "hat", "tag": "@Tom-hat", "category": "prop", "description": "Black hat",
             "candidates": [{"id": "hat_1", "path": "assets/hat.bin"}], "selected_candidate_id": "hat_1"},
            {"id": "station", "tag": "@車站", "category": "environment", "description": "Empty rain platform",
             "candidates": [{"id": "station_1", "path": "assets/station.bin"}], "selected_candidate_id": "station_1"}
        ]
        self.project.update(duration_mode="fixed", total_duration_target=16)
        self.project["chapters"] = [self.chapter("chapter_01", 1, "@Tom-hat"),
                                    self.chapter("chapter_02", 2, "@Tom")]

    def tearDown(self):
        self.temp.cleanup()

    def chapter(self, ident, index, tag):
        return {"id": ident, "chapter_index": index, "title": "雨", "duration": 8,
                "prompt": f"SCENE: {tag} at @車站. Shot 1 (0-3s): {tag} waits. Hard cut. Shot 2 (3-8s): Rain falls.",
                "tagged_assets": [tag, "@車站"], "shots": [
                    {"start": 0, "end": 3, "action": f"{tag} waits"},
                    {"start": 3, "end": 8, "action": "Rain falls"}],
                "storyboards": [], "takes": []}

    def command(self, command, *args, expected=0):
        result = subprocess.run([sys.executable, str(HELPER), command, str(self.root), *args],
                                capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, expected, result.stderr + result.stdout)
        return json.loads(result.stdout) if result.returncode == 0 else result.stderr

    def proposal(self, data=None):
        path = Path(self.temp.name) / "proposal.json"
        path.write_text(module.encoded(data or self.project), encoding="utf-8")
        return str(path)

    def test_commit_and_restore_preserve_revisions_and_unicode(self):
        self.command("commit", "--from", self.proposal(), "--reason", "Initial 雨")
        saved = module.read(self.root / "project.json")
        self.assertEqual(saved["total_estimated_duration"], 16)
        self.assertEqual(saved["project_name"], "Rain / 雨")
        saved["chapters"][0]["prompt"] += " LIGHTING: darker."
        self.command("commit", "--from", self.proposal(saved), "--reason", "Darker")
        self.command("restore", "--revision", "1")
        restored = module.read(self.root / "project.json")
        self.assertEqual(restored["revision"], 3)
        self.assertEqual(restored["chapters"][0]["prompt"], self.project["chapters"][0]["prompt"])
        self.assertEqual(len(list((self.root / "history").glob("*.json"))), 4)

    def test_invalid_commit_keeps_live_state_and_history(self):
        self.project["chapters"][0]["shots"][1]["start"] = 4
        self.command("commit", "--from", self.proposal(), expected=1)
        self.assertEqual(module.read(self.root / "project.json")["revision"], 0)
        self.assertEqual(len(list((self.root / "history").glob("*.json"))), 1)

    def test_stale_proposal_rejected(self):
        proposal = self.proposal()
        self.command("commit", "--from", proposal)
        self.assertIn("revision mismatch", self.command("commit", "--from", proposal, expected=1))

    def test_whole_tag_matching_and_delink(self):
        chapter = self.project["chapters"][0]
        self.assertEqual([a["id"] for a in module.active_assets(self.project, chapter)], ["hat", "station"])
        chapter["linked_asset_ids"] = ["tom"]
        chapter["delinked_asset_ids"] = ["tom"]
        self.assertEqual([a["id"] for a in module.active_assets(self.project, chapter)], ["hat", "station"])
        chapter["delinked_asset_ids"] = ["hat"]
        errors, _ = module.validate(self.root, self.project)
        self.assertTrue(any("delinked" in error for error in errors))

    def test_fingerprint_invalidates_only_relevant_chapters(self):
        before = [module.chapter_fingerprint(self.root, self.project, c) for c in self.project["chapters"]]
        self.project["asset_list"][0]["description"] = "Red coat"
        after = [module.chapter_fingerprint(self.root, self.project, c) for c in self.project["chapters"]]
        self.assertEqual(before[0], after[0])
        self.assertNotEqual(before[1], after[1])
        self.project["style"]["medium"] = "watercolor"
        style = [module.chapter_fingerprint(self.root, self.project, c) for c in self.project["chapters"]]
        self.assertTrue(all(a != b for a, b in zip(after, style)))

    def test_selected_reference_file_content_affects_fingerprint(self):
        chapter = self.project["chapters"][1]
        before = module.chapter_fingerprint(self.root, self.project, chapter)
        (self.root / "assets" / "tom.bin").write_bytes(b"changed fixture")
        self.assertNotEqual(before, module.chapter_fingerprint(self.root, self.project, chapter))

    def test_unknown_and_stale_artifacts_reported(self):
        chapter = self.project["chapters"][0]
        stamp = module.chapter_fingerprint(self.root, self.project, chapter)
        chapter["storyboards"] = [{"id": "sb_1", "path": "assets/hat.bin", "dependency_fingerprint": stamp}]
        self.assertEqual(module.report(self.root, self.project)["artifacts"][-1]["freshness"], "current")
        chapter["prompt"] += " Color: indigo."
        report = module.report(self.root, self.project)
        self.assertEqual(report["artifacts"][-1]["freshness"], "stale")
        self.assertEqual(report["artifacts"][0]["freshness"], "unknown")

    def test_missing_files_escape_and_failed_take_selection(self):
        for bad_path in ("assets/absent.png", "../outside.png", str(self.root / "assets/tom.bin")):
            proposal = copy.deepcopy(self.project)
            proposal["asset_list"][0]["candidates"][0]["path"] = bad_path
            self.assertTrue(module.validate(self.root, proposal)[0])
        chapter = self.project["chapters"][0]
        chapter["takes"] = [{"id": "take_1", "status": "failed", "error": "Failed"}]
        chapter["active_take_id"] = "take_1"
        self.assertTrue(any("must have succeeded" in e for e in module.validate(self.root, self.project)[0]))

    def test_timing_target_and_unknown_tags_fail(self):
        self.project["total_duration_target"] = 20
        self.project["chapters"][0]["prompt"] += " @phantom appears."
        self.project["chapters"][1]["prompt"] = self.project["chapters"][1]["prompt"].replace("3-8s", "3-7s")
        errors, _ = module.validate(self.root, self.project)
        self.assertTrue(any("target" in e for e in errors))
        self.assertTrue(any("unknown tags" in e for e in errors))
        self.assertTrue(any("ranges differ" in e for e in errors))

    def test_export_is_preparation_with_local_paths(self):
        self.command("commit", "--from", self.proposal())
        result = self.command("export")
        package = module.read(result["render_package"])
        self.assertEqual(package["status"], "prepared")
        self.assertEqual(package["source_revision"], 1)
        refs = package["chapters"][0]["references"]
        self.assertEqual([r["tag"] for r in refs], ["@Tom-hat", "@車站"])
        self.assertTrue(all(Path(r["path"]).is_file() for r in refs))
        self.command("init", expected=1)


if __name__ == "__main__":
    unittest.main()
