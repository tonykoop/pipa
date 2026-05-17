# CAD/DXF Authority Plan

Current status: future CAD/DXF authority. No drawing in this repository is
build-ready yet.

## Authority Rule

Fabrication dimensions must be controlled by measured CAD, DXF, design tables,
or explicitly reviewed drawings. Prose, concept art, rendered previews, and the
Wolfram fret study do not control fabrication.

## Planned Drawing Set

| Drawing ID | Planned path | Authority target | Blocks | Required evidence |
| --- | --- | --- | --- | --- |
| DXF-001 | `drawings/pipa-scale-fret-layout.dxf` | Fret and scale fabrication geometry | Fret template cutting | Measured scale length, fret datum, fret count, fret height plan, review against `validation-loop.csv` V001 and V002 |
| DXF-002 | `drawings/pipa-body-outline.dxf` | Body outline and rim template | Body template cutting | Measured body outline or scan, neck/body datum, ergonomic review |
| CAD-001 | `cad/pipa-body-shell.*` | Body bowl/back shell reference | Shell forming or carving | Measured outer and inner profiles, wall thickness plan, process review |
| DT-001 | `design-table-scale-frets.csv` | Numeric source for DXF-001 | Derived previews and inspection | Measured scale length, selected temperament, compensation notes |
| PDF-001 | `drawings/pipa-packet-review.pdf` | Review drawing only until promoted | Human review | Derived from DXF/CAD/design table and marked with authority status |

## Promotion Checklist

- `family-spec.csv` dimension provenance is updated from
  `measurement_required` only when measured values exist.
- `validation-loop.csv` rows V001 through V003 include evidence paths and pass
  status.
- DXF files use a documented unit system and layer naming convention before
  shop use.
- Any preview or image-gen artifact is registered as concept-only or derived
  from a named authority artifact.
- The README names the current governing CAD/DXF/design table before any build
  packet claims are made.

## Current Non-Authority Artifacts

- `wolfram-study.md` and `wolfram-study.wl` are study artifacts only.
- `family-spec.csv` is a planning row only.
- `cut-list.csv` records candidate templates and coupons with `TBD`
  dimensions.
