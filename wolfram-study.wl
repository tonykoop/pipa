(* Pipa L1 fret-position study.
   This uses a published 725 mm effective string length as a study input only.
   It is not fabrication authority. *)

scaleLengthMm = 725.;
maxSemitone = 30;

fretRows = Prepend[
  Table[
    {
      n,
      NumberForm[scaleLengthMm*(1 - 2^(-n/12)), {7, 2}],
      NumberForm[scaleLengthMm*2^(-n/12), {7, 2}]
    },
    {n, 0, maxSemitone}
  ],
  {"semitone", "from_nut_mm", "remaining_scale_mm"}
];

Print[StringRiffle[Map[StringRiffle[ToString /@ #, ","] &, fretRows], "\n"]]
