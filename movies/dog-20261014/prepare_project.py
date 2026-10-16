"""Import the supplied masters and prepare a rough timeline and asset review.

Local preparation only: no credential reads, uploads, provider calls or final prompts.
Run with the bundled Python that includes Pillow. Canonical state is committed
separately through the installed Movi2 project helper.
"""
import hashlib
import json
import re
import shutil
import textwrap
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parent.parent
SOURCE = WORKSPACE / "SOMEWHERE_BETWEEN_US_READY"
ARCHIVE = ROOT / "source" / SOURCE.name
NOW = datetime.now(timezone.utc).isoformat()


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clock(seconds):
    return f"{seconds // 60:02d}:{seconds % 60:02d}"


TAG_OVERRIDES = {
    "Ah_Ming_阿明_Dark_Glasses": "AhMing",
    "Auntie_Lan_Cafe_Worker": "AuntieLan",
    "Bo_Centre_Worker": "Bo",
    "Centre_Colleague_and_Members": "CentreMembers",
    "Growing_Tart_and_Tine": "GrowingDogs",
    "Lok_and_Mother": "LokAndMother",
    "May_阿May": "May",
    "Street_and_Ferry_Supporting_Cast": "StreetAndFerryCast",
    "Tart_Adult_Off_Duty_Attached_Lead": "TartOffDuty",
    "Tart_Adult_Working_Harness_No_Leash": "TartWorking",
    "Tart_Home_Collar_Separate_Lead": "TartHome",
    "Tart_蛋撻_Puppy": "TartPuppy",
    "Tine_阿華田_Adult_Bandanna_Collar_Lead": "TineAdult",
    "Tine_阿華田_Puppy": "TinePuppy",
    "Training_Handlers_and_Volunteer": "TrainingCast",
    "Uncle_Chan_陳伯": "UncleChan",
    "S01_Victoria_Puppy_Yard_Morning": "VictoriaPuppyYard",
    "S01_Victoria_Bench_Rain_Shelter": "VictoriaRainShelter",
    "S01_Covered_Departure_Yard": "VictoriaDepartureYard",
    "S02_Guide_Training_Path": "GuideTrainingPath",
    "S02_Hong_Kong_Practice_and_Introductions": "HKPracticeRoom",
    "S03_Residential_Lift_Lobby": "ResidentialLiftLobby",
    "S03_S04_Central_Lan_Kee_Cha_Chaan_Teng": "LanKee",
    "S03_S07_Ah_Ming_Flat": "AhMingFlat",
    "S04_Centre_Room_Morning": "CentreMorning",
    "S04_Station_Lift": "StationLift",
    "S05_Central_Signalled_Crossing": "CentralCrossing",
    "S06_S08_S09_S10_Centre_Room_Afternoon": "CentreAfternoon",
    "S08_Tsim_Sha_Tsui_Public_Station_Exit": "PublicStationExit",
    "S11_S12_Centre_Entrance_and_Walking_Route": "CentreWalkingRoute",
    "S11_Uncle_Chan_Flat": "UncleChanFlat",
    "S13_S16_Harbour_Geography_Afternoon": "HarbourGeography",
    "S13_Public_Ferry_Forecourt_Junction": "FerryForecourt",
    "S14_S16_Nearer_Seating_Bay": "NearerSeatingBay",
    "S15_Farther_Meeting_Bench": "FartherMeetingBench",
    "Ah_Ming_Folding_White_Cane": "FoldingCane",
    "Ah_Ming_Recording_Equipment": "RecordingEquipment",
    "Canonical_Puppy_Photograph": "PuppyPhotograph",
    "Centre_Furnishings": "CentreFurniture",
    "Centre_Listening_and_Outing_Papers": "OutingPapers",
    "Home_Play_Furnishings": "HomeFurniture",
    "May_Water_Bottle": "MayWaterBottle",
    "Newspaper_Readable": "Newspaper",
    "Puppy_Bench_and_Transport_Crates": "PuppyBenchAndCrates",
    "S01_Puppies_Shallow_Water_Bowl": "PuppyWaterBowl",
    "S03_Ah_Ming_Cup": "AhMingCup",
    "S03_Ah_Ming_Radio": "AhMingRadio",
    "S03_Neighbour_Shopping_Trolley": "NeighbourTrolley",
    "S03_S07_Ah_Ming_Keys": "AhMingKeys",
    "S04_Lan_Kee_Breakfast_Toast_and_Tableware": "LanKeeBreakfast",
    "S04_S13_S15_Passenger_Suitcase": "PassengerSuitcase",
    "S11_Uncle_Chan_Kettle": "UncleChanKettle",
    "Street_Obstructions_and_Cafe_Takeaway": "StreetObstructions",
    "Tart_Brown_Leather_Guide_Harness_Worn_and_Removed": "TartHarness",
    "Tine_Bowl_With_Carrying_Clip": "TineBowl",
    "Tine_Orange_Bandanna_with_Emblem": "TineBandanna",
    "Tine_Orange_Collar_and_Lead": "TineCollarAndLead",
    "Tine_Rest_Mat_and_May_Bag": "TineMatAndMayBag",
    "Two_Ended_Squeaky_Toy_Worn_and_New": "SqueakyToy",
    "Uncle_Chan_Bag": "UncleChanBag",
    "Uncle_Chan_Personal_Effects": "UncleChanEffects",
    "Uncle_Chan_Wife_and_Ah_Wong_Photo": "UncleChanPhotograph",
    "S01_Puppy_Transport_Vehicles": "PuppyTransportVehicles",
    "S03_Central_Tram_With_Driver": "CentralTram",
    "S04_Prearranged_Pet_Friendly_Car": "PetFriendlyCar",
    "S05_Van_and_Queued_Car_With_Drivers": "CrossingVehicles",
    "S12_Star_Ferry_Exterior_Lights_Off_People": "FerryExterior",
    "S12_Star_Ferry_Interior_Afternoon_Passengers": "FerryInterior",
    "S12_Star_Ferry_Gangway_Afternoon_People": "FerryGangway",
    "S05_Crossing_Hold_and_Clear": "CrossingGuidance",
    "S15_Harness_Off_Then_Lead_On": "HarnessGuidance",
    "S16_Reunion_Tug_and_Final_Rest": "ReunionGuidance",
}

