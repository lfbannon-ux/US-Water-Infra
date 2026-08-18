"""Time-series catalogue: direct download endpoints for every series behind this analysis.

Every FRED series ID here was confirmed against FRED's own series pages via search.
They could NOT be fetched from the build environment (egress allowlist), so the
download URLs are constructed, not tested. `fetch_series.py` validates them on a
machine with network access and reports any that fail.

FRED CSV endpoint needs no API key:
    https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES_ID>
Several series at once:
    https://fred.stlouisfed.org/graph/fredgraph.csv?id=<ID1>,<ID2>,<ID3>
"""

FREDCSV = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}"
FREDPAGE = "https://fred.stlouisfed.org/series/{sid}"

# (group, series_id, description, frequency, units, start, why_it_matters)
FRED = [
    # ---- construction put in place: the demand series ----
    ("Construction spending", "TLWSCON", "Total Construction Spending: Water Supply",
     "Monthly", "$m, NSA", "2002", "Sum 12 months for a true annual figure. The headline water supply series."),
    ("Construction spending", "TLWSCONS", "Total Construction Spending: Water Supply",
     "Monthly", "$m, SAAR", "2002", "Seasonally adjusted annual rate — the figure quoted in this analysis."),
    ("Construction spending", "PBWSCON", "Total Public Construction Spending: Water Supply",
     "Monthly", "$m, NSA", "2002", "Public only. Private = total less public."),
    ("Construction spending", "PBWSCONS", "Total Public Construction Spending: Water Supply",
     "Monthly", "$m, SAAR", "2002", "Public only, SAAR."),
    ("Construction spending", "TLSWDCON", "Total Construction Spending: Sewage and Waste Disposal",
     "Monthly", "$m, NSA", "2002", "CAUTION: bundles solid waste facilities with sewerage."),
    ("Construction spending", "TLSWDCONS", "Total Construction Spending: Sewage and Waste Disposal",
     "Monthly", "$m, SAAR", "2002", "Same caution. This is the $54.3bn figure in the analysis."),
    ("Construction spending", "PBSWGCON", "Total Public Construction Spending: Sewage and Waste Disposal",
     "Monthly", "$m, NSA", "2002", "Public only."),
    ("Construction spending", "PBSWGCONS", "Total Public Construction Spending: Sewage and Waste Disposal",
     "Monthly", "$m, SAAR", "2002", "Public only, SAAR."),
    ("Construction spending", "MPCP14XXS", "Total Public Construction Spending: Water Supply",
     "Monthly", "$m, SAAR", "2002", "Census alternate identifier for the same concept — cross-check."),
    ("Construction spending", "MPCP13XXS", "Total Public Construction Spending: Sewage and Waste Disposal",
     "Monthly", "$m, SAAR", "2002", "Census alternate identifier — cross-check."),

    # ---- rates: the funding engine ----
    ("Water rates (CPI)", "CUSR0000SEHG", "CPI-U: Water and Sewer and Trash Collection Services",
     "Monthly", "Index, SA", "1983", "THE key public series for the rate thesis. Monthly, back to 1983, free."),
    ("Water rates (CPI)", "CUUR0000SEHG", "CPI-U: Water and Sewer and Trash Collection Services",
     "Monthly", "Index, NSA", "1983", "Not seasonally adjusted version."),
    ("Water rates (CPI)", "CUSR0000SEHG01", "CPI-U: Water and Sewerage Maintenance",
     "Monthly", "Index, SA", "1983", "Narrower — excludes trash collection. Closer to a pure water/sewer rate index."),
    ("Water rates (CPI)", "CWSR0000SEHG", "CPI-W: Water and Sewer and Trash Collection Services",
     "Monthly", "Index, SA", "1983", "Wage-earner basket version."),
    ("Water rates (CPI)", "CPIAUCSL", "CPI-U: All Items",
     "Monthly", "Index, SA", "1947", "Denominator — use to show water rates outpacing general inflation."),

    # ---- product prices: the distributor margin and revenue driver ----
    ("Pipe prices (PPI)", "WPU072106033", "PPI: Plastics Water Pipe",
     "Monthly", "Index", "varies", "THE direct read on the PVC deflation both CNM and FERG flagged."),
    ("Pipe prices (PPI)", "PCU32612232612218",
     "PPI by Industry: Plastics Sewer, Stormdrain, and Water Main Pipe",
     "Monthly", "Index", "varies", "Industry-based cut of the same product. Most precisely scoped series available."),
    ("Pipe prices (PPI)", "WPU07210604", "PPI: Plastics Pipe Fittings and Unions",
     "Monthly", "Index", "varies", "Fittings, which carry different margin than pipe."),
    ("Pipe prices (PPI)", "PCU3261223261223", "PPI by Industry: Plastics Pipe Fittings and Unions",
     "Monthly", "Index", "varies", "Industry-based cut of fittings."),
    ("Pipe prices (PPI)", "WPU10150211", "PPI: Ductile Iron Pressure Pipe and Fittings",
     "Monthly", "Index", "varies", "The other half of the pipe basket. Ductile iron is 29% of installed mains."),
    ("Pipe prices (PPI)", "WPU101502", "PPI: Pressure and Soil Pipe and Fittings, Cast Iron",
     "Monthly", "Index", "varies", "Broader cast iron aggregate."),
    ("Pipe prices (PPI)", "WPU1015021", "PPI: Pressure Pipe and Fittings, Cast Iron",
     "Monthly", "Index", "varies", "Narrower cast iron cut."),
    ("Pipe prices (PPI)", "WPU10150227",
     "PPI: Cast Iron Pressure and Soil Pipe and Fittings, Except Ductile Pressure Pipe",
     "Monthly", "Index", "varies", "Cast iron excluding ductile — cleanest split."),
]

