#!/usr/bin/env python3
"""Fetch FRED CSVs for LTCYUKA (consol/gilt yield) and BOERUKA (Bank Rate) into data/series.json."""
from __future__ import annotations
import csv, json, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "series.json"
URLS = {
    "consol": ("LTCYUKA", "https://fred.stlouisfed.org/graph/fredgraph.csv?id=LTCYUKA"),
    "bankRate": ("BOERUKA", "https://fred.stlouisfed.org/graph/fredgraph.csv?id=BOERUKA"),
}
YMIN, YMAX = 1694, 1994

def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "the-bank-1694/0.1"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")

def parse(csv_text: str, series_id: str):
    rows = []
    reader = csv.DictReader(csv_text.splitlines())
    for row in reader:
        val = (row.get(series_id) or "").strip()
        if not val or val.upper() in (".", "NA", "NAN"):
            continue
        year = int(row["observation_date"][:4])
        if year < YMIN or year > YMAX:
            continue
        rows.append([year, round(float(val), 4)])
    return rows

def main():
    consol = parse(fetch(URLS["consol"][1]), URLS["consol"][0])
    bank = parse(fetch(URLS["bankRate"][1]), URLS["bankRate"][0])
    series = {
        "consol": consol,
        "bankRate": bank,
        "meta": {
            "consol": {
                "id": "LTCYUKA",
                "name": "Long-term UK government bond / consol yield",
                "units": "percent",
                "source": "FRED / Bank of England Millennium of Macroeconomic Data",
                "url": "https://fred.stlouisfed.org/series/LTCYUKA",
                "coverage": f"{consol[0][0]}–{consol[-1][0]}",
                "note": "Annual average long-term gilt / consol yield. After consols cease being the primary benchmark, LTCYUKA continues as the long UK government yield family.",
            },
            "bankRate": {
                "id": "BOERUKA",
                "name": "Bank of England policy / Bank Rate (annual, end of year)",
                "units": "percent",
                "source": "FRED / Bank of England Millennium of Macroeconomic Data",
                "url": "https://fred.stlouisfed.org/series/BOERUKA",
                "coverage": f"{bank[0][0]}–{bank[-1][0]}",
                "note": "End-of-year Bank Rate / policy rate from BoE Three Centuries / Millennium construction.",
            },
            "chartRange": [YMIN, YMAX],
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(series, indent=2) + "\n")
    print(f"wrote {OUT} consol={len(consol)} bankRate={len(bank)}")

if __name__ == "__main__":
    main()
