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

## Monarch portraits

Portraits in `mon/01.jpg`–`mon/13.jpg` from Wikimedia Commons (public domain / CC). Hover or tap the monarch strip for portrait + blurb.

- **William III** — Godfrey Kneller; Public domain; [King William III of England, (1650-1702).jpg](https://commons.wikimedia.org/wiki/File:King_William_III_of_England,_(1650-1702).jpg)
- **Anne** — Michael Dahl; Public domain; [Anne1705.jpg](https://commons.wikimedia.org/wiki/File:Dahl,_Michael_-_Queen_Anne_-_NPG_6187.jpg)
- **George I** — Workshop of Godfrey Kneller; Public domain; [King George I by Sir Godfrey Kneller, Bt (3).jpg](https://commons.wikimedia.org/wiki/File:King_George_I_by_Sir_Godfrey_Kneller,_Bt_(3).jpg)
- **George II** — Thomas Hudson; Public domain; [George II by Thomas Hudson.jpg](https://commons.wikimedia.org/wiki/File:George_II_by_Thomas_Hudson.jpg)
- **George III** — Allan Ramsay; Public domain; [Allan Ramsay - King George III in coronation robes - Google Art Project.jpg](https://commons.wikimedia.org/wiki/File:Allan_Ramsay_-_King_George_III_in_coronation_robes_-_Google_Art_Project.jpg)
- **George IV** — Thomas Lawrence; Public domain; [George IV 1821 color.jpg](https://commons.wikimedia.org/wiki/File:George_IV_1821_color.jpg)
- **William IV** — Martin Archer Shee; Public domain; [William IV.jpg](https://commons.wikimedia.org/wiki/File:William_IV.jpg)
- **Victoria** — Alexander Bassano; Public domain; [Queen Victoria by Bassano.jpg](https://commons.wikimedia.org/wiki/File:Queen_Victoria_by_Bassano.jpg)
- **Edward VII** — Luke Fildes; Public domain; [Edward VII in coronation robes.jpg](https://commons.wikimedia.org/wiki/File:Edward_VII_in_coronation_robes.jpg)
- **George V** — Bassano Ltd; Public domain; [King George 1923 LCCN2014715558 (cropped).jpg](https://commons.wikimedia.org/wiki/File:King_George_1923_LCCN2014715558_(cropped).jpg)
- **Edward VIII** — Albert H Collings; Public domain; [Edward VIII Portrait - 1936.jpg](https://commons.wikimedia.org/wiki/File:Edward_VIII_Portrait_-_1936.jpg)
- **George VI** — Gerald Kelly; Public domain; [King George VI.jpg](https://commons.wikimedia.org/wiki/File:King_George_VI.jpg)
- **Elizabeth II** — Donald McKague; Public domain; [Queen Elizabeth II official portrait for 1959 tour (retouched) (cropped) (3-to-4 aspect ratio).jpg](https://commons.wikimedia.org/wiki/File:Queen_Elizabeth_II_official_portrait_for_1959_tour_(retouched)_(cropped)_(3-to-4_aspect_ratio).jpg)

## Event archive plates

Event images in `img/NNN-K.jpg` are fetched from Wikimedia Commons via `tools/fetch_artefacts.py` using `tools/artefacts_plan.json`. Manifest: `data/artefacts.json`. Only PD/CC (or equivalent free) licenses are kept; each plate’s credit line links the Commons file page. Re-fetch:

```bash
python3 tools/fetch_artefacts.py
```

### Current plates

- Event **#1** `img/001-1.jpg` — acediscovery; CC BY 4.0; [Commons](https://commons.wikimedia.org/wiki/File:Bank-of-England.jpg)
- Event **#1** `img/001-2.jpg` — Godfrey Kneller; Public domain; [Commons](https://commons.wikimedia.org/wiki/File:King_William_III_of_England,_(1650-1702).jpg)
- Event **#1** `img/001-3.jpg` — Lady Jane Lindsay; Public domain; [Commons](https://commons.wikimedia.org/wiki/File:Bank_of_England_Charter_sealing_1694.jpg)
- Event **#2** `img/002-1.jpg` — Roger Burton West; CC BY-SA 2.5; [Commons](https://commons.wikimedia.org/wiki/File:Mercers_Hall_London.jpg)
- Event **#3** `img/003-1.jpg` — Jojagal; CC BY 4.0; [Commons](https://commons.wikimedia.org/wiki/File:John_Houblon_Governor_Bank_of_England_(cropped).jpg)
- Event **#4** `img/004-1.jpg` — Steve Daniels; CC BY-SA 2.0; [Commons](https://commons.wikimedia.org/wiki/File:The_Bank_of_England_on_Threadneedle_Street_-_geograph.org.uk_-_3898549.jpg)
- Event **#5** `img/005-1.jpg` — Royal Institution of Cornwall, Anna Tyacke, 2004-08-06 22:42:23; CC BY-SA 4.0; [Commons](https://commons.wikimedia.org/wiki/File:Obverse_of_sixpence_of_Elizabeth_I_(FindID_72036).jpg)
- Event **#5** `img/005-2.jpg` — Godfrey Kneller; Public domain; [Commons](https://commons.wikimedia.org/wiki/File:Portrait_of_Sir_Isaac_Newton,_1689_(brightened).jpg)
- Event **#5** `img/005-3.jpg` — Norfolk County Council, Adrian Marsden, 2012-11-14 10:08:18; CC BY-SA 2.0; [Commons](https://commons.wikimedia.org/wiki/File:Post_medieval_coin_weight_for_a_guinea_of_William_III_(FindID_529842).jpg)
- Event **#6** `img/006-1.jpg` — Godfrey Kneller; Public domain; [Commons](https://commons.wikimedia.org/wiki/File:Portrait_of_Sir_Isaac_Newton,_1689_(brightened).jpg)
- Event **#8** `img/008-1.jpg` — Unknown authorUnknown author; Public domain; [Commons](https://commons.wikimedia.org/wiki/File:EB1911_Tally_-_tally_stick_(diagram).jpg)
- Event **#11** `img/011-1.jpg` — Sodacan; CC BY-SA 3.0; [Commons](https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_England_(1702%E2%80%931707).svg)
- Event **#11** `img/011-2.jpg` — No Swan So Fine; CC BY-SA 4.0; [Commons](https://commons.wikimedia.org/wiki/File:Stained_glass_above_altar_of_St_George_the_Martyr,_Holborn.jpg)
- Event **#13** `img/013-1.jpg` — MostEpic; CC BY-SA 4.0; [Commons](https://commons.wikimedia.org/wiki/File:Arms_of_the_South_Sea_Company.svg)
- Event **#13** `img/013-2.jpg` — Acabashi; CC BY-SA 4.0; [Commons](https://commons.wikimedia.org/wiki/File:South_Sea_Company_coat_of_arms_Queen%27s_House_Greenwich_London_England.jpg)
- Event **#14** `img/014-1.jpg` — DavidDijkgraaf; CC0; [Commons](https://commons.wikimedia.org/wiki/File:Final_War_of_the_Spanish_Succession_Collage.jpg)
- Event **#15** `img/015-1.jpg` — Emoscopes; CC BY 2.5; [Commons](https://commons.wikimedia.org/wiki/File:Newcomen_atmospheric_engine_animation.gif)
- Event **#16** `img/016-1.jpg` — The_Treaty_of_Utrecht.jpg: Original uploader was RedCoat10 at en.wikipedia derivative work: Angel paez (talk); Public domain; [Commons](https://commons.wikimedia.org/wiki/File:The_Treaty_of_Utrecht_(clean).jpg)
- Event **#17** `img/017-1.jpg` — Brandon Grossardt for the coin image. George T. Morgan for the coin design.; Public domain; [Commons](https://commons.wikimedia.org/wiki/File:1879S_Morgan_Dollar_NGC_MS67plus_Obverse.png)
- Event **#18** `img/018-2.jpg` — Edward Matthew Ward; Public domain; [Commons](https://commons.wikimedia.org/wiki/File:South_Sea_Bubble.jpg)
- Event **#20** `img/020-1.jpg` — William Hogarth; Public domain; [Commons](https://commons.wikimedia.org/wiki/File:William_Hogarth_-_The_South_Sea_Scheme.png)
- Event **#21** `img/021-1.jpg` — Unknown authorUnknown author; Public domain; [Commons](https://commons.wikimedia.org/wiki/File:South_Sea_Bubble_Cards-Tree.png)
- Event **#22** `img/022-1.jpg` — Studio of Jean-Baptiste van Loo; Public domain; [Commons](https://commons.wikimedia.org/wiki/File:Robert-Walpole-1st-Earl-of-Orford.jpg)
- Event **#23** `img/023-1.jpg` — Thomas Rowlandson and Augustus Pugin; Public domain; [Commons](https://commons.wikimedia.org/wiki/File:Buzaglo_stove.png)
- Event **#24** `img/024-1.jpg` — acediscovery; CC BY 4.0; [Commons](https://commons.wikimedia.org/wiki/File:Bank-of-England.jpg)
- Event **#25** `img/025-1.jpg` — David Morier; Public domain; [Commons](https://commons.wikimedia.org/wiki/File:The_Battle_of_Culloden.jpg)
- Event **#26** `img/026-1.jpg` — JHerbstman; Public domain; [Commons](https://commons.wikimedia.org/wiki/File:1877_4%25_$50_United_States_Consols_.jpg)
- Event **#27** `img/027-1.jpg` — Sodacan; CC BY-SA 3.0; [Commons](https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Great_Britain_(1714%E2%80%931801).svg)
- Event **#28** `img/028-1.jpg` — Blaue Max; CC BY-SA 4.0; [Commons](https://commons.wikimedia.org/wiki/File:Seven_Years%27_War_Collage.jpg)
- Event **#29** `img/029-1.jpg` — Thomas King († circa 1796date QS:P,+1796-00-00T00:00:00Z/9,P1480,Q5727902); Public domain; [Commons](https://commons.wikimedia.org/wiki/File:John_Harrison_(Gem%C3%A4lde).jpg)
- Event **#30** `img/030-1.jpg` — Gabagool; CC BY 3.0; [Commons](https://commons.wikimedia.org/wiki/File:SevenYearsWar.png)
- Event **#31** `img/031-1.jpg` — Markus Schweiß; CC BY-SA 3.0; [Commons](https://commons.wikimedia.org/wiki/File:Spinning_jenny.jpg)
- Event **#32** `img/032-1.jpg` — Carl Frederik von Breda; Public domain; [Commons](https://commons.wikimedia.org/wiki/File:Watt_James_von_Breda.jpg)
- Event **#33** `img/033-1.jpg` — The original uploader was Markus Schweiß at German Wikipedia.; CC BY-SA 3.0; [Commons](https://commons.wikimedia.org/wiki/File:Waterframe.jpg)
- Event **#34** `img/034-1.jpg` — Phil Champion; CC BY-SA 2.0; [Commons](https://commons.wikimedia.org/wiki/File:Lumb_Bank_-_The_Ted_Hughes_Arvon_Centre_-_geograph.org.uk_-_970898.jpg)

_(35 plates in this pass; re-run fetch to fill gaps.)_
