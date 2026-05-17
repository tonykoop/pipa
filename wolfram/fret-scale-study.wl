(* Pipa V5 fret/scale study.
   Readiness: L2 source-only. Do not claim runtime validation unless this file
   is executed and outputs are committed with an execution log. *)

packet = "pipa-image-grounded-prototype";
readiness = "L2 V5 build-packet candidate";
measurementSource = "../measurement-intake.csv";

requiredInputs = <|
  "scaleLengthMm" -> "MEAS-004 nut_to_bridge scale length",
  "fretCount" -> "MEAS-006 fret count from reference member",
  "temperament" -> "reviewed pipa fret model or documented approximation",
  "actionCompensation" -> "measured or luthier-reviewed compensation"
|>;

Clear[fretPositionEqualTemperament];
fretPositionEqualTemperament[scaleLengthMm_, fretNumber_] :=
  scaleLengthMm*(1 - 2^(-fretNumber/12));

sourceOnlyNotice[] := Print[
  packet <> ": source-only fret/scale study. Fill MEAS-004 and MEAS-006 before exporting fret tables."
];

exampleBlockedTable[] := Dataset[{
  <|"fret" -> 1, "status" -> "blocked_pending_MEAS-004", "position_mm" -> Missing["NotMeasured"]|>,
  <|"fret" -> 2, "status" -> "blocked_pending_MEAS-004", "position_mm" -> Missing["NotMeasured"]|>,
  <|"fret" -> 3, "status" -> "blocked_pending_MEAS-004", "position_mm" -> Missing["NotMeasured"]|>
}];

sourceOnlyNotice[];
exampleBlockedTable[];
