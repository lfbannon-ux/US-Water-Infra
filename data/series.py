"""Downloaded and compiled time-series data.

COMPANY DATA: downloaded from Quartr (standardised statements built from primary
filings). Each period carries the Quartr report URL it came from.

MACRO DATA: compiled from published figures located via search. Direct download was
not possible from the build environment (egress allowlist blocks cbo.gov, census.gov,
fred.stlouisfed.org and every other external host). Each row carries its source, a
link, and the exact retrieval route so it can be refreshed automatically later.
"""

Q = "https://web.quartr.com/companies/{cid}?companyId={cid}&documentId={doc}&documentType=report&eventId={ev}"

# ---------------------------------------------------------------- Core & Main
# fiscal year ends the Sunday nearest 31 January; labelled by period end.
# (label, period_end, revenue, gross_profit, ebitda, op_income, net_income, dil_eps, report_url)
CNM_ANNUAL = [
    ("FY2021", "2022-01-30", 5004, 1280, 604, 425, 225, 0.55,
     Q.format(cid=6132, doc=222263, ev=18137)),
    ("FY2022", "2023-01-29", 6651, 1795, 918, 775, 366, 2.13,
     Q.format(cid=6132, doc=222262, ev=48726)),
    ("FY2023", "2024-01-28", 6702, 1818, 889, 740, 371, 2.15,
     Q.format(cid=6132, doc=339060, ev=132879)),
    ("FY2024", "2025-02-02", 7441, 1980, 905, 719, 434, 2.13,
     Q.format(cid=6132, doc=1879607, ev=257949)),
    ("FY2025", "2026-02-01", 7647, 2059, 913, 722, 462, 2.31,
     Q.format(cid=6132, doc=3158198, ev=423486)),
]

# (label, period_end, cfo, capex_abs, note)
CNM_ANNUAL_CF = [
    ("FY2021", "2022-01-30", -31, 20, "Working capital build during the 2021-22 inflation surge"),
    ("FY2022", "2023-01-29", 401, 25, ""),
    ("FY2023", "2024-01-28", 1069, 39, "Inventory unwind released $328m"),
    ("FY2024", "2025-02-02", 621, 35, ""),
    ("FY2025", "2026-02-01", 650, 46, ""),
]

