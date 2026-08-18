"""Build the US Water Infrastructure analysis workbook.

Every figure carries a source. Model sheets are formula-driven off the
Assumptions tab so the reader can change inputs and recalculate.
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment

# ---------------------------------------------------------------- style kit
FONT = "Arial"
NAVY = "1F3B52"
RULE = "BFCBD4"
BAND = "EEF2F5"
YELL = "FFFF00"

BLUE_IN = Font(name=FONT, size=10, color="0000FF")            # hardcoded input
BLACK = Font(name=FONT, size=10)                              # formula / text
GREEN_LINK = Font(name=FONT, size=10, color="008000")         # cross-sheet link
BOLD = Font(name=FONT, size=10, bold=True)
MUTED = Font(name=FONT, size=9, color="5C6E7C")
H1 = Font(name=FONT, size=16, bold=True, color=NAVY)
H2 = Font(name=FONT, size=11, bold=True, color=NAVY)
HDR = Font(name=FONT, size=9, bold=True, color="FFFFFF")

HDR_FILL = PatternFill("solid", fgColor=NAVY)
BAND_FILL = PatternFill("solid", fgColor=BAND)
YELL_FILL = PatternFill("solid", fgColor=YELL)

THIN = Side(style="thin", color=RULE)
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
UNDER = Border(bottom=THIN)

WRAP = Alignment(wrap_text=True, vertical="top")
TOP = Alignment(vertical="top")
CTR = Alignment(horizontal="center", vertical="center")
RIGHT = Alignment(horizontal="right", vertical="top")

F_USD = '$#,##0;($#,##0);"-"'
F_USD1 = '$#,##0.0;($#,##0.0);"-"'
F_NUM1 = '#,##0.0;(#,##0.0);"-"'
F_NUM = '#,##0;(#,##0);"-"'
F_PCT = '0.0%;(0.0%);"-"'
F_X = '0.0x'

wb = Workbook()
wb.remove(wb.active)


def sheet(name, widths, title, subtitle=None, tab=None):
    ws = wb.create_sheet(name)
    ws.sheet_properties.tabColor = tab or NAVY
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws["A1"] = title
    ws["A1"].font = H1
    ws.row_dimensions[1].height = 22
    if subtitle:
        ws["A2"] = subtitle
        ws["A2"].font = MUTED
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = "A4"
    return ws


def head(ws, row, labels, start=1, height=30):
    """Write a header band."""
    ws.row_dimensions[row].height = height
    for j, lab in enumerate(labels):
        c = ws.cell(row=row, column=start + j, value=lab)
        c.font = HDR
        c.fill = HDR_FILL
        c.alignment = Alignment(wrap_text=True, vertical="bottom")
        c.border = BOX
    return row + 1


def row(ws, r, vals, start=1, fonts=None, fmts=None, band=False, aligns=None):
    for j, v in enumerate(vals):
        c = ws.cell(row=r, column=start + j, value=v)
        c.font = (fonts[j] if fonts and j < len(fonts) and fonts[j] else BLACK)
        if fmts and j < len(fmts) and fmts[j]:
            c.number_format = fmts[j]
        c.alignment = (aligns[j] if aligns and j < len(aligns) and aligns[j] else WRAP)
        c.border = BOX
        if band:
            c.fill = BAND_FILL
    return r + 1


def section(ws, r, text):
    ws.cell(row=r, column=1, value=text).font = H2
    return r + 1


def note(ws, r, text):
    c = ws.cell(row=r, column=1, value=text)
    c.font = MUTED
    c.alignment = WRAP
    return r + 1


YEARS = list(range(2026, 2036))          # C..L on the model sheets
COLS = [get_column_letter(3 + i) for i in range(len(YEARS))]

# ============================================================ 1. READ ME
ws = sheet("Read Me", [46, 62, 46], "US Water Infrastructure — Analysis Workbook",
           "Historical spending · forward budget model · technical drivers · Core & Main and Ferguson")
r = 4
r = section(ws, r, "What this workbook contains")
r = note(ws, r, "A quantitative companion to the written analysis. Fourteen tabs covering who funds US water "
                "infrastructure, what annual spend should look like through 2035, the engineering evidence for "
                "replacement, and how both flow through to the two listed distributors with direct exposure.")
r += 1
r = head(ws, r, ["Tab", "What it holds", "Formula-driven?"])
for t, d, f in [
    ("Dashboard", "Headline figures pulled from the other tabs", "Yes — all links"),
    ("Assumptions", "Every model input in one place. THIS IS THE TAB TO EDIT.", "Inputs (blue/yellow)"),
    ("Forward Model", "National water capital spending build-up, 2026–2035", "Yes"),
    ("Scenarios", "Bear / base / bull, driven off the Assumptions levers", "Yes"),
    ("Historical Spending", "CBO 1956–2023 series, Census construction, local capital", "Partly"),
    ("Federal Programs", "SRF, IIJA, WIFIA, earmarks, WRDA 2026", "Partly"),
    ("Needs Estimates", "The four published studies, annualised and reconciled", "Yes"),
    ("Pipe and Assets", "USU break rates, miles by material, asset inventory", "Yes"),
    ("Regulatory", "Lead & Copper Rule Improvements, PFAS, CSO consent decrees", "Partly"),
    ("Core and Main", "Five-year P&L, end-market mix, guidance, derived metrics", "Yes"),
    ("Ferguson", "Eight-year P&L, US customer groups, waterworks estimate", "Yes"),
    ("Comparison", "Side by side plus revenue sensitivity to market growth", "Yes"),
    ("Sources", "Every source with its known interest or bias", "No"),
]:
    r = row(ws, r, [t, d, f])
r += 1

r = section(ws, r, "Colour legend")
r = head(ws, r, ["Format", "Meaning", "Example"])
for a, b, c_, fnt, fill in [
    ("Blue text", "Hardcoded input — safe to change", "68.0", BLUE_IN, None),
    ("Black text", "Formula — do not overwrite", "SUM(B2:B9)", BLACK, None),
    ("Green text", "Link to another tab in this workbook", "'Assumptions'!B5", GREEN_LINK, None),
    ("Yellow fill", "Key assumption the reader should review", "growth rate", BLACK, YELL_FILL),
]:
    r = row(ws, r, [a, b, c_], fonts=[BOLD, BLACK, fnt])
    if fill:
        ws.cell(row=r - 1, column=3).fill = fill
r += 1

r = section(ws, r, "Method and provenance")
for t in [
    "Company financials, segment mix, guidance and management quotations: sourced from Quartr — primary "
    "earnings releases, investor presentations and call transcripts. Core & Main Q1 FY2026 (10 Jun 2026) and "
    "FY2025 results (24 Mar 2026); Ferguson Q2 CY2026 (10 Aug 2026) and CY2025 transition period (24 Feb 2026).",
    "Public spending and technical data: CBO, US Census Bureau, Congressional Research Service, EPA, EPA Office "
    "of Inspector General, GAO, USGS, ASCE, AWWA, Utah State University and Bluefield Research. Each figure is "
    "attributed on its own row.",
    "Derived figures are computed by formula from cited inputs, never typed as results. Where a number is an "
    "estimate rather than a reported figure it is labelled ESTIMATE on its row.",
]:
    r = note(ws, r, t)
    r += 1

r = section(ws, r, "Caveats that belong on the front page")
for t in [
    "DATA ACCESS. This workbook was assembled in an environment whose network policy blocked direct retrieval "
    "from cbo.gov, epa.gov, census.gov, congress.gov, fred.stlouisfed.org and infrastructurereportcard.org. "
    "Public-sector figures were obtained via search results summarising those primary documents. Attributions "
    "are to the correct primary source, but VERIFY EACH HEADLINE NUMBER against the source document before "
    "relying on it for an investment decision. Company financials do not carry this caveat — they came from "
    "Quartr's primary filings.",
    "THE CAPITAL BASE. The $68bn 2026 base on the Assumptions tab is a reconciliation of four independent "
    "sources, not a single reported figure — see the Needs Estimates tab for the derivation. An earlier draft "
    "of this analysis used $88bn, which was Census construction put in place; that series bundles solid waste "
    "with sewerage and includes private work, and overstates water capital spending by roughly 30%.",
    "NO VALUATION. This workbook contains no valuation, no price target and no recommendation. It sizes a "
    "market, models its trajectory, and tests the engineering claims underneath it.",
]:
    r = note(ws, r, t)
    r += 1
ws.cell(row=r, column=1, value="Built August 2026.").font = MUTED

# ============================================================ 2. ASSUMPTIONS
ws = sheet("Assumptions", [40, 14, 12, 62], "Assumptions",
           "Blue = editable input. Every model figure elsewhere in this workbook resolves back to this tab.",
           tab="0B5FA5")
r = 4
r = section(ws, r, "Core model inputs")
r = head(ws, r, ["Input", "Value", "Unit", "Basis"])
A_BASE, A_GROW = r, r + 1
r = row(ws, r, ["National water capital spending, 2026", 68.0, "$bn",
                "Reconciliation of four sources — see Needs Estimates tab. CBO water utilities capital $59bn "
                "(2023) escalated; Census adjusted for solid-waste content; ASCE and AWWA implied."],
        fonts=[BOLD, BLUE_IN, BLACK, MUTED], fmts=[None, F_NUM1, None, None])
ws.cell(row=A_BASE, column=2).fill = YELL_FILL
r = row(ws, r, ["Organic growth rate, nominal", 0.045, "% p.a.",
                "Bluefield treatment capex CAGR 4.4%; water and sewer rate growth ~5%."],
        fonts=[BOLD, BLUE_IN, BLACK, MUTED], fmts=[None, F_PCT, None, None])
ws.cell(row=A_GROW, column=2).fill = YELL_FILL
A_GROSS = r
r = row(ws, r, ["IIJA gross federal step-down", 8.7, "$bn p.a.",
                "Annual SRF funding fell from ~$2.7bn (FY2021) to ~$11.4bn (FY2022-26) — National League of Cities."],
        fonts=[BOLD, BLUE_IN, BLACK, MUTED], fmts=[None, F_NUM1, None, None])
A_REV = r
r = row(ws, r, ["Less: permanent revolving offset", 2.0, "$bn p.a.",
                "ESTIMATE. ~50/50 grant vs loan split implies ~$25bn permanent SRF corpus supporting ongoing lending."],
        fonts=[BOLD, BLUE_IN, BLACK, MUTED], fmts=[None, F_NUM1, None, None])
A_NET = r
r = row(ws, r, ["Net steady-state IIJA drag", f"=B{A_GROSS}-B{A_REV}", "$bn p.a.",
                "Formula. The figure that actually leaves the system once revolving lending is netted off."],
        fonts=[BOLD, BOLD, BLACK, MUTED], fmts=[None, F_NUM1, None, None])
A_PCT = r
r = row(ws, r, ["  as % of the 2026 capital base", f"=B{A_NET}/B{A_BASE}", "%",
                "Formula. The honest measure of the funding cliff."],
        fonts=[BLACK, BOLD, BLACK, MUTED], fmts=[None, F_PCT, None, None])
r += 1

r = section(ws, r, "Scenario levers")
r = head(ws, r, ["Scenario", "Organic growth", "IIJA drag ($bn)", "Regulatory adder multiplier"])
S_BEAR, S_BASE, S_BULL = r, r + 1, r + 2
r = row(ws, r, ["Bear", 0.030, 9.0, 0.5], fonts=[BOLD, BLUE_IN, BLUE_IN, BLUE_IN],
        fmts=[None, F_PCT, F_NUM1, F_X])
r = row(ws, r, ["Base", f"=B{A_GROW}", f"=B{A_NET}", 1.0], fonts=[BOLD, BLACK, BLACK, BLUE_IN],
        fmts=[None, F_PCT, F_NUM1, F_X], band=True)
r = row(ws, r, ["Bull", 0.055, 4.0, 1.1], fonts=[BOLD, BLUE_IN, BLUE_IN, BLUE_IN],
        fmts=[None, F_PCT, F_NUM1, F_X])
r = note(ws, r, "Bear: FY2027 House 16% SRF cut sustained, no WRDA reauthorisation, rate growth decelerates to 3%, "
                "LCRI struck down in part. Bull: WRDA 2026 appropriated in full, LCRI upheld, rate growth holds 5.5%.")
r += 2

r = section(ws, r, "Year-indexed drivers")
DRV = r + 1
hdr = ["Driver", "Unit"] + [str(y) for y in YEARS]
r = head(ws, r, hdr)
P_ROW = r
r = row(ws, r, ["IIJA drawdown phasing", "% of full effect", 0, 0.15, 0.40, 0.75, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        fonts=[BOLD, MUTED] + [BLUE_IN] * 10, fmts=[None, None] + [F_PCT] * 10)
L_ROW = r
r = row(ws, r, ["Lead service line adder", "$bn", 0, 2.0, 3.5, 5.0, 5.5, 5.5, 5.0, 4.5, 3.5, 2.0],
        fonts=[BOLD, MUTED] + [BLUE_IN] * 10, fmts=[None, None] + [F_NUM1] * 10)
F_ROW = r
r = row(ws, r, ["PFAS adder", "$bn", 0, 1.0, 1.8, 2.5, 2.5, 2.0, 1.5, 1.2, 1.0, 1.0],
        fonts=[BOLD, MUTED] + [BLUE_IN] * 10, fmts=[None, None] + [F_NUM1] * 10)
r += 1
r = note(ws, r, "Phasing: only about a third of the ~$50bn IIJA water money had reached municipalities by mid-2026 "
                "(Core & Main, Q1 FY2026 call), so the drawdown lands across 2027-2030 rather than at expiry.")
r = note(ws, r, "Lead adder: 9.2m lines at $4,700-$6,930 each (EPA) over the LCRI ten-year window, net of the $15bn "
                "of dedicated IIJA funding already inside the base.")
r = note(ws, r, "PFAS adder: incremental capital and O&M above base. EPA's 18 May 2026 proposal retains only PFOA "
                "and PFOS and would slip compliance to 2031, so spend shifts right and the peak is lower than the "
                "2024 six-compound rule implied.")

ASM = "Assumptions"

# ============================================================ 3. FORWARD MODEL
ws = sheet("Forward Model", [34, 13] + [11] * 10, "Forward Model — National Water Capital Spending",
           "$bn nominal. Every cell is a formula off the Assumptions tab.", tab="0B5FA5")
r = 4
r = head(ws, r, ["Line", "Basis"] + [str(y) for y in YEARS])
FM_ORG = r
vals = ["Organic base", "grows at assumed rate"]
for i, y in enumerate(YEARS):
    vals.append(f"='{ASM}'!$B${A_BASE}*(1+'{ASM}'!$B${A_GROW})^{i}")
r = row(ws, r, vals, fonts=[BOLD, MUTED] + [GREEN_LINK] * 10, fmts=[None, None] + [F_NUM1] * 10)

FM_IIJA = r
vals = ["IIJA drawdown", "net drag x phasing"]
for c in COLS:
    vals.append(f"=-'{ASM}'!$B${A_NET}*'{ASM}'!{c}${P_ROW}")
r = row(ws, r, vals, fonts=[BOLD, MUTED] + [GREEN_LINK] * 10, fmts=[None, None] + [F_NUM1] * 10)

FM_LSL = r
r = row(ws, r, ["Lead service lines", "regulatory adder"] + [f"='{ASM}'!{c}${L_ROW}" for c in COLS],
        fonts=[BOLD, MUTED] + [GREEN_LINK] * 10, fmts=[None, None] + [F_NUM1] * 10)
FM_PFAS = r
r = row(ws, r, ["PFAS", "regulatory adder"] + [f"='{ASM}'!{c}${F_ROW}" for c in COLS],
        fonts=[BOLD, MUTED] + [GREEN_LINK] * 10, fmts=[None, None] + [F_NUM1] * 10)

FM_TOT = r
r = row(ws, r, ["Total capital spending", "sum"] + [f"=SUM({c}{FM_ORG}:{c}{FM_PFAS})" for c in COLS],
        fonts=[BOLD, MUTED] + [BOLD] * 10, fmts=[None, None] + [F_NUM1] * 10, band=True)
FM_YOY = r
vals = ["  year on year", "growth"]
for i, c in enumerate(COLS):
    if i == 0:
        vals.append(None)
    else:
        p = COLS[i - 1]
        vals.append(f"=IF({p}{FM_TOT}=0,0,{c}{FM_TOT}/{p}{FM_TOT}-1)")
r = row(ws, r, vals, fonts=[BLACK, MUTED] + [BLACK] * 10, fmts=[None, None] + [F_PCT] * 10)
r += 1

r = section(ws, r, "Summary")
r = head(ws, r, ["Metric", "Value", "", "Note"])
r = row(ws, r, ["Cumulative spend 2027-2035 ($bn)", f"=SUM({COLS[1]}{FM_TOT}:{COLS[-1]}{FM_TOT})", "",
                "Base case. Sits between the escalated EPA survey floor and the ASCE/AWWA ceiling."],
        fonts=[BOLD, BOLD, BLACK, MUTED], fmts=[None, F_NUM, None, None])
r = row(ws, r, ["CAGR 2026-2035", f"=({COLS[-1]}{FM_TOT}/{COLS[0]}{FM_TOT})^(1/9)-1", "",
                "Mid-single-digit nominal. Not a boom, not a bust."],
        fonts=[BOLD, BOLD, BLACK, MUTED], fmts=[None, F_PCT, None, None])
r = row(ws, r, ["Trough growth year", f"=INDEX($C$4:$L$4,MATCH(MIN({COLS[1]}{FM_YOY}:{COLS[-1]}{FM_YOY}),"
                f"{COLS[1]}{FM_YOY}:{COLS[-1]}{FM_YOY},0)+1)", "",
                "Where the federal drawdown concentrates."],
        fonts=[BOLD, BOLD, BLACK, MUTED])
r = row(ws, r, ["Trough growth rate", f"=MIN({COLS[1]}{FM_YOY}:{COLS[-1]}{FM_YOY})", "",
                "Even at the worst point, growth stays positive."],
        fonts=[BOLD, BOLD, BLACK, MUTED], fmts=[None, F_PCT, None, None])
r += 1
r = note(ws, r, "Reading: the federal drawdown costs roughly one to one and a half percentage points of market "
                "growth in the 2029-2030 window, and nothing thereafter. There is no credible scenario in which "
                "national water capital spending falls in nominal terms.")

# ============================================================ 4. SCENARIOS
ws = sheet("Scenarios", [34, 13] + [11] * 10, "Scenarios",
           "Bear / base / bull, each driven off its own row of levers on the Assumptions tab.", tab="0B5FA5")
r = 4
r = head(ws, r, ["Scenario", "Levers"] + [str(y) for y in YEARS])
sc_rows = {}
for label, lev in [("Bear", S_BEAR), ("Base", S_BASE), ("Bull", S_BULL)]:
    sc_rows[label] = r
    vals = [label, f"g / drag / adder"]
    for i, c in enumerate(COLS):
        vals.append(
            f"='{ASM}'!$B${A_BASE}*(1+'{ASM}'!$B${lev})^{i}"
            f"-'{ASM}'!$C${lev}*'{ASM}'!{c}${P_ROW}"
            f"+'{ASM}'!$D${lev}*('{ASM}'!{c}${L_ROW}+'{ASM}'!{c}${F_ROW})"
        )
    r = row(ws, r, vals, fonts=[BOLD, MUTED] + [GREEN_LINK] * 10,
            fmts=[None, None] + [F_NUM1] * 10, band=(label == "Base"))
r += 1
r = head(ws, r, ["Spread", "Basis"] + [str(y) for y in YEARS])
SP = r
r = row(ws, r, ["Bull less bear ($bn)", "range"] +
        [f"={c}{sc_rows['Bull']}-{c}{sc_rows['Bear']}" for c in COLS],
        fonts=[BOLD, MUTED] + [BLACK] * 10, fmts=[None, None] + [F_NUM1] * 10)
r = row(ws, r, ["  as % of bear", "range"] +
        [f"={c}{SP}/{c}{sc_rows['Bear']}" for c in COLS],
        fonts=[BLACK, MUTED] + [BLACK] * 10, fmts=[None, None] + [F_PCT] * 10)
r += 1
r = section(ws, r, "Scenario endpoints")
r = head(ws, r, ["Scenario", "2030 ($bn)", "2035 ($bn)", "CAGR 2026-35"])
for label in ("Bear", "Base", "Bull"):
    sr = sc_rows[label]
    r = row(ws, r, [label, f"=G{sr}", f"=L{sr}", f"=(L{sr}/C{sr})^(1/9)-1"],
            fonts=[BOLD, BOLD, BOLD, BOLD], fmts=[None, F_NUM1, F_NUM1, F_PCT],
            band=(label == "Base"))
r += 1
r = note(ws, r, "The bear-to-bull spread by 2035 is the honest measure of confidence in this forecast. The "
                "direction, however, is up in every case — the disagreement is about pace, not sign.")

# ============================================================ 5. HISTORICAL SPENDING
ws = sheet("Historical Spending", [42, 14, 14, 14, 58], "Historical Spending",
           "Who actually pays for US water infrastructure.", tab="12724A")
r = 4
r = section(ws, r, "CBO — public spending on transportation and water infrastructure, 2023")
r = head(ws, r, ["Metric", "Value", "Unit", "Share", "Source"])
CB_TOT = r
r = row(ws, r, ["Total, all transportation and water infrastructure", 626, "$bn", None,
                "CBO, Public Spending on Transportation and Water Infrastructure 1956-2023, Feb 2025"],
        fonts=[BOLD, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_NUM, None, F_PCT, None])
r = row(ws, r, ["  as % of GDP", 0.023, "%", None, "CBO"],
        fonts=[BLACK, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None])
CB_WU = r
r = row(ws, r, ["Water utilities — total spending", 175, "$bn", f"=B{CB_WU}/B{CB_TOT}",
                "CBO via USAFacts. Water utilities take ~28% of the total."],
        fonts=[BOLD, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_NUM, None, F_PCT, None])
CB_CAP = r
r = row(ws, r, ["  of which capital", 59, "$bn", f"=B{CB_CAP}/B{CB_WU}",
                "CBO. THIS IS THE ANCHOR FOR THE FORWARD MODEL BASE."],
        fonts=[BOLD, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_NUM, None, F_PCT, None])
ws.cell(row=CB_CAP, column=2).fill = YELL_FILL
CB_OM = r
r = row(ws, r, ["  of which operations and maintenance", 114, "$bn", f"=B{CB_OM}/B{CB_WU}",
                "CBO. O&M is the majority — capital is the minority of utility spending."],
        fonts=[BLACK, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_NUM, None, F_PCT, None])
r = row(ws, r, ["State and local share of water infrastructure", 0.92, "%", None,
                "CBO. Rises to ~96% on the narrower water supply and wastewater facilities definition."],
        fonts=[BOLD, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None])
r = row(ws, r, ["Federal share of water infrastructure", 0.08, "%", None, "CBO"],
        fonts=[BOLD, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None])
r = row(ws, r, ["O&M as % of all public infrastructure spending", 0.567, "%", None,
                "CBO — $355bn of $625.8bn in 2023. Rising over time."],
        fonts=[BLACK, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None])
r = row(ws, r, ["State and local share of ALL public infrastructure", 0.79, "%", None,
                "CBO — $494.2bn of $625.8bn in 2023."],
        fonts=[BLACK, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None])
r += 1

r = section(ws, r, "Census Bureau — value of construction put in place (C30)")
r = head(ws, r, ["Category", "Value", "Unit", "Basis", "Source and caveat"])
CS_WS = r
r = row(ws, r, ["Water supply — total construction", 36.5, "$bn", "SAAR Jan-2026",
                "Census C30. Includes private work."],
        fonts=[BOLD, BLUE_IN, BLACK, MUTED, MUTED], fmts=[None, F_NUM1, None, None, None])
r = row(ws, r, ["Water supply — public construction", 34.8, "$bn", "SAAR Jan-2026", "Census C30 / FRED PBWSCONS"],
        fonts=[BLACK, BLUE_IN, BLACK, MUTED, MUTED], fmts=[None, F_NUM1, None, None, None])
CS_SW = r
r = row(ws, r, ["Sewage and waste disposal — total", 54.3, "$bn", "SAAR Jan-2026",
                "Census C30. CAUTION: bundles SOLID WASTE facilities with sewerage — overstates wastewater."],
        fonts=[BOLD, BLUE_IN, BLACK, MUTED, MUTED], fmts=[None, F_NUM1, None, None, None])
r = row(ws, r, ["Sewage and waste disposal — public", 53.0, "$bn", "SAAR Jan-2026", "Census C30"],
        fonts=[BLACK, BLUE_IN, BLACK, MUTED, MUTED], fmts=[None, F_NUM1, None, None, None])
CS_NAIVE = r
r = row(ws, r, ["Naive sum (both categories, total construction)", f"=B{CS_WS}+B{CS_SW}", "$bn", "formula",
                "This is the $88bn figure an earlier draft used as the capital base. It is NOT water capital "
                "spending — see the reconciliation on the Needs Estimates tab."],
        fonts=[BOLD, BOLD, BLACK, MUTED, MUTED], fmts=[None, F_NUM1, None, None, None])
r += 1

r = section(ws, r, "Longer-run local capital spending")
r = head(ws, r, ["Metric", "Value", "Unit", "Period", "Source"])
UM_SEW = r
r = row(ws, r, ["Local capital spending — sewer, cumulative", 350, "$bn", "2012-2024",
                "US Conference of Mayors, 2025 Public Infrastructure Spending"],
        fonts=[BOLD, BLUE_IN, BLACK, MUTED, MUTED], fmts=[None, F_NUM, None, None, None])
r = row(ws, r, ["  annual average", f"=B{UM_SEW}/13", "$bn", "formula", "Local government only"],
        fonts=[BLACK, BLACK, BLACK, MUTED, MUTED], fmts=[None, F_NUM1, None, None, None])
UM_WS = r
r = row(ws, r, ["Local capital spending — water supply, cumulative", 226, "$bn", "2012-2024",
                "US Conference of Mayors"],
        fonts=[BOLD, BLUE_IN, BLACK, MUTED, MUTED], fmts=[None, F_NUM, None, None, None])
r = row(ws, r, ["  annual average", f"=B{UM_WS}/13", "$bn", "formula", "Local government only"],
        fonts=[BLACK, BLACK, BLACK, MUTED, MUTED], fmts=[None, F_NUM1, None, None, None])
r = row(ws, r, ["All public community-asset capital spending, 2012", 279, "$bn", "2012", "US Conference of Mayors"],
        fonts=[BLACK, BLUE_IN, BLACK, MUTED, MUTED], fmts=[None, F_NUM, None, None, None])
UM_24 = r
r = row(ws, r, ["All public community-asset capital spending, 2024", 492, "$bn", "2024", "US Conference of Mayors"],
        fonts=[BLACK, BLUE_IN, BLACK, MUTED, MUTED], fmts=[None, F_NUM, None, None, None])
r = row(ws, r, ["  growth 2012-2024", f"=B{UM_24}/B{UM_24-1}-1", "%", "formula", "+76%"],
        fonts=[BLACK, BLACK, BLACK, MUTED, MUTED], fmts=[None, F_PCT, None, None, None])
r += 1

r = section(ws, r, "The real funding engine — rates, debt and water loss")
r = head(ws, r, ["Metric", "Value", "Unit", "Period", "Source"])
for lab, val, unit, per, src, fmt in [
    ("Water and sewer bill increase", 0.051, "%", "2025", "Bluefield Research, US Municipal Water & Sewer Rate Index (50 cities)", F_PCT),
    ("  cumulative five-year increase", 0.242, "%", "2020-2025", "Bluefield Research", F_PCT),
    ("  water rates", 0.060, "%", "2024-25", "Bluefield Research", F_PCT),
    ("  wastewater rates", 0.048, "%", "2024-25", "Bluefield Research", F_PCT),
    ("Water and sewer bond issuance", 27.9, "$bn", "2010 low", "Historical reference range", F_NUM1),
    ("  upper end of range", 39.9, "$bn", "2013 high", "Historical reference range", F_NUM1),
    ("Non-revenue water — share of treated supply", 0.195, "%", "current", "Bluefield Research", F_PCT),
    ("  volume lost daily", 6.75, "bn gallons/day", "current", "Bluefield Research", F_NUM1),
    ("  lost revenue", 6.4, "$bn p.a.", "current", "Bluefield Research", F_NUM1),
]:
    r = row(ws, r, [lab, val, unit, per, src], fonts=[BOLD, BLUE_IN, BLACK, MUTED, MUTED],
            fmts=[None, fmt, None, None, None])
r += 1
r = note(ws, r, "A single year of national rate increases generates more incremental utility spending capacity "
                "than the entire annual IIJA water supplemental. This is the variable that matters most for "
                "distributor revenue, and it is the one least discussed.")

# ============================================================ 6. FEDERAL PROGRAMS
ws = sheet("Federal Programs", [40, 14, 12, 20, 52], "Federal Programs",
           "Four federal channels. Only one is large, and it expires 30 September 2026.", tab="12724A")
r = 4
r = section(ws, r, "State Revolving Funds — appropriations")
r = head(ws, r, ["Item", "Value", "Unit", "Period", "Source"])
for lab, val, unit, per, src, fmt in [
    ("Total annual SRF funding, pre-IIJA", 2.7, "$bn", "FY2021", "National League of Cities", F_NUM1),
    ("Total annual SRF funding, with IIJA", 11.4, "$bn", "FY2022-26 avg", "National League of Cities — a ~4x step up", F_NUM1),
    ("Clean Water SRF — total available", 1.64, "$bn", "FY2021", "CRS", F_NUM1),
    ("Clean Water SRF — regular appropriation", 1.6, "$bn", "FY2025", "CRS", F_NUM1),
    ("Clean Water SRF — IIJA supplemental", 2.6, "$bn", "FY2025", "CRS", F_NUM1),
    ("Drinking Water SRF — regular appropriation", 1.1, "$bn", "FY2025", "CRS", F_NUM1),
    ("Drinking Water SRF — IIJA supplemental", 2.6, "$bn", "FY2025", "CRS", F_NUM1),
    ("EPA water infrastructure programs — total", 3.04, "$bn", "FY2026", "P.L. 119-74, same as FY2025 enacted (P.L. 119-4)", F_NUM1),
]:
    r = row(ws, r, [lab, val, unit, per, src], fonts=[BOLD, BLUE_IN, BLACK, MUTED, MUTED],
            fmts=[None, fmt, None, None, None])
r = note(ws, r, "Regular appropriations for EPA water infrastructure programs have been FLAT across FY2024, "
                "FY2025 and FY2026. All growth in the period came from the IIJA supplemental.")
r += 2

r = section(ws, r, "IIJA / Bipartisan Infrastructure Law supplemental — expiring")
r = head(ws, r, ["Pot", "Amount", "Unit", "Period", "Note"])
I_START = r
for lab, val, per, nt in [
    ("Clean Water SRF general supplemental", 11.7, "FY2022-26", "Predominantly loans"),
    ("Drinking Water SRF general supplemental", 11.7, "FY2022-26", "Predominantly loans"),
    ("DWSRF — lead service line replacement", 15.0, "FY2022-26", "High principal-forgiveness requirement"),
    ("DWSRF — emerging contaminants (PFAS)", 4.0, "FY2022-26", "Grant-like for disadvantaged communities"),
    ("Other pots (CWSRF emerging contaminants etc.)", 7.6, "FY2022-26", "Balance to the >$50bn headline"),
]:
    r = row(ws, r, [lab, val, "$bn", per, nt], fonts=[BOLD, BLUE_IN, BLACK, MUTED, MUTED],
            fmts=[None, F_NUM1, None, None, None])
I_TOT = r
r = row(ws, r, ["Total IIJA water supplemental", f"=SUM(B{I_START}:B{I_TOT-1})", "$bn", "FY2022-26",
                "EPA states 'over $50 billion'. Expires 30 September 2026."],
        fonts=[BOLD, BOLD, BLACK, MUTED, MUTED], fmts=[None, F_NUM1, None, None, None], band=True)
r += 1
r = section(ws, r, "The cliff arithmetic")
r = head(ws, r, ["Step", "Value", "Unit", "", "Reasoning"])
C1 = r
r = row(ws, r, ["1. Gross federal step-down", f"='{ASM}'!B{A_GROSS}", "$bn p.a.", "",
                "$11.4bn (FY22-26) less $2.7bn (FY21)"],
        fonts=[BOLD, GREEN_LINK, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None])
C2 = r
r = row(ws, r, ["  as % of the 2026 capital base", f"=B{C1}/'{ASM}'!B{A_BASE}", "%", "", "Formula"],
        fonts=[BLACK, BLACK, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None])
C3 = r
r = row(ws, r, ["2. Share not yet at municipality level", 0.67, "%", "",
                "Core & Main, Q1 FY2026 call: 'only about a third or less of it has hit the municipality level yet'"],
        fonts=[BOLD, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None])
C4 = r
r = row(ws, r, ["  dollars still to disburse", f"=B{C3}*B{I_TOT}", "$bn", "",
                "Spreads the drawdown across 2027-2030 rather than at expiry"],
        fonts=[BLACK, BOLD, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None])
C5 = r
r = row(ws, r, ["3. Permanent revolving offset", f"='{ASM}'!B{A_REV}", "$bn p.a.", "",
                "ESTIMATE. ~50/50 grant vs loan split; loans recycle into the state corpus"],
        fonts=[BOLD, GREEN_LINK, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None])
C6 = r
r = row(ws, r, ["4. Net steady-state drag", f"='{ASM}'!B{A_NET}", "$bn p.a.", "", "Formula"],
        fonts=[BOLD, GREEN_LINK, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None], band=True)
r = row(ws, r, ["  as % of the 2026 capital base", f"='{ASM}'!B{A_PCT}", "%", "",
                "The honest measure of the cliff — not the 100% often assumed"],
        fonts=[BOLD, GREEN_LINK, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None], band=True)
r += 1

r = section(ws, r, "WIFIA, earmarks and reauthorisation")
r = head(ws, r, ["Item", "Value", "Unit", "As at", "Note"])
for lab, val, unit, per, nt, fmt in [
    ("WIFIA — cumulative financing closed", 23.0, "$bn", "May 2026", "152 closed loans", F_NUM1),
    ("WIFIA — total project value supported", 51.0, "$bn", "May 2026", "Leverage, not subsidy", F_NUM1),
    ("WIFIA — capacity still available", 11.0, "$bn", "2026", "EPA waiving fees for small communities", F_NUM1),
    ("WIFIA — FY2025 closings", 1.2, "$bn", "FY2025", "8 loans", F_NUM1),
    ("WIFIA — 2026 year-to-date closings", 0.682, "$bn", "early 2026", "3 loans", F_NUM1),
    ("FY2027 House bill — proposed SRF cut", -0.16, "%", "FY2027", "Committee markup, June 2026", F_PCT),
    ("FY2027 DWSRF proposed level", 0.910, "$bn", "FY2027", "Down from $1.126bn in FY2026", F_NUM1),
    ("FY2027 earmarks — water projects", 1.0, "$bn", "FY2027", "~1,200 projects, carved OUT of SRF not added to it", F_NUM1),
    ("WRDA 2026 — CWSRF authorisation", 14.0, "$bn", "over 4 yrs", "Senate EPW text, 13 July 2026. AUTHORISATION, not appropriation.", F_NUM1),
    ("WRDA 2026 — DWSRF authorisation", 16.5, "$bn", "over 5 yrs", "$3.3bn/yr — triple current appropriations but BELOW the FY22-26 run-rate", F_NUM1),
    ("WRDA 2026 — WIFIA authorisation", 0.065, "$bn p.a.", "through FY2030", "Senate EPW", F_NUM1),
]:
    r = row(ws, r, [lab, val, unit, per, nt], fonts=[BOLD, BLUE_IN, BLACK, MUTED, MUTED],
            fmts=[None, fmt, None, None, None])

# ============================================================ 7. NEEDS ESTIMATES
ws = sheet("Needs Estimates", [40, 16, 12, 14, 56], "Needs Estimates and the Capital Base",
           "The four published studies disagree by 3x because they measure different things.", tab="A8451C")
r = 4
r = head(ws, r, ["Study", "Headline", "Unit", "Annualised ($bn)", "What it measures / whose interest"])
N1 = r
r = row(ws, r, ["EPA 7th DWINSA (Sep 2023)", 625, "$bn / 20yr", f"=B{N1}/20",
                "SRF-ELIGIBLE drinking water projects, self-reported by states. Jan-2021 dollars; $648.8bn in "
                "2022 dollars per CRS. Allocation instrument — states self-report into their own funding formula."],
        fonts=[BOLD, BLUE_IN, BLACK, BOLD, MUTED], fmts=[None, F_NUM, None, F_NUM1, None])
N2 = r
r = row(ws, r, ["EPA CWNS 2022 (Apr 2024)", 630.1, "$bn / 20yr", f"=B{N2}/20",
                "SRF-ELIGIBLE clean water needs with documentation. +73% vs 2012, but first survey with 100% "
                "state participation — which mechanically inflates the increase."],
        fonts=[BOLD, BLUE_IN, BLACK, BOLD, MUTED], fmts=[None, F_NUM1, None, F_NUM1, None])
N3 = r
r = row(ws, r, ["ASCE Bridging the Gap (2024)", 99, "$bn/yr gap", f"=B{N3}+'{ASM}'!B{A_BASE}",
                "Annualised column = gap + actual spend. Full economic need incl. resilience and growth, from the "
                "civil engineers' professional society. Up from $81bn in 2021. NOTE: ASCE separately reports "
                "wastewater+stormwater annual capital NEEDS of $99bn with a $69bn gap — the same headline number "
                "used two different ways. Route 3 of the base reconciliation uses the latter."],
        fonts=[BOLD, BLUE_IN, BLACK, BOLD, MUTED], fmts=[None, F_NUM, None, F_NUM1, None])
N4 = r
r = row(ws, r, ["AWWA Beyond the Replacement Era (Mar 2026)", 2250, "$bn / 25yr", f"=B{N4}/25",
                "Drinking water ONLY. Replacement + PFAS + lead + climate + cyber + O&M. Midpoint of $2.1-2.4tn "
                "(2025 dollars). Utility trade association; requires a 168% increase in annual capital investment."],
        fonts=[BOLD, BLUE_IN, BLACK, BOLD, MUTED], fmts=[None, F_NUM, None, F_NUM1, None])
r += 1

r = section(ws, r, "EPA surveys — combined and escalated")
r = head(ws, r, ["Step", "Value", "Unit", "", "Basis"])
E1 = r
r = row(ws, r, ["Combined annualised eligible need", f"=D{N1}+D{N2}", "$bn/yr", "", "2021/2022 dollars, un-escalated"],
        fonts=[BOLD, BOLD, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None])
E2 = r
r = row(ws, r, ["Construction cost escalation", 0.045, "% p.a.", "", "Assumed"],
        fonts=[BLACK, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None])
E3 = r
r = row(ws, r, ["Years to escalate", 4.5, "yrs", "", "Mid-2021/22 base to 2026"],
        fonts=[BLACK, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None])
E4 = r
r = row(ws, r, ["Escalated eligible need, 2026 dollars", f"=B{E1}*(1+B{E2})^B{E3}", "$bn/yr", "", "Formula"],
        fonts=[BOLD, BOLD, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None], band=True)
r += 1

r = section(ws, r, "Reconciling the capital base — four independent routes to the same number")
r = head(ws, r, ["Route", "Value", "Unit", "", "Derivation"])
R1 = r
r = row(ws, r, ["1. CBO water utilities capital, 2023", 59, "$bn", "",
                "CBO. Public sector, water supply and wastewater."],
        fonts=[BOLD, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_NUM, None, None, None])
R1b = r
r = row(ws, r, ["   escalated to 2026 at 4.5% p.a.", f"=B{R1}*(1+B{E2})^3", "$bn", "", "Formula"],
        fonts=[BLACK, BOLD, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None])
R2a = r
r = row(ws, r, ["2. Census water supply (total construction)", 36.5, "$bn", "", "Census C30, SAAR Jan-2026"],
        fonts=[BOLD, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None])
R2b = r
r = row(ws, r, ["   Census sewage and waste disposal", 54.3, "$bn", "", "Census C30, SAAR Jan-2026"],
        fonts=[BLACK, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None])
R2c = r
r = row(ws, r, ["   assumed sewerage share of that category", 0.65, "%", "",
                "ESTIMATE. The rest is solid waste disposal — landfill, waste-to-energy."],
        fonts=[BLACK, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None])
R2d = r
r = row(ws, r, ["   adjusted total, public share (95%)", f"=(B{R2a}+B{R2b}*B{R2c})*0.95", "$bn", "", "Formula"],
        fonts=[BLACK, BOLD, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None])
R3a = r
r = row(ws, r, ["3. ASCE implied wastewater + stormwater actual", 30, "$bn", "",
                "ASCE: annual capital needs $99bn, gap $69bn, so ~30% of needs met."],
        fonts=[BOLD, BLUE_IN, BLACK, BLACK, MUTED], fmts=[None, F_NUM, None, None, None])
R4a = r
r = row(ws, r, ["4. AWWA implied drinking water actual", f"=D{N4}/2.68", "$bn", "",
                "AWWA requires a 168% increase to reach its target, so current spend is target / 2.68."],
        fonts=[BOLD, BOLD, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None])
R34 = r
r = row(ws, r, ["   routes 3 + 4 combined", f"=B{R3a}+B{R4a}", "$bn", "", "Formula"],
        fonts=[BLACK, BOLD, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None])
RPRIM = r
r = row(ws, r, ["Average of routes 1 and 2 (primary)", f"=AVERAGE(B{R1b},B{R2d})", "$bn", "",
                "The two strongest routes: a non-partisan scorekeeper and official construction statistics."],
        fonts=[BOLD, BOLD, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None])
RALL = r
r = row(ws, r, ["Average of all three routes", f"=AVERAGE(B{R1b},B{R2d},B{R34})", "$bn", "",
                "Routes 3 and 4 are weaker — both read advocacy claims backwards — and pull the average down."],
        fonts=[BLACK, BOLD, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None])
RRANGE = r
r = row(ws, r, ["Implied range", f"=MIN(B{R1b},B{R2d},B{R34})", "$bn", f"=MAX(B{R1b},B{R2d},B{R34})",
                "Low to high across the three routes."],
        fonts=[BLACK, BOLD, BLACK, BOLD, MUTED], fmts=[None, F_NUM1, None, F_NUM1, None])
RAVG = r
r = row(ws, r, ["ADOPTED BASE", f"='{ASM}'!B{A_BASE}", "$bn", "",
                "Rounded to $68bn — the midpoint of the two primary routes. Sits at the upper end of the "
                "three-route range because routes 3 and 4 are derived from advocacy studies read in reverse "
                "and are the least reliable. Change it on the Assumptions tab to test the low end."],
        fonts=[BOLD, GREEN_LINK, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None], band=True)
ws.cell(row=RAVG, column=2).fill = YELL_FILL
DIFF = r
r = row(ws, r, ["  variance vs three-route average", f"='{ASM}'!B{A_BASE}/B{RALL}-1", "%", "",
                "Formula. The model is ~2.5% above the most conservative reading of the base."],
        fonts=[BLACK, BOLD, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None])
GAP = r
r = row(ws, r, ["Gap: escalated need less actual spend", f"=B{E4}-'{ASM}'!B{A_BASE}", "$bn/yr", "",
                "The documented, SRF-eligible shortfall — an order of magnitude below the ASCE headline."],
        fonts=[BOLD, BOLD, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None])
r = row(ws, r, ["  as % of actual spend", f"=B{GAP}/'{ASM}'!B{A_BASE}", "%", "", "Formula"],
        fonts=[BLACK, BOLD, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None])
r += 1
r = note(ws, r, "WHY THE FOUR STUDIES DIVERGE. The EPA surveys are floors by construction: they count only what "
                "states could document as eligible, and assume a 0.5%/yr pipe replacement rate — which imputes a "
                "200-YEAR pipe life against an observed 53-year average failure age. The ASCE and AWWA figures are "
                "ceilings by construction, produced by parties that advocate for higher appropriations. The truth "
                "is bracketed, not split.")
r += 1
r = section(ws, r, "Market-research forecasts (the view that maps to distributor revenue)")
r = head(ws, r, ["Forecast", "Value", "Unit", "Period", "Source"])
BF1 = r
for lab, val, unit, per, src, fmt in [
    ("US municipal water + wastewater treatment capex", 515.4, "$bn", "through 2035", "Bluefield Research — 4.4% CAGR", F_NUM1),
    ("  starting annual rate", 37.2, "$bn", "2026", "Bluefield Research", F_NUM1),
    ("  ending annual rate", 57.3, "$bn", "2035", "Bluefield Research", F_NUM1),
    ("  of which wastewater", 310.4, "$bn", "through 2035", "Bluefield Research — 58% of total", F_NUM1),
    ("  of which upgrades / rehab of existing assets", 406.4, "$bn", "through 2035",
     "Bluefield Research — 79%. The replacement thesis, quantified.", F_NUM1),
    ("US + Canada municipal pipe capex", 99.3, "$bn", "2026-2035", "Bluefield Research — ~$10bn/yr", F_NUM1),
]:
    r = row(ws, r, [lab, val, unit, per, src], fonts=[BOLD, BLUE_IN, BLACK, MUTED, MUTED],
            fmts=[None, fmt, None, None, None])

# ============================================================ 8. PIPE AND ASSETS
ws = sheet("Pipe and Assets", [34, 14, 14, 14, 14, 44], "Pipe and Assets — the Engineering Evidence",
           "Utah State University, Water Main Break Rates in the USA and Canada, Dec 2023.", tab="A8451C")
r = 4
r = section(ws, r, "Study scope")
r = head(ws, r, ["Metric", "Value", "Unit", "", "", "Note"])
for lab, val, unit, nt, fmt in [
    ("Utilities surveyed", 802, "count", "49 US states and all 10 Canadian provinces", F_NUM),
    ("Population served by respondents", 0.30, "%", ">30% of the US and Canada population", F_PCT),
    ("Miles of main represented", 400000, "miles", ">17% of the estimated 2.3m miles in both countries", F_NUM),
    ("Publication date", 2023, "year", "Released Feb 2024 by USU's Utah Water Research Laboratory", '0'),
]:
    r = row(ws, r, [lab, val, unit, None, None, nt], fonts=[BOLD, BLUE_IN, BLACK, BLACK, BLACK, MUTED],
            fmts=[None, fmt, None, None, None, None])
r = note(ws, r, "BIAS NOTE: the study is academic but distributed by pipe-manufacturer interests, and its "
                "material-by-material results favour PVC. It is also the best dataset available — and its "
                "finding that break rates FELL cuts against its own $452bn funding-gap headline.")
r += 2

r = section(ws, r, "Break rates and material mix")
MAT_HDR = r
r = head(ws, r, ["Material", "Breaks per 100 mi/yr", "Miles surveyed", "% of surveyed miles",
                 "% over 50 yrs old", "Failure mechanism"])
MAT0 = r
mats = [
    ("Cast iron", 28.6, 90657, 0.86, "Graphitic corrosion — iron matrix leaches away leaving a graphite skeleton "
                                     "that holds shape and pressure until it fails without warning. Plus tuberculation."),
    ("Asbestos cement", 10.3, 42365, 0.41, "Cement matrix leaches from both faces; progressive wall-strength loss. "
                                           "Handling, worker-safety and disposal premiums on replacement."),
    ("Steel", 9.2, 11358, None, "External and internal corrosion; joint and weld failure."),
    ("Ductile iron", 5.1, 108670, None, "Corrosion where unprotected; polyethylene encasement materially extends life."),
    ("PVC", 2.9, 116345, None, "Low failure rate; failures typically installation-related or from impact/third-party damage."),
]
for name, br, mi, old, mech in mats:
    r = row(ws, r, [name, br, mi, None, old, mech],
            fonts=[BOLD, BLUE_IN, BLUE_IN, BLACK, BLUE_IN, MUTED],
            fmts=[None, F_NUM1, F_NUM, F_PCT, F_PCT, None])
MAT1 = r - 1
MAT_TOT = r
r = row(ws, r, ["Total surveyed", None, f"=SUM(C{MAT0}:C{MAT1})", f"=SUM(D{MAT0}:D{MAT1})", None, "Formula"],
        fonts=[BOLD, BLACK, BOLD, BOLD, BLACK, MUTED], fmts=[None, None, F_NUM, F_PCT, None, None], band=True)
for rr in range(MAT0, MAT1 + 1):
    ws.cell(row=rr, column=4, value=f"=C{rr}/$C${MAT_TOT}").number_format = F_PCT
    ws.cell(row=rr, column=4).font = BLACK
    ws.cell(row=rr, column=4).border = BOX
NAT = r
r = row(ws, r, ["National average break rate", 11.1, None, None, None,
                "Down from 14.0 in the 2018 study — a ~20% decline in five years."],
        fonts=[BOLD, BLUE_IN, BLACK, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None, None])
R2018 = r
r = row(ws, r, ["2018 study national average", 14.0, None, None, None, "USU 2018"],
        fonts=[BLACK, BLUE_IN, BLACK, BLACK, BLACK, MUTED], fmts=[None, F_NUM1, None, None, None, None])
r = row(ws, r, ["Change 2018 to 2023", f"=B{NAT}/B{R2018}-1", None, None, None,
                "THE COUNTER-EVIDENCE: the network is measurably getting MORE reliable, not less."],
        fonts=[BOLD, BOLD, BLACK, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None, None], band=True)
CI_RATIO = r
r = row(ws, r, ["Cast iron vs PVC failure ratio", f"=B{MAT0}/B{MAT0+4}", None, None, None,
                "The single most defensible number in the replacement case."],
        fonts=[BOLD, BOLD, BLACK, BLACK, BLACK, MUTED], fmts=[None, F_X, None, None, None, None], band=True)
r += 1

r = section(ws, r, "Asset inventory and condition")
r = head(ws, r, ["Metric", "Value", "Unit", "", "", "Source"])
for lab, val, unit, src, fmt in [
    ("Drinking water transmission and distribution mains", 2200000, "miles", "EPA / ASCE", F_NUM),
    ("Community water systems", 50000, "count", "EPA — of 148,000+ public water systems total", F_NUM),
    ("Public sewers", 800000, "miles", "ASCE — plus ~500,000 miles of private laterals", F_NUM),
    ("Publicly owned treatment works", 17544, "count", "EPA CWNS 2022 — serving 270.4m people, 82% of population", F_NUM),
    ("POTW average utilisation of design capacity", 0.81, "%", "ASCE", F_PCT),
    ("POTWs at or over design capacity", 0.15, "%", "ASCE", F_PCT),
    ("Water mains over 50 years old", 0.33, "%", "USU 2023 — approximately 770,000 miles", F_PCT),
    ("Water mains beyond useful life", 0.194, "%", "USU 2023 — approximately 452,000 miles", F_PCT),
    ("Average age of failing water main", 53, "years", "USU 2023", F_NUM),
    ("Estimated cost to replace aging mains", 452, "$bn", "USU 2023, US and Canada", F_NUM),
    ("Water main breaks per year", 260000, "count", "USU 2023, US and Canada — one every two minutes", F_NUM),
    ("Annual repair cost of those breaks", 2.6, "$bn", "USU 2023", F_NUM1),
    ("Combined sewer communities", 860, "count", "EPA", F_NUM),
    ("Untreated CSO discharge", 850, "bn gallons/yr", "EPA", F_NUM),
]:
    r = row(ws, r, [lab, val, unit, None, None, src], fonts=[BOLD, BLUE_IN, BLACK, BLACK, BLACK, MUTED],
            fmts=[None, fmt, None, None, None, None])
BRK = r
r = row(ws, r, ["Implied average cost per break", "=B" + str(r - 3) + "*1000000000/B" + str(r - 4), "$", None, None,
                "Formula. Direct repair cost only — excludes boil-water notices, road closure and third-party damage."],
        fonts=[BOLD, BOLD, BLACK, BLACK, BLACK, MUTED], fmts=[None, F_USD, None, None, None, None])
r += 1

r = section(ws, r, "Demand — the evidence against capacity expansion")
r = head(ws, r, ["Metric", "Value", "Unit", "Period", "", "Source"])
for lab, val, unit, per, src, fmt in [
    ("Per capita withdrawal, 2000", 140, "gal/capita/day", "2000", "USGS", F_NUM),
    ("Per capita withdrawal, 2020", 127, "gal/capita/day", "2020", "USGS", F_NUM),
    ("Public-supply domestic per capita, 2010", 88, "gal/day", "2010", "USGS", F_NUM),
    ("Public-supply domestic per capita, 2015", 82, "gal/day", "2015", "USGS", F_NUM),
    ("Total US withdrawals, 2015", 322, "bn gal/day", "2015", "USGS — down 9% from 2010", F_NUM),
]:
    r = row(ws, r, [lab, val, unit, per, None, src], fonts=[BOLD, BLUE_IN, BLACK, MUTED, BLACK, MUTED],
            fmts=[None, fmt, None, None, None, None])
r = note(ws, r, "Public-supply withdrawals fell even as population grew 4%. The sector's spending need is almost "
                "entirely RENEWAL, not expansion — which means capacity-expansion arguments outside data-centre "
                "and Sun Belt growth corridors are weak, and some existing infrastructure is oversized for "
                "current demand.")

# ============================================================ 9. REGULATORY
ws = sheet("Regulatory", [38, 18, 12, 20, 52], "Regulatory Drivers",
           "Legally dated obligations — the highest-conviction component of the forecast.", tab="A8451C")
r = 4
r = section(ws, r, "Lead and Copper Rule Improvements")
r = head(ws, r, ["Item", "Value", "Unit", "Date / status", "Note"])
LS1 = r
r = row(ws, r, ["National lead service lines", 9200000, "count", "EPA 7th DWINSA",
                "First-ever national count."],
        fonts=[BOLD, BLUE_IN, BLACK, MUTED, MUTED], fmts=[None, F_NUM, None, None, None])
LS2 = r
r = row(ws, r, ["EPA cost per line — low", 4700, "$", "EPA", "Utilities dispute as too low."],
        fonts=[BLACK, BLUE_IN, BLACK, MUTED, MUTED], fmts=[None, F_USD, None, None, None])
LS3 = r
r = row(ws, r, ["EPA cost per line — high", 6930, "$", "EPA", "New York estimates up to $11,000."],
        fonts=[BLACK, BLUE_IN, BLACK, MUTED, MUTED], fmts=[None, F_USD, None, None, None])
LS4 = r
r = row(ws, r, ["Implied national cost — low", f"=B{LS1}*B{LS2}/1000000000", "$bn", "formula",
                "Consensus estimates cluster at $45-60bn."],
        fonts=[BOLD, BOLD, BLACK, MUTED, MUTED], fmts=[None, F_NUM1, None, None, None])
LS5 = r
r = row(ws, r, ["Implied national cost — high", f"=B{LS1}*B{LS3}/1000000000", "$bn", "formula", ""],
        fonts=[BOLD, BOLD, BLACK, MUTED, MUTED], fmts=[None, F_NUM1, None, None, None])
LS6 = r
r = row(ws, r, ["Dedicated IIJA funding", 15.0, "$bn", "FY2022-26", "Covers roughly a quarter to a third."],
        fonts=[BLACK, BLUE_IN, BLACK, MUTED, MUTED], fmts=[None, F_NUM1, None, None, None])
r = row(ws, r, ["Unfunded balance (midpoint)", f"=AVERAGE(B{LS4}:B{LS5})-B{LS6}", "$bn", "formula",
                "Must come from rates. This is the rate-driver, not the grant story."],
        fonts=[BOLD, BOLD, BLACK, MUTED, MUTED], fmts=[None, F_NUM1, None, None, None], band=True)
r = row(ws, r, ["Baseline inventory / plan deadline", None, None, "1 November 2027",
                "Inventory, replacement plan, school and childcare list, updated sampling plan."],
        fonts=[BOLD, BLACK, BLACK, BOLD, MUTED])
r = row(ws, r, ["Full replacement deadline", None, None, "2034-2037",
                "Ten years from compliance date, REGARDLESS of measured lead levels."],
        fonts=[BOLD, BLACK, BLACK, BOLD, MUTED])
r = row(ws, r, ["Litigation", None, None, "Oral argument expected Fall 2026",
                "AWWA v. EPA — challenges mandated replacement of lines 'under the control' of the utility. "
                "THE LARGEST BINARY RISK IN THIS FORECAST."],
        fonts=[BOLD, BLACK, BLACK, BOLD, MUTED])
ws.cell(row=r - 1, column=4).fill = YELL_FILL
r += 1

r = section(ws, r, "PFAS")
r = head(ws, r, ["Item", "Value", "Unit", "Date / status", "Note"])
for lab, val, unit, dt, nt, fmt in [
    ("PFOA / PFOS maximum contaminant level", 4, "ppt", "RETAINED", "EPA proposal of 18 May 2026 upholds these.", F_NUM),
    ("Original compliance deadline", None, None, "26 April 2029", "2024 final rule.", None),
    ("Proposed extended deadline", None, None, "26 April 2031", "On request, not automatic — EPA declined an automatic extension.", None),
    ("PFHxS, PFNA, GenX, Hazard Index MCLs", None, None, "PROPOSED FOR RESCISSION",
     "On legal and procedural grounds under the SDWA, NOT on the health science.", None),
    ("Comment period", None, None, "Closed 20 July 2026", "Public hearing held 7 July 2026.", None),
    ("Sector treatment cost", 50, "$bn / 20yr", "AWWA / Black & Veatch", "Trade-association model produced to argue against a stricter rule.", F_NUM),
    ("CERCLA disposal cost if designated", 3.5, "$bn p.a.", "potential", "Residuals disposal exposure.", F_NUM1),
    ("Household rate impact — low", 305, "$ p.a.", "AWWA", "", F_USD),
    ("Household rate impact — high", 3570, "$ p.a.", "AWWA", "Worst for small systems, where fewer households share the cost.", F_USD),
]:
    r = row(ws, r, [lab, val, unit, dt, nt], fonts=[BOLD, BLUE_IN, BLACK, BOLD, MUTED],
            fmts=[None, fmt, None, None, None])
r = note(ws, r, "NET EFFECT of the 2026 proposals: the PFAS opportunity is SMALLER and LATER than the 2024 rule "
                "implied. Retaining only PFOA and PFOS reduces the number of systems triggered, and slipping "
                "compliance two years pushes capital into 2029-2031. Any model built on the full six-compound "
                "rule is stale.")
r += 2
r = section(ws, r, "Other regulatory drivers")
r = head(ws, r, ["Driver", "Scale", "Unit", "Mechanism", "Note"])
for lab, val, unit, mech, nt, fmt in [
    ("CSO / SSO consent decrees", 860, "communities", "Court-supervised Clean Water Act settlements",
     "A court order is not a budget line — non-deferrable, multi-decade.", F_NUM),
    ("Untreated CSO discharge", 850, "bn gal/yr", "EPA", "Concentrated in older Northeast, Great Lakes and Pacific Northwest cities.", F_NUM),
    ("POTW end-of-life", 40, "yr design life", "1972 Clean Water Act cohort", "Equipment life 15-20 years; plants 40-50.", F_NUM),
    ("Data centre water consumption today", 18, "bn gal/yr", "New demand", "Midpoint of 17-19bn.", F_NUM),
    ("Data centre water consumption 2030", 85, "bn gal/yr", "New demand", "Midpoint of 60-110bn. 97% supplied by municipal systems.", F_NUM),
]:
    r = row(ws, r, [lab, val, unit, mech, nt], fonts=[BOLD, BLUE_IN, BLACK, MUTED, MUTED],
            fmts=[None, fmt, None, None, None])

# ============================================================ 10. CORE AND MAIN
ws = sheet("Core and Main", [34, 14, 14, 14, 14, 14, 34], "Core & Main (CNM)",
           "Fiscal years end the Sunday nearest 31 January and are labelled by end date. $m unless stated. "
           "Data sourced from Quartr.", tab="0B5FA5")
r = 4
r = section(ws, r, "Income statement — five years")
CNM_HDR = r
r = head(ws, r, ["$m", "FY end Jan-2022", "FY end Jan-2023", "FY end Jan-2024", "FY end Feb-2025",
                 "FY end Feb-2026", "Note"])
CNM_REV = r
r = row(ws, r, ["Net sales", 5004, 6651, 6702, 7441, 7647, "Quartr — standardised income statement"],
        fonts=[BOLD] + [BLUE_IN] * 5 + [MUTED], fmts=[None] + [F_NUM] * 5 + [None])
CNM_GRW = r
r = row(ws, r, ["  growth", None] + [f"={get_column_letter(3+i)}{CNM_REV}/{get_column_letter(2+i)}{CNM_REV}-1"
                                     for i in range(4)] + ["Formula"],
        fonts=[BLACK] + [BLACK] * 5 + [MUTED], fmts=[None] + [F_PCT] * 5 + [None])
CNM_GP = r
r = row(ws, r, ["Gross profit", 1280, 1795, 1818, 1980, 2059, "Quartr"],
        fonts=[BOLD] + [BLUE_IN] * 5 + [MUTED], fmts=[None] + [F_NUM] * 5 + [None])
CNM_GM = r
r = row(ws, r, ["  gross margin"] + [f"={get_column_letter(2+i)}{CNM_GP}/{get_column_letter(2+i)}{CNM_REV}"
                                     for i in range(5)] + ["Formula"],
        fonts=[BLACK] + [BLACK] * 5 + [MUTED], fmts=[None] + [F_PCT] * 5 + [None])
CNM_EB = r
r = row(ws, r, ["EBITDA (standardised)", 604, 918, 889, 905, 913, "Quartr. Company-reported Adjusted EBITDA for "
                                                                  "FY end Feb-2026 was $931m."],
        fonts=[BOLD] + [BLUE_IN] * 5 + [MUTED], fmts=[None] + [F_NUM] * 5 + [None])
CNM_EM = r
r = row(ws, r, ["  EBITDA margin"] + [f"={get_column_letter(2+i)}{CNM_EB}/{get_column_letter(2+i)}{CNM_REV}"
                                      for i in range(5)] + ["Formula"],
        fonts=[BLACK] + [BLACK] * 5 + [MUTED], fmts=[None] + [F_PCT] * 5 + [None])
CNM_OP = r
r = row(ws, r, ["Operating income", 425, 775, 740, 719, 722, "Quartr"],
        fonts=[BOLD] + [BLUE_IN] * 5 + [MUTED], fmts=[None] + [F_NUM] * 5 + [None])
CNM_NI = r
r = row(ws, r, ["Net income", 225, 366, 371, 434, 462, "Quartr"],
        fonts=[BOLD] + [BLUE_IN] * 5 + [MUTED], fmts=[None] + [F_NUM] * 5 + [None])
r = row(ws, r, ["Diluted EPS ($)", 0.55, 2.13, 2.15, 2.13, 2.31, "Quartr"],
        fonts=[BOLD] + [BLUE_IN] * 5 + [MUTED], fmts=[None] + ['$0.00'] * 5 + [None])
CNM_CAGR = r
r = row(ws, r, ["Revenue CAGR, FY22 to FY26", f"=(F{CNM_REV}/B{CNM_REV})^(1/4)-1", None, None, None, None,
                "Formula. Includes the 2021-22 inflation surge."],
        fonts=[BOLD, BOLD, BLACK, BLACK, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None, None, None])
r += 1

r = section(ws, r, "End-market and product mix — fiscal year ended 1 February 2026")
r = head(ws, r, ["Segment", "% of net sales", "Implied $m", "", "", "", "Source"])
MIX0 = r
for lab, pct in [("Municipal", 0.44), ("Non-residential", 0.38), ("Residential", 0.18)]:
    r = row(ws, r, [lab, pct, f"=B{r}*$F${CNM_REV}", None, None, None,
                    "Core & Main Q1 FY2026 investor presentation, slide 12"],
            fonts=[BOLD, BLUE_IN, BOLD, BLACK, BLACK, BLACK, MUTED],
            fmts=[None, F_PCT, F_NUM, None, None, None, None])
MIX1 = r - 1
r = row(ws, r, ["Total", f"=SUM(B{MIX0}:B{MIX1})", f"=SUM(C{MIX0}:C{MIX1})", None, None, None, "Formula"],
        fonts=[BOLD, BOLD, BOLD, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, F_PCT, F_NUM, None, None, None, None], band=True)
r += 1
r = head(ws, r, ["Split", "Share", "", "", "", "", "Source"])
for lab, pct, src in [
    ("New construction", 0.50, "Core & Main Q1 FY2026 deck"),
    ("Repair and replace", 0.50, "The least cyclical revenue in the sector — funded from rates and O&M"),
]:
    r = row(ws, r, [lab, pct, None, None, None, None, src],
            fonts=[BOLD, BLUE_IN, BLACK, BLACK, BLACK, BLACK, MUTED], fmts=[None, F_PCT, None, None, None, None, None])
r += 1

r = section(ws, r, "Market position and scale")
r = head(ws, r, ["Metric", "Value", "Unit", "", "", "", "Source"])
CNM_TAM = r
for lab, val, unit, src, fmt in [
    ("US total addressable market", 39.0, "$bn", "Core & Main deck, based on third-party research", F_NUM1),
    ("US market share", 0.20, "%", "Core & Main deck", F_PCT),
    ("US + Canada TAM", 44.0, "$bn", "Core & Main deck", F_NUM1),
    ("US + Canada market share", 0.17, "%", "Core & Main deck", F_PCT),
    ("Branches", 370, "count", "As at 3 May 2026", F_NUM),
    ("Associates", 5600, "count", "As at 3 May 2026", F_NUM),
    ("Customers", 60000, "count", "As at 3 May 2026", F_NUM),
    ("Products", 225000, "count", "As at 3 May 2026", F_NUM),
]:
    r = row(ws, r, [lab, val, unit, None, None, None, src],
            fonts=[BOLD, BLUE_IN, BLACK, BLACK, BLACK, BLACK, MUTED],
            fmts=[None, fmt, None, None, None, None, None])
CHK = r
r = row(ws, r, ["Cross-check: TAM x share", f"=B{CNM_TAM}*B{CNM_TAM+1}*1000", "$m", None, None, None,
                "Formula. Compare with reported net sales of $7,647m — internally consistent."],
        fonts=[BOLD, BOLD, BLACK, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, F_NUM, None, None, None, None, None], band=True)
r += 1

r = section(ws, r, "Q1 fiscal 2026 (quarter ended 3 May 2026) and guidance")
r = head(ws, r, ["Metric", "Q1 FY26", "Q1 FY25", "Change", "", "", "Note"])
Q0 = r
for lab, cur, pri, fmt in [
    ("Net sales ($m)", 1911, 1910, F_NUM),
    ("Gross profit ($m)", 520, 510, F_NUM),
    ("Adjusted EBITDA ($m)", 226, 224, F_NUM),
    ("Net income ($m)", 113, 105, F_NUM),
]:
    r = row(ws, r, [lab, cur, pri, f"=B{r}/C{r}-1", None, None, "Core & Main Q1 FY2026 deck"],
            fonts=[BOLD, BLUE_IN, BLUE_IN, BLACK, BLACK, BLACK, MUTED],
            fmts=[None, fmt, fmt, F_PCT, None, None, None])
r = row(ws, r, ["Gross margin", 0.272, 0.267, f"=B{r}-C{r}", None, None, "+50bps"],
        fonts=[BOLD, BLUE_IN, BLUE_IN, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, F_PCT, F_PCT, F_PCT, None, None, None])
r = row(ws, r, ["Adjusted diluted EPS ($)", 0.72, 0.68, f"=B{r}/C{r}-1", None, None, "+6%"],
        fonts=[BOLD, BLUE_IN, BLUE_IN, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, '$0.00', '$0.00', F_PCT, None, None, None])
r += 1
r = head(ws, r, ["FY2026 guidance", "Low", "High", "vs FY2025", "", "", "Note"])
G0 = r
r = row(ws, r, ["Net sales ($m)", 7800, 7900, f"=AVERAGE(B{r}:C{r})/$F${CNM_REV}-1", None, None,
                "Reaffirmed at Q1. Growth of 2-3%."],
        fonts=[BOLD, BLUE_IN, BLUE_IN, BOLD, BLACK, BLACK, MUTED],
        fmts=[None, F_NUM, F_NUM, F_PCT, None, None, None])
r = row(ws, r, ["Adjusted EBITDA ($m)", 950, 980, None, None, None, "FY2025 adjusted EBITDA was $931m"],
        fonts=[BOLD, BLUE_IN, BLUE_IN, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, F_NUM, F_NUM, None, None, None, None])
r = row(ws, r, ["Adjusted EBITDA margin", 0.122, 0.124, None, None, None, "FY2025 margin 12.2%"],
        fonts=[BOLD, BLUE_IN, BLUE_IN, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, F_PCT, F_PCT, None, None, None, None])
r += 1
r = section(ws, r, "Above-market growth initiatives")
r = head(ws, r, ["Initiative", "5-yr sales CAGR", "Size", "", "", "", "Driver"])
r = row(ws, r, ["Treatment plant solutions", "15-25%", "mid-single-digit % of net sales", None, None, None,
                "Aging facilities plus regulatory requirements; management: 'supported by durable funding' and "
                "'non-discretionary'"],
        fonts=[BOLD, BOLD, BLACK, BLACK, BLACK, BLACK, MUTED])
r = row(ws, r, ["Smart utility / AMI metering", "15-25%", "not disclosed; growing double digits", None, None, None,
                "Multi-year municipal AMI programmes; non-revenue water economics"],
        fonts=[BOLD, BOLD, BLACK, BLACK, BLACK, BLACK, MUTED])
r = note(ws, r, "The deck reports 15% and 25% five-year CAGRs for the two initiatives; the pairing is ambiguous in "
                "the source layout, so both are shown as a range rather than assigned. Management confirmed "
                "treatment plant is mid-single-digit % of sales and growing double digits.")

# ============================================================ 11. FERGUSON
ws = sheet("Ferguson", [34, 12, 12, 12, 12, 12, 12, 12, 12, 30], "Ferguson Enterprises (FERG)",
           "Fiscal years ended 31 July through FY2025; the company then moved to a 31 December year end. "
           "$m. Data sourced from Quartr.", tab="0B5FA5")
r = 4
r = section(ws, r, "Income statement — eight periods")
FG_HDR = r
r = head(ws, r, ["$m", "FY Jul-19", "FY Jul-20", "FY Jul-21", "FY Jul-22", "FY Jul-23", "FY Jul-24",
                 "FY Jul-25", "CY Dec-25", "Note"])
FG_REV = r
r = row(ws, r, ["Net sales", 22010, 21819, 22792, 28566, 29734, 29635, 30762, 31316,
                "CY Dec-25 is a transition period, not comparable to the July years"],
        fonts=[BOLD] + [BLUE_IN] * 8 + [MUTED], fmts=[None] + [F_NUM] * 8 + [None])
FG_GRW = r
r = row(ws, r, ["  growth", None] + [f"={get_column_letter(3+i)}{FG_REV}/{get_column_letter(2+i)}{FG_REV}-1"
                                     for i in range(7)] + ["Formula"],
        fonts=[BLACK] + [BLACK] * 8 + [MUTED], fmts=[None] + [F_PCT] * 8 + [None])
FG_GP = r
r = row(ws, r, ["Gross profit", 6458, 6421, 6980, 8756, 9025, 9053, 9435, 9708, "Quartr"],
        fonts=[BOLD] + [BLUE_IN] * 8 + [MUTED], fmts=[None] + [F_NUM] * 8 + [None])
FG_GM = r
r = row(ws, r, ["  gross margin"] + [f"={get_column_letter(2+i)}{FG_GP}/{get_column_letter(2+i)}{FG_REV}"
                                     for i in range(8)] + ["Formula"],
        fonts=[BLACK] + [BLACK] * 8 + [MUTED], fmts=[None] + [F_PCT] * 8 + [None])
FG_EB = r
r = row(ws, r, ["EBITDA", None, 1581, 2168, 3121, 2980, 2987, 2979, 3243, "Quartr; FY Jul-19 not available"],
        fonts=[BOLD] + [BLUE_IN] * 8 + [MUTED], fmts=[None] + [F_NUM] * 8 + [None])
FG_OP = r
r = row(ws, r, ["Operating income", 1402, 1422, 2034, 2820, 2659, 2652, 2606, 2789, "Quartr"],
        fonts=[BOLD] + [BLUE_IN] * 8 + [MUTED], fmts=[None] + [F_NUM] * 8 + [None])
FG_OM = r
r = row(ws, r, ["  operating margin"] + [f"={get_column_letter(2+i)}{FG_OP}/{get_column_letter(2+i)}{FG_REV}"
                                         for i in range(8)] + ["Formula"],
        fonts=[BLACK] + [BLACK] * 8 + [MUTED], fmts=[None] + [F_PCT] * 8 + [None])
FG_NI = r
r = row(ws, r, ["Net income", 1108, 961, 1508, 2122, 1889, 1735, 1856, 2006, "Quartr"],
        fonts=[BOLD] + [BLUE_IN] * 8 + [MUTED], fmts=[None] + [F_NUM] * 8 + [None])
r += 1

r = section(ws, r, "US net sales by customer group — quarter ended 30 June 2026")
r = head(ws, r, ["Customer group", "% of US sales", "Growth Q2 CY26", "Growth Q2 CY25", "Implied $m/qtr",
                 "", "", "", "", "Source"])
CG0 = r
cgs = [
    ("Waterworks", 0.24, 0.03, 0.15),
    ("Ferguson Home", 0.20, -0.01, 0.02),
    ("Commercial / Mechanical", 0.16, 0.15, 0.20),
    ("Residential Trade Plumbing", 0.14, 0.00, -0.02),
    ("HVAC", 0.13, 0.11, 0.01),
    ("Industrial", 0.07, 0.18, 0.06),
    ("Facilities Supply", 0.04, 0.05, 0.02),
    ("Fire & Fabrication", 0.02, -0.13, 0.05),
]
for name, sh, g1, g0 in cgs:
    r = row(ws, r, [name, sh, g1, g0, f"=B{r}*$B${r+len(cgs)-list(x[0] for x in cgs).index(name)+0}",
                    None, None, None, None, "Ferguson Q2 CY2026 deck, slide 7"],
            fonts=[BOLD, BLUE_IN, BLUE_IN, BLUE_IN, BLACK, BLACK, BLACK, BLACK, BLACK, MUTED],
            fmts=[None, F_PCT, F_PCT, F_PCT, F_NUM, None, None, None, None, None])
CG1 = r - 1
CG_US = r
r = row(ws, r, ["US total", f"=SUM(B{CG0}:B{CG1})", 0.050, 0.068, 8343, None, None, None, None,
                "US segment net sales, quarter ended 30 June 2026"],
        fonts=[BOLD, BOLD, BLUE_IN, BLUE_IN, BLUE_IN, BLACK, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, F_PCT, F_PCT, F_PCT, F_NUM, None, None, None, None, None], band=True)
# fix the implied $m column to reference the US total row
for i, rr in enumerate(range(CG0, CG1 + 1)):
    ws.cell(row=rr, column=5, value=f"=B{rr}*$E${CG_US}").number_format = F_NUM
    ws.cell(row=rr, column=5).font = BLACK
    ws.cell(row=rr, column=5).border = BOX
r = row(ws, r, ["Canada", None, -0.019, None, 408, None, None, None, None, "Canada segment, same quarter"],
        fonts=[BOLD, BLACK, BLUE_IN, BLACK, BLUE_IN, BLACK, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, None, F_PCT, None, F_NUM, None, None, None, None, None])
FG_GRP = r
r = row(ws, r, ["Group total", None, 0.046, None, 8751, None, None, None, None, "Quarter ended 30 June 2026"],
        fonts=[BOLD, BLACK, BLUE_IN, BLACK, BLUE_IN, BLACK, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, None, F_PCT, None, F_NUM, None, None, None, None, None], band=True)
r += 1

r = section(ws, r, "Waterworks revenue — ESTIMATE, not a reported figure")
r = head(ws, r, ["Step", "Value", "Unit", "", "", "", "", "", "", "Basis"])
W1 = r
r = row(ws, r, ["Group revenue, calendar 2025", 31316, "$m", None, None, None, None, None, None, "Reported"],
        fonts=[BOLD, BLUE_IN, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, F_NUM, None, None, None, None, None, None, None, None])
W2 = r
r = row(ws, r, ["Canada, annualised from Q2", f"=E{FG_GRP-1}*4", "$m", None, None, None, None, None, None,
                "ESTIMATE — $408m x 4"],
        fonts=[BOLD, BOLD, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, F_NUM, None, None, None, None, None, None, None, None])
W3 = r
r = row(ws, r, ["Implied US revenue", f"=B{W1}-B{W2}", "$m", None, None, None, None, None, None, "Formula"],
        fonts=[BOLD, BOLD, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, F_NUM, None, None, None, None, None, None, None, None])
W4 = r
r = row(ws, r, ["Waterworks share — full-year low", 0.22, "%", None, None, None, None, None, None,
                "ESTIMATE. Q2 is seasonally the strongest waterworks quarter, so the reported 24% overstates "
                "the full-year share."],
        fonts=[BOLD, BLUE_IN, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, F_PCT, None, None, None, None, None, None, None, None])
W5 = r
r = row(ws, r, ["Waterworks share — Q2 reported", 0.24, "%", None, None, None, None, None, None, "Reported"],
        fonts=[BOLD, BLUE_IN, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, F_PCT, None, None, None, None, None, None, None, None])
W6 = r
r = row(ws, r, ["Estimated waterworks revenue — low", f"=B{W3}*B{W4}", "$m", None, None, None, None, None, None,
                "Formula"],
        fonts=[BOLD, BOLD, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, F_NUM, None, None, None, None, None, None, None, None], band=True)
W7 = r
r = row(ws, r, ["Estimated waterworks revenue — high", f"=B{W3}*B{W5}", "$m", None, None, None, None, None, None,
                "Formula"],
        fonts=[BOLD, BOLD, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, F_NUM, None, None, None, None, None, None, None, None], band=True)
r = row(ws, r, ["  as % of group revenue", f"=B{W7}/B{W1}", "%", None, None, None, None, None, None, "Formula"],
        fonts=[BLACK, BOLD, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, MUTED],
        fmts=[None, F_PCT, None, None, None, None, None, None, None, None])
r += 1
r = section(ws, r, "Other")
r = head(ws, r, ["Item", "Value", "Unit", "", "", "", "", "", "", "Note"])
for lab, val, unit, nt, fmt in [
    ("Large capital projects, % of group revenue", 0.07, "%",
     "Mid- to high-single-digit and trending up. Backlogs building above realised growth rates, incl. waterworks.", F_PCT),
    ("Commodities, % of revenue", 0.15, "%", "PVC still in double-digit deflation in Q2 CY26.", F_PCT),
    ("FloWorks acquisition — price", 1600, "$m", "~$1bn revenue; ~10x LTM adjusted EBITDA incl. synergies; expected close Q3 2026.", F_NUM),
    ("FloWorks — expected annual synergies", 45, "$m", "Cross-sell into waterworks, commercial/mechanical and industrial.", F_NUM),
    ("Net debt : adjusted EBITDA", 1.3, "x", "Target range 1-2x; ~1.8x expected at FloWorks closing.", F_X),
    ("CY2026 operating margin guidance — low", 0.095, "%", "Raised at Q2.", F_PCT),
    ("CY2026 operating margin guidance — high", 0.098, "%", "", F_PCT),
]:
    r = row(ws, r, [lab, val, unit, None, None, None, None, None, None, nt],
            fonts=[BOLD, BLUE_IN, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, MUTED],
            fmts=[None, fmt, None, None, None, None, None, None, None, None])

# ============================================================ 12. COMPARISON
ws = sheet("Comparison", [40, 20, 20, 50], "Core & Main vs Ferguson",
           "Two very different ways to own the same theme. Sensitivity computed by formula.", tab="0B5FA5")
r = 4
r = section(ws, r, "Side by side")
r = head(ws, r, ["Metric", "Core & Main", "Ferguson", "Note"])
CMP0 = r
CMP_REV = r
r = row(ws, r, ["Latest full-year revenue ($m)", f"='Core and Main'!F{CNM_REV}", f"='Ferguson'!I{FG_REV}",
                "CNM: FY ended 1 Feb 2026. FERG: calendar 2025."],
        fonts=[BOLD, GREEN_LINK, GREEN_LINK, MUTED], fmts=[None, F_NUM, F_NUM, None])
CMP_WW = r
r = row(ws, r, ["Estimated waterworks revenue ($m)", f"='Core and Main'!F{CNM_REV}", f"='Ferguson'!B{W7}",
                "CNM is 100% water. FERG figure is an ESTIMATE — see Ferguson tab."],
        fonts=[BOLD, GREEN_LINK, GREEN_LINK, MUTED], fmts=[None, F_NUM, F_NUM, None])
CMP_WWP = r
r = row(ws, r, ["  as % of group revenue", f"=B{CMP_WW}/B{CMP_REV}", f"=C{CMP_WW}/C{CMP_REV}", "Formula"],
        fonts=[BLACK, BOLD, BOLD, MUTED], fmts=[None, F_PCT, F_PCT, None])
CMP_MUN = r
r = row(ws, r, ["Municipal revenue ($m)", f"='Core and Main'!C{MIX0}", "n/d",
                "Ferguson does not disclose a municipal split."],
        fonts=[BOLD, GREEN_LINK, BLACK, MUTED], fmts=[None, F_NUM, None, None])
r = row(ws, r, ["  as % of group revenue", f"=B{CMP_MUN}/B{CMP_REV}", "n/d", "Formula"],
        fonts=[BLACK, BOLD, BLACK, MUTED], fmts=[None, F_PCT, None, None])
CMP_MGN = r
r = row(ws, r, ["Profitability margin", 0.122, 0.107,
                "CNM adjusted EBITDA margin FY2025. FERG adjusted operating margin Q2 CY26 — not like for like."],
        fonts=[BOLD, BLUE_IN, BLUE_IN, MUTED], fmts=[None, F_PCT, F_PCT, None])
r = row(ws, r, ["Repair & replace share", 0.50, "n/d", "CNM deck. Ferguson does not disclose."],
        fonts=[BOLD, BLUE_IN, BLACK, MUTED], fmts=[None, F_PCT, None, None])
r += 1

r = section(ws, r, "Combined market position")
r = head(ws, r, ["Metric", "Value", "", "Basis"])
CB1 = r
r = row(ws, r, ["Combined waterworks revenue ($m)", f"=B{CMP_WW}+C{CMP_WW}", "", "Formula"],
        fonts=[BOLD, BOLD, BLACK, MUTED], fmts=[None, F_NUM, None, None])
CB2 = r
r = row(ws, r, ["US TAM ($m)", f"='Core and Main'!B{CNM_TAM}*1000", "", "Core & Main deck"],
        fonts=[BOLD, GREEN_LINK, BLACK, MUTED], fmts=[None, F_NUM, None, None])
r = row(ws, r, ["Combined share of US TAM", f"=B{CB1}/B{CB2}", "",
                "A duopoly at the head of a long fragmented tail — the structural reason both can consolidate "
                "and hold pricing."],
        fonts=[BOLD, BOLD, BLACK, MUTED], fmts=[None, F_PCT, None, None], band=True)
r += 1

r = section(ws, r, "Sensitivity — what 100bp of market growth is actually worth")
r = head(ws, r, ["Metric", "Core & Main", "Ferguson", "Note"])
SN0 = r
SN_BASE = r
r = row(ws, r, ["Exposed revenue base ($m)", f"=B{CMP_MUN}", f"=C{CMP_WW}",
                "CNM: municipal revenue. FERG: estimated waterworks revenue."],
        fonts=[BOLD, BLACK, BLACK, MUTED], fmts=[None, F_NUM, F_NUM, None])
SN_BP = r
r = row(ws, r, ["Market growth change", 0.01, 0.01, "Editable — change to test other increments."],
        fonts=[BOLD, BLUE_IN, BLUE_IN, MUTED], fmts=[None, F_PCT, F_PCT, None])
ws.cell(row=SN_BP, column=2).fill = YELL_FILL
ws.cell(row=SN_BP, column=3).fill = YELL_FILL
SN_REV = r
r = row(ws, r, ["Revenue impact ($m)", f"=B{SN_BASE}*B{SN_BP}", f"=C{SN_BASE}*C{SN_BP}", "Formula"],
        fonts=[BOLD, BOLD, BOLD, MUTED], fmts=[None, F_NUM, F_NUM, None])
SN_PCT = r
r = row(ws, r, ["  as % of group revenue", f"=B{SN_REV}/B{CMP_REV}", f"=C{SN_REV}/C{CMP_REV}",
                "THE NUMBER MOST INVESTORS GET WRONG. Even for the pure play this is under half a percent."],
        fonts=[BOLD, BOLD, BOLD, MUTED], fmts=[None, F_PCT, F_PCT, None], band=True)
SN_EB = r
r = row(ws, r, ["EBITDA impact ($m)", f"=B{SN_REV}*B{CMP_MGN}", f"=C{SN_REV}*C{CMP_MGN}",
                "At current margins. Incremental margin on distribution volume is typically higher."],
        fonts=[BOLD, BOLD, BOLD, MUTED], fmts=[None, F_NUM, F_NUM, None])
r += 1
r = head(ws, r, ["IIJA peak drag scenario", "Core & Main", "Ferguson", "Note"])
D_PP = r
r = row(ws, r, ["Market growth points lost at peak", 0.0125, 0.0125,
                "Midpoint of the 1.0-1.5pt range, concentrated in 2029-2030 — see Forward Model."],
        fonts=[BOLD, BLUE_IN, BLUE_IN, MUTED], fmts=[None, F_PCT, F_PCT, None])
D_REV = r
r = row(ws, r, ["Revenue growth impact", f"=B{SN_BASE}*B{D_PP}/B{CMP_REV}", f"=C{SN_BASE}*C{D_PP}/C{CMP_REV}",
                "Formula. Well under 100bps for either company."],
        fonts=[BOLD, BOLD, BOLD, MUTED], fmts=[None, F_PCT, F_PCT, None], band=True)
r += 1
r = note(ws, r, "Residential construction — 18% of Core & Main's mix and about half of Ferguson's US mix — moves "
                "both companies materially more than the federal funding question does. That is the risk worth "
                "underwriting.")

# ============================================================ 13. DASHBOARD
ws = sheet("Dashboard", [46, 18, 12, 60], "Dashboard",
           "Every figure below is a live link to the tab that derives it.", tab="1F3B52")
r = 4
r = section(ws, r, "The funding map")
r = head(ws, r, ["Metric", "Value", "Unit", "Reads"])
for lab, f, unit, nt, fmt in [
    ("State and local share of water infrastructure", "='Historical Spending'!B10", "%",
     "CBO. Federal policy sets rules far more powerfully than it sets budgets.", F_PCT),
    ("Water utilities total spending, 2023", "='Historical Spending'!B7", "$bn",
     "CBO — of which capital is the minority.", F_NUM),
    ("  of which capital", "='Historical Spending'!B8", "$bn", "The anchor for the forward model.", F_NUM),
    ("Water and sewer bill increase, 2025", "='Historical Spending'!B44", "%",
     "Bluefield. The variable that matters most for distributor revenue.", F_PCT),
]:
    r = row(ws, r, [lab, f, unit, nt], fonts=[BOLD, GREEN_LINK, BLACK, MUTED],
            fmts=[None, fmt, None, None])
r += 1
r = section(ws, r, "The forward model")
r = head(ws, r, ["Metric", "Value", "Unit", "Reads"])
for lab, f, unit, nt, fmt in [
    ("2026 capital base", f"='{ASM}'!B{A_BASE}", "$bn", "Reconciliation of four independent sources.", F_NUM1),
    ("2030 total spending (base case)", f"='Forward Model'!G{FM_TOT}", "$bn", "", F_NUM1),
    ("2035 total spending (base case)", f"='Forward Model'!L{FM_TOT}", "$bn", "", F_NUM1),
    ("CAGR 2026-2035", f"=('Forward Model'!L{FM_TOT}/'Forward Model'!C{FM_TOT})^(1/9)-1", "%",
     "Mid-single-digit nominal. Not a boom and not a bust.", F_PCT),
    ("Net IIJA drag as % of base", f"='{ASM}'!B{A_PCT}", "%",
     "The honest measure of the cliff — not the 100% often assumed.", F_PCT),
    ("2035 bear case", f"='Scenarios'!L{sc_rows['Bear']}", "$bn", "", F_NUM1),
    ("2035 bull case", f"='Scenarios'!L{sc_rows['Bull']}", "$bn",
     "No credible scenario has spending falling in nominal terms.", F_NUM1),
]:
    r = row(ws, r, [lab, f, unit, nt], fonts=[BOLD, GREEN_LINK, BLACK, MUTED], fmts=[None, fmt, None, None])
r += 1
r = section(ws, r, "The engineering evidence")
r = head(ws, r, ["Metric", "Value", "Unit", "Reads"])
for lab, f, unit, nt, fmt in [
    ("Cast iron vs PVC failure ratio", f"='Pipe and Assets'!B{CI_RATIO}", "x",
     "The single most defensible number in the replacement case.", F_X),
    ("Change in national break rate, 2018-2023", f"='Pipe and Assets'!B{CI_RATIO-1}", "%",
     "THE COUNTER-EVIDENCE. The network is getting more reliable, not less.", F_PCT),
    ("Lead service lines", f"='Regulatory'!B5", "count", "Hard legal replacement mandate.", F_NUM),
    ("Lead replacement unfunded balance", f"='Regulatory'!B11", "$bn",
     "Must come from rates. This is the rate-driver.", F_NUM1),
]:
    r = row(ws, r, [lab, f, unit, nt], fonts=[BOLD, GREEN_LINK, BLACK, MUTED], fmts=[None, fmt, None, None])
r += 1
r = section(ws, r, "The companies")
r = head(ws, r, ["Metric", "Value", "Unit", "Reads"])
for lab, f, unit, nt, fmt in [
    ("Core & Main revenue ($m)", f"='Comparison'!B{CMP_REV}", "$m", "FY ended 1 Feb 2026.", F_NUM),
    ("Ferguson revenue ($m)", f"='Comparison'!C{CMP_REV}", "$m", "Calendar 2025.", F_NUM),
    ("Combined share of US TAM", f"='Comparison'!B{CB1+2}", "%",
     "A duopoly at the head of a fragmented tail.", F_PCT),
    ("100bp market growth — CNM revenue impact", f"='Comparison'!B{SN_PCT}", "% of sales",
     "The IIJA cliff is worth less than this to either company.", F_PCT),
    ("100bp market growth — FERG revenue impact", f"='Comparison'!C{SN_PCT}", "% of sales", "", F_PCT),
]:
    r = row(ws, r, [lab, f, unit, nt], fonts=[BOLD, GREEN_LINK, BLACK, MUTED], fmts=[None, fmt, None, None])
r += 1
r = note(ws, r, "VERIFY BEFORE USE: public-sector figures in this workbook were obtained via search results "
                "summarising primary documents, because this environment's network policy blocked direct access "
                "to cbo.gov, epa.gov, census.gov, congress.gov and fred.stlouisfed.org. Company financials came "
                "from Quartr's primary filings and do not carry this caveat. See the Read Me tab.")

# ============================================================ 14. SOURCES
ws = sheet("Sources", [34, 34, 14, 58], "Sources and Known Biases",
           "Every source with the interest of the party that produced it, so the reader can discount accordingly.",
           tab="5C6E7C")
r = 4
groups = [
    ("Public spending — historical", [
        ("CBO", "Public Spending on Transportation and Water Infrastructure, 1956 to 2023", "Feb 2025",
         "Non-partisan scorekeeper — the most neutral source in the sector. Caveat: 'water utilities' bundles "
         "supply and wastewater and includes O&M."),
        ("USAFacts", "Summary of the CBO series", "2025",
         "Non-partisan aggregator. Used for the modal and capital/O&M breakdown."),
        ("US Census Bureau", "Value of Construction Put in Place (C30)", "Monthly",
         "Official statistics, no advocacy. Caveat: 'sewage and waste disposal' bundles solid waste with "
         "sewerage, overstating the wastewater component."),
        ("US Conference of Mayors", "2025 Public Infrastructure Spending", "2025",
         "Municipal advocacy organisation — interest in demonstrating local fiscal burden."),
    ]),
    ("Federal programmes", [
        ("CRS", "IF13177 — FY2026 Appropriations for EPA Water Infrastructure Programs", "2026",
         "Non-partisan congressional research. High reliability."),
        ("CRS", "R48565 — Wastewater Infrastructure Funding", "2025", "Same."),
        ("CRS", "R47878 — Drinking Water Infrastructure Needs", "2024",
         "Same. Source of the $648.8bn (2022 dollars) restatement of DWINSA."),
        ("EPA", "Water Infrastructure Investments; BIL fact sheets; WIFIA announcements", "2021-26",
         "Agency communicating its own programme — presents funding favourably."),
        ("National League of Cities", "Water infrastructure funding cliff advocacy", "May 2026",
         "ADVOCACY — lobbying to extend federal funding. Source of the $2.7bn to $11.4bn framing; directionally "
         "verifiable but framed to maximise the cliff."),
        ("Senate EPW", "Water Resources Development Act of 2026", "Jul 2026",
         "Primary legislative source. Authorisation is not appropriation."),
    ]),
    ("Needs estimates and forecasts", [
        ("EPA", "7th Drinking Water Infrastructure Needs Survey and Assessment", "Sep 2023",
         "ALLOCATION INSTRUMENT. States self-report and the results drive their own funding formula — a "
         "structural incentive to report high. EPA concedes transmission and distribution is undercounted."),
        ("EPA", "Clean Watersheds Needs Survey 2022", "Apr 2024",
         "Same structure. First survey with 100% state participation, which mechanically inflates the "
         "year-on-year increase."),
        ("GAO", "GAO-24-106251", "2024",
         "Independent auditor. CRITICAL of EPA's needs estimate and the 1987 CWSRF allocation formula. Used "
         "here as the counterweight."),
        ("EPA Office of Inspector General", "Report on 7th DWINSA lead service line allotments", "2024",
         "Independent internal auditor. Also critical."),
        ("ASCE", "2025 Infrastructure Report Card — drinking water C-, wastewater D+", "Mar 2025",
         "PROFESSIONAL SOCIETY OF CIVIL ENGINEERS. Direct commercial interest in higher infrastructure "
         "spending. Grading methodology not externally audited."),
        ("ASCE", "Bridging the Gap — $99bn/yr water gap", "2024",
         "Same. Uses a broader 'economic need' definition not comparable to EPA's eligible-need definition."),
        ("AWWA", "Beyond the Replacement Era — $2.1-2.4tn / 25yr", "Mar 2026",
         "WATER UTILITY TRADE ASSOCIATION. Interest in federal funding and in justifying rate increases to "
         "regulators. Broadest definition of the four; the 168% required increase should be read as a "
         "bargaining position."),
        ("Bluefield Research", "Treatment capex, pipe capex, rate index, non-revenue water", "2025-26",
         "COMMERCIAL MARKET RESEARCH sold to vendors and investors. Interest in a large addressable market, but "
         "methodology is bottom-up from project pipelines and is the closest to a revenue-relevant forecast."),
        ("McKinsey", "Water resilience: closing the funding gap for utilities", "2024",
         "Consultancy. Used only as a cross-check on total utility spending (~$183bn implied)."),
    ]),
    ("Technical", [
        ("Utah State University", "Water Main Break Rates in the USA and Canada", "Dec 2023",
         "Academic, but distributed by pipe-manufacturer interests, and its material-by-material break rates "
         "favour PVC. It is also the best data available — and its finding that break rates FELL cuts against "
         "its own $452bn headline, which is a point in favour of the data's integrity."),
        ("USGS", "Water Use in the United States", "2015/2020 series",
         "Federal scientific agency. Neutral. Caveat: the national compilation is published on a five-year lag."),
        ("Springer / ASM / EPA", "Peer-reviewed literature on graphitic corrosion and tuberculation", "various",
         "Neutral engineering literature."),
    ]),
    ("Regulatory", [
        ("EPA", "Lead and Copper Rule Improvements — final Oct 2024", "2024-26", "Primary rulemaking source."),
        ("NRDC tracker", "American Water Works Association v. EPA", "2026",
         "Environmental advocacy organisation, used only for case status. Oral argument expected Fall 2026."),
        ("Federal Register", "Extending the Compliance Deadline for the PFOA and PFOS MCLs", "20 May 2026",
         "Primary source."),
        ("AWWA / Black & Veatch", "PFAS National Cost Model — >$50bn/20yr", "2023",
         "Trade-association cost model, produced to argue against a stricter rule."),
        ("CRS", "R49057 — Data Centers and Water: FAQ", "Jul 2026", "Non-partisan congressional research."),
    ]),
    ("Company data — all via Quartr", [
        ("Core & Main", "Q1 FY2026 results and investor presentation", "10 Jun 2026",
         "Primary. Net sales, mix, TAM, guidance, management commentary on the IIJA cliff."),
        ("Core & Main", "FY2025 full-year results", "24 Mar 2026", "Primary. Five-year income statement."),
        ("Ferguson", "Q2 CY2026 results and presentation", "10 Aug 2026",
         "Primary. US customer-group table, segment revenue, FloWorks terms."),
        ("Ferguson", "CY2025 transition-period results", "24 Feb 2026", "Primary. Eight-period income statement."),
    ]),
]
for gname, items in groups:
    r = section(ws, r, gname)
    r = head(ws, r, ["Publisher", "Document", "Date", "Known interest / bias"])
    for a, b, c_, d in items:
        r = row(ws, r, [a, b, c_, d], fonts=[BOLD, BLACK, MUTED, MUTED])
    r += 1

wb.save("/home/user/US-Water-Infra/US-Water-Infrastructure-Analysis.xlsx")
print("saved")
