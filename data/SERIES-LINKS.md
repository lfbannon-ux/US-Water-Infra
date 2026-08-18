# Time-Series Links

Direct download endpoints for every series behind this analysis. FRED CSV needs **no API key**.

Run [`fetch_series.py`](fetch_series.py) to pull all FRED series at once:

```bash
python3 data/fetch_series.py --check   # verify every ID resolves
python3 data/fetch_series.py           # download + merge to data/fred/
```

> **Not verified live.** Every FRED ID below was confirmed against its FRED series page via search, but could not be fetched from the build environment (egress allowlist). `--check` validates them on your machine and names any that fail.

---

## FRED series


### Construction spending

| Series ID | Description | Freq | Units | From | CSV | Page |
| --- | --- | --- | --- | --- | --- | --- |
| `TLWSCON` | Total Construction Spending: Water Supply | Monthly | $m, NSA | 2002 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=TLWSCON) | [page](https://fred.stlouisfed.org/series/TLWSCON) |
| `TLWSCONS` | Total Construction Spending: Water Supply | Monthly | $m, SAAR | 2002 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=TLWSCONS) | [page](https://fred.stlouisfed.org/series/TLWSCONS) |
| `PBWSCON` | Total Public Construction Spending: Water Supply | Monthly | $m, NSA | 2002 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=PBWSCON) | [page](https://fred.stlouisfed.org/series/PBWSCON) |
| `PBWSCONS` | Total Public Construction Spending: Water Supply | Monthly | $m, SAAR | 2002 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=PBWSCONS) | [page](https://fred.stlouisfed.org/series/PBWSCONS) |
| `TLSWDCON` | Total Construction Spending: Sewage and Waste Disposal | Monthly | $m, NSA | 2002 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=TLSWDCON) | [page](https://fred.stlouisfed.org/series/TLSWDCON) |
| `TLSWDCONS` | Total Construction Spending: Sewage and Waste Disposal | Monthly | $m, SAAR | 2002 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=TLSWDCONS) | [page](https://fred.stlouisfed.org/series/TLSWDCONS) |
| `PBSWGCON` | Total Public Construction Spending: Sewage and Waste Disposal | Monthly | $m, NSA | 2002 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=PBSWGCON) | [page](https://fred.stlouisfed.org/series/PBSWGCON) |
| `PBSWGCONS` | Total Public Construction Spending: Sewage and Waste Disposal | Monthly | $m, SAAR | 2002 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=PBSWGCONS) | [page](https://fred.stlouisfed.org/series/PBSWGCONS) |
| `MPCP14XXS` | Total Public Construction Spending: Water Supply | Monthly | $m, SAAR | 2002 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=MPCP14XXS) | [page](https://fred.stlouisfed.org/series/MPCP14XXS) |
| `MPCP13XXS` | Total Public Construction Spending: Sewage and Waste Disposal | Monthly | $m, SAAR | 2002 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=MPCP13XXS) | [page](https://fred.stlouisfed.org/series/MPCP13XXS) |

### Water rates (CPI)

| Series ID | Description | Freq | Units | From | CSV | Page |
| --- | --- | --- | --- | --- | --- | --- |
| `CUSR0000SEHG` | CPI-U: Water and Sewer and Trash Collection Services | Monthly | Index, SA | 1983 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=CUSR0000SEHG) | [page](https://fred.stlouisfed.org/series/CUSR0000SEHG) |
| `CUUR0000SEHG` | CPI-U: Water and Sewer and Trash Collection Services | Monthly | Index, NSA | 1983 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=CUUR0000SEHG) | [page](https://fred.stlouisfed.org/series/CUUR0000SEHG) |
| `CUSR0000SEHG01` | CPI-U: Water and Sewerage Maintenance | Monthly | Index, SA | 1983 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=CUSR0000SEHG01) | [page](https://fred.stlouisfed.org/series/CUSR0000SEHG01) |
| `CWSR0000SEHG` | CPI-W: Water and Sewer and Trash Collection Services | Monthly | Index, SA | 1983 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=CWSR0000SEHG) | [page](https://fred.stlouisfed.org/series/CWSR0000SEHG) |
| `CPIAUCSL` | CPI-U: All Items | Monthly | Index, SA | 1947 | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL) | [page](https://fred.stlouisfed.org/series/CPIAUCSL) |

### Pipe prices (PPI)

| Series ID | Description | Freq | Units | From | CSV | Page |
| --- | --- | --- | --- | --- | --- | --- |
| `WPU072106033` | PPI: Plastics Water Pipe | Monthly | Index | varies | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=WPU072106033) | [page](https://fred.stlouisfed.org/series/WPU072106033) |
| `PCU32612232612218` | PPI by Industry: Plastics Sewer, Stormdrain, and Water Main Pipe | Monthly | Index | varies | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=PCU32612232612218) | [page](https://fred.stlouisfed.org/series/PCU32612232612218) |
| `WPU07210604` | PPI: Plastics Pipe Fittings and Unions | Monthly | Index | varies | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=WPU07210604) | [page](https://fred.stlouisfed.org/series/WPU07210604) |
| `PCU3261223261223` | PPI by Industry: Plastics Pipe Fittings and Unions | Monthly | Index | varies | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=PCU3261223261223) | [page](https://fred.stlouisfed.org/series/PCU3261223261223) |
| `WPU10150211` | PPI: Ductile Iron Pressure Pipe and Fittings | Monthly | Index | varies | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=WPU10150211) | [page](https://fred.stlouisfed.org/series/WPU10150211) |
| `WPU101502` | PPI: Pressure and Soil Pipe and Fittings, Cast Iron | Monthly | Index | varies | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=WPU101502) | [page](https://fred.stlouisfed.org/series/WPU101502) |
| `WPU1015021` | PPI: Pressure Pipe and Fittings, Cast Iron | Monthly | Index | varies | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=WPU1015021) | [page](https://fred.stlouisfed.org/series/WPU1015021) |
| `WPU10150227` | PPI: Cast Iron Pressure and Soil Pipe and Fittings, Except Ductile Pressure Pipe | Monthly | Index | varies | [csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=WPU10150227) | [page](https://fred.stlouisfed.org/series/WPU10150227) |

**Why these matter**

- `TLSWDCON` — CAUTION: bundles solid waste facilities with sewerage.
- `CUSR0000SEHG` — THE key public series for the rate thesis. Monthly, back to 1983, free.
- `WPU072106033` — THE direct read on the PVC deflation both CNM and FERG flagged.

---

## Bulk data portals and primary documents


### Public spending

| Source | Format | Coverage | Note |
| --- | --- | --- | --- |
| [CBO — Public Spending on Transportation and Water Infrastructure, 1956-2023](https://www.cbo.gov/publication/60874) | XLSX supplementary workbook | 1956-2023 annual | THE anchor source. The page carries a supplementary data workbook with the full annual series by mode, split capital vs operations & maintenance and federal vs state/local. This is where the $59bn water utilities capital figure comes from. |
| [Census Bureau — Construction Spending (C30) historical time series](https://www.census.gov/construction/c30/historical_data.html) | XLSX / CSV | 1993- monthly | Official source behind the FRED construction series. Longer history than FRED for some cuts. |
| [Census Bureau — Construction Spending landing page](https://www.census.gov/construction/c30/) | PDF / XLSX | Monthly releases | Monthly release tables including water supply and sewage & waste disposal. |
| [US Conference of Mayors — 2025 Public Infrastructure Spending](https://www.usmayors.org/p3/2025-public-infrastructure-spending/) | PDF | 2012-2024 | Local-government-only capital spending on sewer and water supply, cumulative and annual. |

### Federal programmes

| Source | Format | Coverage | Note |
| --- | --- | --- | --- |
| [CRS IF13177 — FY2026 Appropriations for EPA Water Infrastructure Programs](https://www.congress.gov/crs-product/IF13177) | PDF / HTML | FY2025-FY2026 | Table 1 has enacted appropriations by programme. The clean source for the SRF fiscal-year series. |
| [CRS IF12950 — EPA Water Infrastructure Programs and FY2025 Appropriations](https://www.congress.gov/crs-product/IF12950) | PDF / HTML | FY2024-FY2025 | Table 1. |
| [CRS R47474 — Clean Water SRF Allotment Formula](https://www.congress.gov/crs-product/R47474) | PDF / HTML | Historical | Longer-run CWSRF appropriations history and the 1987 allotment formula. |
| [CRS R47878 — Drinking Water Infrastructure Needs](https://www.congress.gov/crs-product/R47878) | PDF / HTML | DWINSA vintages | Restates DWINSA in 2022 dollars ($648.8bn). |
| [CRS R48565 — Wastewater Infrastructure Funding](https://www.congress.gov/crs-product/R48565) | PDF / HTML | Historical | EPA wastewater needs table and affordability analysis. |
| [EPA — WIFIA closed loans](https://www.epa.gov/wifia/wifia-program-announcements) | HTML list | 2018- | Loan-by-loan record: borrower, amount, project value, close date. |
| [EPA — Water Infrastructure Investments (BIL/IIJA)](https://www.epa.gov/infrastructure/water-infrastructure-investments) | HTML / PDF | FY2022-FY2026 | IIJA allocation by pot and by state. |

### Needs surveys

| Source | Format | Coverage | Note |
| --- | --- | --- | --- |
| [EPA CWNS 2022 — facility-level data download](https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download) | CSV / MS Access | 2022 survey | GENUINELY DOWNLOADABLE AND FACILITY-LEVEL. Every table as CSV, nationwide or by state, with a data dictionary. The single richest free dataset in the sector. |
| [EPA CWNS — report and data landing page](https://www.epa.gov/cwns/clean-watersheds-needs-survey-cwns-2022-report-and-data) | PDF / dashboard | 1984-2022 | Report to Congress plus the interactive needs dashboard. |
| [CUAHSI HydroShare — Clean Watersheds Needs Surveys 1984-2022](https://www.hydroshare.org/resource/3dab07fd628a4af2ba812f038b1af89f/) | CSV | 1984-2022 | Third-party archive converting the older Access-format surveys to CSV. Use for the long vintage series. |
| [EPA DWSRF — Drinking Water Infrastructure Needs Survey and Assessment](https://www.epa.gov/dwsrf) | PDF | 1995-2023 (7 surveys) | Reports to Congress. Underlying utility responses are not public. |

### Technical

| Source | Format | Coverage | Note |
| --- | --- | --- | --- |
| [USGS — Water Use in the United States](https://www.usgs.gov/mission-areas/water-resources/science/water-use-united-states) | CSV / PDF | 1950-2020, five-yearly | National compilation by category and state. Circular 1441 is the 2015 edition. |
| [USU — Water Main Break Rates in the USA and Canada](https://digitalcommons.usu.edu/water_rep/) | PDF | 2012, 2018, 2023 | Three survey vintages. Break rate by material, pipe age distribution, material mix. |
| [PHMSA — By-Decade Inventory (gas and hazardous liquid pipelines)](https://www.phmsa.dot.gov/data-and-statistics/pipeline-replacement/decade-inventory) | XLSX | 2005- | Mileage by decade of installation. THE COMPARATOR: this is what water has no equivalent of. |
| [EPA SDWIS — Safe Drinking Water Information System](https://sdwis.epa.gov/ords/sfdw_pub/f?p=SDWIS_FED_REPORTS_PUBLIC) | HTML / CSV | Current | Compliance, violations and basic system inventory. NO pipe age or distribution asset data. |

### Estimates

| Source | Format | Coverage | Note |
| --- | --- | --- | --- |
| [ASCE — Bridging the Gap economic study](https://bridgingthegap.infrastructurereportcard.org/) | PDF | 2024 | $99bn/yr water sector gap. |
| [ASCE — 2025 Infrastructure Report Card](https://infrastructurereportcard.org/) | PDF / HTML | 2025 | Drinking water C-, wastewater D+. |
| [AWWA — Beyond the Replacement Era](https://www.awwa.org/beyond-the-replacement-era/) | PDF | 2026 | $2.1-2.4tn over 2026-2050. |
| [Bluefield Research — municipal water & sewer rate index](https://www.bluefieldresearch.com/research/u-s-municipal-water-sewer-rate-index/) | Subscription | 50 cities, annual | PAID. The free public substitute is CPI series CUSR0000SEHG01. |

### Utility & company

| Source | Format | Coverage | Note |
| --- | --- | --- | --- |
| [MSRB EMMA — municipal bond official statements and continuing disclosure](https://emma.msrb.org/) | PDF | 1990- | FREE. System descriptions with miles of main, material mix, age profile, CIP and rate history. The highest-density public source for utility-level asset and spending data. |
| [SEC EDGAR full-text search](https://efts.sec.gov/LATEST/search-index?q=%22water%20main%22&forms=10-K) | HTML / JSON API | 2001- | Investor-owned water utility 10-Ks: replacement cycles, miles replaced, capital plans. |
| [Quartr — Core & Main](https://web.quartr.com/companies/6132) | API / web | FY2021- | Source of every Core & Main figure in this workbook. |
| [Quartr — Ferguson Enterprises](https://web.quartr.com/companies/3672) | API / web | FY2018- | Source of every Ferguson figure in this workbook. |

### Asset-level

| Source | Format | Coverage | Note |
| --- | --- | --- | --- |
| [Seattle GeoData — water mains and services](https://data-seattlecitygis.opendata.arcgis.com/) | Shapefile / GeoJSON / CSV | Current | Segment-level main layer with installation year and material, plus a 'presumed unlined' layer. |
| [Open Data DC — DC Water main breaks](https://opendata.dc.gov/datasets/dc-water-main-breaks) | CSV / GeoJSON | Rolling 5 years | Break location and date, updated weekly. The closest public proxy for repair history. |
| [data.gov — geospatial catalogue](https://catalog.data.gov/dataset?metadata_type=geospatial) | Various | Current | Federated search across city open-data portals for water main layers. |
| [New York State — Lead Service Line Inventory Map](https://health.data.ny.gov/Health/New-York-State-Lead-Service-Line-Inventory-Map/fkii-zkcq) | CSV / API | 2024- | Socrata dataset — genuinely queryable service line material by location. |
| [Minnesota — Lead Infrastructure Transparency Tool](https://maps.umn.edu/LSL/) | Web map | 2024- | Address-level search. |

---

## What is genuinely downloadable, ranked

1. **FRED** — every series above, CSV, no key, one command.
2. **EPA CWNS 2022 facility-level data** — CSV or Access, nationwide or by state, with a data dictionary. The richest free dataset in the sector.
3. **CBO supplementary workbook** — the full 1956-2023 annual series by mode, capital vs O&M, federal vs state/local. One XLSX behind [publication 60874](https://www.cbo.gov/publication/60874).
4. **Census C30 historical time series** — monthly construction spending back to 1993.
5. **Municipal GIS portals** — segment-level pipe age and material, utility by utility.
6. **MSRB EMMA** — free, and the densest utility-level asset and capital-plan disclosure available.

## What is not

- **Bluefield rate index** — subscription. Free substitute: FRED `CUSR0000SEHG01`.
- **EPA DWINSA underlying responses** — aggregated only; utility-level data not published.
- **AWIA risk and resilience assessments** — confidential by statute.
- **PIPEiD** — exists, but is a secured utility platform, not open data.
- **A national water pipe age registry** — does not exist. PHMSA's By-Decade Inventory is the gas-sector comparator showing what is missing.

