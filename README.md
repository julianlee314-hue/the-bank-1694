# The Bank, 1694–1994

Three centuries of the Bank of England — wars, panics, gold, and the long rate of money — with science and tech peppered in.

**Live:** https://julianlee314-hue.github.io/the-bank-1694/

Companion Dow site (1896→): https://julianlee314-hue.github.io/dow-timeline/v0.2/

## What’s in v0

- **212** dated events (money / science / both), 1–4 per busy year
- Primary chart: UK long-term / consol gilt yield % (FRED `LTCYUKA`, 1703–1994)
- Compare toggle: Bank Rate (FRED `BOERUKA`, 1694–1994)
- Searchable register, category + kind filters, era zoom
- **No images yet** — event cards are text-only; archive plates come later

## Local preview

```bash
cd the-bank-1694
python3 -m http.server 8765
# open http://localhost:8765/
```

Same-origin `fetch` loads `data/events.json` and `data/series.json` (needed for local file:// as well as Pages).

## Refresh series

```bash
python3 tools/fetch_series.py
```

## License note

Series: Bank of England Millennium calculations via FRED — cite sources (see `CREDITS.md`). Event copy is editorial draft. Site code: use freely with attribution to Julius / this repo.