# (fiscal label, period_end, reported, revenue, gross_profit, ebitda, op_income, net_income, dil_eps, url)
CNM_QUARTERLY = [
    ("Q2 FY2021", "2021-08-01", "2021-09-14", 1297.6, 325.2, 175.0, 99.8, 9.5, -0.14, Q.format(cid=6132, doc=441963, ev=4798)),
    ("Q3 FY2021", "2021-10-31", "2021-12-07", 1404.8, 370.6, 183.3, 147.5, 64.4, 0.39, Q.format(cid=6132, doc=441966, ev=11600)),
    ("Q4 FY2021", "2022-01-30", "2022-03-30", 1246.0, 327.0, 145.0, 109.0, 79.0, 0.28, Q.format(cid=6132, doc=2547335, ev=18137)),
    ("Q1 FY2022", "2022-05-01", "2022-06-14", 1598.0, 421.0, 216.0, 180.0, 86.0, 0.50, Q.format(cid=6132, doc=441962, ev=24012)),
    ("Q2 FY2022", "2022-07-31", "2022-09-13", 1861.0, 501.0, 271.0, 237.0, 115.0, 0.67, Q.format(cid=6132, doc=441965, ev=33541)),
    ("Q3 FY2022", "2022-10-30", "2022-12-13", 1818.0, 500.0, 344.0, 234.0, 111.0, 0.65, Q.format(cid=6132, doc=441958, ev=42148)),
    ("Q4 FY2022", "2023-01-29", "2023-03-28", 1374.0, 373.0, 160.0, 124.0, 84.0, 0.31, Q.format(cid=6132, doc=148368, ev=48726)),
    ("Q1 FY2023", "2023-04-30", "2023-06-06", 1574.0, 439.0, 217.0, 181.0, 86.0, 0.50, Q.format(cid=6132, doc=441957, ev=60565)),
    ("Q2 FY2023", "2023-07-30", "2023-09-06", 1861.0, 501.0, 301.0, 226.0, 110.0, 0.66, Q.format(cid=6132, doc=441961, ev=72325)),
    ("Q3 FY2023", "2023-10-29", "2023-12-05", 1827.0, 494.0, 255.0, 217.0, 112.0, 0.65, Q.format(cid=6132, doc=441956, ev=101436)),
    ("Q4 FY2023", "2024-01-28", "2024-03-19", 1440.0, 384.0, 154.0, 116.0, 63.0, 0.34, Q.format(cid=6132, doc=339055, ev=132879)),
    ("Q1 FY2024", "2024-05-05", "2024-06-04", 1741.0, 468.0, 212.0, 168.0, 95.0, 0.49, Q.format(cid=6132, doc=441954, ev=177254)),
    ("Q2 FY2024", "2024-08-04", "2024-09-04", 1964.0, 518.0, 250.0, 204.0, 126.0, 0.61, Q.format(cid=6132, doc=470183, ev=196829)),
    ("Q3 FY2024", "2024-11-03", "2024-12-03", 2038.0, 543.0, 367.0, 223.0, 140.0, 0.69, Q.format(cid=6132, doc=1797676, ev=227496)),
    ("Q4 FY2024", "2025-02-02", "2025-03-25", 1698.0, 451.0, 318.0, 124.0, 67.0, 0.33, Q.format(cid=6132, doc=1879604, ev=257949)),
    ("Q1 FY2025", "2025-05-04", "2025-06-10", 1911.0, 510.0, 219.0, 171.0, 100.0, 0.52, Q.format(cid=6132, doc=1985947, ev=330126)),
    ("Q2 FY2025", "2025-08-03", "2025-09-09", 2093.0, 560.0, 259.0, 213.0, 141.0, 0.70, Q.format(cid=6132, doc=2132390, ev=351231)),
    ("Q3 FY2025", "2025-11-02", "2025-12-09", 2062.0, 561.0, 267.0, 220.0, 143.0, 0.72, Q.format(cid=6132, doc=2492848, ev=384614)),
    ("Q4 FY2025", "2026-02-01", "2026-03-24", 1581.0, 428.0, 169.0, 118.0, 73.0, 0.37, Q.format(cid=6132, doc=3158185, ev=423486)),
    ("Q1 FY2026", "2026-05-03", "2026-06-10", 1910.0, 520.0, 223.0, 177.0, 113.0, 0.57, Q.format(cid=6132, doc=3542255, ev=614274)),
]

# ---------------------------------------------------------------- Ferguson
# FY ended 31 July through FY2025; moved to a 31 December year end thereafter.
FERG_ANNUAL = [
    ("FY2018", "2018-07-31", 20752, 6044, 1687, 1360, 1267, None,
     Q.format(cid=3672, doc=289297, ev=147685)),
    ("FY2019", "2019-07-31", 22010, 6458, None, 1402, 1108, None,
     Q.format(cid=3672, doc=289278, ev=147677)),
    ("FY2020", "2020-07-31", 21819, 6421, 1581, 1422, 961, None,
     Q.format(cid=3672, doc=289263, ev=147673)),
    ("FY2021", "2021-07-31", 22792, 6980, 2168, 2034, 1508, None,
     Q.format(cid=3672, doc=112879, ev=1080)),
    ("FY2022", "2022-07-31", 28566, 8756, 3121, 2820, 2122, 9.69,
     Q.format(cid=3672, doc=409293, ev=28198)),
    ("FY2023", "2023-07-31", 29734, 9025, 2980, 2659, 1889, 9.12,
     Q.format(cid=3672, doc=409292, ev=72323)),
    ("FY2024", "2024-07-31", 29635, 9053, 2987, 2652, 1735, 8.53,
     Q.format(cid=3672, doc=2180577, ev=196669)),
    ("FY2025", "2025-07-31", 30762, 9435, 2979, 2606, 1856, 9.32,
     Q.format(cid=3672, doc=2180538, ev=347925)),
    ("CY2025", "2025-12-31", 31316, 9708, 3243, 2789, 2006, 10.16,
     Q.format(cid=3672, doc=2916561, ev=568148)),
]