# (group, name, url, format, coverage, note)
PORTALS = [
    ("Public spending", "CBO — Public Spending on Transportation and Water Infrastructure, 1956-2023",
     "https://www.cbo.gov/publication/60874", "XLSX supplementary workbook", "1956-2023 annual",
     "THE anchor source. The page carries a supplementary data workbook with the full annual series "
     "by mode, split capital vs operations & maintenance and federal vs state/local. This is where "
     "the $59bn water utilities capital figure comes from."),
    ("Public spending", "Census Bureau — Construction Spending (C30) historical time series",
     "https://www.census.gov/construction/c30/historical_data.html", "XLSX / CSV", "1993- monthly",
     "Official source behind the FRED construction series. Longer history than FRED for some cuts."),
    ("Public spending", "Census Bureau — Construction Spending landing page",
     "https://www.census.gov/construction/c30/", "PDF / XLSX", "Monthly releases",
     "Monthly release tables including water supply and sewage & waste disposal."),
    ("Public spending", "US Conference of Mayors — 2025 Public Infrastructure Spending",
     "https://www.usmayors.org/p3/2025-public-infrastructure-spending/", "PDF", "2012-2024",
     "Local-government-only capital spending on sewer and water supply, cumulative and annual."),

    ("Federal programmes", "CRS IF13177 — FY2026 Appropriations for EPA Water Infrastructure Programs",
     "https://www.congress.gov/crs-product/IF13177", "PDF / HTML", "FY2025-FY2026",
     "Table 1 has enacted appropriations by programme. The clean source for the SRF fiscal-year series."),
    ("Federal programmes", "CRS IF12950 — EPA Water Infrastructure Programs and FY2025 Appropriations",
     "https://www.congress.gov/crs-product/IF12950", "PDF / HTML", "FY2024-FY2025", "Table 1."),
    ("Federal programmes", "CRS R47474 — Clean Water SRF Allotment Formula",
     "https://www.congress.gov/crs-product/R47474", "PDF / HTML", "Historical",
     "Longer-run CWSRF appropriations history and the 1987 allotment formula."),
    ("Federal programmes", "CRS R47878 — Drinking Water Infrastructure Needs",
     "https://www.congress.gov/crs-product/R47878", "PDF / HTML", "DWINSA vintages",
     "Restates DWINSA in 2022 dollars ($648.8bn)."),
    ("Federal programmes", "CRS R48565 — Wastewater Infrastructure Funding",
     "https://www.congress.gov/crs-product/R48565", "PDF / HTML", "Historical",
     "EPA wastewater needs table and affordability analysis."),
    ("Federal programmes", "EPA — WIFIA closed loans",
     "https://www.epa.gov/wifia/wifia-program-announcements", "HTML list", "2018-",
     "Loan-by-loan record: borrower, amount, project value, close date."),
    ("Federal programmes", "EPA — Water Infrastructure Investments (BIL/IIJA)",
     "https://www.epa.gov/infrastructure/water-infrastructure-investments", "HTML / PDF", "FY2022-FY2026",
     "IIJA allocation by pot and by state."),

    ("Needs surveys", "EPA CWNS 2022 — facility-level data download",
     "https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download", "CSV / MS Access", "2022 survey",
     "GENUINELY DOWNLOADABLE AND FACILITY-LEVEL. Every table as CSV, nationwide or by state, with a "
     "data dictionary. The single richest free dataset in the sector."),
    ("Needs surveys", "EPA CWNS — report and data landing page",
     "https://www.epa.gov/cwns/clean-watersheds-needs-survey-cwns-2022-report-and-data", "PDF / dashboard",
     "1984-2022", "Report to Congress plus the interactive needs dashboard."),
    ("Needs surveys", "CUAHSI HydroShare — Clean Watersheds Needs Surveys 1984-2022",
     "https://www.hydroshare.org/resource/3dab07fd628a4af2ba812f038b1af89f/", "CSV", "1984-2022",
     "Third-party archive converting the older Access-format surveys to CSV. Use for the long vintage series."),
    ("Needs surveys", "EPA DWSRF — Drinking Water Infrastructure Needs Survey and Assessment",
     "https://www.epa.gov/dwsrf", "PDF", "1995-2023 (7 surveys)",
     "Reports to Congress. Underlying utility responses are not public."),

    ("Technical", "USGS — Water Use in the United States",
     "https://www.usgs.gov/mission-areas/water-resources/science/water-use-united-states", "CSV / PDF",
     "1950-2020, five-yearly", "National compilation by category and state. Circular 1441 is the 2015 edition."),
    ("Technical", "USU — Water Main Break Rates in the USA and Canada",
     "https://digitalcommons.usu.edu/water_rep/", "PDF", "2012, 2018, 2023",
     "Three survey vintages. Break rate by material, pipe age distribution, material mix."),
    ("Technical", "PHMSA — By-Decade Inventory (gas and hazardous liquid pipelines)",
     "https://www.phmsa.dot.gov/data-and-statistics/pipeline-replacement/decade-inventory", "XLSX", "2005-",
     "Mileage by decade of installation. THE COMPARATOR: this is what water has no equivalent of."),
    ("Technical", "EPA SDWIS — Safe Drinking Water Information System",
     "https://sdwis.epa.gov/ords/sfdw_pub/f?p=SDWIS_FED_REPORTS_PUBLIC", "HTML / CSV", "Current",
     "Compliance, violations and basic system inventory. NO pipe age or distribution asset data."),

    ("Estimates", "ASCE — Bridging the Gap economic study",
     "https://bridgingthegap.infrastructurereportcard.org/", "PDF", "2024", "$99bn/yr water sector gap."),
    ("Estimates", "ASCE — 2025 Infrastructure Report Card",
     "https://infrastructurereportcard.org/", "PDF / HTML", "2025", "Drinking water C-, wastewater D+."),
    ("Estimates", "AWWA — Beyond the Replacement Era",
     "https://www.awwa.org/beyond-the-replacement-era/", "PDF", "2026", "$2.1-2.4tn over 2026-2050."),
    ("Estimates", "Bluefield Research — municipal water & sewer rate index",
     "https://www.bluefieldresearch.com/research/u-s-municipal-water-sewer-rate-index/", "Subscription",
     "50 cities, annual", "PAID. The free public substitute is CPI series CUSR0000SEHG01."),

    ("Utility & company", "MSRB EMMA — municipal bond official statements and continuing disclosure",
     "https://emma.msrb.org/", "PDF", "1990-",
     "FREE. System descriptions with miles of main, material mix, age profile, CIP and rate history. "
     "The highest-density public source for utility-level asset and spending data."),
    ("Utility & company", "SEC EDGAR full-text search",
     "https://efts.sec.gov/LATEST/search-index?q=%22water%20main%22&forms=10-K", "HTML / JSON API", "2001-",
     "Investor-owned water utility 10-Ks: replacement cycles, miles replaced, capital plans."),
    ("Utility & company", "Quartr — Core & Main",
     "https://web.quartr.com/companies/6132", "API / web", "FY2021-",
     "Source of every Core & Main figure in this workbook."),
    ("Utility & company", "Quartr — Ferguson Enterprises",
     "https://web.quartr.com/companies/3672", "API / web", "FY2018-",
     "Source of every Ferguson figure in this workbook."),

    ("Asset-level", "Seattle GeoData — water mains and services",
     "https://data-seattlecitygis.opendata.arcgis.com/", "Shapefile / GeoJSON / CSV", "Current",
     "Segment-level main layer with installation year and material, plus a 'presumed unlined' layer."),
    ("Asset-level", "Open Data DC — DC Water main breaks",
     "https://opendata.dc.gov/datasets/dc-water-main-breaks", "CSV / GeoJSON", "Rolling 5 years",
     "Break location and date, updated weekly. The closest public proxy for repair history."),
    ("Asset-level", "data.gov — geospatial catalogue",
     "https://catalog.data.gov/dataset?metadata_type=geospatial", "Various", "Current",
     "Federated search across city open-data portals for water main layers."),
    ("Asset-level", "New York State — Lead Service Line Inventory Map",
     "https://health.data.ny.gov/Health/New-York-State-Lead-Service-Line-Inventory-Map/fkii-zkcq", "CSV / API",
     "2024-", "Socrata dataset — genuinely queryable service line material by location."),
    ("Asset-level", "Minnesota — Lead Infrastructure Transparency Tool",
     "https://maps.umn.edu/LSL/", "Web map", "2024-", "Address-level search."),
]
