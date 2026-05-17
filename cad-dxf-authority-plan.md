# CAD/DXF Authority Plan

Status: B3 additive plan for issue #1. This file is a review and gating plan,
not a claim that final pipa geometry has been measured.

## Authority Split

| Evidence class | Examples | Current role | Can control fabrication now? | Promotion requirement |
| --- | --- | --- | --- | --- |
| Historical/reference assumptions | Round 8 photo notes, missing `/tmp` handoffs, pipa-like visual features | Preserve context and guide what to measure next | No | Recover source media or replace with reviewed references, then record source ids. |
| Repo-tracked L2 DXF | `cad/v2-dxf-starter.dxf`, `drawings/pipa-v5-starter.dxf` | Flat silhouette and layout review | Yes, but only for flat mule review | CAD import check, measured-template comparison, and revision notes. |
| Source-only CAD/notebook files | `cad/pipa.scad`, `wolfram/fret-scale-study.wl` | Parametric and math scaffolds | No | Fill measured inputs, run tools, commit execution/export evidence. |
| Measured or reviewed authority | Physical pipa measurements, reviewed orthographic plan, design table | Future fabrication basis | Not present yet | Tie every final dimension to measurement ids and reviewer/date. |
| Concept imagery | `concept-image-prompt-brief.md`, future generated images | Communication and visual BOM support | No | Keep non-dimensional and outside toolpath authority chain. |

## CAD/DXF Revision Path

| Step | Artifact | Required evidence | Output | No-go condition |
| --- | --- | --- | --- | --- |
| 1 | `cad/v2-dxf-starter.dxf` | CAD import in millimeters plus layer-name review | L2 import note or screenshot reference in `validation-loop.csv` | Units or layers cannot be confirmed. |
| 2 | `source-media-evidence.csv` | Recovered private source pointer or replacement reviewed reference | Source ids for visual facts and missing assumptions | Source media remains unavailable or cannot be cited privately. |
| 3 | `measurement-intake.csv` | Overall length, body stations, scale length, bridge, fret, string-spacing rows | Measured-value rows with source ids | Measurements conflict without a selected reference basis. |
| 4 | `fret-scale-evidence.csv` | MEAS-004, MEAS-005, MEAS-006, MEAS-007 | Approved fret/scale input package | Fret model is still generic or unreviewed. |
| 5 | `wolfram/fret-scale-study.wl` | Completed input package and chosen fret model | Runtime log and exported draft fret table | Wolfram was not run or output lacks source ids. |
| 6 | `cad/pipa.scad` and DXF | Measured outline template and approved fret/bridge schedule | Revised CAD/DXF with explicit revision notes | Any final geometry traces only to generated image or angled photo. |
| 7 | `drawings/pipa-v5-starter.dxf` | Synchronized CAD-path DXF revision | Drawings-path review copy | Drawings copy diverges from CAD source without a logged reason. |

## Layer Plan

| Layer | Keep in L2? | Future action | Authority note |
| --- | --- | --- | --- |
| `AUTH_OUTLINE` | Yes | Replace from measured front template or reviewed plan. | Current outline controls flat review only. |
| `REFERENCE_CENTERLINES` | Yes | Retain as datum geometry after source datum is selected. | Alignment aid, not a cut feature by itself. |
| `PROVISIONAL_STRINGS` | Yes | Replace with measured nut and bridge string spacing. | Visual planning only. |
| `PROVISIONAL_BRIDGE` | Yes | Replace after MEAS-004 and MEAS-007 agree. | Do not route, glue, or drill from this block. |
| `UNRESOLVED_FRETS` | Yes | Replace or move to warning layer after approved schedule exists. | No permanent fret cutting from this layer. |
| `TEXT_NOTES` | Yes | Preserve readiness and no-cut warnings on review exports. | Documentation layer. |

## Reference Assumptions To Preserve But Not Fabricate From

| Assumption | Why useful | Why not authoritative |
| --- | --- | --- |
| Pear-shaped pipa front silhouette | Guides outline review and source-photo search. | Perspective and scale are not measured. |
| Four-string layout | Matches visible/planned instrument class. | String spacing and gauges are unresolved. |
| Fret markers visible in reference | Confirms fret evidence is required. | Count, height, station, and temperament are not established. |
| Bridge appears on soundboard | Guides measurement checklist. | Bridge footprint, height, and active scale datum are missing. |
| Short neck and pegbox direction | Guides side-photo shotlist. | Side profile and break angle are absent. |

## Release Gate

The packet can remain an L2 V5 build-packet candidate with the current DXF
starter and these evidence tables. It must not be described as CNC-ready,
intonation-validated, or final-fret-ready until the measured/reviewed authority
rows in `measurement-intake.csv`, `source-media-evidence.csv`, and
`fret-scale-evidence.csv` have matching source ids and validation evidence.
