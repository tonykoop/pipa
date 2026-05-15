# Pipa Image-Grounded Prototype Packet

Status: L2 prototype scaffold, not CNC-ready final geometry.

This packet promotes the Round 8 pipa exploration into a repo-tracked,
DXF-first prototype packet for issue #151. It is intentionally useful for
layout review, visual planning, sourcing, and first measurement work, while
refusing to claim that one angled reference photo can determine final CNC
geometry.

Fabrication authority starts with `cad/v2-dxf-starter.dxf` and any later
measured templates or reviewed CAD. Generated concept images and photo-derived
sketches are support material only; they do not control outline, fret location,
bridge placement, pegbox side profile, rear shell depth, or toolpaths.

## File Map

| File | Purpose |
| --- | --- |
| `design.md` | Visible/inferred/unresolved geometry split and prototype intent. |
| `cad/v2-dxf-starter.dxf` | DXF-first starter layout for review and tracing. |
| `cad-notes.md` | CAD handoff notes, layer intent, and unresolved surfaces. |
| `bom.csv` | Prototype material and hardware planning list. |
| `sourcing.csv` | Search terms and source expectations. |
| `cut-list.csv` | Flat-mule-only cut planning rows. |
| `drawing-brief.md` | Shop drawing brief and non-claims. |
| `visual-bom-brief.md` | Visual BOM plan with authority warnings. |
| `assembly-manual.md` | Flat silhouette mule assembly/review workflow. |
| `supplier-rfq.md` | Measurement-first vendor and reviewer request. |
| `risks.md` | Fabrication and evidence risks. |
| `wolfram-starter.wl` | Measurement notebook starter. |
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

## Explicit Non-Claims

- Not a CNC-ready pipa body.
- Not a final fret or intonation schedule.
- Not a verified rear-shell carve or bowl-depth model.
- Not a source for pegbox side-profile angle.
- Not a substitute for measured reference-member review.
