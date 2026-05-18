# Pipa Image-Grounded Prototype Packet

Status: L2 V5 build-packet candidate.

This packet promotes the Round 8 pipa exploration into a repo-tracked,
DXF-first V5 candidate packet for `tonykoop/pipa#1`, carrying prior
`tonykoop/instrument-maker#151` context. It is intentionally useful for
layout review, visual planning, sourcing, Wolfram source-first fret/scale
study, and first measurement work, while refusing to claim that one angled
reference photo can determine final CNC geometry.

Fabrication authority starts with `cad/v2-dxf-starter.dxf`,
`drawings/pipa-v5-starter.dxf`, and any later measured templates or reviewed
CAD. The current DXF authority is limited to flat outline review. Generated
concept images, prompt text, and photo-derived sketches are support material
only; they do not control outline, fret location, bridge placement, pegbox side
profile, rear shell depth, or toolpaths.

Open `explorer.html` for a studio-facing showcase of the packet evidence,
DXF/CAD authority boundary, Wolfram source files, print packet, and validation
gates. `site/index.html` redirects to the same explorer until a fuller public
build-log site is ready.

## File Map

| File | Purpose |
| --- | --- |
| `explorer.html` | Generated studio explorer for packet review. |
| `explorer-sections/` | Local explorer section overrides for pipa authority and evidence gates. |
| `site/index.html` | Minimal cross-link to the root explorer; not a full public site. |
| `design.md` | Visible/inferred/unresolved geometry split and prototype intent. |
| `source-media-evidence.csv` | Source-media availability and reference-assumption authority table. |
| `fret-scale-evidence.csv` | Fret, scale, bridge, string-spacing evidence gates and blocked claims. |
| `cad-dxf-authority-plan.md` | CAD/DXF revision plan separating assumptions from fabrication authority. |
| `family-spec.csv` | Single-instrument family/spec equivalent for V5 packet inventory. |
| `measurement-intake.csv` | Measurement checklist that blocks L3/L4 promotion until complete. |
| `validation-loop.csv` | Empirical validation loop scaffold for future build feedback. |
| `cad/v2-dxf-starter.dxf` | DXF-first starter layout for review and tracing. |
| `drawings/pipa-v5-starter.dxf` | V5 drawings-path copy of the starter DXF for migration review. |
| `cad/pipa.scad` | Source-only OpenSCAD scaffold with unresolved dimensions flagged. |
| `cad/mcp-session-log.md` | V5 provenance log for packet, CAD, visual, and runtime-tool outputs. |
| `cad-notes.md` | CAD handoff notes, layer intent, and unresolved surfaces. |
| `bom.csv` | Prototype material and hardware planning list. |
| `sourcing.csv` | Search terms and source expectations. |
| `cut-list.csv` | Flat-mule-only cut planning rows. |
| `drawing-brief.md` | Shop drawing brief and non-claims. |
| `photo-shotlist.md` | Reference and shop-photo intake list. |
| `visual-bom-brief.md` | Visual BOM plan with authority warnings. |
| `assembly-manual.md` | Flat silhouette mule assembly/review workflow. |
| `supplier-rfq.md` | Measurement-first vendor and reviewer request. |
| `risks.md` | Fabrication and evidence risks. |
| `wolfram-starter.wl` | Measurement notebook starter. |
| `wolfram/fret-scale-study.wl` | Source-only fret/scale study; no runtime claim yet. |
| `validation.csv` | Measurement, drawing, and prototype validation gates. |
| `visual-output-register.csv` | Fabrication-authority and concept-image separation. |
| `concept-image-prompt-brief.md` | Image-gen prompt constraints for non-authoritative visuals. |
| `capstone-deck.md` | Markdown review deck stub. |
| `print-packet.md` / `print-packet.html` | Printable review packet. |
| `capstone-manifest.json` | Machine-readable packet manifest. |

## First Build Recommendation

Start with a flat acrylic, MDF, or plywood silhouette mule from the DXF starter,
then overlay full-scale prints against the original reference photo and a real
pipa or published reference measurements before generating any carved body,
rear shell, pegbox side profile, or final fret layout.

## B3 Evidence Gate

Use `source-media-evidence.csv` to decide which reference facts are available,
private, missing, or future validation evidence. Use `fret-scale-evidence.csv`
before changing any fret, scale, bridge, or string-spacing geometry. Use
`cad-dxf-authority-plan.md` as the CAD/DXF promotion checklist; it keeps the
historical pipa-reference assumptions separate from the repo-tracked L2 DXF
and future measured fabrication authority.

## Explicit Non-Claims

- Not a CNC-ready pipa body.
- Not a final fret or intonation schedule.
- Not a verified rear-shell carve or bowl-depth model.
- Not a source for pegbox side-profile angle.
- Not a substitute for measured reference-member review.
- Not a Wolfram-runtime-validated model; the `.wl` files are source-only until
  an execution log and exported results are committed.
