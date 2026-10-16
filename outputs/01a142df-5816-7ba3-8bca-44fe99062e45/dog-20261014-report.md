# dog-20261014 generation and cost report

Report date: 16 October 2026. Project revision: 57. Scope: recorded Seedance video generation for this project.

| Metric | Result |
|---|---:|
| Planned generation segments | 70 |
| Screenplay scenes / planned camera shots | 16 / 169 |
| Final timeline | 20:00 (1,200 seconds) |
| Model | Dreamina Seedance 2.5 (`dreamina-seedance-2-5-260628`) |
| Native video format | 480p, 854×480, 16:9, 24 fps |
| Segment durations | 8–24 seconds |
| Total API requests | 96 |
| Accepted provider tasks | 94 |
| Successful returned videos | 91 |
| Failed after acceptance | 3 |
| Rejected before generation | 2 |
| Selected video sources | 70 |
| Successful superseded videos | 21 |
| Successful output duration, before selection | 26:04 (1,564 nominal seconds) |
| Requested duration across all requests | 27:36 (1,656 seconds, including requests that failed) |
| Returned completion tokens | 15,062,518 |
| Estimated Seedance cost (USD) | US$161.16894260 |
| Estimated Seedance cost (HKD) | HK$1,264.69 |
| Unresolved charge attempts | 0 |

The ledger and the full take history match on all 96 unique attempt IDs. All 91 successful source files exist and their recorded verification is 854×480 at 24 fps. Every planned segment has a selected source.

## What “successful” means

A successful API request returned a video. Some returned videos still needed revisions for dialogue, character identity, guide-dog handling, staging or continuity. The report therefore shows both requests to the first API success and all requests used to reach the selected final take.

| Requests per segment, including rejections | Number of segments |
|---:|---:|
| 1 | 51 |
| 2 | 14 |
| 3 | 3 |
| 4 | 2 |

68 segments returned a video on their first request. s04_c06 first succeeded on request 2. s12_c02 first succeeded on request 4. A total of 51 segments used just one request through final selection; 19 segments had multiple requests.

## Cost calculation

Estimated USD = returned completion_tokens × US$10.70 / 1,000,000. This uses the published no-video-input rate. All requests used image references, with zero reference-video seconds. Still images extracted from prior clips remain image input.