FERG_ANNUAL_CF = [
    ("FY2018", "2018-07-31", 1323, 265, ""),
    ("FY2019", "2019-07-31", 1609, 382, ""),
    ("FY2020", "2020-07-31", 1868, 215, "Capex cut during COVID"),
    ("FY2021", "2021-07-31", 1541, 174, ""),
    ("FY2022", "2022-07-31", 1149, 290, "Working capital build"),
    ("FY2023", "2023-07-31", 2723, 441, "Inventory unwind released $607m"),
    ("FY2024", "2024-07-31", 1873, 372, ""),
    ("FY2025", "2025-07-31", 1908, 305, ""),
    ("CY2025", "2025-12-31", 2181, 354, "Transition to calendar year end"),
]

# ---------------------------------------------------------------- Macro
# (series, period, value, unit, source, link, download_route)
MACRO = [
    # --- public spending ---
    ("Public spending, transportation + water infrastructure", "2023", 626, "$bn",
     "CBO, Public Spending on Transportation and Water Infrastructure 1956-2023 (Feb 2025)",
     "https://www.cbo.gov/publication/60874",
     "CBO publishes a supplementary data workbook with the full 1956-2023 series"),
    ("  as % of GDP", "2023", 0.023, "%", "CBO", "https://www.cbo.gov/publication/60874", "Same workbook"),
    ("Water utilities — total spending", "2023", 175, "$bn", "CBO via USAFacts",
     "https://usafacts.org/articles/how-much-does-the-government-spend-on-transportation-and-water-infrastructure/",
     "CBO supplementary workbook, water utilities series 1956-2023"),
    ("Water utilities — capital", "2023", 59, "$bn", "CBO", "https://www.cbo.gov/publication/60874",
     "CBO supplementary workbook. ANCHOR FOR THE FORWARD MODEL BASE"),
    ("Water utilities — operations & maintenance", "2023", 114, "$bn", "CBO",
     "https://www.cbo.gov/publication/60874", "CBO supplementary workbook"),
    ("State + local share of water infrastructure", "2023", 0.92, "%", "CBO",
     "https://www.cbo.gov/publication/60874", "CBO supplementary workbook"),
    ("State + local share of all public infrastructure", "2023", 0.79, "%", "CBO",
     "https://www.cbo.gov/publication/60874", "$494.2bn of $625.8bn"),
    ("O&M share of all public infrastructure spending", "2023", 0.567, "%", "CBO",
     "https://www.cbo.gov/publication/60874", "$355bn of $625.8bn"),

    # --- construction put in place ---
    ("Construction put in place — water supply, total", "Jan-2026 SAAR", 36.5, "$bn",
     "US Census Bureau C30", "https://www.census.gov/construction/c30/",
     "FRED series TLWSCONS (SAAR) / TLWSCON (NSA monthly, sum for annual)"),
    ("Construction put in place — water supply, public", "Jan-2026 SAAR", 34.8, "$bn",
     "US Census Bureau C30", "https://www.census.gov/construction/c30/",
     "FRED series PBWSCONS (SAAR) / PBWSCON (NSA monthly). History from 2002"),
    ("Construction put in place — sewage & waste disposal, total", "Jan-2026 SAAR", 54.3, "$bn",
     "US Census Bureau C30", "https://www.census.gov/construction/c30/",
     "FRED series TLSWDCONS / TLSWDCON. CAUTION: includes solid waste facilities"),
    ("Construction put in place — sewage & waste disposal, public", "Jan-2026 SAAR", 53.0, "$bn",
     "US Census Bureau C30", "https://www.census.gov/construction/c30/",
     "FRED series PBSWGCONS / PBSWGCON"),
    ("Local capital spending — sewer, cumulative", "2012-2024", 350, "$bn",
     "US Conference of Mayors, 2025 Public Infrastructure Spending",
     "https://www.usmayors.org/p3/2025-public-infrastructure-spending/", "Report PDF, annual detail inside"),
    ("Local capital spending — water supply, cumulative", "2012-2024", 226, "$bn",
     "US Conference of Mayors", "https://www.usmayors.org/p3/2025-public-infrastructure-spending/", "Report PDF"),
    ("All public community-asset capital spending", "2012", 279, "$bn", "US Conference of Mayors",
     "https://www.usmayors.org/p3/2025-public-infrastructure-spending/", "Report PDF"),
    ("All public community-asset capital spending", "2024", 492, "$bn", "US Conference of Mayors",
     "https://www.usmayors.org/p3/2025-public-infrastructure-spending/", "+76% over 2012"),

    # --- federal programmes ---
    ("Total annual SRF funding (federal)", "FY2021", 2.7, "$bn", "National League of Cities",
     "https://www.nlc.org/article/2026/05/15/what-congress-needs-to-advance-on-water-infrastructure-for-americas-communities/",
     "CRS appropriations tables give the full fiscal-year series"),
    ("Total annual SRF funding (federal, incl. IIJA)", "FY2022-26 avg", 11.4, "$bn",
     "National League of Cities",
     "https://www.nlc.org/article/2026/05/15/what-congress-needs-to-advance-on-water-infrastructure-for-americas-communities/",
     "CRS IF13177 Table 1"),
    ("Clean Water SRF — total available", "FY2021", 1.64, "$bn", "CRS",
     "https://www.congress.gov/crs-product/R47474", "CRS R47474"),
    ("Clean Water SRF — regular appropriation", "FY2025", 1.6, "$bn", "CRS",
     "https://www.congress.gov/crs-product/IF12950", "CRS IF12950 Table 1"),
    ("Clean Water SRF — IIJA supplemental", "FY2025", 2.6, "$bn", "CRS",
     "https://www.congress.gov/crs-product/IF12950", "CRS IF12950 Table 1"),
    ("Drinking Water SRF — regular appropriation", "FY2025", 1.1, "$bn", "CRS",
     "https://www.congress.gov/crs-product/IF12950", "CRS IF12950 Table 1"),
    ("Drinking Water SRF — IIJA supplemental", "FY2025", 2.6, "$bn", "CRS",
     "https://www.congress.gov/crs-product/IF12950", "CRS IF12950 Table 1"),
    ("EPA water infrastructure programmes — total enacted", "FY2025", 3.04, "$bn", "P.L. 119-4, via CRS",
     "https://www.congress.gov/crs-product/IF13177", "CRS IF13177 Table 1"),
    ("EPA water infrastructure programmes — total enacted", "FY2026", 3.04, "$bn", "P.L. 119-74, via CRS",
     "https://www.congress.gov/crs-product/IF13177", "Flat vs FY2025"),
    ("Drinking Water SRF — House proposal", "FY2027", 0.910, "$bn", "House Appropriations Cttee markup",
     "https://waterfm.com/house-advances-spending-bill-with-proposed-16-srf-cut/", "Down from $1.126bn FY2026"),
    ("SRF proposed change", "FY2027", -0.16, "%", "House Appropriations Cttee markup",
     "https://waterfm.com/house-advances-spending-bill-with-proposed-16-srf-cut/", "Committee report"),
    ("IIJA — Clean Water SRF supplemental", "FY2022-26", 11.7, "$bn", "IIJA (P.L. 117-58), via CRS",
     "https://www.epa.gov/infrastructure/water-infrastructure-investments", "EPA BIL fact sheet"),
    ("IIJA — Drinking Water SRF supplemental", "FY2022-26", 11.7, "$bn", "IIJA, via CRS",
     "https://www.epa.gov/infrastructure/water-infrastructure-investments", "EPA BIL fact sheet"),
    ("IIJA — lead service line replacement", "FY2022-26", 15.0, "$bn", "IIJA, via CRS",
     "https://www.epa.gov/infrastructure/water-infrastructure-investments", "EPA BIL fact sheet"),
    ("IIJA — emerging contaminants (PFAS)", "FY2022-26", 4.0, "$bn", "IIJA, via CRS",
     "https://www.epa.gov/infrastructure/water-infrastructure-investments", "EPA BIL fact sheet"),
    ("WIFIA — cumulative financing closed", "May-2026", 23.0, "$bn", "EPA WIFIA",
     "https://www.epa.gov/wifia/wifia-program-announcements", "EPA publishes a closed-loans list"),
    ("WIFIA — total project value supported", "May-2026", 51.0, "$bn", "EPA WIFIA",
     "https://www.epa.gov/wifia/wifia-program-announcements", "EPA closed-loans list"),
    ("WIFIA — closings", "FY2025", 1.2, "$bn", "EPA WIFIA",
     "https://www.epa.gov/wifia/wifia-program-announcements", "8 loans"),
    ("WRDA 2026 — CWSRF authorisation (4 yrs)", "2026 bill", 14.0, "$bn", "Senate EPW",
     "https://www.epw.senate.gov/public/index.cfm/2026/7/epw-committee-passes-bipartisan-water-resources-development-act-of-2026",
     "Authorisation, not appropriation"),
    ("WRDA 2026 — DWSRF authorisation (5 yrs)", "2026 bill", 16.5, "$bn", "Senate EPW",
     "https://www.epw.senate.gov/public/index.cfm/2026/7/epw-committee-passes-bipartisan-water-resources-development-act-of-2026",
     "$3.3bn/yr"),

    # --- needs estimates, as a vintage series ---
    ("EPA CWNS — 20-year clean water needs", "2012 survey", 364.2, "$bn", "EPA CWNS (derived)",
     "https://www.epa.gov/cwns/clean-watersheds-needs-survey-cwns-2022-report-and-data",
     "DERIVED: 2022 total was +73% on 2012. Confirm against the 2012 report"),
    ("EPA CWNS — 20-year clean water needs", "2022 survey", 630.1, "$bn", "EPA CWNS 2022",
     "https://www.epa.gov/cwns/clean-watersheds-needs-survey-cwns-2022-report-and-data",
     "Facility-level data downloadable at sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download"),
    ("EPA DWINSA — 20-year drinking water needs", "6th (2018)", 472.6, "$bn", "EPA DWINSA 6th",
     "https://www.epa.gov/dwsrf", "EPA report to Congress"),
    ("EPA DWINSA — 20-year drinking water needs", "7th (2023)", 625.0, "$bn", "EPA DWINSA 7th",
     "https://www.epa.gov/dwsrf", "Jan-2021 dollars; $648.8bn in 2022 dollars per CRS R47878"),
    ("ASCE — water sector investment gap", "2021", 81, "$bn p.a.", "ASCE Failure to Act",
     "https://infrastructurereportcard.org/", "ASCE economic study"),
    ("ASCE — water sector investment gap", "2024", 99, "$bn p.a.", "ASCE Bridging the Gap",
     "https://bridgingthegap.infrastructurereportcard.org/", "ASCE economic study"),
    ("AWWA — 25-year drinking water needs", "2012 (Buried No Longer)", 1000, "$bn", "AWWA",
     "https://www.awwa.org/", "'will top $1 trillion over 25 years'"),
    ("AWWA — 25-year drinking water needs", "2026 (Beyond the Replacement Era)", 2250, "$bn", "AWWA",
     "https://www.awwa.org/beyond-the-replacement-era/", "Midpoint of $2.1-2.4tn, 2025 dollars"),

    # --- technical series ---
    ("Water main break rate", "2018 study", 14.0, "per 100 mi/yr", "Utah State University",
     "https://digitalcommons.usu.edu/water_rep/", "USU Buried Structures Laboratory"),
    ("Water main break rate", "2023 study", 11.1, "per 100 mi/yr", "Utah State University",
     "https://digitalcommons.usu.edu/water_rep/", "802 utilities, ~400,000 miles. -20.7% vs 2018"),
    ("Cast iron + asbestos cement share of installed mains", "2018 study", 0.41, "%",
     "Utah State University", "https://digitalcommons.usu.edu/water_rep/", ""),
    ("Cast iron + asbestos cement share of installed mains", "2023 study", 0.33, "%",
     "Utah State University", "https://digitalcommons.usu.edu/water_rep/", "-8pts in five years"),
    ("Average age of US water pipes", "1970", 25, "years", "UMich Center for Sustainable Systems",
     "https://css.umich.edu/publications/factsheets/water/us-water-supply-and-distribution-factsheet", ""),
    ("Average age of US water pipes", "2020", 45, "years", "UMich Center for Sustainable Systems",
     "https://css.umich.edu/publications/factsheets/water/us-water-supply-and-distribution-factsheet", ""),
    ("Per capita water withdrawal", "2000", 140, "gal/capita/day", "USGS",
     "https://www.usgs.gov/mission-areas/water-resources/science/water-use-united-states",
     "USGS publishes a five-yearly national compilation"),
    ("Per capita water withdrawal", "2020", 127, "gal/capita/day", "USGS",
     "https://www.usgs.gov/mission-areas/water-resources/science/water-use-united-states", "Five-yearly series"),
    ("Public-supply domestic per capita use", "2010", 88, "gal/day", "USGS",
     "https://www.usgs.gov/mission-areas/water-resources/science/water-use-united-states", "Circular 1441"),
    ("Public-supply domestic per capita use", "2015", 82, "gal/day", "USGS",
     "https://www.usgs.gov/mission-areas/water-resources/science/water-use-united-states", "Circular 1441"),
    ("Total US water withdrawals", "2015", 322, "bn gal/day", "USGS",
     "https://pubs.usgs.gov/publication/cir1441", "-9% vs 2010"),

    # --- rates ---
    ("US water + sewer bill increase", "2025", 0.051, "%", "Bluefield Research rate index (50 cities)",
     "https://www.bluefieldresearch.com/research/u-s-municipal-water-sewer-rate-index/", "Subscription series"),
    ("  cumulative five-year increase", "2020-2025", 0.242, "%", "Bluefield Research",
     "https://www.bluefieldresearch.com/research/u-s-municipal-water-sewer-rate-index/", "Subscription"),
    ("  water rates", "2024-25", 0.060, "%", "Bluefield Research",
     "https://www.bluefieldresearch.com/research/u-s-municipal-water-sewer-rate-index/", "Subscription"),
    ("  wastewater rates", "2024-25", 0.048, "%", "Bluefield Research",
     "https://www.bluefieldresearch.com/research/u-s-municipal-water-sewer-rate-index/", "Subscription"),
    ("Non-revenue water — share of treated supply", "current", 0.195, "%", "Bluefield Research",
     "https://www.bluefieldresearch.com/ns/water-losses-cost-u-s-utilities-us6-4-billion-annually/", ""),
    ("Non-revenue water — lost revenue", "current", 6.4, "$bn p.a.", "Bluefield Research",
     "https://www.bluefieldresearch.com/ns/water-losses-cost-u-s-utilities-us6-4-billion-annually/", ""),
]
