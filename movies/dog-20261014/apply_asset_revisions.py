"""Register inspected ImageGen edits and build review-only galleries.

Does not edit canonical project.json; commit the proposal with Movi2's helper.
Does not generate video, upload references, or read credentials.
"""
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
RECEIPTS = ROOT / "exports/asset-edits-r03/generation-records-final.json"
NOW = datetime.now(timezone.utc).isoformat()
SPECS = {
    "bo": ("@Bo", "bo_edit02", True, "Mature broad face, cropped pixie hair, smaller almond eyes and fuller build; original teal staff outfit."),
    "mother": ("@LokAndMother", "lok_and_mother_edit02", False, "Intermediate mother revision; superseded by the subsequent Lok revision."),
    "lok": ("@LokAndMother", "lok_and_mother_edit03", True, "Lok has softer cheeks, neat black fringe, warm almond eyes and a shy mischievous smile; mother has oval face, burgundy rectangular glasses and low bun."),
    "street_cast": ("@StreetAndFerryCast", "street_and_ferry_cast_edit02", True, "Rust-jacket woman has elongated mature face and dark-auburn curls. Ferry worker wears blue sailor jumper, square piped collar, matching trousers and round sailor cap."),
    "crossing": ("@CentralCrossing", "central_crossing_edit02", True, "Exactly one visible pedestrian signal at far-right opposite pavement; left duplicate removed."),
    "car": ("@PetFriendlyCar", "pet_friendly_car_edit02", False, "Rejected: first edit retained wrong rear hinge. Do not select."),
    "car_fixed": ("@PetFriendlyCar", "pet_friendly_car_edit03", True, "Rear passenger door hinges at forward B-pillar and swings outward toward front; front door closed in open-door view."),
    "tram": ("@CentralTram", "central_tram_edit02", True, "Deep green painted panels and window surrounds, off-white bands/roof, one trolley pole; driver and passengers retained."),
    "crossing_guidance": ("@CrossingGuidance", "crossing_guidance_edit02", True, "One visible far-right pedestrian signal per panel, consistent with location; blocked green phase and fresh clear green phase remain distinct."),
    "harness": ("@HarnessGuidance", "harness_guidance_edit02", True, "Tart stands beside seated Ah Ming outside both legs in all panels. Harness on without lead; harness fully off; then held brown collar lead."),
    "gangway": ("@FerryGangway", "ferry_gangway_edit02", True, "Both ferry workers in blue sailor clothing; rust-jacket woman matches updated mature curly-haired design."),
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


project = json.loads((ROOT / "project.json").read_text(encoding="utf-8"))
receipts = json.loads(RECEIPTS.read_text(encoding="utf-8"))
by_tag = {a["tag"]: a for a in project["asset_list"]}
changed = []
checks = []
for record in receipts:
    key = record["key"]
    tag, candidate_id, selected, note = SPECS[key]
    asset = by_tag[tag]
    source = Path(record["generated_path"])
    target = ROOT / "assets" / asset["id"] / (candidate_id + ".png")
    if target.exists():
        assert sha(target) == sha(source), target
    else:
        shutil.copy2(source, target)
    with Image.open(target) as image:
        dimensions = list(image.size)
        image.verify()
    if not any(c["id"] == candidate_id for c in asset["candidates"]):
        refs = []
        for ref in record["referenced_image_paths"]:
            ref_path = Path(ref).resolve()
            assert ref_path.is_relative_to(ROOT)
            refs.append(ref_path.relative_to(ROOT).as_posix())
        asset["candidates"].append({
            "id": candidate_id, "path": target.relative_to(ROOT).as_posix(),
            "prompt": record["prompt"], "source_revision": project["revision"],
            "created_at": record["created_at"], "source": "edited", "tool": "built-in image_gen",
            "input_reference_paths": refs, "dimensions": dimensions, "sha256": sha(target),
            "inspection": {"status": "inspected" if selected else "superseded_or_rejected", "notes": note},
        })
    if selected:
        asset["selected_candidate_id"] = candidate_id
        asset["design_revision_notes"] = note
        asset["description"] += " User-directed revision 2026-10-15: " + note
        asset["source"] = "supplied_with_user_requested_edit"
        changed.append(asset["id"])
    checks.append({"tag": tag, "candidate_id": candidate_id, "selected": selected,
                   "sha256": sha(target), "dimensions": dimensions, "decode": "passed", "notes": note})

partial = "--allow-partial" in sys.argv
assert len(set(changed)) == (8 if partial else 9)
if partial:
    by_tag["@FerryGangway"]["selected_candidate_id"] = None
    by_tag["@FerryGangway"]["status"] = "revision_pending"
    project["pending_asset_revisions"] = [{"tag": "@FerryGangway", "reason": "Repeated built-in ImageGen network failures; updated woman and blue sailor clothing still required. Old candidate retained but deselected. CLI fallback requires explicit user choice."}]
else:
    project["pending_asset_revisions"] = []
project["production_stage"] = "asset_revision_partial" if partial else "awaiting_revised_asset_review"
project.setdefault("asset_revision_requests", []).append({
    "date": "2026-10-15", "reason": "User requested distinct faces, authentic blue ferry sailor clothing and tram colours, corrected car door hinges, single crossing signal and safe harness staging; follow-up requests a cuter Hong Kong-looking Lok.",
    "changed_asset_ids": list(dict.fromkeys(changed)), "generation_receipts": "exports/asset-edits-r03/generation-records-final.json",
})
project["critical_locks"].extend([
    "Bo cropped pixie and broad mature face; Lok mother burgundy glasses/low bun; rust-jacket woman auburn curls/long mature face. May's original identity remains the anchor.",
    "Lok follows revised softer-cheeked, neat-fringe Hong Kong schoolboy design; preserve exact mustard outfit and current mother design.",
    "Ferry sailors use blue sailor workwear, square piped collar and round cap; no white pilot shirts or officer epaulettes.",
    "Tram uses deep green and off-white painted livery, no cream/gold exterior wood treatment, one trolley pole.",
    "Crossing has only one visible far-right pedestrian signal per planned view; guidance matches location.",
    "Rear car door has conventional front B-pillar hinge, never C-pillar suicide hinge. Driving scenes must use Hong Kong right-hand-drive layout; door geometry rather than driver's seat is this reference's primary role.",
    "During harbour harness transition Tart stands beside outside of Ah Ming's legs, never under/between/straddled by knees.",
])
project["cast_design_overrides"] = {
    "Bo": "Original source bob is superseded by revised short pixie design under user direction.",
    "Lok_and_mother": "Revised boy and mother's face/hair/glasses supersede earlier pack sheet; dialogue and wardrobe retained.",
    "street_woman_and_ferry_sailors": "Revised design applies to individual cast sheet and populated gangway reference.",
}
save_json(ROOT / "proposal-asset-revisions.json", project)
save_json(ROOT / "exports/asset-edits-r03/inspection.json", {
    "inspected_at": NOW, "changed_asset_count": len(set(changed)), "retained_candidate_count": len(checks),
    "candidates": checks, "seedance_submissions": 0,
    "duration_seconds": sum(c["duration"] for c in project["chapters"]),
    "source_pack_untouched": True,
})

gallery_root = ROOT / "exports/asset-review-r03"
gallery_root.mkdir(parents=True, exist_ok=True)
font = "C:/Windows/Fonts/arial.ttf"
title_font, tag_font, id_font = (ImageFont.truetype(font, n) for n in (30, 23, 17))


def sheet(batch, title, filename):
    cols = min(3, len(batch))
    cell_w, cell_h, top = 644, 434, 84
    rows = (len(batch) + cols - 1) // cols
    canvas = Image.new("RGB", (cols * cell_w + 24, rows * cell_h + top + 20), "#f2eee6")
    draw = ImageDraw.Draw(canvas)
    draw.text((24, 22), title, font=title_font, fill="#202936")
    for n, asset in enumerate(batch):
        candidate = next((c for c in asset["candidates"] if c["id"] == asset["selected_candidate_id"]), None)
        left, y = 12 + (n % cols) * cell_w, top + (n // cols) * cell_h
        draw.rounded_rectangle((left, y, left + cell_w - 8, y + cell_h - 12), radius=12, fill="white")
        if candidate:
            with Image.open(ROOT / candidate["path"]) as image:
                preview = ImageOps.contain(image.convert("RGB"), (624, 352))
            canvas.paste(preview, (left + 10 + (624 - preview.width) // 2, y + 8 + (352 - preview.height) // 2))
        else:
            draw.text((left + 50, y + 135), "Replacement pending", font=title_font, fill="#93502d")
            draw.text((left + 50, y + 185), "Old image deselected", font=tag_font, fill="#93502d")
        draw.text((left + 12, y + 365), asset["tag"], font=tag_font, fill="#153c51")
        draw.text((left + 12, y + 396), candidate["id"] if candidate else "No candidate selected", font=id_font, fill="#465265")
    output = gallery_root / filename
    canvas.save(output, quality=95, subsampling=0)
    return output


gallery, index = [], ["# dog-20261014 - asset revision progress", "", f"{len(set(changed))} references revised on 15 October 2026. Original candidates and source pack retained. All 72 assets are listed; the gangway replacement is pending and its old candidate is deselected. Review sheets are never renderer inputs.", ""]
groups = [("01_CHARACTERS", "Characters", 8), ("02_LOCATIONS", "Environments", 10),
          ("03_PROPS", "Main props", 9), ("04_VEHICLES", "Vehicles and ferry", 7), ("05_STAGING", "Planning-only choreography", 3)]
for prefix, title, per_page in groups:
    members = sorted([a for a in project["asset_list"] if a["source_pack_file"].startswith(prefix)], key=lambda a: a["tag"].lower())
    for page, offset in enumerate(range(0, len(members), per_page), 1):
        batch = members[offset:offset + per_page]
        output = sheet(batch, f"{title} | {page} | current selections", f"{prefix.lower()}-{page:02d}.jpg")
        gallery.append({"group": title, "sheet": output.relative_to(ROOT).as_posix(), "asset_ids": [a["id"] for a in batch]})
        index.extend([f"## {title} - {page}", "", f"![{title}](<{output.as_posix()}>)", ""])
        for asset in batch:
            candidate = next((c for c in asset["candidates"] if c["id"] == asset["selected_candidate_id"]), None)
            if candidate:
                index.append(f"- **{asset['name']}** - {asset['tag']} - `{candidate['id']}` - [full-size](<{(ROOT / candidate['path']).as_posix()}>)")
            else:
                index.append(f"- **{asset['name']}** - {asset['tag']} - replacement pending; no candidate selected")
        index.append("")
assert len({i for g in gallery for i in g["asset_ids"]}) == 72
save_json(gallery_root / "gallery.json", gallery)
(gallery_root / "index.md").write_text("\n".join(index) + "\n", encoding="utf-8")

changed_groups = [
    ("Revised cast", ["@Bo", "@LokAndMother", "@StreetAndFerryCast"], "changes-01-cast.jpg"),
    ("Revised transport", ["@PetFriendlyCar", "@CentralTram", "@FerryGangway"], "changes-02-transport.jpg"),
    ("Revised location and choreography", ["@CentralCrossing", "@CrossingGuidance", "@HarnessGuidance"], "changes-03-layout.jpg"),
]
for title, tags, name in changed_groups:
    sheet([by_tag[t] for t in tags], title, name)

faces = [
    ("May - unchanged", "@May", (.60, .12, 1.0, .97)),
    ("Bo", "@Bo", (.60, .12, 1.0, .97)),
    ("Lok's mother", "@LokAndMother", (.60, .50, 1.0, 1.0)),
    ("Street-cast woman", "@StreetAndFerryCast", (.32, .07, .47, .35)),
    ("Lok", "@LokAndMother", (.60, .01, 1.0, .445)),
]
comparison = Image.new("RGB", (2000, 600), "#f2eee6")
draw = ImageDraw.Draw(comparison)
draw.text((24, 20), "Face comparison - revised identities beside unchanged May", font=title_font, fill="#202936")
for i, (label, tag, bounds) in enumerate(faces):
    asset = by_tag[tag]
    candidate = next(c for c in asset["candidates"] if c["id"] == asset["selected_candidate_id"])
    with Image.open(ROOT / candidate["path"]) as image:
        width, height = image.size
        crop = image.crop(tuple(round(n * (width if j % 2 == 0 else height)) for j, n in enumerate(bounds)))
        preview = ImageOps.contain(crop.convert("RGB"), (376, 448))
    comparison.paste(preview, (i * 400 + 12 + (376 - preview.width) // 2, 78 + (448 - preview.height) // 2))
    draw.text((i * 400 + 16, 548), label, font=tag_font, fill="#153c51")
comparison.save(gallery_root / "face-comparison.jpg", quality=95, subsampling=0)
print(json.dumps({"changed_assets": len(set(changed)), "preserved_edit_candidates": len(checks),
                  "proposal": str(ROOT / "proposal-asset-revisions.json"), "review_gallery": str(gallery_root)}, indent=2))
