#!/usr/bin/env python3
"""Local Movi2 state, immutable revisions, dependency fingerprints and exports.

Standard library only. Does not call any model, network, database or cloud API.
"""
import argparse
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
from datetime import datetime, timezone
from uuid import uuid4


TAG = re.compile(r"@[\w-]+", re.UNICODE)
IDENTIFIER = re.compile(r"[a-zA-Z0-9][a-zA-Z0-9_-]*\Z")
RANGE = re.compile(r"(?:Shot\s+\d+|镜头\s*\d+|鏡頭\s*\d+)\s*[（(]\s*(\d+(?:\.\d+)?)s?\s*[-–—]\s*(\d+(?:\.\d+)?)s?\s*[）)]", re.I)


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def encoded(value):
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"


def atomic_write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + "." + uuid4().hex + ".tmp")
    try:
        temporary.write_text(encoded(value), encoding="utf-8")
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def local_path(root, value):
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise ValueError(f"Media path must be a nonempty project-relative path: {value!r}")
    target = (root / value).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError(f"Media path escapes project: {value!r}")
    return target


def tags(text):
    # Exclude old unused-assets annotations from active bindings.
    active = re.split(r"(?:【|\[)Unused Assets(?:】|\])", text or "", flags=re.I)[0]
    return {match.casefold() for match in TAG.findall(active)}


def active_assets(project, chapter):
    used = tags(chapter.get("prompt", ""))
    used |= {tag.casefold() for tag in chapter.get("tagged_assets", [])}
    linked = set(chapter.get("linked_asset_ids", []))
    delinked = set(chapter.get("delinked_asset_ids", []))
    return [asset for asset in project["asset_list"] if asset["id"] not in delinked
            and (asset["id"] in linked or asset["tag"].casefold() in used)]


def selected_media(asset):
    return next((item for item in asset.get("candidates", [])
                 if item["id"] == asset.get("selected_candidate_id")), None)


def digest(value):
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, allow_nan=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def file_stamp(root, relative):
    path = local_path(root, relative)
    if not path.is_file():
        return {"path": relative, "sha256": None}
    checksum = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            checksum.update(chunk)
    return {"path": relative, "sha256": checksum.hexdigest()}


def asset_fingerprint(root, project, asset):
    return digest({"style": project.get("style"), "tag": asset["tag"],
                   "category": asset["category"], "description": asset["description"],
                   "references": [file_stamp(root, p) for p in asset.get("reference_paths", [])]})


