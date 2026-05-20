#!/usr/bin/env python3
"""Pipa fret-schedule generator (L2 review-only).

Readiness: L2 V5 build-packet candidate. This script reproduces the
equal-temperament formula in `wolfram/fret-scale-study.wl` and writes a
CSV that can be inspected before any fabrication step. Fret positions are
*not* authority until `MEAS-004` (nut-to-bridge scale length) and
`MEAS-006` (fret count from a reference member) are recorded in
`measurement-intake.csv` with a non-empty `current_value`. Pipa fretting
in practice often deviates from strict 12-TET; this generator is a
review aid, not a luthier specification.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INTAKE = ROOT / "measurement-intake.csv"
DEFAULT_OUT = ROOT / "fret-schedule.csv"
EXPLORATION_OUT = ROOT / "fret-schedule-exploration.csv"

SCALE_MEAS_ID = "MEAS-004"
FRET_COUNT_MEAS_ID = "MEAS-006"


def fret_position_mm(scale_length_mm: float, fret_number: int) -> float:
    """Equal-temperament fret station from the nut, in millimetres."""
    return scale_length_mm * (1 - 2 ** (-fret_number / 12))


def load_intake(path: Path) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    with path.open(newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            mid = (row.get("measurement_id") or "").strip()
            if mid:
                rows[mid] = row
    return rows


def _parse_float(value: str) -> float | None:
    value = (value or "").strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def _parse_int(value: str) -> int | None:
    value = (value or "").strip()
    if not value:
        return None
    try:
        return int(float(value))
    except ValueError:
        return None


def resolve_inputs(intake: dict[str, dict[str, str]]) -> tuple[float | None, int | None, list[str]]:
    blockers: list[str] = []
    scale_row = intake.get(SCALE_MEAS_ID)
    fret_row = intake.get(FRET_COUNT_MEAS_ID)
    if scale_row is None:
        blockers.append(f"{SCALE_MEAS_ID}: missing row in measurement-intake.csv")
    if fret_row is None:
        blockers.append(f"{FRET_COUNT_MEAS_ID}: missing row in measurement-intake.csv")

    scale = _parse_float(scale_row.get("current_value", "")) if scale_row else None
    fret_count = _parse_int(fret_row.get("current_value", "")) if fret_row else None

    if scale_row is not None and scale is None:
        blockers.append(f"{SCALE_MEAS_ID}: current_value empty — measure nut-to-bridge scale length")
    if fret_row is not None and fret_count is None:
        blockers.append(f"{FRET_COUNT_MEAS_ID}: current_value empty — record fret count from reference member")
    return scale, fret_count, blockers


def schedule_rows(scale_mm: float, fret_count: int, label: str, status: str) -> Iterable[dict[str, str]]:
    for n in range(1, fret_count + 1):
        yield {
            "fret": str(n),
            "scale_length_mm": f"{scale_mm:.3f}",
            "position_from_nut_mm": f"{fret_position_mm(scale_mm, n):.3f}",
            "status": status,
            "source": label,
        }


def blocked_rows(blockers: list[str], placeholder_count: int = 12) -> Iterable[dict[str, str]]:
    reason = "blocked_pending_" + "+".join(b.split(":")[0] for b in blockers)
    for n in range(1, placeholder_count + 1):
        yield {
            "fret": str(n),
            "scale_length_mm": "",
            "position_from_nut_mm": "",
            "status": reason,
            "source": "measurement-intake.csv",
        }


def write_csv(path: Path, rows: Iterable[dict[str, str]]) -> int:
    fieldnames = ["fret", "scale_length_mm", "position_from_nut_mm", "status", "source"]
    materialised = list(rows)
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(materialised)
    return len(materialised)


def cmd_check(args: argparse.Namespace) -> int:
    intake = load_intake(args.intake)
    scale, fret_count, blockers = resolve_inputs(intake)
    print(f"intake: {args.intake}")
    print(f"{SCALE_MEAS_ID}: {scale!r}")
    print(f"{FRET_COUNT_MEAS_ID}: {fret_count!r}")
    if blockers:
        print("blockers:")
        for b in blockers:
            print(f"  - {b}")
    # Spot-check the formula against the wolfram study.
    sample_scale = 690.0
    f12 = fret_position_mm(sample_scale, 12)
    expected = sample_scale / 2.0
    if abs(f12 - expected) > 1e-6:
        print(f"FAIL: fret 12 at scale {sample_scale} = {f12}, expected {expected}")
        return 1
    print(f"formula self-check: fret 12 @ scale {sample_scale} mm = {f12:.3f} mm (expected {expected})")
    return 0


def cmd_emit(args: argparse.Namespace) -> int:
    intake = load_intake(args.intake)
    scale, fret_count, blockers = resolve_inputs(intake)
    if blockers and not args.allow_blocked:
        count = write_csv(args.out, blocked_rows(blockers))
        print(f"wrote {count} blocked rows to {args.out}")
        for b in blockers:
            print(f"  blocker: {b}")
        return 0
    assert scale is not None and fret_count is not None
    count = write_csv(args.out, schedule_rows(scale, fret_count, label=str(args.intake), status="derived_from_measured"))
    print(f"wrote {count} rows to {args.out}")
    return 0


def cmd_explore(args: argparse.Namespace) -> int:
    scales = [float(s) for s in args.scales.split(",") if s.strip()]
    fret_count = args.fret_count
    rows: list[dict[str, str]] = []
    for scale in scales:
        rows.extend(schedule_rows(
            scale,
            fret_count,
            label=f"exploration:{scale:.1f}mm",
            status="exploration_not_authority",
        ))
    count = write_csv(args.out, rows)
    print(f"wrote {count} exploration rows ({len(scales)} scales x {fret_count} frets) to {args.out}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--intake", type=Path, default=DEFAULT_INTAKE,
                        help="measurement-intake.csv path")
    sub = parser.add_subparsers(dest="cmd", required=False)

    p_check = sub.add_parser("check", help="Resolve MEAS-004/006 and report blockers")
    p_check.set_defaults(func=cmd_check)

    p_emit = sub.add_parser("emit", help="Write fret-schedule.csv from measured inputs")
    p_emit.add_argument("--out", type=Path, default=DEFAULT_OUT)
    p_emit.add_argument("--allow-blocked", action="store_true",
                        help="Fail if blockers are present (default: write a blocked CSV instead)")
    p_emit.set_defaults(func=cmd_emit)

    p_explore = sub.add_parser("explore", help="Write deterministic exploration CSV at given scales")
    p_explore.add_argument("--scales", default="660,690,720",
                           help="Comma-separated scale lengths in mm")
    p_explore.add_argument("--fret-count", type=int, default=24)
    p_explore.add_argument("--out", type=Path, default=EXPLORATION_OUT)
    p_explore.set_defaults(func=cmd_explore)

    args = parser.parse_args(argv)
    if not getattr(args, "func", None):
        # Default action: run check.
        return cmd_check(args)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
