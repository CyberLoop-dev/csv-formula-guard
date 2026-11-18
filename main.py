#!/usr/bin/env python3
"""Find and optionally neutralize spreadsheet-formula-like CSV cells."""
import argparse
import csv
from pathlib import Path
import sys

FORMULA_PREFIXES = ("=", "+", "-", "@")

def is_formula_like(value):
    candidate = value.lstrip(" \t\r\n")
    if not candidate:
        return False
    if candidate[0] in ("+", "-"):
        try:
            float(candidate)
            return False
        except ValueError:
            pass
    return candidate[0] in FORMULA_PREFIXES

def scan_rows(rows):
    findings = []
    for row_number, row in enumerate(rows, start=1):
        for column_number, value in enumerate(row, start=1):
            if is_formula_like(value):
                findings.append({"row": row_number, "column": column_number, "value": value})
    return findings

def read_csv(path, delimiter=","):
    with Path(path).open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.reader(stream, delimiter=delimiter))

def sanitize_csv(source, destination, delimiter=",", force=False):
    src, dst = Path(source).resolve(), Path(destination).resolve()
    if src == dst:
        raise ValueError("Output path must differ from input path.")
    if dst.exists() and not force:
        raise FileExistsError(f"{dst} exists; pass --force to replace it.")
    rows = read_csv(src, delimiter)
    safe = [["'" + cell if is_formula_like(cell) else cell for cell in row] for row in rows]
    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter=delimiter)
        writer.writerows(safe)
    return scan_rows(rows), len(rows)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    scan = sub.add_parser("scan")
    scan.add_argument("input")
    scan.add_argument("--delimiter", default=",")
    clean = sub.add_parser("sanitize")
    clean.add_argument("input")
    clean.add_argument("--output", required=True)
    clean.add_argument("--delimiter", default=",")
    clean.add_argument("--force", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "scan":
            findings = scan_rows(read_csv(args.input, args.delimiter))
            for item in findings:
                print(f"row {item['row']}, column {item['column']}: {item['value']!r}")
            print(f"Found {len(findings)} formula-like cell(s).")
            return 1 if findings else 0
        findings, count = sanitize_csv(args.input, args.output, args.delimiter, args.force)
        print(f"Wrote sanitized copy to {args.output}; reviewed {count} row(s), neutralized {len(findings)} cell(s).")
        return 0
    except (OSError, ValueError, csv.Error) as exc:
        print(f"csv-formula-guard: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
