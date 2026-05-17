# MCP Session Log

Status: V5 provenance starter for the pipa packet. This log records known
packet-local tool/provenance facts and preserves unknowns instead of turning
them into authority claims.

| artifact_id | pipeline | tool_and_version | input_authority | operator_action | output_path | authority_result | validation_evidence | unresolved_assumption |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DXF-001 | historical_cad_handoff | unknown Round 8 toolchain | private_round8_reference_photo_not_in_repo | Promoted existing starter DXF named by issue handoff | `cad/v2-dxf-starter.dxf` | fabrication | not_yet_validated | Original `/tmp` sources were not present in this checkout; DXF remains flat-review only. |
| DXF-002 | manual_repo_migration | cp file copy | DXF-001 | Copied starter DXF into V5 `drawings/` path for migration review | `drawings/pipa-v5-starter.dxf` | fabrication | byte/geometry comparison pending | Must stay synchronized with DXF-001 or document divergence. |
| CAD-SCAD-001 | openscad_scaffold | Codex text authoring; OpenSCAD runtime not used | FAMILY-001; MEAS-INTAKE pending | Added source-only parametric scaffold with placeholder dimensions | `cad/pipa.scad` | reference_only | not_yet_validated | No OpenSCAD MCP/runtime execution happened in this lane; measurement is still required before fabrication authority. |
| WLFRET-001 | wolfram_source | Codex text authoring; Wolfram runtime not used | MEAS-004 pending | Added source-only fret/scale study and missing-measurement gate | `wolfram/fret-scale-study.wl` | reference_only | source_only_no_runtime | No Wolfram execution happened in this lane; measurement and runtime logs are required before fret authority. |
| IMG-PROMPT-001 | ai_image_gen_prompt | prompt text only | DXF-001 | Preserved non-dimensional concept-image prompt constraints | `concept-image-prompt-brief.md` | concept_only | prompt review pending | No image generation happened in this lane. |