def chapter_fingerprint(root, project, chapter):
    references = []
    for asset in active_assets(project, chapter):
        selected = selected_media(asset)
        references.append({"id": asset["id"], "definition": asset_fingerprint(root, project, asset),
                           "selected": selected and selected["id"],
                           "media": file_stamp(root, selected["path"]) if selected else None})
    return digest({"style": project.get("style"), "idea": project.get("high_level_idea"),
                   "aspect_ratio": project.get("aspect_ratio"),
                   "chapter": {key: chapter.get(key) for key in
                               ("prompt", "shots", "duration", "resolution", "audio", "handoff")},
                   "references": references,
                   "materials": [{**item, "file": file_stamp(root, item["path"])}
                                 for item in chapter.get("materials", [])]})


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def validate(root, project):
    errors, warnings = [], []
    if project.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if not isinstance(project.get("revision"), int) or project["revision"] < 0:
        errors.append("revision must be a nonnegative integer")
    if project.get("duration_mode") not in ("fixed", "adaptive"):
        errors.append("duration_mode must be fixed or adaptive")
    assets, chapters = project.get("asset_list", []), project.get("chapters", [])
    if not isinstance(assets, list) or not isinstance(chapters, list):
        return ["asset_list and chapters must be arrays"], []
    ids, asset_tags = set(), set()

    def identity(item, scope):
        value = item.get("id", "")
        if not isinstance(value, str) or not IDENTIFIER.fullmatch(value) or value in scope:
            errors.append(f"Invalid or duplicate id: {value!r}")
        scope.add(value)

    def media(items, chosen=None, take=False):
        item_ids = set()
        for item in items:
            identity(item, item_ids)
            if not take or item.get("status") == "succeeded":
                if not item.get("path"):
                    errors.append(f"Completed media {item.get('id')} needs a local path")
            if take and item.get("status") not in ("pending", "processing", "succeeded", "failed"):
                errors.append(f"Unknown take status: {item.get('id')}")
        if chosen and chosen not in item_ids:
            errors.append(f"Selected media id not found: {chosen}")
        if take and chosen:
            selected = next((i for i in items if i.get("id") == chosen), {})
            if selected.get("status") != "succeeded":
                errors.append(f"Selected take must have succeeded: {chosen}")

    for asset in assets:
        identity(asset, ids)
        tag = asset.get("tag", "")
        if not isinstance(tag, str) or not TAG.fullmatch(tag) or tag.casefold() in asset_tags:
            errors.append(f"Invalid or duplicate tag: {tag!r}")
        asset_tags.add(tag.casefold())
        if asset.get("category") not in ("character", "environment", "prop", "reference"):
            errors.append(f"Unknown category for {tag}")
        if not isinstance(asset.get("description"), str):
            errors.append(f"Asset description must be text: {tag}")
        media(asset.get("candidates", []), asset.get("selected_candidate_id"))

    limits = project.get("chapter_limits", {"min": 4, "max": 30})
    minimum, maximum = limits.get("min", 4), limits.get("max", 30)
    if not number(minimum) or not number(maximum) or minimum <= 0 or maximum < minimum:
        errors.append("Invalid chapter_limits")
        minimum, maximum = 4, 30
    total = 0
    for index, chapter in enumerate(chapters, 1):
        identity(chapter, ids)
        label = chapter.get("id", str(index))
        if chapter.get("chapter_index") != index:
            errors.append(f"{label}: chapter_index must be consecutive from 1")
        duration = chapter.get("duration")
        if not number(duration) or not minimum <= duration <= maximum:
            errors.append(f"{label}: duration outside configured chapter limits")
            duration = 0
        total += duration
        chapter_tags = tags(chapter.get("prompt", ""))
        chapter_tags |= {t.casefold() for t in chapter.get("tagged_assets", [])}
        for shot in chapter.get("shots", []):
            chapter_tags |= tags(shot.get("action", "") + " " + shot.get("audio", ""))
        if chapter_tags - asset_tags:
            errors.append(f"{label}: unknown tags {sorted(chapter_tags - asset_tags)}")
        declared = {t.casefold() for t in chapter.get("tagged_assets", [])}
        if chapter_tags - declared:
            errors.append(f"{label}: prompt/shot tags missing from tagged_assets")
        for field in ("linked_asset_ids", "delinked_asset_ids"):
            if set(chapter.get(field, [])) - {a["id"] for a in assets}:
                errors.append(f"{label}: unknown asset ids in {field}")
        delinked = set(chapter.get("delinked_asset_ids", []))
        if any(a["id"] in delinked and a["tag"].casefold() in chapter_tags for a in assets):
            errors.append(f"{label}: active prompt/shot/tag references a delinked asset")
        shots, cursor = chapter.get("shots", []), 0
        for shot in shots:
            start, end = shot.get("start"), shot.get("end")
            if not number(start) or not number(end) or abs(start - cursor) > 1e-6 or end <= start:
                errors.append(f"{label}: shots must be positive and contiguous from 0")
                break
            cursor = end
        if shots and abs(cursor - duration) > 1e-6:
            errors.append(f"{label}: shots do not span chapter duration")
        if chapter.get("prompt") and not shots:
            errors.append(f"{label}: a prompt needs structured shots")
        prompt_ranges = [(float(a), float(b)) for a, b in RANGE.findall(chapter.get("prompt", ""))]
        if prompt_ranges and prompt_ranges != [(s.get("start"), s.get("end")) for s in shots]:
            errors.append(f"{label}: prompt shot ranges differ from structured shots")
        if chapter.get("prompt") and not prompt_ranges:
            warnings.append(f"{label}: prompt timing syntax needs manual review")
        media(chapter.get("storyboards", []), chapter.get("selected_storyboard_id"))
        media(chapter.get("takes", []), chapter.get("active_take_id"), take=True)
        for asset in active_assets(project, chapter):
            if not selected_media(asset):
                warnings.append(f"{label}: {asset['tag']} has no selected local reference")

    target = project.get("total_duration_target")
    if project.get("duration_mode") == "fixed":
        if not number(target) or target <= 0:
            errors.append("Fixed mode needs positive total_duration_target")
        elif chapters and abs(total - target) > 1e-6:
            errors.append(f"Chapter total {total}s differs from target {target}s")

    def paths(value):
        if isinstance(value, dict):
            for key, child in value.items():
                if (key == "path" or key.endswith("_path")) and child:
                    try:
                        if not local_path(root, child).is_file():
                            errors.append(f"Missing local file: {child}")
                    except ValueError as error:
                        errors.append(str(error))
                elif key.endswith("_paths"):
                    for entry in child:
                        try:
                            if not local_path(root, entry).is_file():
                                errors.append(f"Missing reference file: {entry}")
                        except ValueError as error:
                            errors.append(str(error))
                else:
                    paths(child)
        elif isinstance(value, list):
            for child in value:
                paths(child)
    paths(project)
    return errors, warnings