# (duration, first source block, last source block, editorial purpose).
# These are action/dialogue units, not final shot prompts or uniform partitions.
PLAN = {
    1: [(16, 0, 4, "Bench puzzle and Tine's stuck-bottom gag"),
        (16, 5, 12, "Two squeaks, contrasting bows, accidental sit and sharing"),
        (14, 13, 14, "Brisk run and wet-paw reaction"),
        (18, 15, 21, "Rain, failed dry spot, cuddle and canonical photograph"),
        (21, 22, 27, "Months later: contact, separate crates and departures")],
    2: [(18, 0, 1, "Tart learns to clear a route for two bodies"),
        (16, 2, 3, "Tine learns to respect a withdrawn hand"),
        (18, 4, 5, "Ah Ming and May introductions; chin-on-knee compromise"),
        (8, 6, 7, "May receives the same print; young-to-adult paw match")],
    3: [(20, 0, 4, "Touch-led morning routine, harness excitement and work cue"),
        (14, 5, 8, "Neighbour trolley clears the lift"),
        (18, 9, 12, "Stationary tram recording interrupted by delivery trolley"),
        (18, 13, 17, "Stationary reply and breakfast anticipation")],
    4: [(18, 0, 2, "Match footsteps across two jobs; both complete a task"),
        (16, 3, 4, "Suitcase clearance matched to Lok's peekaboo"),
        (14, 5, 7, "Toast and crumb temptation, restraint and untidy leg"),
        (19, 8, 12, "Cafe name mix-up, payment and clear departure"),
        (15, 13, 16, "Minutes-later takeaway and first missed encounter"),
        (8, 17, 20, "Route opens; invited touch; newspaper foreshadowing")],
    5: [(16, 0, 8, "Establish van hazard; cue, refusal and creeping wheel"),
        (20, 9, 16, "Pedestrian confirms hazard; van clears; choose next phase"),
        (19, 17, 21, "Fresh signal, complete crossing and shoulder-rub payoff")],
    6: [(18, 0, 7, "Refusal respected; Tine chooses mat and rest"),
        (16, 8, 11, "Fallen flyer tests Tine's restraint without intrusion"),
        (22, 12, 20, "Rest-as-work exchange, funny name and open hand"),
        (24, 21, 27, "Invitation, shoulder contact and reluctant goodbye")],
    7: [(13, 0, 3, "Harness off, whole-body shake and impatient toy delivery"),
        (17, 4, 8, "Knee-switch squeak and determined tug"),
        (15, 9, 10, "Cushion collision, laugh and returned toy"),
        (10, 11, 13, "Seated editing and quiet dog-to-foot contact")],
    8: [(16, 0, 3, "Establish public routes and wall occlusion"),
        (14, 4, 7, "Ear response, fleeting cream coat and second near miss"),
        (16, 8, 10, "Unopened newspaper and two umbrella-stand clangs"),
        (14, 11, 15, "Chan calls Tine; exuberance eases into careful approach")],
    9: [(20, 0, 6, "Remembered touch; puppy print appears and is put away"),
        (18, 7, 10, "Offer-withdraw toy gag resolves with a squeak and bow"),
        (17, 11, 13, "Lok asks, waits, strokes and withdraws"),
        (18, 14, 20, "Separate old photograph, slipper joke and towel memory"),
        (12, 21, 24, "Harbour invitation leaves Chan an independent choice")],
    10: [(21, 0, 7, "Listening game: tram, trolley and one-ear reaction"),
         (19, 8, 13, "Ferry recording connects to Chan's former work"),
         (18, 14, 18, "Home-toy joke opens into the harbour invitation"),
         (22, 19, 24, "Brief chosen pause; Tine matters; Chan signs up"),
         (10, 25, 27, "Agree ferry arrival and meeting point; sleeping-paw button")],
    11: [(24, 0, 5, "Independent evening: kettle, hat, packed bag and phone"),
         (21, 6, 9, "Saturday match on hat; Tine waits for Chan to settle")],
    12: [(15, 0, 2, "13:00 group check, bowl clip and short public walking route"),
         (22, 3, 8, "Afternoon ferry child asks and offers a morning greeting"),
         (15, 9, 10, "One eye opens; leaf temptation returns to Chan's pace"),
         (18, 11, 14, "Moored-ferry call, phone packed, cue and disembarkation")],
    13: [(13, 0, 3, "Public forecourt routes bring both dogs into one frame"),
         (17, 4, 8, "Suitcase gap, tentative step and interrupted safe route"),
         (17, 9, 13, "Group turns inland; Tart clears route east; third near miss"),
         (8, 14, 14, "Water break carries the cut into the seating bay")],
    14: [(18, 0, 4, "Shake anticipation, one drop, tissue and exaggerated wipe"),
         (22, 5, 12, "Horn changes Chan's expression; Tine turns back; May listens"),
         (12, 13, 16, "Shoulder in reach and group chooses to remain"),
         (23, 17, 23, "Stationary call relocates meeting; open hand ends the beat")],
    15: [(14, 0, 2, "Stationary phone away and guided return"),
         (22, 3, 9, "Narrow entrance, spoken help and suitcase clearance"),
         (20, 10, 17, "First sensory contact; task comes first; secure seating"),
         (19, 18, 21, "Harness fully off, then brown lead clipped; off-duty shake")],
    16: [(18, 0, 6, "Permission, curved approach and reciprocal sniffing"),
         (16, 7, 13, "Tine waits; squeak invites Tart to the free toy end"),
         (20, 14, 19, "Accidental sit, returned toy, matching bows and ear gag"),
         (15, 20, 24, "Humans hear generosity; keep dogs playing underneath"),
         (24, 25, 29, "May connects names, same print and Victoria origin"),
         (20, 30, 34, "Describe puppy pose to Ah Ming; confirmation after behaviour"),
         (13, 35, 38, "Chan chooses longer rest and makes room for family"),
         (24, 39, 49, "Offer room, settle into puppy pose; live harbour and brief fade")],
}

