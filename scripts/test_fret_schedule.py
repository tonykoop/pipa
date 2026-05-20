#!/usr/bin/env python3
"""Offline checks for fret_schedule.py. Run: python scripts/test_fret_schedule.py"""

from __future__ import annotations

import csv
import io
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import fret_schedule as fs  # noqa: E402


def check(condition: bool, message: str) -> None:
    if not condition:
        print(f"FAIL: {message}")
        sys.exit(1)
    print(f"ok: {message}")


def test_fret_12_is_half_scale() -> None:
    scale = 690.0
    position = fs.fret_position_mm(scale, 12)
    check(abs(position - scale / 2) < 1e-9, f"fret 12 @ {scale}mm = {position} ≈ {scale/2}")


def test_fret_24_is_quarter_scale() -> None:
    scale = 720.0
    position = fs.fret_position_mm(scale, 24)
    check(abs(position - (scale * 3 / 4)) < 1e-9, f"fret 24 @ {scale}mm = {position} ≈ {scale*3/4}")


def test_resolve_missing_inputs() -> None:
    intake = {
        "MEAS-004": {"measurement_id": "MEAS-004", "current_value": ""},
        "MEAS-006": {"measurement_id": "MEAS-006", "current_value": ""},
    }
    scale, fret_count, blockers = fs.resolve_inputs(intake)
    check(scale is None and fret_count is None, "both inputs unresolved when current_value empty")
    check(len(blockers) == 2, f"two blockers reported, got {blockers}")


def test_resolve_measured_inputs() -> None:
    intake = {
        "MEAS-004": {"measurement_id": "MEAS-004", "current_value": "690"},
        "MEAS-006": {"measurement_id": "MEAS-006", "current_value": "23"},
    }
    scale, fret_count, blockers = fs.resolve_inputs(intake)
    check(scale == 690.0, f"scale resolved to {scale}")
    check(fret_count == 23, f"fret count resolved to {fret_count}")
    check(blockers == [], f"no blockers, got {blockers}")


def test_exploration_csv_is_deterministic() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "explore.csv"
        import argparse
        args = argparse.Namespace(scales="660,690,720", fret_count=24, out=out)
        fs.cmd_explore(args)
        first = out.read_bytes()
        fs.cmd_explore(args)
        second = out.read_bytes()
        check(first == second, "exploration CSV is byte-identical across runs")
        # Quick sanity: 3 scales x 24 frets = 72 rows + header.
        reader = csv.reader(io.StringIO(first.decode()))
        rows = list(reader)
        check(len(rows) == 73, f"got {len(rows)} lines (header + 72 rows)")


def test_blocked_csv_when_intake_empty() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        intake_path = Path(tmp) / "intake.csv"
        with intake_path.open("w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=["measurement_id", "current_value"])
            writer.writeheader()
            writer.writerow({"measurement_id": "MEAS-004", "current_value": ""})
            writer.writerow({"measurement_id": "MEAS-006", "current_value": ""})
        out = Path(tmp) / "fret-schedule.csv"
        import argparse
        args = argparse.Namespace(intake=intake_path, out=out, allow_blocked=False)
        rc = fs.cmd_emit(args)
        check(rc == 0, "emit returned 0 with blocked rows")
        with out.open() as fh:
            rows = list(csv.DictReader(fh))
        check(len(rows) == 12, f"12 placeholder blocked rows written, got {len(rows)}")
        check(all(r["status"].startswith("blocked_pending_") for r in rows),
              "all rows tagged blocked_pending_*")


def main() -> int:
    test_fret_12_is_half_scale()
    test_fret_24_is_quarter_scale()
    test_resolve_missing_inputs()
    test_resolve_measured_inputs()
    test_exploration_csv_is_deterministic()
    test_blocked_csv_when_intake_empty()
    print("all tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
