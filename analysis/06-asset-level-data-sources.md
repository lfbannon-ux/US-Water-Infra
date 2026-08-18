# 6. Pipe Age and Repair History — What Is Actually in the Public Record

*Answering: can you find pipeline age, or the last period of repair, from public sources?*

---

## 6.1 The short answer

**At the individual utility level: yes, often at segment or address granularity, and it is free.
Nationally: no — and the gap is structural, not accidental.**

The contrast that makes this concrete is gas. For natural gas and hazardous liquid pipelines,
operators must file annual reports to PHMSA, and PHMSA publishes a
[**By-Decade Inventory**](https://www.phmsa.dot.gov/data-and-statistics/pipeline-replacement/decade-inventory)
— national mileage broken out by decade of installation, updated yearly, for gas distribution,
gas transmission and hazardous liquid. Material, diameter, age and mileage all reported.

**Water has no equivalent, and never has.** There is no federal reporting requirement for pipe
age. SDWIS — the federal drinking water database — carries compliance, violations, enforcement
and basic system inventory, but no distribution-system asset data. Responsibility sits with
~50,000 community water systems, each of which decides for itself what to publish.

The consequence for the analysis in this repo: **national pipe-age figures are all survey
estimates, not censuses**, and should be read as such.

---

## 6.2 Tier 1 — genuinely asset-level, and genuinely public

This is where "pipeline age" and "last repair" actually exist as data rather than estimates.

### (a) Municipal GIS open-data portals — the single best source for pipe age

Many US utilities publish their water main GIS layer as open data, one record per pipe
segment, typically carrying **installation year, material, diameter, length** and sometimes
lining status and pressure zone. Published via ArcGIS Hub, Socrata or data.gov.

| Example | What it is |
| --- | --- |
| [Seattle Public Utilities — Water Mains](https://data-seattlecitygis.opendata.arcgis.com/) | Segment-level main layer, plus separate Water Services and a "Presumed Unlined" layer (a direct condition flag). Last updated June 2026. |
| [Seattle GeoData](https://data-seattlecitygis.opendata.arcgis.com/) / [data.seattle.gov](https://data.seattle.gov/) | Portal hosting the above |
| [Open Data DC](https://opendata.dc.gov/) | DC Water layers including materials |
| [Baltimore Service Line Partnership](https://service-line-partnership-baltimoredpw.hub.arcgis.com/) | Service line material identification hub |
| [data.gov geospatial catalogue](https://catalog.data.gov/dataset?metadata_type=geospatial) | Federated search across city portals |

**This is the real answer to "pipeline age."** A single query over one of these layers gives a
vintage histogram for that utility — how many miles installed per decade, by material — which
is exactly what PHMSA publishes nationally for gas and nobody publishes nationally for water.

### (b) Water main break datasets — the closest thing to "last repair"

[**DC Water's open data portal**](https://www.dcwater.com/resources/open-data-portal/water-main-breaks-dashboard)
publishes **five years of water main breaks, updated weekly, with location** — dashboard plus
downloadable data. That is a location-and-date record of where the system has failed and been
repaired. Several other large utilities publish equivalents.

Note what this is *not*: it is a record of **breaks**, not of planned replacement. A segment
replaced on schedule generates no break record. Read the two together — a segment with old
install year and no breaks may have been quietly relined or replaced.

### (c) Street opening / excavation permits — the underused proxy

Every excavation in a city street requires a permit, and those permits are records with a
location, a date, an applicant and a stated purpose. NYC runs
[NYCStreets](https://streetworksmanual.nyc/) permit management; Chicago's CDOT
[Office of Underground Coordination](https://www.chicago.gov/city/en/depts/cdot/provdrs/construction_information.html)
handles public-way opening permits. Both cities publish permit data through their open data
portals.

This is the best available public proxy for **"last period of repair"** on a given street: who
dug, where, when, and why. It captures planned replacement that break datasets miss.

### (d) Lead service line inventories — new, mandated, and address-level

The most significant *new* public asset record in the sector, and it exists because of
regulation rather than voluntary transparency:

| Requirement | Detail |
| --- | --- |
| Initial inventory deadline | **16 October 2024** — every community and NTNC water system |
| Public accessibility | **Mandatory.** Systems serving **>50,000 people must publish it online** |
| Contents | Service line material by location, including lead, galvanized-requiring-replacement, and *unknown* |
| Baseline inventory | **1 November 2027** under the LCRI — all service lines *and connectors*, regardless of ownership |
| Replacement plan | Publicly accessible, online for systems >50,000, **updated annually** |

State-level searchable dashboards already exist, including
[New York State's Lead Service Line Inventory Map](https://health.data.ny.gov/Health/New-York-State-Lead-Service-Line-Inventory-Map/fkii-zkcq)
and [Minnesota's Lead Infrastructure Transparency Tool](https://maps.umn.edu/LSL/) (address
search). Coverage and quality vary by state; the
[Environmental Policy Innovation Center](https://www.policyinnovation.org/insights/digging-into-lead-service-line-mapping-and-inventories)
tracks who has published what.

**Why this matters for the forecast:** the annually-updated replacement plans required from
November 2027 will, for the first time, create a rolling public record of *how fast lead
replacement is actually happening* — a direct, checkable read on a multi-billion-dollar
line item in the model.

---

## 6.3 Tier 2 — system-level, public, and the most useful for an investor

### (a) Municipal bond official statements — the best-value source in the sector

[**MSRB EMMA**](https://emma.msrb.org/) is free and holds official statements for essentially
every municipal bond issued since 1990, plus ongoing continuing-disclosure filings.

A water or sewer revenue bond official statement typically contains a system description with
**miles of main, material mix, age profile, treatment capacity, historical and projected
capital spending, the CIP, replacement rates, rate history and rate covenants** — because
disclosure liability compels the issuer to describe the asset it is borrowing against.

For anyone modelling distributor demand, this is the highest-density public source available,
and it updates every time a utility comes to market.

### (b) Asset management plans and capital improvement plans

Utilities increasingly publish these directly — for example
[Sacramento Suburban Water District's Distribution Main Asset Management Plan](https://www.sswd.org/departments/engineering/reports/distribution-main-asset-management-plan).
A serious plan registers every pipe segment with material, diameter, installation year,
replacement value and maintenance history, and translates risk scores into a sequenced CIP.
Where published, it gives both the age profile and the forward replacement schedule.

### (c) Investor-owned utilities — 10-Ks and state PUC rate cases

The regulated water utilities disclose replacement pace directly, and it is auditable:

| Disclosure | Source |
| --- | --- |
| Pipe renewal rate improved from a **250-year replacement cycle (2009)** to an approximate **125-year cycle by 2028** | American Water 10-K |
| ~**2,000 miles** of mains and collection pipe to be replaced 2024–2028 | American Water 10-K |
| **$34–38bn** of capital investment over ten years, largely pipe replacement and treatment upgrades | American Water 10-K |

State PUC rate-case dockets go further: **depreciation studies** filed in rate cases set
assumed service lives by asset class, and plant-in-service schedules show vintage. These are
public docket filings.

A 125-year replacement cycle against a **53-year observed average failure age** is the
industry's own admission of the gap, stated in an SEC filing rather than an advocacy report.
That makes it one of the more credible data points available.

### (d) Consent decrees

CSO and SSO consent decrees lodged by DOJ/EPA are public and typically annex detailed system
condition assessments and dated remediation schedules — effectively a court-supervised,
published asset plan for the affected collection system.

---

## 6.4 Tier 3 — national aggregates, which are estimates not censuses

| Source | What it gives | Limitation |
| --- | --- | --- |
| [USU, *Water Main Break Rates in the USA and Canada*](https://digitalcommons.usu.edu/water_rep/) (Dec 2023) | Break rate and age by material; **avg failure age 53 yrs**; 33% of mains >50 yrs; 86% of cast iron >50 yrs | Survey of **802 utilities, ~400,000 miles — >17%** of the 2.3m miles in US+Canada. Best available, still a sample |
| [EPA CWNS 2022](https://www.epa.gov/cwns/clean-watersheds-needs-survey-cwns-2022-report-and-data) | **Facility-level** project and needs data, downloadable as CSV or Access from [sdwis.epa.gov](https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download) | Projects and costs, **not pipe age**. Wastewater only |
| EPA DWINSA (7th) | National and state needs, 9.2m lead service lines | Aggregated; underlying utility responses not public |
| [UMich Center for Sustainable Systems factsheet](https://css.umich.edu/publications/factsheets/water/us-water-supply-and-distribution-factsheet) | Average age of US water pipes **45 years in 2020**, up from 25 years in 1970 | Derived estimate |

### What does not exist

- **No federal water analogue to PHMSA's By-Decade Inventory.** No agency collects water pipe
  age.
- **SDWIS contains no distribution-system asset inventory.**
- **[PIPEiD](https://www.pipeid.org/)** — Virginia Tech's SWIM Center, funded by the Bureau of
  Reclamation, has compiled data from **500+ US water utilities and 100 federal facilities** to
  build exactly this national pipeline database. But it is a *secured* platform built for
  utility decision support, not an open public dataset. Its continued existence is the clearest
  evidence that the gap is real and recognised.
- **AWIA §2013 risk and resilience assessments are confidential by statute** — deliberately, on
  security grounds.

---

## 6.5 How to actually build a bottom-up view

If the goal is to sanity-check distributor guidance against physical replacement demand rather
than trusting national estimates:

1. **Select** the 20–30 utilities with the largest capital programmes (identifiable from EMMA
   issuance volume and CWNS project data).
2. **Pull each one's water main GIS layer** and build a vintage histogram: miles by installation
   decade and material. Compute the implied replacement rate from year-on-year layer changes.
3. **Pull the EMMA official statement and CIP** for the stated forward capital plan, and the
   continuing-disclosure filings for actuals versus plan.
4. **Pull the LSL inventory** for service line counts, and from November 2027 the annually
   updated replacement plan for realised pace.
5. **Pull break datasets and street-opening permits** to validate that stated replacement is
   physically happening.

That produces a genuinely bottom-up, verifiable demand estimate for a defined share of the
market — and one that can be compared directly against what Core & Main and Ferguson say about
municipal volumes.

### Known limitations of that approach

- **Coverage is skewed to large, well-resourced utilities.** Most of the ~50,000 community water
  systems are small and publish nothing. Extrapolating from the transparent ones overstates
  system quality and understates need.
- **Installation year is frequently null** for the oldest segments — precisely the ones that
  matter most. Absence of a date is itself a signal.
- **"Last repair" is almost never an attribute.** Breaks and excavation permits are proxies, and
  they miss trenchless rehabilitation such as CIPP lining and pipe bursting, which leaves little
  surface trace.
- **Schemas are not standardised** across utilities, so combining layers requires per-utility
  mapping. This is the specific problem PIPEiD exists to solve, and it has not been solved.

---

## 6.6 Verification caveat

**None of the portals or datasets above could be opened from the session that produced this
document.** This environment's network egress allowlist blocks all external hosts, so the
descriptions here are built from search evidence about what those sources contain, not from
inspecting them directly. URLs are given so they can be checked.

Before relying on any single dataset, confirm its actual schema — specifically whether an
installation-year field is present and how sparsely it is populated. That varies by utility and
is the difference between a usable vintage histogram and a misleading one.

---

**Back to:** [3. Technical Drivers](03-technical-drivers.md) · [Index](../README.md)
