# Risks

## Evidence Risks

- Round 8 source files were named by issue #151 but were not available in this
  checkout, so the repo packet preserves provenance without embedding private
  or missing media.
- A single angled photo can distort outline, fret spacing, bridge placement,
  and pegbox angle.

## Fabrication Risks

- Cutting frets from the placeholder bands would produce a misleading or
  unplayable instrument.
- Treating `cad/pipa.scad` as fabrication CAD before measurement intake would
  convert placeholder parameters into false authority.
- Rear-shell depth and soundboard structure are absent and cannot be inferred
  from the front starter DXF.
- Pegbox side profile and string break angle are unresolved.

## Mitigations

- Keep the packet at L2 V5 build-packet candidate readiness.
- Validate the visual authority register before publishing concept imagery.
- Keep Wolfram work source-only until the study is executed with measured scale
  input and committed outputs.
- Require measured reference-member review before advancing to CNC-ready CAD.
