#!/usr/bin/env python3
"""Download every FRED series in the catalogue to CSV, then build a merged wide table.

Run this on a machine with network access:

    python3 data/fetch_series.py                  # download all
    python3 data/fetch_series.py --group "Pipe"   # only groups matching a substring
    python3 data/fetch_series.py --check          # verify each ID resolves, download nothing

Writes to data/fred/<SERIES_ID>.csv plus data/fred/_merged_monthly.csv.
No API key required — fredgraph.csv is a public endpoint.
"""
import argparse
import csv
import io
import os
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catalogue import FRED, FREDCSV  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fred")
UA = {"User-Agent": "us-water-infra-analysis/1.0"}


def fetch(sid, timeout=60):
    req = urllib.request.Request(FREDCSV.format(sid=sid), headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", default="", help="only series whose group contains this text")
    ap.add_argument("--check", action="store_true", help="verify IDs resolve, write nothing")
    args = ap.parse_args()

    rows = [s for s in FRED if args.group.lower() in s[0].lower()]
    if not args.check:
        os.makedirs(OUT, exist_ok=True)

    series, ok, bad = {}, [], []
    for group, sid, desc, freq, units, start, why in rows:
        try:
            body = fetch(sid)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            bad.append((sid, desc, str(e)))
            print(f"FAIL  {sid:22} {desc[:52]:54} {e}")
            continue

        reader = list(csv.reader(io.StringIO(body)))
        header, data = reader[0], [r for r in reader[1:] if len(r) >= 2 and r[1] not in ("", ".")]
        if not data:
            bad.append((sid, desc, "empty"))
            print(f"EMPTY {sid:22} {desc[:52]:54}")
            continue

        ok.append((sid, desc, len(data), data[0][0], data[-1][0]))
        print(f"OK    {sid:22} {desc[:52]:54} {len(data):>5} obs  {data[0][0]} -> {data[-1][0]}")

        if not args.check:
            with open(os.path.join(OUT, f"{sid}.csv"), "w", newline="") as f:
                f.write(body)
            series[sid] = {r[0]: r[1] for r in data}

    if not args.check and series:
        dates = sorted({d for s in series.values() for d in s})
        ids = list(series)
        with open(os.path.join(OUT, "_merged_monthly.csv"), "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["date"] + ids)
            for d in dates:
                w.writerow([d] + [series[i].get(d, "") for i in ids])
        print(f"\nmerged -> {os.path.join(OUT, '_merged_monthly.csv')}  "
              f"({len(dates)} dates x {len(ids)} series)")

    print(f"\n{len(ok)} ok, {len(bad)} failed")
    if bad:
        print("Failed IDs (check them on fred.stlouisfed.org — FRED occasionally retires or renames):")
        for sid, desc, err in bad:
            print(f"  {sid:22} {desc}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
