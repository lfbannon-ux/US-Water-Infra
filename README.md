# US Water Infrastructure Analysis

An investor-oriented analysis of US water and wastewater infrastructure spending, forward
budgets, and the engineering reality behind replacement demand — framed against the two
listed distributors with the most direct exposure: **Core & Main (CNM)** and **Ferguson
Enterprises (FERG)**.

## Contents

| Document | What it covers |
| --- | --- |
| [`analysis/01-historical-spending.md`](analysis/01-historical-spending.md) | Who actually pays for US water infrastructure — federal, state, municipal — 1956 to 2026, and how each dollar reaches CNM/FERG |
| [`analysis/02-forward-budget.md`](analysis/02-forward-budget.md) | What annual spend should look like FY2026–2035: needs estimates vs. real budgets, the IIJA cliff, and a transparent build-up model |
| [`analysis/03-technical-drivers.md`](analysis/03-technical-drivers.md) | Why the infrastructure actually needs replacement — materials, failure mechanisms, break-rate data, and the evidence that cuts *against* the consensus |
| [`analysis/04-company-linkage.md`](analysis/04-company-linkage.md) | Sizing CNM and FERG against the addressable market, sensitivity to the funding cliff, and what to monitor |
| [`analysis/05-sources-and-caveats.md`](analysis/05-sources-and-caveats.md) | Every source, its known bias, and where this analysis is uncertain |
| [`analysis/06-asset-level-data-sources.md`](analysis/06-asset-level-data-sources.md) | Where pipe installation year and repair history actually exist in the public record — and where they don't |
| [`US-Water-Infrastructure-Analysis.xlsx`](US-Water-Infrastructure-Analysis.xlsx) | 19-tab workbook: every figure with its source, a live formula-driven forward model, **Annual** and **Quarterly** tabs holding the full downloaded company history plus 74 sourced macro series, and **Evidence and Monitor** carrying verbatim management commentary with independent checks |
| [`data/series.py`](data/series.py) | The raw data behind those tabs, as a plain Python module — every period carries its source URL |
| [`data/SERIES-LINKS.md`](data/SERIES-LINKS.md) | **Every time-series download link** — 23 FRED series with direct CSV endpoints, plus 32 bulk data portals and primary documents |
| [`data/fetch_series.py`](data/fetch_series.py) | Run it on a networked machine to pull every FRED series to CSV and build a merged table. No API key needed |
| [`data/series_catalogue.csv`](data/series_catalogue.csv) | The same catalogue, machine-readable |

## Published report

A designed, single-page version of this analysis (with charts) is published as an artifact:
**[The Buried Balance Sheet](https://claude.ai/code/artifact/35f197f4-2b41-4874-a67f-fc33c277f891)**.
The source is checked in as [`report.html`](report.html).

## Headline conclusions

1. **Federal money is a rounding error at the margin, not the base.** State and local
   governments fund 92–96% of US water infrastructure spending, and have done so
   continuously since 1956. The IIJA supplemental — which expires 30 September 2026 — was
   large in *federal* terms (a ~4x increase in annual SRF capitalization) but equates to
   **12.8% of the $68bn national water capital base gross, and ~9.9% net** of the share that
   revolves back into state funds.
2. **The "cliff" is real but lagged and partially self-refilling.** Only about a third of
   IIJA water money had reached municipalities as of mid-2026; a material share was lent,
   not granted, and revolves back into state funds. The drawdown is a 2027–2029 headwind
   of low-single-digit percentage points on national capex, not a step-change.
3. **The capital base is $68bn, not the $88bn a naive reading of Census construction data
   gives.** CBO puts water utilities capital spending at $59bn in 2023 ($114bn more in O&M);
   escalated and cross-checked against Census, ASCE and AWWA, three independent routes
   converge on ~$68bn for 2026. Getting this right makes the federal cliff proportionally
   *larger* and reveals a real ~12% documented funding gap.
4. **Rates and municipal bonds are the actual funding engine, and both are inflecting up.**
   US water and sewer bills rose 5.1% in 2025 and 24.2% cumulatively over five years,
   outpacing CPI. This is the variable that matters most for distributor revenue.
5. **The engineering case for replacement is genuine but narrower than the advocacy
   numbers imply.** Roughly 770,000 miles of water main — a third of the network — is over
   50 years old, and cast iron fails at nearly ten times the rate of PVC. But national
   break rates *fell 20%* between 2018 and 2023, per capita demand is declining, and the
   headline "needs" figures come from surveys with documented upward bias.
6. **Regulation, not decay, is the marginal spending driver through 2030.** Lead service
   line replacement (9.2M lines) and PFAS treatment are calendar-dated legal obligations
   with hard deadlines. Corroding pipe is a discretionary, deferrable expense; a consent
   decree is not.
7. **There is no national water pipe registry — but pipe age is obtainable utility by
   utility.** Gas pipelines have PHMSA's By-Decade Inventory; water has no equivalent, and
   SDWIS holds no asset data. Installation year is nevertheless published at *segment level*
   by many municipal GIS open-data portals, and repair history is recoverable from water main
   break datasets and street-opening permits. See
   [`06-asset-level-data-sources.md`](analysis/06-asset-level-data-sources.md).

## Data access limitation

Direct retrieval of primary documents was attempted and re-attempted. Every external host
tested is blocked by this environment's network egress allowlist — `cbo.gov`, `epa.gov`,
`census.gov`, `congress.gov`, `everycrsreport.com`, `fred.stlouisfed.org`,
`infrastructurereportcard.org`, `digitalcommons.usu.edu`, even `wikipedia.org`. The allowlist
covers package registries, GitHub and Anthropic only. Public-sector figures therefore come via
search results summarising those primary documents; each is attributed to the correct source,
but **verify headline numbers against the source document before relying on them**. Company
financials came from Quartr's primary filings and do not carry this caveat.

Retested since: still blocked. Only GitHub is reachable. Company financials **were** downloaded
live, from Quartr's API, and carry per-period source URLs. The macro series on the `Annual` tab
are compiled from published figures, each with a link and the exact retrieval route (FRED series
ID, CRS table reference, EPA portal) so they can be refreshed automatically once network access
allows.

To lift this, the environment's network policy would need widening — see
https://code.claude.com/docs/en/claude-code-on-the-web.

## Method note

Company financials, segment mix and management commentary are sourced from Quartr
(primary filings, earnings decks and call transcripts). Public spending and technical
data come from CBO, EPA, USGS, GAO, Census, ASCE, AWWA, Utah State University and
Bluefield Research, each cited inline. Every derived figure states its inputs.

Data sourced from Quartr for all company-level financials.
