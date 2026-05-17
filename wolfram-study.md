# Wolfram Fret Study

Status: study evidence only, not fabrication authority.

`wolframscript` was available at `/usr/bin/wolframscript` during this pass.
The command below was run from the repo root to compute 12-TET fret positions
from a published 725 mm effective string length:

```sh
wolframscript -code 'l=725.; rows=Table[{n,NumberForm[l*(1-2^(-n/12)),{7,2}],NumberForm[l*2^(-n/12),{7,2}]},{n,0,24}]; Print[StringRiffle[Prepend[Map[StringRiffle[ToString /@ #, ","]&,rows],"semitone,from_nut_mm,remaining_scale_mm"],"\n"]]'
```

The output was:

```csv
semitone,from_nut_mm,remaining_scale_mm
0,0.00,725.00
1,40.69,684.31
2,79.10,645.90
3,115.35,609.65
4,149.57,575.43
5,181.86,543.14
6,212.35,512.65
7,241.12,483.88
8,268.28,456.72
9,293.91,431.09
10,318.11,406.89
11,340.94,384.06
12,362.50,362.50
13,382.85,342.15
14,402.05,322.95
15,420.18,304.82
16,437.28,287.72
17,453.43,271.57
18,468.67,256.33
19,483.06,241.94
20,496.64,228.36
21,509.46,215.54
22,521.55,203.45
23,532.97,192.03
24,543.75,181.25
```

## Formula

For semitone `n` on a 12-TET string of scale length `L`:

- Distance from nut: `L * (1 - 2^(-n/12))`
- Remaining speaking length: `L * 2^(-n/12)`

## Use Boundary

This table is useful for checking the math path that a future
`design-table-scale-frets.csv` can use. It does not account for final pipa
fret height, bridge compensation, string stiffness, player setup, or measured
reference-instrument deviations.