assert sum(item[0] for scene in PLAN.values() for item in scene) == 1200
assert all(4 <= item[0] <= 30 for scene in PLAN.values() for item in scene)

if ARCHIVE.exists():
    raise SystemExit("Source archive already exists: inspect current state before rerunning.")
shutil.copytree(SOURCE, ARCHIVE)
source_checks = []
for original in sorted(SOURCE.rglob("*")):
    if original.is_file():
        relative = original.relative_to(SOURCE)
        copied = ARCHIVE / relative
        source_checks.append({"file": relative.as_posix(), "sha256": sha(original),
                              "copy_matches": sha(original) == sha(copied)})
assert all(item["copy_matches"] for item in source_checks)

manifest = json.loads((ARCHIVE / "06_CONTINUITY/ASSET_MANIFEST.json").read_text(encoding="utf-8"))
structure = json.loads((ARCHIVE / "06_CONTINUITY/SCREENPLAY_STRUCTURE.json").read_text(encoding="utf-8"))
prompt_records = json.loads((ARCHIVE / "06_CONTINUITY/IMAGE_PROMPT_SET.json").read_text(encoding="utf-8"))
generation_prompts = {p["delivered_asset"]: p["generation_record"].get("prompt", "")
                      for p in prompt_records["prompts"]}