Estimated HKD = estimated USD × 7.847. The conversion uses the [YCharts ECB-derived USD/HKD value for 15 October 2026](https://ycharts.com/indicators/us_dollar_to_hong_kong_dollar_exchange_rate), checked on 16 October 2026.

The [BytePlus pricing page](https://docs.byteplus.com/id/docs/modelark/model-pricing?redirect=1) lists the rate and states that unsuccessful video generations are not charged. The five confirmed failed/rejected requests are therefore estimated at zero. The successful replaced takes remain included.

Selected video sources account for US$123.65979300 (HK$970.36). Superseded successful videos account for US$37.50914960 (HK$294.33).

These are usage-based list-price estimates. The account invoice, discounts, credits, taxes and card exchange fees were not available. Image generation and Codex subscription costs are outside this Seedance video total.

## All planned segments

Model and native format above apply to every row. Duration is the planned timeline / nominal generated duration for one take. “Videos” counts successful outputs only. “First success” is the request number that first returned a video. “HKD” includes every successful take for that segment, including superseded takes.

| # | Segment | Description | Duration (s) | Requests | Videos | Failed / rejected | First success | Selected take | Est. HKD |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|
| 1 | s01_c01 | Bench puzzle and Tine's stuck-bottom gag | 16 | 1 | 1 | 0/0 | 1 | take_01 | 12.94 |
| 2 | s01_c02 | Two squeaks, contrasting bows, accidental sit and sharing | 16 | 1 | 1 | 0/0 | 1 | take_01 | 12.94 |
| 3 | s01_c03 | Brisk run and wet-paw reaction | 14 | 1 | 1 | 0/0 | 1 | take_01 | 11.33 |
| 4 | s01_c04 | Rain, failed dry spot, cuddle and canonical photograph | 18 | 1 | 1 | 0/0 | 1 | take_01 | 14.55 |
| 5 | s01_c05 | Months later: contact, separate crates and departures | 21 | 1 | 1 | 0/0 | 1 | take_01 | 16.97 |
| 6 | s02_c01 | Tart learns to clear a route for two bodies | 18 | 1 | 1 | 0/0 | 1 | take_01 | 14.55 |
| 7 | s02_c02 | Tine learns to respect a withdrawn hand | 16 | 1 | 1 | 0/0 | 1 | take_01 | 12.94 |
| 8 | s02_c03 | Ah Ming and May introductions; chin-on-knee compromise | 18 | 4 | 3 | 1/0 | 1 | take_04 | 43.66 |
| 9 | s02_c04 | May receives the same print; young-to-adult paw match | 8 | 1 | 1 | 0/0 | 1 | take_01 | 6.49 |
| 10 | s03_c01 | Touch-led morning routine, harness excitement and work cue | 20 | 2 | 2 | 0/0 | 1 | take_02 | 32.33 |
| 11 | s03_c02 | Neighbour trolley clears the lift | 14 | 2 | 2 | 0/0 | 1 | take_02 | 22.65 |
| 12 | s03_c03 | Stationary tram recording interrupted by delivery trolley | 18 | 2 | 2 | 0/0 | 1 | take_02 | 29.11 |
| 13 | s03_c04 | Stationary reply and breakfast anticipation | 18 | 2 | 2 | 0/0 | 1 | take_02 | 29.11 |
| 14 | s04_c01 | Match footsteps across two jobs; both complete a task | 18 | 2 | 2 | 0/0 | 1 | take_02 | 29.11 |
| 15 | s04_c02 | Suitcase clearance matched to Lok's peekaboo | 16 | 2 | 2 | 0/0 | 1 | take_02 | 25.88 |
| 16 | s04_c03 | Toast and crumb temptation, restraint and untidy leg | 14 | 1 | 1 | 0/0 | 1 | take_01 | 11.33 |
| 17 | s04_c04 | Cafe name mix-up, payment and clear departure | 19 | 2 | 2 | 0/0 | 1 | take_02 | 30.72 |
| 18 | s04_c05 | Minutes-later takeaway and first missed encounter | 15 | 1 | 1 | 0/0 | 1 | take_01 | 12.13 |
| 19 | s04_c06 | Route opens; invited touch; newspaper foreshadowing | 8 | 3 | 2 | 0/1 | 2 | take_03 | 12.97 |
| 20 | s05_c01 | Establish van hazard; cue, refusal and creeping wheel | 16 | 1 | 1 | 0/0 | 1 | take_01 | 12.94 |
| 21 | s05_c02 | Pedestrian confirms hazard; van clears; choose next phase | 20 | 1 | 1 | 0/0 | 1 | take_01 | 16.17 |
| 22 | s05_c03 | Fresh signal, complete crossing and shoulder-rub payoff | 19 | 1 | 1 | 0/0 | 1 | take_01 | 15.36 |
| 23 | s06_c01 | Refusal respected; Tine chooses mat and rest | 18 | 1 | 1 | 0/0 | 1 | take_01 | 14.55 |
| 24 | s06_c02 | Fallen flyer tests Tine's restraint without intrusion | 16 | 1 | 1 | 0/0 | 1 | take_01 | 12.94 |
| 25 | s06_c03 | Rest-as-work exchange, funny name and open hand | 22 | 1 | 1 | 0/0 | 1 | take_01 | 17.78 |
| 26 | s06_c04 | Invitation, shoulder contact and reluctant goodbye | 24 | 1 | 1 | 0/0 | 1 | take_01 | 19.39 |
| 27 | s07_c01 | Harness off, whole-body shake and impatient toy delivery | 13 | 1 | 1 | 0/0 | 1 | take_01 | 10.52 |
| 28 | s07_c02 | Knee-switch squeak and determined tug | 17 | 1 | 1 | 0/0 | 1 | take_01 | 13.75 |
| 29 | s07_c03 | Cushion collision, laugh and returned toy | 15 | 2 | 2 | 0/0 | 1 | take_02 | 24.27 |
| 30 | s07_c04 | Seated editing and quiet dog-to-foot contact | 10 | 1 | 1 | 0/0 | 1 | take_01 | 8.10 |
| 31 | s08_c01 | Establish public routes and wall occlusion | 16 | 1 | 1 | 0/0 | 1 | take_01 | 12.94 |
| 32 | s08_c02 | Ear response, fleeting cream coat and second near miss | 14 | 2 | 2 | 0/0 | 1 | take_02 | 22.65 |
| 33 | s08_c03 | Unopened newspaper and two umbrella-stand clangs | 16 | 1 | 1 | 0/0 | 1 | take_01 | 12.94 |
| 34 | s08_c04 | Chan calls Tine; exuberance eases into careful approach | 14 | 1 | 1 | 0/0 | 1 | take_01 | 11.33 |
| 35 | s09_c01 | Remembered touch; puppy print appears and is put away | 18 | 1 | 1 | 0/0 | 1 | take_01_crop02 | 14.55 |
| 36 | s09_c02 | Offer-withdraw toy gag resolves with a squeak and bow | 16 | 1 | 1 | 0/0 | 1 | take_01 | 12.94 |
| 37 | s09_c03 | Lok asks, waits, strokes and withdraws | 16 | 1 | 1 | 0/0 | 1 | take_01 | 12.94 |
| 38 | s09_c04 | Separate old photograph, slipper joke and towel memory | 24 | 1 | 1 | 0/0 | 1 | take_01 | 19.39 |
| 39 | s09_c05 | Harbour invitation leaves Chan an independent choice | 11 | 1 | 1 | 0/0 | 1 | take_01 | 8.91 |
| 40 | s10_c01 | Listening game: tram, trolley and one-ear reaction | 21 | 1 | 1 | 0/0 | 1 | take_01 | 16.97 |
| 41 | s10_c02 | Ferry recording connects to Chan's former work | 15 | 1 | 1 | 0/0 | 1 | take_01 | 12.13 |
| 42 | s10_c03 | Home-toy joke opens into the harbour invitation | 18 | 1 | 1 | 0/0 | 1 | take_01 | 14.55 |
| 43 | s10_c04 | Brief chosen pause; Tine matters; Chan signs up | 22 | 1 | 1 | 0/0 | 1 | take_01 | 17.78 |
| 44 | s10_c05 | Agree ferry arrival and meeting point; sleeping-paw button | 14 | 1 | 1 | 0/0 | 1 | take_01 | 11.33 |
| 45 | s11_c01 | Independent evening: kettle, hat, packed bag and phone | 24 | 1 | 1 | 0/0 | 1 | take_01 | 19.39 |
| 46 | s11_c02 | Saturday match on hat; Tine waits for Chan to settle | 21 | 1 | 1 | 0/0 | 1 | take_01 | 16.97 |
| 47 | s12_c01 | 13:00 group check, bowl clip and short public walking route | 15 | 1 | 1 | 0/0 | 1 | take_01 | 12.13 |
| 48 | s12_c02 | Afternoon ferry child asks and offers a morning greeting | 22 | 4 | 1 | 2/1 | 4 | take_04 | 17.78 |
| 49 | s12_c03 | One eye opens; leaf temptation returns to Chan's pace | 13 | 1 | 1 | 0/0 | 1 | take_01 | 10.52 |
| 50 | s12_c04 | Moored-ferry call, phone packed, cue and disembarkation | 20 | 1 | 1 | 0/0 | 1 | take_01 | 16.17 |
| 51 | s13_c01 | Public forecourt routes bring both dogs into one frame | 13 | 2 | 2 | 0/0 | 1 | take_02_mix01 | 21.04 |
| 52 | s13_c02 | Suitcase gap, tentative step and interrupted safe route | 17 | 1 | 1 | 0/0 | 1 | take_01 | 13.75 |
| 53 | s13_c03 | Group turns inland; Tart clears route east; third near miss | 17 | 1 | 1 | 0/0 | 1 | take_01 | 13.75 |
| 54 | s13_c04 | Water break carries the cut into the seating bay | 8 | 1 | 1 | 0/0 | 1 | take_01 | 6.49 |
| 55 | s14_c01 | Shake anticipation, one drop, tissue and exaggerated wipe | 18 | 1 | 1 | 0/0 | 1 | take_01 | 14.55 |
| 56 | s14_c02 | Horn changes Chan's expression; Tine turns back; May listens | 22 | 2 | 2 | 0/0 | 1 | take_02 | 35.56 |
| 57 | s14_c03 | Shoulder in reach and group chooses to remain | 12 | 2 | 2 | 0/0 | 1 | take_02 | 19.43 |
| 58 | s14_c04 | Stationary call relocates meeting; open hand ends the beat | 23 | 1 | 1 | 0/0 | 1 | take_01 | 18.59 |
| 59 | s15_c01 | Stationary phone away and guided return | 12 | 1 | 1 | 0/0 | 1 | take_01 | 9.71 |
| 60 | s15_c02 | Narrow entrance, spoken help and suitcase clearance | 22 | 3 | 3 | 0/0 | 1 | take_03 | 53.34 |
| 61 | s15_c03 | First sensory contact; task comes first; secure seating | 22 | 1 | 1 | 0/0 | 1 | take_01 | 17.78 |
| 62 | s15_c04 | Harness fully off, then brown lead clipped; off-duty shake | 19 | 1 | 1 | 0/0 | 1 | take_01 | 15.36 |
| 63 | s16_c01 | Permission, curved approach and reciprocal sniffing | 18 | 1 | 1 | 0/0 | 1 | take_01 | 14.55 |
| 64 | s16_c02 | Tine waits; squeak invites Tart to the free toy end | 16 | 2 | 2 | 0/0 | 1 | take_02 | 25.88 |
| 65 | s16_c03 | Accidental sit, returned toy, matching bows and ear gag | 20 | 1 | 1 | 0/0 | 1 | take_01 | 16.17 |
| 66 | s16_c04 | Humans hear generosity; keep dogs playing underneath | 15 | 1 | 1 | 0/0 | 1 | take_01 | 12.13 |
| 67 | s16_c05 | May connects names, same print and Victoria origin | 24 | 3 | 3 | 0/0 | 1 | take_03 | 58.18 |
| 68 | s16_c06 | Describe puppy pose to Ah Ming; confirmation after behaviour | 20 | 1 | 1 | 0/0 | 1 | take_01 | 16.17 |
| 69 | s16_c07 | Chan chooses longer rest and makes room for family | 13 | 2 | 2 | 0/0 | 1 | take_02 | 21.04 |
| 70 | s16_c08 | Offer room, settle into puppy pose; live harbour and brief fade | 24 | 1 | 1 | 0/0 | 1 | take_01 | 19.39 |

Per-row amounts are shown to cents. The total is calculated from unrounded amounts, so displayed cents can have a small rounding difference.

## Revision notes

| Segment | Reason / local edit |
|---|---|
| s02_c03 | Guide lead and floor staging revised. Take 03 failed output-audio policy. |
| s03_c01 | Cantonese dialogue alignment revised. |
| s03_c02 | Cantonese dialogue alignment revised. |
| s03_c03 | Guide-handle continuity revised. |
| s03_c04 | Guide-handle continuity revised. |
| s04_c01 | Guide control and visiting-dog floor staging revised. |
| s04_c02 | Guide control and visiting-dog floor staging revised. |
| s04_c04 | Cafe departure staging and Cantonese dialogue revised. |
| s04_c06 | Input privacy rejection, then guide-control revision. |
| s07_c03 | Evening lighting continuity revised. |
| s08_c02 | Walking direction and location continuity revised. |
| s09_c01 | Local crop removes duplicate child. One Seedance output, no added generation fee. |
| s12_c02 | One input privacy rejection and two output-video policy failures; take 04 succeeded. |
| s13_c01 | Dogs separated across forecourt. Local ambience replacement after take 02. |
| s14_c02 | May character identity revised. |
| s14_c03 | Dog floor staging revised. |
| s15_c02 | Open-air planter-gap geography revised twice. |
| s16_c02 | Dogs on floor, lead ownership and toy invitation revised. |
| s16_c05 | Dogs on floor and reunion coverage revised twice. |
| s16_c07 | Character identity and group seating coverage revised. |

The selected local edits are s09_c01 take_01_crop02 (one generated source) and s13_c01 take_02_mix01 (two generated sources for that segment). These edits do not count as new Seedance generations. An unused crop trial and final assembly exports are also excluded from API request counts.

## Failed and rejected requests

| Segment | Take | Result | Provider code | Est. HKD |
|---|---|---|---|---:|
| s02_c03 | take_03 | failed | OutputAudioSensitiveContentDetected.PolicyViolation | 0.00 |
| s04_c06 | take_01 | rejected | InputImageSensitiveContentDetected.PrivacyInformation | 0.00 |
| s12_c02 | take_01 | rejected | InputImageSensitiveContentDetected.PrivacyInformation | 0.00 |
| s12_c02 | take_02 | failed | OutputVideoSensitiveContentDetected.PolicyViolation | 0.00 |
| s12_c02 | take_03 | failed | OutputVideoSensitiveContentDetected.PolicyViolation | 0.00 |

## Evidence and timing

Sources: canonical project revision 57, usage.json, exports/task-journal.json including all prior_takes, exports/assembly-settings.json, selected local-edit records, exports/verification.json and the production-session usage report. The accompanying workbook includes all 96 attempt IDs and 94 provider task IDs for reconciliation.

Production session: 14 October 2026 19:32:52 to 15 October 2026 14:45:23 Hong Kong time. Elapsed time: 19 hours 12 minutes 31 seconds, including preparation, queues, review and approval waits. It is not model processing time.
