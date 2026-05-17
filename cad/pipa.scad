// Pipa V5 source-only CAD scaffold.
// Readiness: L2 V5 build-packet candidate.
// This file is not fabrication geometry until parameters are replaced with
// measured-template, design-table, or reviewed-drawing values.

packet_readiness = "L2 V5 build-packet candidate";
units = "mm";

// Placeholder review parameters. Replace from measurement-intake.csv before
// treating any output as fabrication authority.
overall_length_mm = 720;
body_length_mm = 470;
body_max_width_mm = 240;
neck_length_mm = overall_length_mm - body_length_mm;
neck_width_mm = 48;
review_thickness_mm = 3;

module unresolved_label_block() {
  // Text is intentionally part of the CAD source so preview exports carry the
  // L2-only warning.
  translate([-body_max_width_mm / 2, -40, review_thickness_mm])
    linear_extrude(0.4)
      text("L2 review scaffold - measure before fabrication", size = 8);
}

module body_outline_review_plate() {
  scale([body_max_width_mm / 2, body_length_mm / 2, 1])
    circle(r = 1, $fn = 96);
}

module neck_review_plate() {
  translate([-neck_width_mm / 2, body_length_mm / 2 - 5, 0])
    square([neck_width_mm, neck_length_mm + 5], center = false);
}

module centerline_reference() {
  translate([-0.5, -body_length_mm / 2, review_thickness_mm])
    cube([1, overall_length_mm, 0.5], center = false);
}

module pipa_l2_review_scaffold() {
  union() {
    linear_extrude(review_thickness_mm)
      union() {
        body_outline_review_plate();
        neck_review_plate();
      }
    centerline_reference();
    unresolved_label_block();
  }
}

pipa_l2_review_scaffold();
