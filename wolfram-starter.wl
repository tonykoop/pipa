(* Pipa image-grounded prototype measurement starter.
   This notebook is a placeholder for measured-reference review, not a
   source of final fret locations. *)

packet = "pipa-image-grounded-prototype";
readiness = "L2 V5 build-packet candidate";

requiredMeasurements = {
  "overall_length_mm",
  "body_max_width_mm",
  "waist_station_mm",
  "nut_to_bridge_mm",
  "bridge_footprint_mm",
  "neck_width_nut_mm",
  "neck_width_body_join_mm",
  "pegbox_break_angle_deg",
  "rear_shell_depth_stations_mm"
};

Print[packet <> ": collect measured reference values before fret or CNC claims."];
Print["Run wolfram/fret-scale-study.wl only after measured scale length is available."];
