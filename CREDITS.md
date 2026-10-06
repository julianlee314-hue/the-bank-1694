# Credits & sources

## Yield series

- **Long UK government / consol yield** — FRED series [`LTCYUKA`](https://fred.stlouisfed.org/series/LTCYUKA), constructed by the Bank of England as part of *A Millennium of Macroeconomic Data for the UK* (Three Centuries project). Annual, percent. Coverage used here: **1703–1994**. After consols cease being *the* market benchmark, the series continues as the long UK government yield (consol / gilt family). Cite BoE / FRED when reusing.
- **Bank Rate / policy rate** — FRED series [`BOERUKA`](https://fred.stlouisfed.org/series/BOERUKA), same Millennium release. Annual, end-of-year, percent. Coverage used here: **1694–1994**. Underlying official Bank Rate records have gaps; BoE compilers document assumptions in the Millennium spreadsheet.

Refresh locally with:

```bash
python3 tools/fetch_series.py
```

## Events

Event labels and short summaries are an editorial draft for *The Bank, 1694–1994* (v0). They draw on standard secondary histories of the Bank of England, public BoE timelines, and well-known science/tech milestones peppered alongside money and geopolitics. They are **not** a primary-source edition. Spot-check dates before treating any beat as definitive.

## Design

Visual family (Bodoni Moda / Libre Franklin / IBM Plex Mono, engraved-ledger palette) follows Julius’s companion site [The Dow, 1896–2016](https://julianlee314-hue.github.io/dow-timeline/v0.2/). Charting uses [D3](https://d3js.org/) 7.9 from cdnjs.

## Images

v0 ships **without** archive images. Artefacts may be added later under a separate CREDITS pass (Wikimedia / public-domain plates).
