# Drawing Brief

## Drawing Set

Produce a review drawing set from `cad/v2-dxf-starter.dxf` with these sheets:

1. Front outline and centerline registration.
2. Provisional bridge and string-path overlay.
3. Unresolved fret-zone overlay with warning labels.
4. Measurement request sheet for rear shell, pegbox side profile, bridge, and
   fret schedule.

## Required Notes On Every Sheet

- L2 prototype scaffold; not final CNC geometry.
- DXF controls only front-layout review geometry.
- Generated images are concept-only and cannot supply dimensions.
- Rear shell, pegbox side profile, final bridge placement, and final fret
  geometry require measured reference review.

## Drawing Dependencies

Do not create side elevation, carved shell section, final neck section, or fret
coordinate table until the validation gates in `validation.csv` move from
pending to reviewed.