def save(root, current, proposal, reason):
    if proposal.get("id") != current["id"] or proposal.get("revision") != current["revision"]:
        raise ValueError("Project id/revision mismatch; reload current state before editing")
    errors, warnings = validate(root, proposal)
    if errors:
        raise ValueError("Validation failed:\n" + "\n".join(errors))
    result = copy.deepcopy(proposal)
    result["revision"] = current["revision"] + 1
    result["updated_at"] = datetime.now(timezone.utc).isoformat()
    result["last_change"] = reason
    result["total_estimated_duration"] = sum(c["duration"] for c in result["chapters"])
    history = root / "history" / f"revision-{result['revision']:06d}.json"
    # Exclusive reservation also stops two edits from committing the same base revision.
    with history.open("x", encoding="utf-8") as output:
        output.write(encoded(result))
    atomic_write(root / "project.json", result)
    return {"revision": result["revision"], "snapshot": str(history), "warnings": warnings}


def report(root, project):
    errors, warnings = validate(root, project)
    artifacts = []
    def add(item, expected, owner, kind):
        recorded = item.get("dependency_fingerprint")
        state = "unknown" if not recorded else ("current" if recorded == expected else "stale")
        artifacts.append({"owner": owner, "kind": kind, "id": item["id"], "freshness": state})
    for asset in project["asset_list"]:
        stamp = asset_fingerprint(root, project, asset)
        for item in asset.get("candidates", []):
            add(item, stamp, asset["tag"], "candidate")
    for chapter in project["chapters"]:
        stamp = chapter_fingerprint(root, project, chapter)
        for kind in ("storyboards", "takes"):
            for item in chapter.get(kind, []):
                add(item, stamp, chapter["id"], kind)
    return {"project": project["project_name"], "revision": project["revision"],
            "duration": sum(c["duration"] for c in project["chapters"]),
            "errors": errors, "warnings": warnings, "artifacts": artifacts}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["init", "check", "status", "commit", "restore", "fingerprint", "export"])
    parser.add_argument("root", type=Path)
    parser.add_argument("--name")
    parser.add_argument("--from", dest="source", type=Path)
    parser.add_argument("--reason", default="Project update")
    parser.add_argument("--revision", type=int)
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--chapter")
    selection.add_argument("--asset")
    args = parser.parse_args()
    root = args.root.resolve()
    if args.command == "init":
        root.mkdir(parents=True, exist_ok=True)
        if (root / "project.json").exists() or (root / "history").exists():
            raise ValueError("Project already exists; load it instead")
        for name in ("history", "assets", "chapters", "exports"):
            (root / name).mkdir(exist_ok=True)
        now = datetime.now(timezone.utc).isoformat()
        project = {"schema_version": 1, "id": uuid4().hex, "revision": 0,
                   "project_name": args.name or root.name, "created_at": now, "updated_at": now,
                   "source_text": "", "input_mode": "idea", "language": "auto",
                   "high_level_idea": "", "detailed_script": "", "master_prompt_raw": "",
                   "style": {"medium": "cinematic realism", "palette": "", "lighting": "", "constraints": []},
                   "aspect_ratio": "16:9", "duration_mode": "adaptive", "total_duration_target": None,
                   "chapter_limits": {"min": 4, "max": 30}, "asset_list": [], "chapters": []}
        atomic_write(root / "history" / "revision-000000.json", project)
        atomic_write(root / "project.json", project)
        return {"project": str(root / "project.json"), "revision": 0}
    current = read(root / "project.json")
    project = read(args.source) if args.source else current
    if args.command in ("check", "status"):
        result = report(root, project)
        print(encoded(result), end="")
        return 1 if result["errors"] else 0
    if args.command == "commit":
        if not args.source:
            raise ValueError("commit requires --from edited JSON; do not edit project.json directly")
        return save(root, current, project, args.reason)
    if args.command == "restore":
        if args.revision is None or args.revision < 0:
            raise ValueError("restore requires a nonnegative --revision")
        previous = read(root / "history" / f"revision-{args.revision:06d}.json")
        previous["revision"] = current["revision"]
        return save(root, current, previous, f"Restore revision {args.revision}: {args.reason}")
    if args.command == "fingerprint":
        if args.chapter:
            chapter = next(c for c in project["chapters"] if c["id"] == args.chapter)
            return {"dependency_fingerprint": chapter_fingerprint(root, project, chapter)}
        if args.asset:
            asset = next(a for a in project["asset_list"] if a["id"] == args.asset or a["tag"] == args.asset)
            return {"dependency_fingerprint": asset_fingerprint(root, project, asset)}
        raise ValueError("fingerprint requires --chapter ID or --asset ID/@tag")
    if args.command == "export":
        errors, warnings = validate(root, project)
        if errors:
            raise ValueError("Validation failed:\n" + "\n".join(errors))
        package = {"project_id": project["id"], "source_revision": project["revision"],
                   "style": project["style"], "aspect_ratio": project["aspect_ratio"],
                   "status": "prepared", "warnings": warnings, "chapters": []}
        for chapter in project["chapters"]:
            references = []
            for asset in active_assets(project, chapter):
                item = selected_media(asset)
                references.append({"tag": asset["tag"], "category": asset["category"],
                                   "candidate_id": item["id"] if item else None,
                                   "path": str(local_path(root, item["path"])) if item else None})
            package["chapters"].append({"id": chapter["id"], "duration": chapter["duration"],
                                        "prompt": chapter.get("prompt", ""), "shots": chapter.get("shots", []),
                                        "references": references, "materials": chapter.get("materials", []),
                                        "dependency_fingerprint": chapter_fingerprint(root, project, chapter)})
        path = root / "exports" / f"render-package-r{project['revision']:06d}.json"
        atomic_write(path, package)
        return {"render_package": str(path), "status": "prepared", "warnings": warnings}


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    try:
        result = main()
        if isinstance(result, int):
            sys.exit(result)
        print(encoded(result), end="")
    except (ValueError, KeyError, TypeError, AttributeError, OSError, StopIteration) as error:
        print(f"Movi2: {error}", file=sys.stderr)
        sys.exit(1)