project = json.loads((ROOT / "project.json").read_text(encoding="utf-8"))
project.update({
    "input_mode": "script", "language": "zh-Hant-HK; Cantonese spoken dialogue; English direction",
    "source_text": (ARCHIVE / "00_SCRIPT/Somewhere_Between_Us_Revised_Screenplay.txt").read_text(encoding="utf-8"),
    "high_level_idea": "Tart and Tine grow up together on a ranch in Victoria, Australia, take distinct adult paths as a guide dog and a visiting companion dog in Hong Kong, and reunite through earned coincidences at Victoria Harbour.",
    "duration_mode": "fixed", "total_duration_target": 1200, "aspect_ratio": "16:9",
    "production_stage": "asset_review_preparation", "source_pack_revision": "2026-10-14",
    "source_archive": "source/SOMEWHERE_BETWEEN_US_READY",
    "style": {
        "medium": "Warm stylized feature-quality 3D animation inspired by the visual warmth and expressive timing of Up, matching the supplied original masters",
        "palette": "Cream and warm earth in Victoria; teal, sage, coral and tactile wood in Hong Kong; bright afternoon harbour blues",
        "lighting": "Soft motivated daylight, dimensional faces and fur, tactile fabric and polished feature-animation materials",
        "constraints": ["Original supplied characters only; no existing Pixar characters", "Hong Kong Chinese human cast and local Cantonese performances", "No author credit, opening title, end title, subtitles, location/date cards, watermarks or credits", "No spoken dogs or narrator", "Normal-speed action, brisk comic timing, engaging suspense and short earned quiet reactions", "Multi-view sheets depict one identity; no split-screen sheets or annotations in movie frames"]
    },
    "render_intent": {"provider": "Seedance 2.5 via an authorized available route", "resolution": "1080p", "resolution_basis": "Proposed default for full-length feature animation; user can change during review", "generate_audio": True, "output_format": "mp4", "watermark": False, "submission_state": "not_submitted", "credentials": "Workspace .env: VOLC_ACCESS_KEY, VOLC_SECRET_KEY_RAW, VOLC_PROJECT_NAME, VOLC_ENDPOINT_SEEDANCE_25; values not read during preparation"},
    "user_constraints": ["NEW movie project dog-20261014", "Exactly 20 minutes", "Generally follow the well-written supplied screenplay; only necessary minor adaptations", "Use supplied assets and their guidance; add only essential missing assets", "Up-inspired look; original designs and predominantly Hong Kong Chinese characters", "No author, title or subtitle", "Fun and engaging; no dragged-out scenes"],
    "script_changes": [
        {"type": "explicit_user_override", "change": "Remove source opening TITLE and closing END TITLE from rendered content. No author credit or credit sequence."},
        {"type": "timing_only", "change": "Reconcile 16-scene story to exactly 1,200 seconds through variable action/dialogue units. Preserve every spoken Cantonese line verbatim."},
        {"type": "presentation", "change": "Keep source headings, authorship and production notes in the archival source only. In-world photograph captions and cafe lettering remain diegetic props, never subtitle overlays."}
    ],
    "continuity_bible": (ARCHIVE / "06_CONTINUITY/CONTINUITY_LOCK.txt").read_text(encoding="utf-8"),
    "critical_locks": ["Tine heart is on anatomical RIGHT rump; Tart has no heart marking", "No collar lead attached during Tart's harness work", "Ah Ming sits securely, removes harness fully, folds handle, THEN attaches brown collar lead", "Both slack leads remain separate and held during greeting and tug", "May holds Tine's orange lead clipped to collar, never bandanna", "Dogs recognise behaviour before the single canonical puppy print confirms their past", "Uncle Chan's wife/Ah Wong photograph is a separate physical image", "Ah Ming records and phones only stationary; headphones only seated editing", "Tine stays on public pavement outside MTR and ferry terminal", "Afternoon Star Ferry has practical lights off, passengers and crew; vehicles have drivers", "Three near misses escalate by minutes, wall/seconds, then passenger occlusion; no recognition until scene16", "Tine's decision to stay with Chan causes the changed meeting point and reunion"],
    "audio_plan": {"dialogue": "Original Cantonese, no translated dialogue or subtitles", "dogs": "Natural breath, paws, collar ticks, play sounds; never speak", "score": "Original light acoustic/orchestral score with comic rhythmic accents; restrained under dialogue, no triumphant score at crossing; final score resolves into live harbour", "recordings": "Exactly two fictional in-story clips at listening activity: tram/delivery trolley and earlier ferry ambience; no supplied voice recordings exist", "continuity": "Stable speaker voices, match live versus played-back sound, preserve native dialogue and foley in assembly"},
    "prompt_library": {"root": "workspace prompt-library", "read": ["README.md", "TEMPLATE.md"], "status": "Relevant performance/dialogue examples will be consulted when finalising prompts after approval"},
    "preparation_notes": ["All 72 supplied images are proposed unchanged; no new critical asset is currently missing", "Three supplied multi-panel staging images are planning guidance only and excluded from generation payloads", "Populated ferry/vehicle references are supplied masters; assign their geometry, vehicle, background cast and light roles explicitly", "Source generation prompts are provenance only and must not override this brief", "No final scene prompts, video jobs or external uploads before asset approval"],
})

