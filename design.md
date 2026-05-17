# Design Notes

## Project Identity

- Project name: Pipa starter packet.
- Instrument family: plucked lute, pipa-style pear-shaped four-string lute.
- Intended build method: measurement-led CAD/DXF study followed by shop packet
  only after validation.
- Current status: bare-bones readiness packet.
- Build readiness: not build-ready.

## Design Intent

Create a first honest pipa packet that can grow into a measured build package.
The near-term goal is not to publish a cut-ready instrument. The useful first
step is to define the evidence chain for body geometry, scale length, fret
placement, bridge location, string tension, and soundboard response.

## Known Inputs

| Input | Value | Provenance | Status |
| --- | --- | --- | --- |
| Instrument type | Four-string pear-shaped plucked lute | B.C. Chinese Music Association pipa overview | reference-only |
| Reference fret count | 20 to 25 frets in general pipa overview; 30 frets in one physical-modeling paper | BCCMA overview and Zhang 2022 Csound paper | reference-only |
| Reference scale length | 725 mm effective string length | Zhang 2022 Csound paper | reference-only, not build authority |
| Reference tuning | A2 D3 E3 A3 | Zhang 2022 Csound paper | reference-only |
| Soundboard/body material | Published references commonly describe a wooden pear-shaped instrument; project material selection remains open | Published references plus maker review needed | measurement-required |
| Fabrication process | CAD/DXF layout after measurement | Sprint assignment and instrument-maker visual authority rule | assumption |

## Current Assumptions

- The starter packet treats the pipa as four single string courses, not paired
  courses.
- The scale and fret study starts from a 725 mm reference length only to test
  math and file shape.
- Equal-tempered fret positions are a CAD study baseline. A real pipa layout
  may need instrument-specific fret heights, compensation, and measured
  placement.
- Bridge placement cannot be finalized from nominal scale length alone.
- Body bowl, back thickness, soundboard thickness, brace pattern, and bridge
  footprint are all `measurement-required`.

## Open Measurements

| Measurement | Why it matters | Owner/source | Status |
| --- | --- | --- | --- |
| Nut-to-bridge scale length on target reference | Controls every fret and bridge datum | Physical reference pipa or measured drawing | measurement-required |
| Nut, bridge, and saddle compensation geometry | Controls intonation and CAD datum stack | Setup measurement and player review | measurement-required |
| Fret count, fret heights, fret material, and fret crown locations | Controls playability and pitch accuracy | Reference pipa measurement | measurement-required |
| Soundboard outline, thickness, brace layout, and bridge footprint | Controls structural response and tone | Measurement plus tap/deflection test | measurement-required |
| Body bowl outer profile, inner cavity, rim, and neck joint | Controls ergonomics, resonance, and manufacturability | 3D scan, templates, or measured drawings | measurement-required |
| String gauges and target tensions | Controls top loading and feel | Verified string set and tension model | measurement-required |

## CAD/DXF Authority Notes

- Future fabrication authority must be a measured DXF/CAD/design-table artifact
  named in `drawing-brief.md`.
- The current Wolfram fret table is study evidence only. It does not set final
  fret, bridge, nut, or body dimensions.
- Any generated images or rendered previews are concept-only unless derived
  from the governing DXF/CAD/design table.

## Promotion Notes

Promote this repo beyond L1 only after `validation-loop.csv` has a pass path for
scale/fret verification, bridge placement, string tension, soundboard response,
tuning, sourcing, and CAD authority. Until then, all dimensions that affect
tuning, machining, fit, or structure remain `measurement-required`.
