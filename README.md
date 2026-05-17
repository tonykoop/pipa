# Pipa Starter Packet

Status: bare-bones readiness packet.

This repository is an L1 starter packet for a Chinese pipa design and build
study. It records the current assumptions, provenance, validation gates, and
CAD/DXF authority plan before any build-ready body, fret, bridge, or tooling
dimensions are claimed.

## Current Authority

- Readiness: L1 starter only.
- Build readiness: not build-ready.
- Fabrication authority: future measured CAD/DXF or design table, not this
  README or any study note.
- CAD/DXF status: future authority unless measured geometry is added and
  reviewed.
- Sourcing status: unverified until checked at purchase time.
- Measurement status: `measurement-required` for dimensions that affect scale,
  fret placement, bridge placement, soundboard response, body fit, string
  tension, or ergonomics.

## File Map

| File | Purpose |
| --- | --- |
| `design.md` | Pipa intent, assumptions, provenance, unknowns, and authority notes. |
| `family-spec.csv` | Lute-family starter row for string courses, scale, fret plan, bridge, soundboard, body shell, and dimension provenance. |
| `bom.csv` | Starter materials and components with readiness and source status. |
| `sourcing.csv` | Search and supplier placeholders without current purchase claims. |
| `cut-list.csv` | Candidate blanks, coupons, and templates with `TBD` dimensions. |
| `validation-loop.csv` | Scale, fret, bridge, tension, soundboard, and tuning gates. |
| `drawing-brief.md` | CAD/DXF authority plan and promotion requirements. |
| `wolfram-study.md` | Wolfram evidence for 12-TET fret study math. |
| `wolfram-study.wl` | Diffable Wolfram source for the fret-position study. |
| `risks.md` | Starter acoustic, fabrication, sourcing, and scope risks. |

## Next Gates

1. Measure or choose a physical reference pipa before adopting final body,
   scale, bridge, fret, or bowl geometry.
2. Promote a DXF/CAD/design-table artifact as fabrication authority only after
   the measured scale and fret plan are reviewed.
3. Verify string set gauges, tuning, and bridge placement with a tension
   calculation and a physical setup test.
4. Build and record soundboard/bridge response tests before claiming tone or
   structural readiness.
5. Update BOM and sourcing rows after current supplier verification.

## Provenance Snapshot

The packet uses published pipa descriptions as reference inputs only. The
B.C. Chinese Music Association describes the pipa as a pear-shaped four-string
lute with a fretboard in the 20 to 25 fret range:
https://www.bccma.net/instruments/pipa/

The Wolfram study uses the 725 mm effective string length and 30-fret modern
pipa model reported in Ningxin Zhang, "Using a Waveguide to Model the Pipa in
Csound":
https://csound.com/icsc2022/proceedings/Using%20a%20Waveguide%20to%20Model%20the%20Pipa%20in%20Csound.pdf

These references do not make this repository build-ready.