assets, audit = [], []
for record in manifest["assets"]:
    file = record["file"]
    original = ARCHIVE / file
    assert sha(original) == record["sha256"], file
    with Image.open(original) as image:
        dimensions = list(image.size)
        image.verify()
    assert dimensions == record["dimensions"], file
    stem = Path(file).stem
    tag_name = TAG_OVERRIDES[stem]
    asset_id = "asset_" + re.sub(r"(?<!^)(?=[A-Z])", "_", tag_name).lower()
    candidate_id = asset_id.removeprefix("asset_") + "_ready01"
    target = ROOT / "assets" / asset_id / (candidate_id + ".png")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(original, target)
    category = ("character" if file.startswith("01_") else "environment" if file.startswith("02_")
                else "reference" if file.startswith("05_") else "prop")
    name = stem.replace("_", " ")
    is_guidance = file.startswith("05_")
    role = ("planning_guidance_only" if is_guidance else "vehicle_and_layout" if file.startswith("04_")
            else "identity_and_wardrobe" if category == "character" else "geography_and_light" if category == "environment" else "shape_material_state")
    description = name + ". Supplied finished visual master; preserve exact identity, material, layout and applicable state. "
    description += ("Read its choreography as planning guidance only. Do not include the multi-panel canvas in Seedance inputs."
                    if is_guidance else "Use only the view/state required by a shot; sheet backgrounds and repeated views must not appear as duplicated subjects.")
    asset = {"id": asset_id, "tag": "@" + tag_name, "name": name, "category": category,
             "description": description, "source": "supplied", "media_type": "Image", "status_variants": [],
             "reference_paths": [], "source_pack_file": file, "script_scenes": record["script_scenes"],
             "reference_role": role, "generation_eligible": not is_guidance,
             "candidates": [{"id": candidate_id, "path": target.relative_to(ROOT).as_posix(),
                              "prompt": generation_prompts.get(file, "Supplied canonical raster; no generation performed in this project."),
                              "source_revision": 0, "created_at": NOW, "source": "supplied",
                              "dimensions": dimensions, "sha256": sha(target), "freshness": "original supplied reference"}],
             "selected_candidate_id": candidate_id}
    assets.append(asset)
    audit.append({"tag": asset["tag"], "source_pack_file": file, "sha256": sha(target),
                  "manifest_hash_matches": True, "copied_bytes_match": sha(target) == sha(original),
                  "dimensions": dimensions, "image_decode": "passed", "visual_inspection": "pending"})
project["asset_list"] = assets

