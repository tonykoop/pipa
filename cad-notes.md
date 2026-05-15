# CAD Notes

## Authority Boundary

The starter DXF is the only fabrication-authority artifact in this packet, and
only for prototype front-layout review. It is not a final cut file. Any CAD
model built from it must preserve the unresolved flags for fret geometry, rear
shell, and pegbox side profile until measured or reference-reviewed evidence is
added.

## Layer Contract

| Layer | Meaning | Shop Use |
| --- | --- | --- |
| `AUTH_OUTLINE` | Prototype outline curves and neck rectangle. | Trace/review flat silhouette only. |
| `REFERENCE_CENTERLINES` | Registration and body station lines. | Alignment aid; do not cut as features. |
| `PROVISIONAL_STRINGS` | Four visual string paths. | Visual planning only. |
| `PROVISIONAL_BRIDGE` | Candidate bridge block footprint. | Locate during mockup; verify before cutting. |
| `UNRESOLVED_FRETS` | Placeholder fret bands. | Do not cut; measurement required. |
| `TEXT_NOTES` | Embedded caution labels. | Documentation only. |

## CAD Follow-Up

1. Import `cad/v2-dxf-starter.dxf` into CAD in millimeters.
2. Lock `REFERENCE_CENTERLINES`, `PROVISIONAL_STRINGS`, and `UNRESOLVED_FRETS`.
3. Trace or replace `AUTH_OUTLINE` from a measured front template.
4. Add side and rear elevations only after measured references are available.
5. Generate shop drawings with revision notes naming the measurement source.

