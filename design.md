# Pipa Image-Grounded Prototype Design Notes

## Intent

Create an attractive, reviewable pipa-inspired prototype packet from the Round 8
image-grounded exploration while keeping the fabrication authority honest. The
deliverable should let a maker, CAD modeler, or reviewer see the proposed front
layout and next measurements without mistaking inferred photo geometry for final
instrument dimensions.

Readiness: L2 prototype scaffold. Use for concept review, drawing iteration,
measurement planning, and first flat silhouette mule only.

## Provenance

Issue #151 cites these Round 8 sources as the promotion basis:

- `/tmp/twingrid-r8-gpt55-dan-pipa/build_packet.md`
- `/tmp/twingrid-r8-gpt55-dan-pipa/image_access_preflight.md`
- `/tmp/twingrid-r8-gpt55-dan-pipa/v2-visual-output-pipeline.md`
- `/tmp/twingrid-r8-gpt54-dan-pipa/cad/v2-dxf-starter.dxf`

Those `/tmp` sources were not present in this checkout during promotion, so
this repo packet records the issue contract and keeps all photo-derived claims
as provisional until the source image or a measured reference member is reviewed.

## Geometry Classification

| Feature | Packet Treatment | Authority |
| --- | --- | --- |
| Pear/teardrop front silhouette | Captured as a symmetric DXF starter outline for scale and tracing review. | Prototype DXF only. |
| Neck centerline and body centerline | Included as registration lines. | Prototype DXF only. |
| Four-string path | Included as visual/string-layout reference lines. | Prototype DXF only; not final string spacing. |
| Bridge block location | Marked as provisional. | Requires measured scale length and reference pipa review. |
| Fret positions | Shown as placeholders only. | Unresolved; requires scale, temperament, action, and reference review. |
| Soundboard thickness and bracing | Not specified. | Requires luthier/CAD review and material testing. |
| Rear shell depth and carve | Explicitly omitted. | Requires side/rear references or measured object. |
| Pegbox side profile and break angle | Explicitly omitted. | Requires side photo or measured object. |
| Finish/inlay direction | Suitable for concept imagery. | Concept only, not fabrication authority. |

## DXF Starter Scope

`cad/v2-dxf-starter.dxf` is a 2D front-layout starter with separate layers for:

- `AUTH_OUTLINE`: reviewable prototype body/neck outline.
- `REFERENCE_CENTERLINES`: center and registration geometry.
- `PROVISIONAL_STRINGS`: visual string paths.
- `PROVISIONAL_BRIDGE`: bridge planning block.
- `UNRESOLVED_FRETS`: placeholder fret bands that must not be cut as final.

The DXF deliberately avoids rear shell contours, pegbox side elevation, final
fret spacing, and tooling details.

## Next Measurements

Before advancing beyond a flat mule, capture:

- full-length front orthographic reference or measured outline template;
- body maximum width, waist location, and lower/upper bout transitions;
- nut-to-bridge string length and bridge footprint;
- fret count, fret heights, and fret placement basis;
- neck width at nut/body join and string spacing;
- pegbox side profile, tuner/peg geometry, and break angle;
- rear shell depth map or cross-sections at lower, waist, and upper stations.