chapters, timeline, detailed = [], [], []
movie_time = 0
for scene in structure["scenes"]:
    scene_number = scene["number"]
    detailed.append(scene["heading"])
    covered = []
    for index, (duration, first, last, purpose) in enumerate(PLAN[scene_number], 1):
        source_blocks = [{**block, "source_block_index": n} for n, block in enumerate(scene["blocks"])
                         if first <= n <= last and not block["text"].startswith(("TITLE:", "END TITLE:"))]
        covered.extend(b["source_block_index"] for b in source_blocks)
        chapter_id = f"s{scene_number:02d}_c{index:02d}"
        linked = [a["id"] for a in assets if f"{scene_number:02d}" in a["script_scenes"] and a["generation_eligible"]]
        notes = [a["id"] for a in assets if f"{scene_number:02d}" in a["script_scenes"] and not a["generation_eligible"]]
        text = "\n\n".join((b.get("cue", "") + "\n" if b["type"] == "dialogue" else "") + b["text"] for b in source_blocks)
        chapter = {"id": chapter_id, "chapter_index": len(chapters) + 1, "source_scene": scene_number,
                   "title": purpose, "duration": duration, "absolute_start": movie_time,
                   "absolute_end": movie_time + duration, "high_level_idea": project["high_level_idea"],
                   "scene_summary": purpose, "pacing_reason": purpose + "; stage the complete causal action, speakable original lines and brief reaction at normal speed.",
                   "planning_source_blocks": source_blocks, "planning_text": text,
                   "planning_asset_ids": linked, "planning_guidance_ids": notes,
                   "prompt": "", "initial_prompt": "", "tagged_assets": [], "linked_asset_ids": [],
                   "delinked_asset_ids": [a["id"] for a in assets if not a["generation_eligible"]],
                   "shots": [], "materials": [], "storyboards": [], "selected_storyboard_id": None,
                   "takes": [], "active_take_id": None, "screenshots": [],
                   "prompt_status": "rough plan; final direction awaits asset approval"}
        chapters.append(chapter)
        timeline.append({"id": chapter_id, "source_scene": scene_number, "start": clock(movie_time),
                         "end": clock(movie_time + duration), "duration_seconds": duration, "purpose": purpose})
        detailed.extend([f"[{clock(movie_time)} - {clock(movie_time + duration)} | {chapter_id} | {duration}s]", text])
        movie_time += duration
    expected = [n for n, b in enumerate(scene["blocks"]) if not b["text"].startswith(("TITLE:", "END TITLE:")) and b["text"] != "END."]
    assert sorted(covered) == expected, (scene_number, covered, expected)
assert movie_time == 1200
project["chapters"] = chapters
project["detailed_script"] = "\n\n".join(detailed)
original_dialogue = [(s["number"], b["cue"], b["text"]) for s in structure["scenes"] for b in s["blocks"] if b["type"] == "dialogue"]
planned_dialogue = [(c["source_scene"], b["cue"], b["text"]) for c in chapters for b in c["planning_source_blocks"] if b["type"] == "dialogue"]
assert original_dialogue == planned_dialogue
assert "TITLE:" not in project["detailed_script"]
write_json(ROOT / "proposal.json", project)
write_json(ROOT / "exports/source-audit.json", {"source_pack": SOURCE.name, "checked_at": NOW,
            "copied_file_count": len(source_checks), "source_files": source_checks, "assets": audit,
            "asset_count": len(assets), "group_counts": dict(Counter(Path(a["source_pack_file"]).parts[0] for a in assets)),
            "dialogue_lines_preserved": len(original_dialogue), "timeline_seconds": movie_time,
            "chapter_count": len(chapters), "all_scene_blocks_covered": True, "credentials_read": False,
            "new_images_generated": 0, "provider_calls": 0})
write_json(ROOT / "exports/rough-timeline.json", timeline)
(ROOT / "exports/timed-screenplay.txt").write_text(project["detailed_script"] + "\n", encoding="utf-8")
timeline_md = ["# dog-20261014 - rough production timeline", "", "Exactly 20:00. Original 16 scenes and every Cantonese spoken line retained. Final shot direction awaits image approval.", "", "| Clip | Scene | Movie time | Seconds | Purpose |", "| --- | --- | --- | ---: | --- |"]
timeline_md.extend(f"| {r['id']} | {r['source_scene']:02d} | {r['start']}-{r['end']} | {r['duration_seconds']} | {r['purpose']} |" for r in timeline)
(ROOT / "exports/rough-timeline.md").write_text("\n".join(timeline_md) + "\n", encoding="utf-8")

