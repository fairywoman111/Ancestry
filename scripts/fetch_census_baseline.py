#!/usr/bin/env python3
"""
Phase 1 - Macro census baseline (America), state level.

Pulls ACS 5-year table B03002 (Hispanic or Latino Origin by Race) for every
state + DC, maps the Census variable codes to the project's macro groups
(see docs/macro_groups.md), computes counts + shares, and writes a small
derived CSV to data/tier1_census/.

Why B03002: it separates Hispanic/Latino origin from race, producing mutually
exclusive macro categories in the OMB-1997 style (race-alone, Not-Hispanic,
plus Hispanic-of-any-race). This is the standard table for a clean macro cut.

Run:
    python scripts/fetch_census_baseline.py            # ACS 2023 5-year
    python scripts/fetch_census_baseline.py --year 2020
A free Census API key (CENSUS_API_KEY env var) is optional for this volume.

Note: requires outbound network access to api.census.gov.
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
from pathlib import Path

import requests

# B03002 variable code -> macro group label (see docs/macro_groups.md).
# These are the mutually-exclusive rows we keep for the baseline.
MACRO_VARS = {
    "B03002_001E": "total",
    "B03002_003E": "white_nh",             # White alone, not Hispanic
    "B03002_004E": "black_nh",             # Black or African American alone, NH
    "B03002_005E": "amerindian_ak_nh",     # American Indian & Alaska Native alone, NH
    "B03002_006E": "asian_nh",             # Asian alone, NH
    "B03002_007E": "nhpi_nh",              # Native Hawaiian & Other Pacific Islander, NH
    "B03002_008E": "some_other_nh",        # Some other race alone, NH
    "B03002_009E": "two_or_more_nh",       # Two or more races, NH
    "B03002_012E": "hispanic_any_race",    # Hispanic or Latino (of any race)
}

# Race-alone / ethnicity components that should sum to the total.
SHARE_COLS = [v for v in MACRO_VARS.values() if v != "total"]


def fetch(year: int) -> list[dict]:
    url = f"https://api.census.gov/data/{year}/acs/acs5"
    params = {
        "get": "NAME," + ",".join(MACRO_VARS.keys()),
        "for": "state:*",
    }
    key = os.environ.get("CENSUS_API_KEY")
    if key:
        params["key"] = key

    resp = requests.get(url, params=params, timeout=60)
    resp.raise_for_status()
    rows = resp.json()
    header, *data = rows

    out = []
    for row in data:
        rec = dict(zip(header, row))
        item = {"state": rec["NAME"], "state_fips": rec["state"], "scheme": "omb_1997"}
        for code, label in MACRO_VARS.items():
            item[label] = int(rec[code])
        total = item["total"] or 1
        for label in SHARE_COLS:
            item[f"{label}_share"] = round(item[label] / total, 5)
        out.append(item)
    out.sort(key=lambda r: r["state"])
    return out


def write_csv(rows: list[dict], year: int) -> Path:
    out_dir = Path(__file__).resolve().parent.parent / "data" / "tier1_census"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"acs{year}_5yr_state_macro_race_ethnicity.csv"
    fieldnames = (
        ["state", "state_fips", "scheme", "total"]
        + SHARE_COLS
        + [f"{c}_share" for c in SHARE_COLS]
    )
    with out_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    return out_path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--year", type=int, default=2023, help="ACS 5-year end year")
    args = ap.parse_args()

    try:
        rows = fetch(args.year)
    except requests.RequestException as e:
        print(f"ERROR: could not reach the Census API: {e}", file=sys.stderr)
        print("This environment may block outbound network access.", file=sys.stderr)
        return 1

    out_path = write_csv(rows, args.year)
    national = sum(r["total"] for r in rows)
    print(f"Wrote {len(rows)} rows -> {out_path}")
    print(f"Total population across states+DC: {national:,}")
    print("Remember to log the source in CITATIONS.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
