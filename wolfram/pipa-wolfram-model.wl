(* ============================================================
   PIPA — Wolfram Interactive Model (deployable)
   instrument-maker V5 | image-grounded prototype

   Status: L2 SOURCE-ONLY. Every fret position below is an
   EQUAL-TEMPERAMENT ESTIMATE from the scale length only —
   real pipa fret placement requires measured scale length
   (MEAS-004), measured fret count (MEAS-006), and luthier
   compensation. Do NOT claim runtime validation without an
   execution log.

   This file RETURNS a Manipulate (SaveDefinitions->True) so it
   can be CloudDeploy'd as a public interactive explorer.
   ============================================================ *)

(* ─── Parametric core (estimate-only) ───────────────────────── *)

Clear[fretPositionEqualTemperamentEstimate];
(* Distance from nut to fret n, equal temperament. EMPIRICAL placement —
   ignores action/compensation. *)
fretPositionEqualTemperamentEstimate[scaleLengthMm_, fretNumber_] :=
  scaleLengthMm*(1 - 2^(-fretNumber/12));

Clear[fretTableEstimate];
fretTableEstimate[scaleLengthMm_, fretCount_] :=
  Table[
    {n,
     fretPositionEqualTemperamentEstimate[scaleLengthMm, n],
     scaleLengthMm - fretPositionEqualTemperamentEstimate[scaleLengthMm, n]},
    {n, 1, fretCount}
  ];

(* ─── Interactive explorer (the deployable return value) ────── *)

Manipulate[
  Module[{tbl, neck},
    tbl = fretTableEstimate[scaleLengthMm, fretCount];
    neck = Graphics[
      {
       {GrayLevel[0.85], Rectangle[{0, -1}, {scaleLengthMm, 1}]},
       {Red, Thickness[0.004],
        Line[{{#, -1}, {#, 1}}] & /@ (fretPositionEqualTemperamentEstimate[scaleLengthMm, #] & /@ Range[fretCount])},
       {Black, Thickness[0.006], Line[{{0, -1}, {0, 1}}]}   (* nut *)
      },
      PlotRange -> {{-10, scaleLengthMm + 10}, {-1.5, 1.5}},
      AspectRatio -> 0.18, ImageSize -> 560,
      PlotLabel -> "Pipa fretboard — EQUAL-TEMPERAMENT ESTIMATE (not measured)"
    ];
    Column[{
      neck,
      Style["Fret positions are estimates from scale length only. "
        <> "Verify MEAS-004 (scale length) and MEAS-006 (fret count) before cutting.",
        Italic, Darker[Red]],
      Grid[
        Prepend[
          Map[{#[[1]], NumberForm[#[[2]], {6, 1}], NumberForm[#[[3]], {6, 1}]} &, tbl],
          {"Fret", "From nut (mm)", "From bridge (mm)"}
        ],
        Frame -> All, Background -> {None, {LightGray}}
      ]
    }, Center]
  ],
  {{scaleLengthMm, 730, "scale length (mm) — ESTIMATE"}, 600, 800, 5},
  {{fretCount, 24, "fret count — ESTIMATE"}, 12, 31, 1},
  ControlPlacement -> Left,
  SaveDefinitions -> True
]
