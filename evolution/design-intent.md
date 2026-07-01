# Design Intent — pipa rev A

- Master CAD: `cad/pipa.scad` (sha256: 14f7828ba85a6ef2289ac46218108eb5fbfe69b31b87e5e8688e69a2e1debd6a) — source-only scaffold. Current flat fabrication-authority artifact is `cad/v2-dxf-starter.dxf`; design-table inventory is `family-spec.csv` (sha256: 7ae0c919876f02fed33ac1201a0ae1a5c315bcfcce4d5064324f56a76f414244).
- Function: Image-grounded pipa-inspired prototype — a pear/teardrop-front, short-neck, four-string plucked lute chordophone. Four strings run from a provisional bridge zone over placeholder fret bands to the pegbox; body is a resonating carved shell (rear depth and bracing not yet specified). Packet is for layout review, drawing iteration, measurement planning, and a first flat silhouette mule only.
- Environment: indoor plucked instrument; carved wooden body responds to humidity. String pull is a sustained structural load once real geometry exists. This packet does NOT claim that one angled reference photo can determine final CNC geometry.
- Target qty: 1 (prototype). Deadline: TBD. Budget/unit ceiling: TBD.

## Critical dimensions (carry tolerances)

| Feature | Nominal | Tolerance | Why critical | Source |
| --- | --- | --- | --- | --- |
| Nut-to-bridge scale length | TBD | measured on reference member | intonation / fret schedule primary input | measurement-intake.csv MEAS-004 (missing, blocks L3) |
| Fret count + placement | TBD | reference-member documented | fret authority / playability | measurement-intake.csv MEAS-006 (missing, blocks L3) |
| Body max width + station | TBD | measured lower bout | outline authority (replaces starter DXF) | measurement-intake.csv MEAS-002 (missing, blocks L3) |
| Overall length | ~720 mm (scaffold placeholder) | measured, not photo-scaled | outline authority | pipa.scad placeholder / MEAS-001 (missing) |
| String spacing at nut + bridge | TBD | measured string centers | playability | measurement-intake.csv MEAS-005 (missing, blocks L3) |
| Soundboard thickness + bracing | TBD | measured or reviewed luthier drawing | structure vs. tone | measurement-intake.csv MEAS-008 (missing, blocks L3) |
| Bridge footprint + height | TBD | measured contact patch/saddle | intonation / structure | measurement-intake.csv MEAS-007 (missing, blocks L3) |

## Incidental (free for DFM)

- Front silhouette styling within reviewed outline envelope, cosmetic finish, non-mating decorative surfaces.

## Must-nots (DFM may never violate)

- Do not treat `cad/pipa.scad` placeholder parameters as fabrication authority (risks.md — converts placeholders into false authority).
- Do not cut frets from the placeholder bands — requires measured scale length + temperament review (risks.md, MEAS-004/006).
- Do not scale final body outline from the single angled reference photo (risks.md).
- Keep Wolfram work source-only until executed with measured scale input and committed outputs (risks.md mitigations).
- Rear-shell depth / soundboard structure absent — not inferable from the front starter DXF.

## Material intent

- Prototype: 3 mm MDF/plywood/acrylic flat mule; spruce/cedar/paulownia soundboard test panel; hardwood neck and bridge mockups per bom.csv. Dimensions provisional.
- Acceptable subs: per sourcing.csv (spec-first; live prices unverified).
- Forbidden: none recorded.

## Stage status

Stage 0 intake complete 2026-07-01. Gate A (Alpha shop compile) NOT yet run — no concessions logged, nothing presented as shippable. L3/L4 promotion blocked until measurement-intake.csv rows are filled from a measured or reviewed reference member.