review_dir = ROOT / "exports/asset-review"
review_dir.mkdir(parents=True, exist_ok=True)
font_path = Path("C:/Windows/Fonts/arial.ttf")
title_font = ImageFont.truetype(str(font_path), 30)
tag_font = ImageFont.truetype(str(font_path), 23)
id_font = ImageFont.truetype(str(font_path), 17)
groups = [("01_CHARACTERS", "Characters", 8), ("02_LOCATIONS", "Environments", 10),
          ("03_PROPS", "Main props", 9), ("04_VEHICLES", "Vehicles and ferry views", 7),
          ("05_STAGING", "Supplied choreography guidance - planning only", 3)]
gallery_index = ["# dog-20261014 - selected asset gallery", "", "All 72 supplied master images are proposed unchanged. Labels show stable tags and exact candidate IDs. Full-size links follow each sheet. The three choreography sheets are planning guidance only and will not be video inputs.", ""]
gallery = []
for group, title, per_page in groups:
    members = sorted([a for a in assets if a["source_pack_file"].startswith(group)], key=lambda a: a["tag"].lower())
    for page, offset in enumerate(range(0, len(members), per_page), 1):
        batch = members[offset:offset + per_page]
        cols = min(3, len(batch))
        cell_w, cell_h, top = 644, 434, 84
        rows = (len(batch) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * cell_w + 24, rows * cell_h + top + 20), "#f2eee6")
        draw = ImageDraw.Draw(sheet)
        draw.text((24, 22), f"{title} | {page} | candidate set ready01", font=title_font, fill="#202936")
        for n, asset in enumerate(batch):
            candidate = asset["candidates"][0]
            left, y = 12 + (n % cols) * cell_w, top + (n // cols) * cell_h
            image_box = (left + 10, y + 8, left + cell_w - 10, y + 360)
            draw.rounded_rectangle((left, y, left + cell_w - 8, y + cell_h - 12), radius=12, fill="white")
            with Image.open(ROOT / candidate["path"]) as image:
                preview = ImageOps.contain(image.convert("RGB"), (image_box[2] - image_box[0], image_box[3] - image_box[1]))
                sheet.paste(preview, (image_box[0] + (image_box[2] - image_box[0] - preview.width) // 2,
                                     image_box[1] + (image_box[3] - image_box[1] - preview.height) // 2))
            draw.text((left + 12, y + 365), asset["tag"], font=tag_font, fill="#153c51")
            draw.text((left + 12, y + 396), candidate["id"], font=id_font, fill="#465265")
        output = review_dir / f"{group.lower()}-{page:02d}.jpg"
        sheet.save(output, quality=94, subsampling=0)
        gallery.append({"group": title, "sheet": output.relative_to(ROOT).as_posix(), "asset_ids": [a["id"] for a in batch]})
        gallery_index.extend([f"## {title} - {page}", "", f"![{title} {page}]({output.as_posix()})", ""])
        gallery_index.extend(f"- **{a['name']}** - {a['tag']} - `{a['selected_candidate_id']}` - [full-size original](<{(ROOT / a['candidates'][0]['path']).as_posix()}>)" for a in batch)
        gallery_index.append("")
write_json(review_dir / "gallery.json", gallery)
(review_dir / "index.md").write_text("\n".join(gallery_index) + "\n", encoding="utf-8")
(ROOT / "STATUS.md").write_text("# dog-20261014\n\nPrepared for required asset review; no video generated yet.\n\nThe original pack is archived byte-for-byte. All 72 selected supplied images are registered as ready01 candidates. The 16-scene story is planned as 70 varied clips totalling exactly 1,200 seconds. Every original Cantonese dialogue line is retained. Opening/closing titles and author credits are omitted from the production script.\n\nThe proposed profile is native 1080p, 16:9 with generated audio. No credentials have been read and no provider jobs or uploads have been submitted. Final shot prompts await approval. The production session stays open across this required review.\n\nSee exports/asset-review/index.md for every selected image and full-size originals; exports/rough-timeline.md for the action-led timeline; exports/source-audit.json for copy/decode/dialogue evidence.\n", encoding="utf-8")
print(json.dumps({"source_files": len(source_checks), "assets": len(assets), "chapters": len(chapters),
                  "duration_seconds": movie_time, "dialogue_lines_preserved": len(original_dialogue),
                  "gallery_sheets": len(gallery), "proposal": str(ROOT / "proposal.json")}, indent=2))
