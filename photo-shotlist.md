# Photo Shotlist

Status: L2 V5 build-packet candidate support. Photos are evidence or
communication artifacts only; they do not become fabrication authority unless
they are tied to measured dimensions or reviewed CAD/DXF records.

| shot_id | subject | purpose | authority | required_before_l3 | notes |
| --- | --- | --- | --- | --- | --- |
| PHOTO-001 | Full-front orthographic reference pipa | Replace starter outline with measured template | reference_only until scaled from measured dimensions | yes | Avoid angled or perspective-heavy shots for final outline. |
| PHOTO-002 | Side profile and pegbox | Capture break angle and pegbox geometry | reference_only until measured | yes | Needed before pegbox fabrication. |
| PHOTO-003 | Rear shell cross-section or depth stations | Capture carved body depth | reference_only until measured | yes | Can be physical depth-gauge photos or reviewed drawing. |
| PHOTO-004 | Bridge close-up with ruler/calipers | Support bridge footprint measurement | measured_template when paired with measurement log | yes | Include source id matching `measurement-intake.csv`. |
| PHOTO-005 | Fret board close-up with scale | Support fret count and station measurement | measured_template when paired with measurement log | yes | Blocks final fret schedule until complete. |
| PHOTO-006 | Flat silhouette mule overlay | Validate DXF review outline | validation_evidence | no | Use after first print/cut, not as final geometry. |
| PHOTO-007 | Concept render or visual BOM image | Communicate prototype intent | concept_only | no | Must have a `visual-output-register.csv` row. |
