# Pipa Image-Grounded Prototype Design Notes

## Intent

Create an attractive, reviewable pipa-inspired prototype packet from the Round 8
image-grounded exploration while keeping the fabrication authority honest. The
deliverable should let a maker, CAD modeler, or reviewer see the proposed front
layout and next measurements without mistaking inferred photo geometry for final
instrument dimensions.

Readiness: L2 V5 build-packet candidate. Use for concept review, drawing
iteration, measurement planning, source-only fret/scale modeling, and first flat
silhouette mule only. L3/L4 promotion is blocked until measured or reviewed
authority exists for critical geometry.

## Provenance

`tonykoop/pipa#1` carries prior `tonykoop/instrument-maker#151` context and
cites these Round 8 sources as the promotion basis:

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
| Pear/teardrop front silhouette | Captured as a symmetric DXF starter outline for scale and tracing review. | L2 prototype DXF only; replace or approve from measured template before L3. |
| Neck centerline and body centerline | Included as registration lines. | L2 prototype DXF only. |
| Four-string path | Included as visual/string-layout reference lines. | L2 prototype DXF only; not final string spacing. |
| Bridge block location | Marked as provisional. | Requires measured scale length and reference pipa review. |
| Fret positions | Shown as placeholders only. | Unresolved; requires scale, temperament, action, and reference review. |
| Soundboard thickness and bracing | Not specified. | Requires luthier/CAD review and material testing. |
| Rear shell depth and carve | Explicitly omitted. | Requires side/rear references or measured object. |
| Pegbox side profile and break angle | Explicitly omitted. | Requires side photo or measured object. |
| Finish/inlay direction | Suitable for concept imagery. | Concept only, not fabrication authority. |

## DXF Starter Scope

`cad/v2-dxf-starter.dxf` and `drawings/pipa-v5-starter.dxf` are the same 2D
front-layout starter with separate layers for:

- `AUTH_OUTLINE`: reviewable prototype body/neck outline.
- `REFERENCE_CENTERLINES`: center and registration geometry.
- `PROVISIONAL_STRINGS`: visual string paths.
- `PROVISIONAL_BRIDGE`: bridge planning block.
- `UNRESOLVED_FRETS`: placeholder fret bands that must not be cut as final.

The DXF deliberately avoids rear shell contours, pegbox side elevation, final
fret spacing, and tooling details.

## V5 Authority Chain

| Artifact | Current authority | Promotion blocker |
| --- | --- | --- |
| `source-media-evidence.csv` | Source availability and assumption-control register. | Needs recovered private source pointers or replacement reviewed references. |
| `fret-scale-evidence.csv` | Fret/scale/bridge evidence gate; no geometry authority yet. | Needs measured scale length, fret set, string spacing, bridge datum, and reviewed model. |
| `cad-dxf-authority-plan.md` | CAD/DXF revision plan and no-go list. | Needs completed measurement/source rows before final CAD revision. |
| `family-spec.csv` | Single-instrument inventory and unknown list. | Needs measured scale length, body stations, and reference review rows. |
| `cad/pipa.scad` | Source-only parametric scaffold for review. | Needs dimensions loaded from measured template or design table before fabrication. |
| `cad/v2-dxf-starter.dxf` | Flat outline review geometry only. | Needs CAD import check and measured-template comparison. |
| `drawings/pipa-v5-starter.dxf` | V5 drawings-path copy of the starter DXF. | Same blockers as `cad/v2-dxf-starter.dxf`. |
| `wolfram/fret-scale-study.wl` | Source-only fret/scale equations and missing-measurement gate. | Needs Wolfram execution and measured scale input before fret claims. |
| Generated or refined images | Concept-only communication. | Cannot promote to fabrication authority. |

## Next Measurements

Before advancing beyond a flat mule, capture:

- full-length front orthographic reference or measured outline template;
- body maximum width, waist location, and lower/upper bout transitions;
- nut-to-bridge string length and bridge footprint;
- fret count, fret heights, and fret placement basis;
- neck width at nut/body join and string spacing;
- pegbox side profile, tuner/peg geometry, and break angle;
- rear shell depth map or cross-sections at lower, waist, and upper stations.
