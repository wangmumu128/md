#!/usr/bin/env python3
"""Parse LAMMPS thermo tables from a log file."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from statistics import mean, pstdev


def is_number(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def parse_tables(text: str) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    header: list[str] | None = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        parts = line.split()
        if parts[0] == "Step":
            header = parts
            continue
        if header and len(parts) == len(header) and all(is_number(p) for p in parts):
            rows.append({key: float(value) for key, value in zip(header, parts)})
            continue
        if line.startswith("Loop time"):
            header = None
    return rows


def summarize(rows: list[dict[str, float]]) -> dict[str, dict[str, float]]:
    if not rows:
        return {}
    columns = rows[0].keys()
    summary: dict[str, dict[str, float]] = {}
    for col in columns:
        values = [row[col] for row in rows if col in row]
        summary[col] = {
            "count": float(len(values)),
            "min": min(values),
            "max": max(values),
            "mean": mean(values),
            "std": pstdev(values) if len(values) > 1 else 0.0,
        }
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract LAMMPS thermo rows and summary statistics.")
    parser.add_argument("logfile", help="Path to log.lammps.")
    parser.add_argument("--csv", help="Optional CSV output path.")
    parser.add_argument("--summary", help="Optional JSON summary output path.")
    args = parser.parse_args()

    text = Path(args.logfile).read_text(encoding="utf-8", errors="replace")
    rows = parse_tables(text)
    stats = summarize(rows)

    if args.csv and rows:
        with Path(args.csv).open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)

    if args.summary:
        Path(args.summary).write_text(json.dumps(stats, indent=2), encoding="utf-8")

    print(json.dumps({"rows": len(rows), "columns": list(rows[0].keys()) if rows else []}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
