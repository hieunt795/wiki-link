"""
BCBS Basel III Monitoring Workbook — Excel Builder
Structure: Cover | A-Capital | B-Leverage | C-LCR | D-NSFR
Color convention (BCBS standard):
  Yellow  = INPUT cells (bank fills in)
  Green   = CALCULATED / formula output
  Navy    = Section headers
  White   = Description / read-only rows
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUT_FILE = "04_research/alm_notes/bcbs_monitoring_workbook.xlsx"

# ─── Palette ──────────────────────────────────────────────────────────────────
C = dict(
    navy="1F3864",        # section header bg
    mid_blue="2E75B6",    # column header bg
    light_blue="BDD7EE",  # sub-header bg
    input_bg="FFFF99",    # yellow — BCBS input cells
    calc_bg="E2EFDA",     # light green — calculated cells
    section_bg="D6E4F0",  # light blue-grey — section title rows
    warn_bg="FFE0B2",     # orange — breach / shortfall
    white="FFFFFF",
    light_grey="F5F5F5",
    dark_text="1F1F1F",
    red="C62828",
    green_text="1B5E20",
)

# ─── Style helpers ─────────────────────────────────────────────────────────────
def _fill(hex_):
    return PatternFill("solid", fgColor=hex_)

def _font(bold=False, color="000000", size=10, italic=False):
    return Font(bold=bold, color=color, size=size, italic=italic, name="Cambria")

def _align(h="left", v="center", wrap=False):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)

def _border(style="thin", clr="BFBFBF"):
    s = Side(style=style, color=clr)
    return Border(left=s, right=s, top=s, bottom=s)

def cell(ws, r, c, val=None, bold=False, color="000000", size=10, italic=False,
         bg=None, h="left", v="center", wrap=False, fmt=None, border=True):
    cl = ws.cell(row=r, column=c, value=val)
    cl.font = _font(bold=bold, color=color, size=size, italic=italic)
    cl.alignment = _align(h=h, v=v, wrap=wrap)
    if border:
        cl.border = _border()
    if bg:
        cl.fill = _fill(bg)
    if fmt:
        cl.number_format = fmt
    return cl

def merge(ws, r, c1, c2, val=None, bold=False, color="000000", size=10,
          italic=False, bg=None, h="left", v="center", wrap=False, fmt=None, border=True):
    ws.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
    cl = cell(ws, r, c1, val, bold=bold, color=color, size=size, italic=italic,
              bg=bg, h=h, v=v, wrap=wrap, fmt=fmt, border=border)
    return cl

def section_bar(ws, r, c1, c2, text, bg=None, fg="FFFFFF", size=11):
    bg = bg or C["navy"]
    merge(ws, r, c1, c2, text, bold=True, color=fg, size=size, bg=bg, h="left")
    ws.row_dimensions[r].height = 20

def col_hdr(ws, r, c, text, bg=None, wrap=True):
    bg = bg or C["mid_blue"]
    cell(ws, r, c, text, bold=True, color="FFFFFF", size=9, bg=bg, h="center", v="center", wrap=wrap)

def input_cell(ws, r, c, val, fmt=None):
    cl = cell(ws, r, c, val, color=C["navy"], size=10, bg=C["input_bg"], h="right", bold=True)
    if fmt:
        cl.number_format = fmt
    return cl

def calc_cell(ws, r, c, val, fmt=None):
    cl = cell(ws, r, c, val, color=C["green_text"], size=10, bg=C["calc_bg"], h="right", italic=True)
    if fmt:
        cl.number_format = fmt
    return cl

def desc_row(ws, r, code, description, indent=0):
    prefix = "  " * indent
    cell(ws, r, 1, code, bold=True, color=C["mid_blue"], size=9, bg=C["white"], h="center")
    cell(ws, r, 2, f"{prefix}{description}", color=C["dark_text"], size=10, bg=C["white"], wrap=True)

def set_cols(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

def sheet_setup(ws, freeze="A6"):
    ws.sheet_view.showGridLines = False
    if freeze:
        ws.freeze_panes = freeze

def title_block(ws, r, c1, c2, title, subtitle=None):
    merge(ws, r, c1, c2, title, bold=True, color="FFFFFF", size=14,
          bg=C["navy"], h="center")
    ws.row_dimensions[r].height = 30
    if subtitle:
        merge(ws, r + 1, c1, c2, subtitle, italic=True, color=C["navy"],
              size=9, bg="EBF3FB", h="center")
        ws.row_dimensions[r + 1].height = 16


# ══════════════════════════════════════════════════════════════════════════════
# WORKBOOK
# ══════════════════════════════════════════════════════════════════════════════
wb = openpyxl.Workbook()
wb.remove(wb.active)


# ══════════════════════════════════════════════════════════════════════════════
# COVER SHEET
# ══════════════════════════════════════════════════════════════════════════════
cv = wb.create_sheet("Cover")
sheet_setup(cv, freeze=None)
set_cols(cv, [4, 32, 28, 8])

merge(cv, 1, 1, 4, "BASEL III MONITORING EXERCISE", bold=True, color="FFFFFF",
      size=16, bg=C["navy"], h="center")
cv.row_dimensions[1].height = 36
merge(cv, 2, 1, 4, "Quantitative Impact Study — Reporting Workbook",
      italic=True, color=C["navy"], size=11, bg="EBF3FB", h="center")
cv.row_dimensions[2].height = 20
cv.row_dimensions[3].height = 10

# Legend
section_bar(cv, 4, 1, 4, "  COLOUR LEGEND", bg=C["navy"])
for r, (code, desc, bg) in enumerate([
    ("INPUT",      "Yellow cells — data to be filled in by reporting bank", C["input_bg"]),
    ("CALCULATED", "Green cells  — formula / auto-calculated values",        C["calc_bg"]),
    ("N/A",        "Grey cells   — not applicable to this row",              "E0E0E0"),
], start=5):
    cell(cv, r, 2, f"  {code}", bold=True, size=10, bg=bg, color=C["dark_text"])
    cell(cv, r, 3, desc, size=10, bg=bg, color=C["dark_text"])
    cv.row_dimensions[r].height = 18

cv.row_dimensions[8].height = 10

# Bank info block
section_bar(cv, 9, 1, 4, "  REPORTING INSTITUTION INFORMATION", bg=C["navy"])
INFO = [
    ("Bank / Group name",            "Sample Bank Group"),
    ("Country of incorporation",     "Vietnam"),
    ("Reporting date",               "31 December 2024"),
    ("Reporting currency",           "VND"),
    ("Units",                        "VND billions (tỷ đồng)"),
    ("Group structure (tick one)",   "International active bank"),
    ("Consolidation basis",          "Full consolidation"),
    ("Contact person",               "Chief Risk Officer"),
    ("Submission date",              "31 January 2025"),
]
for i, (label, val) in enumerate(INFO, start=10):
    cell(cv, i, 2, label, bold=True, color=C["navy"], size=10, bg=C["light_grey"])
    input_cell(cv, i, 3, val)
    cv.row_dimensions[i].height = 18

cv.row_dimensions[19].height = 10
section_bar(cv, 20, 1, 4, "  WORKSHEET INDEX", bg=C["navy"])
SHEETS = [
    ("Cover",       "Institution information and colour legend"),
    ("A - Capital", "Panel A: Capital adequacy — CET1, Tier 1, Total Capital, RWA, buffers"),
    ("B - Leverage","Panel B: Leverage ratio — Tier 1 exposure measure"),
    ("C - LCR",     "Panel C: Liquidity Coverage Ratio — HQLA, outflows, inflows"),
    ("D - NSFR",    "Panel D: Net Stable Funding Ratio — ASF, RSF"),
]
for i, (sh, desc) in enumerate(SHEETS, start=21):
    cell(cv, i, 2, sh, bold=True, color=C["mid_blue"], size=10, bg=C["white"])
    cell(cv, i, 3, desc, color=C["dark_text"], size=10, bg=C["white"])
    cv.row_dimensions[i].height = 16


# ══════════════════════════════════════════════════════════════════════════════
# PANEL A — CAPITAL
# ══════════════════════════════════════════════════════════════════════════════
wa = wb.create_sheet("A - Capital")
sheet_setup(wa, freeze="A7")
set_cols(wa, [8, 52, 18, 18, 18, 18, 22])

title_block(wa, 1, 1, 7,
            "PANEL A — CAPITAL ADEQUACY",
            "Unit: VND billions  |  Yellow = INPUT  |  Green = CALCULATED  |  Ref: Basel III § 92–145, CRR2 Art. 25–91")
wa.row_dimensions[3].height = 6

# Legend row
merge(wa, 4, 1, 2, "  Ref. period: 31 Dec 2024  |  Currency: VND  |  Units: billions",
      italic=True, size=9, color=C["navy"], bg="EBF3FB")
wa.row_dimensions[4].height = 14
wa.row_dimensions[5].height = 6

# Column headers
HDRS_A = ["Code", "Description / Basel III reference",
          "Current (T0)", "Prior year (T-1)", "Minimum req.", "Buffer req.", "Notes"]
for i, h in enumerate(HDRS_A, 1):
    col_hdr(wa, 6, i, h)
wa.row_dimensions[6].height = 28

# ─── Data: Capital ─────────────────────────────────────────────────────────
#  (code, description, T0_value, T-1_value, min_req, buffer_req, note, row_type)
#  row_type: "section" | "input" | "calc" | "ratio" | "spacer"
CAPITAL_ROWS = [
    # ── Section 1: Regulatory Capital ──────────────────────────────────────
    (None, "SECTION 1 — REGULATORY CAPITAL COMPONENTS", None, None, None, None, None, "section"),
    ("CA1",  "Common Equity Tier 1 (CET1) capital",           85_000, 78_000, None, None, "Paid-up capital + retained earnings − deductions", "input"),
    ("CA2",  "Additional Tier 1 (AT1) capital instruments",    8_500,  7_200, None, None, "Qualifying AT1 instruments", "input"),
    ("CA3",  "Tier 1 capital  [= CA1 + CA2]",                 93_500, 85_200, None, None, "Auto-calculated", "calc"),
    ("CA4",  "Tier 2 capital instruments",                     12_000, 11_000, None, None, "Qualifying Tier 2 instruments & provisions", "input"),
    ("CA5",  "Total regulatory capital  [= CA3 + CA4]",       105_500, 96_200, None, None, "Auto-calculated", "calc"),
    (None, None, None, None, None, None, None, "spacer"),
    # ── Section 2: Risk-Weighted Assets ────────────────────────────────────
    (None, "SECTION 2 — RISK-WEIGHTED ASSETS (RWA)", None, None, None, None, None, "section"),
    ("CA6",  "Credit risk RWA — Standardised Approach",       420_000, 395_000, None, None, "SA exposures", "input"),
    ("CA7",  "Credit risk RWA — IRB Approach",                180_000, 175_000, None, None, "F-IRB / A-IRB", "input"),
    ("CA8",  "Market risk RWA",                                28_000,  25_000, None, None, "IMA or SA-MR", "input"),
    ("CA9",  "Operational risk RWA",                           35_000,  32_000, None, None, "BIA / SMA", "input"),
    ("CA10", "Credit Valuation Adjustment (CVA) RWA",           4_500,   4_200, None, None, "SA-CVA or BA-CVA", "input"),
    ("CA11", "Total RWA  [= CA6+CA7+CA8+CA9+CA10]",           667_500, 631_200, None, None, "Auto-calculated", "calc"),
    (None, None, None, None, None, None, None, "spacer"),
    # ── Section 3: Capital Ratios ───────────────────────────────────────────
    (None, "SECTION 3 — CAPITAL RATIOS", None, None, None, None, None, "section"),
    ("CA12", "CET1 ratio  [= CA1 / CA11]",                    0.1273, 0.1236,  0.045, None, "Min 4.5%  (Pillar 1)", "ratio"),
    ("CA13", "Tier 1 ratio  [= CA3 / CA11]",                  0.1401, 0.1350,  0.060, None, "Min 6.0%  (Pillar 1)", "ratio"),
    ("CA14", "Total capital ratio  [= CA5 / CA11]",           0.1581, 0.1524,  0.080, None, "Min 8.0%  (Pillar 1)", "ratio"),
    (None, None, None, None, None, None, None, "spacer"),
    # ── Section 4: Capital Buffers ──────────────────────────────────────────
    (None, "SECTION 4 — CAPITAL BUFFERS (CET1 basis)", None, None, None, None, None, "section"),
    ("CA15", "Capital Conservation Buffer (CCB)",              None, None, 0.025, 0.025, "Fixed at 2.5% of RWA", "input"),
    ("CA16", "Countercyclical Capital Buffer (CCyB)",          None, None, 0.000, 0.000, "Jurisdiction-specific; currently 0%", "input"),
    ("CA17", "G-SIB / D-SIB additional surcharge",            None, None, 0.010, 0.010, "1.0% for D-SIB bucket 1", "input"),
    ("CA18", "Combined buffer requirement  [= CA15+CA16+CA17]",None,None, 0.035, 0.035, "Auto-calculated", "calc"),
    ("CA19", "CET1 available for buffers  [= CA12 − 4.5%]",   0.0773, 0.0736, None, None, "Surplus above Pillar 1 minimum", "calc"),
    ("CA20", "Surplus (+) / Shortfall (−) vs. combined buffer",0.0423, 0.0386, None, None, "CA19 − CA18", "calc"),
    (None, None, None, None, None, None, None, "spacer"),
    # ── Section 5: CET1 Deductions ─────────────────────────────────────────
    (None, "SECTION 5 — PRINCIPAL CET1 DEDUCTIONS", None, None, None, None, None, "section"),
    ("CA21", "Goodwill and other intangible assets (net)",      3_500,  3_200, None, None, "Deducted in full from CET1", "input"),
    ("CA22", "Deferred tax assets (DTA) — temporary differences",1_200, 1_100, None, None, "Threshold deduction applies", "input"),
    ("CA23", "Significant investments in financial entities",    2_100,  1_900, None, None, "Above 10% threshold", "input"),
    ("CA24", "Shortfall of provisions to expected losses (IRB)",   800,    750, None, None, "IRB banks only", "input"),
    ("CA25", "Total CET1 deductions (sum CA21–CA24)",            7_600,  6_950, None, None, "Auto-calculated", "calc"),
]

r = 7
for row in CAPITAL_ROWS:
    code, desc, t0, t1, mn, buf, note, rtype = row
    if rtype == "spacer":
        wa.row_dimensions[r].height = 6
        r += 1
        continue
    if rtype == "section":
        section_bar(wa, r, 1, 7, f"  {desc}", bg=C["navy"])
        r += 1
        continue
    # code + description
    desc_row(wa, r, code, desc)
    if rtype == "ratio":
        fmt_t = "0.00%"
        fn = calc_cell if "calc" in rtype else input_cell
        input_cell(wa, r, 3, t0, fmt=fmt_t) if rtype == "ratio" else calc_cell(wa, r, 3, t0, fmt=fmt_t)
        input_cell(wa, r, 4, t1, fmt=fmt_t)
        cell(wa, r, 5, mn, bold=True, color=C["red"], size=10, bg="FFF3F3", h="right", fmt=fmt_t) if mn else cell(wa, r, 5, "—", color="9E9E9E", bg=C["white"], h="center")
        cell(wa, r, 6, buf, color=C["dark_text"], size=10, bg=C["white"], h="right", fmt=fmt_t) if buf else cell(wa, r, 6, "—", color="9E9E9E", bg=C["white"], h="center")
    elif rtype == "calc":
        fmt_t = "0.00%" if isinstance(t0, float) and t0 < 1 else '#,##0'
        calc_cell(wa, r, 3, t0, fmt=fmt_t)
        calc_cell(wa, r, 4, t1, fmt=fmt_t)
        cell(wa, r, 5, mn, bold=True, color=C["red"], size=10, bg="FFF3F3", h="right", fmt="0.00%") if mn else cell(wa, r, 5, "—", color="9E9E9E", bg=C["white"], h="center")
        cell(wa, r, 6, buf, color=C["dark_text"], size=10, bg=C["white"], h="right", fmt="0.00%") if buf else cell(wa, r, 6, "—", color="9E9E9E", bg=C["white"], h="center")
    else:
        fmt_t = "0.00%" if isinstance(t0, float) and t0 < 1 else '#,##0'
        input_cell(wa, r, 3, t0, fmt=fmt_t) if t0 is not None else cell(wa, r, 3, "—", color="9E9E9E", bg=C["white"], h="center")
        input_cell(wa, r, 4, t1, fmt=fmt_t) if t1 is not None else cell(wa, r, 4, "—", color="9E9E9E", bg=C["white"], h="center")
        cell(wa, r, 5, mn, bold=True, color=C["red"], size=10, bg="FFF3F3", h="right", fmt="0.00%") if mn else cell(wa, r, 5, "—", color="9E9E9E", bg=C["white"], h="center")
        cell(wa, r, 6, buf, color=C["dark_text"], size=10, bg=C["white"], h="right", fmt="0.00%") if buf else cell(wa, r, 6, "—", color="9E9E9E", bg=C["white"], h="center")
    cell(wa, r, 7, note or "", color="595959", size=9, bg=C["white"], italic=True, wrap=True)
    wa.row_dimensions[r].height = 18
    r += 1


# ══════════════════════════════════════════════════════════════════════════════
# PANEL B — LEVERAGE RATIO
# ══════════════════════════════════════════════════════════════════════════════
wb_ = wb.create_sheet("B - Leverage")
sheet_setup(wb_, freeze="A7")
set_cols(wb_, [8, 56, 18, 18, 16, 22])

title_block(wb_, 1, 1, 6,
            "PANEL B — LEVERAGE RATIO",
            "Unit: VND billions  |  Ref: Basel III § 153–156 (Jan 2014 rev.), CRR2 Art. 429–429h  |  Minimum 3.0%")
wb_.row_dimensions[3].height = 6

merge(wb_, 4, 1, 2, "  Ref. period: 31 Dec 2024",
      italic=True, size=9, color=C["navy"], bg="EBF3FB")
wb_.row_dimensions[4].height = 14
wb_.row_dimensions[5].height = 6

for i, h in enumerate(["Code", "Description", "Current (T0)", "Prior year (T-1)", "Min. req.", "Notes"], 1):
    col_hdr(wb_, 6, i, h)
wb_.row_dimensions[6].height = 28

LEVERAGE_ROWS = [
    (None, "SECTION 1 — TIER 1 CAPITAL (NUMERATOR)", None, None, None, None, "section"),
    ("LR1", "Tier 1 capital (= CA3 from Panel A)",         93_500,  85_200, None,  "Consistent with Panel A CA3", "input"),
    (None, None, None, None, None, None, "spacer"),
    (None, "SECTION 2 — EXPOSURE MEASURE (DENOMINATOR)", None, None, None, None, "section"),
    ("LR2", "On-balance sheet assets (excl. derivatives/SFTs)", 920_000, 865_000, None, "At accounting value, net of provisions", "input"),
    ("LR3", "Derivative financial instruments",               45_000,  40_000, None, "Replacement cost + add-on (SA-CCR)", "input"),
    ("LR4", "Securities financing transactions (SFTs)",       55_000,  50_000, None, "Net counterparty exposure", "input"),
    ("LR5", "Off-balance sheet items (credit conversion)",    32_000,  28_000, None, "CCF applied per BCBS 279 §73–76", "input"),
    ("LR6", "Total leverage exposure measure [= LR2+LR3+LR4+LR5]",1_052_000, 983_000, None, "Auto-calculated", "calc"),
    (None, None, None, None, None, None, "spacer"),
    (None, "SECTION 3 — LEVERAGE RATIO", None, None, None, None, "section"),
    ("LR7", "Basel III Leverage Ratio [= LR1 / LR6]",         0.0888,  0.0867,  0.030, "Min 3.0%; G-SIBs: 3.5%", "ratio"),
    ("LR8", "Leverage ratio excl. central bank reserves",      0.0921,  0.0899,  None,  "Optional supplementary measure", "calc"),
    (None, None, None, None, None, None, "spacer"),
    (None, "SECTION 4 — MEMO ITEMS", None, None, None, None, "section"),
    ("LR9",  "Total on-balance sheet assets (IFRS/local GAAP)",920_000, 865_000, None, "For reference", "input"),
    ("LR10", "Repo / reverse repo netting adjustment",          -8_000,  -7_500, None, "Master netting agreements applied", "input"),
    ("LR11", "Written credit derivatives (notional)",           12_000,  11_000, None, "Added back to exposure", "input"),
]

r = 7
for row in LEVERAGE_ROWS:
    code, desc, t0, t1, mn, note, rtype = row
    if rtype == "spacer":
        wb_.row_dimensions[r].height = 6; r += 1; continue
    if rtype == "section":
        section_bar(wb_, r, 1, 6, f"  {desc}", bg=C["navy"]); r += 1; continue
    desc_row(wb_, r, code, desc)
    if rtype == "ratio":
        input_cell(wb_, r, 3, t0, fmt="0.00%")
        input_cell(wb_, r, 4, t1, fmt="0.00%")
        cell(wb_, r, 5, mn, bold=True, color=C["red"], size=10, bg="FFF3F3", h="right", fmt="0.00%")
    elif rtype == "calc":
        fmt = "0.00%" if isinstance(t0, float) and t0 < 1 else '#,##0'
        calc_cell(wb_, r, 3, t0, fmt=fmt)
        calc_cell(wb_, r, 4, t1, fmt=fmt)
        cell(wb_, r, 5, "—", color="9E9E9E", bg=C["white"], h="center")
    else:
        fmt = '#,##0' if isinstance(t0, int) or (t0 and abs(t0) > 1) else "0.00%"
        input_cell(wb_, r, 3, t0, fmt=fmt)
        input_cell(wb_, r, 4, t1, fmt=fmt)
        cell(wb_, r, 5, mn if mn else "—", color="9E9E9E" if not mn else C["red"],
             size=10, bg="FFF3F3" if mn else C["white"], h="right" if mn else "center",
             fmt="0.00%" if mn else None)
    cell(wb_, r, 6, note or "", color="595959", size=9, bg=C["white"], italic=True, wrap=True)
    wb_.row_dimensions[r].height = 18
    r += 1


# ══════════════════════════════════════════════════════════════════════════════
# PANEL C — LCR
# ══════════════════════════════════════════════════════════════════════════════
wc = wb.create_sheet("C - LCR")
sheet_setup(wc, freeze="A7")
set_cols(wc, [8, 54, 16, 14, 12, 12, 22])

title_block(wc, 1, 1, 7,
            "PANEL C — LIQUIDITY COVERAGE RATIO (LCR)",
            "Unit: VND billions  |  Ref: BCBS Jan 2013 (rev. 2014), LCR = HQLA / Net Cash Outflows ≥ 100%")
wc.row_dimensions[3].height = 6

merge(wc, 4, 1, 2, "  Ref. period: 31 Dec 2024  |  30-day stress horizon",
      italic=True, size=9, color=C["navy"], bg="EBF3FB")
wc.row_dimensions[4].height = 14
wc.row_dimensions[5].height = 6

for i, h in enumerate(["Code", "Description", "Unweighted value", "Weighted value", "Rate (%)", "Min. req.", "Notes"], 1):
    col_hdr(wc, 6, i, h)
wc.row_dimensions[6].height = 28

LCR_ROWS = [
    # HQLA
    (None, "SECTION 1 — HIGH-QUALITY LIQUID ASSETS (HQLA)", None, None, None, None, None, "section"),
    ("LC1",  "Level 1 assets (0% haircut)",                  62_000,  62_000,  0.00,  None, "HQLA Level 1: cash, CB reserves, OECD sov. 0% RW", "input"),
    ("LC2",  "Level 2A assets (15% haircut)",                 18_000,  15_300,  0.15,  None, "GSE securities, non-0%-RW sov., covered bonds", "input"),
    ("LC3",  "Level 2B assets (25–50% haircut)",               8_000,   4_800,  0.40,  None, "Eligible RMBS, non-fin. corp. bonds, equities", "input"),
    ("LC4",  "Stock of HQLA (before caps)  [= LC1+LC2+LC3]", None,    82_100,  None,  None, "Auto-calculated", "calc"),
    ("LC5",  "Level 2 cap adjustment",                         None,        0,  None,  None, "Level 2 capped at 40% of HQLA; Level 2B capped at 15%", "calc"),
    ("LC6",  "Adjusted stock of HQLA  [= LC4 − LC5]",         None,    82_100,  None,  None, "Auto-calculated — NUMERATOR", "calc"),
    (None, None, None, None, None, None, None, "spacer"),
    # Outflows
    (None, "SECTION 2 — CASH OUTFLOWS (30-day stress)", None, None, None, None, None, "section"),
    ("LC7",  "Retail deposits — stable (run-off rate: 3%)",   42_000,   1_260,  0.03,  None, "Insured, relationship deposits", "input"),
    ("LC8",  "Retail deposits — less stable (10%)",            18_000,   1_800,  0.10,  None, "Higher risk retail deposits", "input"),
    ("LC9",  "Unsecured wholesale — operational (25%)",        22_000,   5_500,  0.25,  None, "Clearing, custody, cash mgmt", "input"),
    ("LC10", "Unsecured wholesale — non-operational (100%)",   15_000,  15_000,  1.00,  None, "All other corporate deposits", "input"),
    ("LC11", "Unsecured wholesale — financial (100%)",          8_000,   8_000,  1.00,  None, "FI wholesale funding", "input"),
    ("LC12", "Secured funding (haircut applies)",               5_000,   2_500,  0.50,  None, "Non-Level 1 backed repos", "input"),
    ("LC13", "Drawdowns on committed credit facilities",        3_500,   1_400,  0.40,  None, "Retail undrawn committed facilities", "input"),
    ("LC14", "Derivative payables & collateral calls",          2_200,   2_200,  1.00,  None, "Mark-to-market + contractual outflows", "input"),
    ("LC15", "Total cash outflows  [= LC7 to LC14]",            None,   37_660,  None,  None, "Auto-calculated", "calc"),
    (None, None, None, None, None, None, None, "spacer"),
    # Inflows
    (None, "SECTION 3 — CASH INFLOWS (30-day stress)", None, None, None, None, None, "section"),
    ("LC16", "Secured lending — Level 1 collateral (0%)",        5_000,       0,  0.00,  None, "Reverse repos backed by HQLA Level 1", "input"),
    ("LC17", "Secured lending — Level 2A collateral (15%)",      3_000,   2_550,  0.85,  None, "", "input"),
    ("LC18", "Performing inflows — retail loans",                 4_500,   2_250,  0.50,  None, "50% of contractual payments due", "input"),
    ("LC19", "Performing inflows — wholesale / financial",        6_000,   6_000,  1.00,  None, "100% of contractual payments due", "input"),
    ("LC20", "Total cash inflows (uncapped)  [= LC16 to LC19]",  None,   10_800,  None,  None, "Auto-calculated", "calc"),
    ("LC21", "Inflow cap (max 75% of outflows)",                  None,   28_245,  None,  None, "75% × LC15", "calc"),
    ("LC22", "Net cash outflows  [= LC15 − min(LC20, LC21)]",    None,   26_860,  None,  None, "DENOMINATOR — Auto-calculated", "calc"),
    (None, None, None, None, None, None, None, "spacer"),
    # LCR Result
    (None, "SECTION 4 — LCR RESULT", None, None, None, None, None, "section"),
    ("LC23", "Liquidity Coverage Ratio  [= LC6 / LC22]",         None,    3.056,  None,  1.00, "Min 100%  (fully phased-in Jan 2019)", "ratio"),
    ("LC24", "Surplus HQLA  [= LC6 − LC22]",                     None,   55_240,  None,  None, "Absolute buffer above minimum", "calc"),
]

r = 7
for row in LCR_ROWS:
    code, desc, unw, w, rate, mn, note, rtype = row
    if rtype == "spacer":
        wc.row_dimensions[r].height = 6; r += 1; continue
    if rtype == "section":
        section_bar(wc, r, 1, 7, f"  {desc}", bg=C["navy"]); r += 1; continue
    desc_row(wc, r, code, desc)
    if rtype == "ratio":
        calc_cell(wc, r, 3, unw or "—")
        calc_cell(wc, r, 4, w, fmt="0.00%")
        cell(wc, r, 5, rate, color="9E9E9E", size=9, bg=C["white"], h="center")
        cell(wc, r, 6, mn, bold=True, color=C["red"], size=10, bg="FFF3F3", h="right", fmt="0.00%")
    elif rtype == "calc":
        cell(wc, r, 3, unw or "—", color="9E9E9E", size=9, bg=C["white"], h="center")
        calc_cell(wc, r, 4, w, fmt='#,##0' if isinstance(w, int) else "0.00%")
        cell(wc, r, 5, f"{rate*100:.0f}%" if rate is not None else "—", color="9E9E9E", size=9, bg=C["white"], h="center")
        cell(wc, r, 6, "—", color="9E9E9E", bg=C["white"], h="center")
    else:
        input_cell(wc, r, 3, unw, fmt='#,##0')
        input_cell(wc, r, 4, w,   fmt='#,##0')
        cell(wc, r, 5, f"{rate*100:.0f}%" if rate is not None else "—", bold=True, color=C["mid_blue"], size=10, bg=C["light_blue"], h="center")
        cell(wc, r, 6, "—", color="9E9E9E", bg=C["white"], h="center")
    cell(wc, r, 7, note or "", color="595959", size=9, bg=C["white"], italic=True, wrap=True)
    wc.row_dimensions[r].height = 18
    r += 1


# ══════════════════════════════════════════════════════════════════════════════
# PANEL D — NSFR
# ══════════════════════════════════════════════════════════════════════════════
wd = wb.create_sheet("D - NSFR")
sheet_setup(wd, freeze="A7")
set_cols(wd, [8, 58, 18, 14, 12, 22])

title_block(wd, 1, 1, 6,
            "PANEL D — NET STABLE FUNDING RATIO (NSFR)",
            "Unit: VND billions  |  Ref: BCBS Oct 2014  |  NSFR = ASF / RSF ≥ 100%")
wd.row_dimensions[3].height = 6

merge(wd, 4, 1, 2, "  Ref. period: 31 Dec 2024  |  1-year horizon",
      italic=True, size=9, color=C["navy"], bg="EBF3FB")
wd.row_dimensions[4].height = 14
wd.row_dimensions[5].height = 6

for i, h in enumerate(["Code", "Description", "Carrying value", "ASF / RSF factor", "Weighted amount", "Notes"], 1):
    col_hdr(wd, 6, i, h)
wd.row_dimensions[6].height = 28

NSFR_ROWS = [
    # ASF
    (None, "SECTION 1 — AVAILABLE STABLE FUNDING (ASF)", None, None, None, None, "section"),
    ("NS1",  "Tier 1 & Tier 2 regulatory capital",                  105_500, 1.00,  105_500, "100% factor — permanent funding", "input"),
    ("NS2",  "Other preferred stock / instruments (residual ≥ 1Y)", 12_000,  1.00,  12_000,  "100% factor", "input"),
    ("NS3",  "Stable retail demand/term deposits (< 1Y)",            42_000,  0.95,  39_900,  "95% factor — insured, sticky", "input"),
    ("NS4",  "Less stable retail deposits (< 1Y)",                   18_000,  0.90,  16_200,  "90% factor", "input"),
    ("NS5",  "Wholesale non-fin. / corporate (< 6M)",                22_000,  0.50,  11_000,  "50% factor — operational relationships", "input"),
    ("NS6",  "Wholesale funding — other (6M–1Y)",                    10_000,  0.50,   5_000,  "50% factor", "input"),
    ("NS7",  "Wholesale funding — other (≥ 1Y)",                      8_000,  1.00,   8_000,  "100% factor", "input"),
    ("NS8",  "Other liabilities (no residual maturity)",              5_000,  0.00,       0,  "0% factor — e.g., overnight wholesale", "input"),
    ("NS9",  "Total ASF  [= sum NS1–NS8]",                           None,    None, 197_600,  "Auto-calculated", "calc"),
    (None, None, None, None, None, None, "spacer"),
    # RSF
    (None, "SECTION 2 — REQUIRED STABLE FUNDING (RSF)", None, None, None, None, "section"),
    ("NS10", "Level 1 HQLA (unencumbered)",                           62_000,  0.00,       0, "0% RSF — cash, CB reserves, 0%-RW sov.", "input"),
    ("NS11", "Level 2A HQLA (unencumbered)",                          18_000,  0.15,   2_700, "15% RSF", "input"),
    ("NS12", "Level 2B HQLA (unencumbered)",                           8_000,  0.50,   4_000, "50% RSF", "input"),
    ("NS13", "Performing loans — retail/SME (< 1Y)",                  28_000,  0.50,  14_000, "50% RSF", "input"),
    ("NS14", "Performing loans — corporate (< 1Y)",                   35_000,  0.50,  17_500, "50% RSF", "input"),
    ("NS15", "Performing loans — retail/SME (≥ 1Y)",                  45_000,  0.65,  29_250, "65% RSF — <35% risk weight", "input"),
    ("NS16", "Performing loans — other (≥ 1Y, RW > 35%)",            80_000,  0.85,  68_000, "85% RSF", "input"),
    ("NS17", "Derivatives receivables (net)",                          15_000,  1.00,  15_000, "100% RSF", "input"),
    ("NS18", "All other assets",                                       25_000,  1.00,  25_000, "100% RSF", "input"),
    ("NS19", "Off-balance sheet commitments (5% of undrawn)",         35_500,  0.05,   1_775, "5% RSF — committed credit/liquidity facilities", "input"),
    ("NS20", "Total RSF  [= sum NS10–NS19]",                          None,    None, 177_225, "Auto-calculated", "calc"),
    (None, None, None, None, None, None, "spacer"),
    # NSFR Result
    (None, "SECTION 3 — NSFR RESULT", None, None, None, None, "section"),
    ("NS21", "Net Stable Funding Ratio  [= NS9 / NS20]",              None,    None,   1.115, "Min 100%  (phased-in Jan 2018)", "ratio"),
    ("NS22", "NSFR surplus  [= NS9 − NS20]",                          None,    None,  20_375, "Absolute stable funding buffer", "calc"),
    ("NS23", "Memo: Short-term wholesale funding dependency",          None,    None,   0.102, "Wholesale < 1Y / Total liabilities", "input"),
]

r = 7
for row in NSFR_ROWS:
    code, desc, carry, factor, wt, note, rtype = row
    if rtype == "spacer":
        wd.row_dimensions[r].height = 6; r += 1; continue
    if rtype == "section":
        section_bar(wd, r, 1, 6, f"  {desc}", bg=C["navy"]); r += 1; continue
    desc_row(wd, r, code, desc)
    if rtype == "ratio":
        cell(wd, r, 3, "—", color="9E9E9E", bg=C["white"], h="center")
        cell(wd, r, 4, "—", color="9E9E9E", bg=C["white"], h="center")
        calc_cell(wd, r, 5, wt, fmt="0.00%")
        cell(wd, r, 6, note or "", color="595959", size=9, bg=C["white"], italic=True, wrap=True)
    elif rtype == "calc":
        cell(wd, r, 3, "—", color="9E9E9E", bg=C["white"], h="center")
        cell(wd, r, 4, "—", color="9E9E9E", bg=C["white"], h="center")
        fmt = '#,##0' if isinstance(wt, int) or (wt and abs(wt) > 1) else "0.00%"
        calc_cell(wd, r, 5, wt, fmt=fmt)
        cell(wd, r, 6, note or "", color="595959", size=9, bg=C["white"], italic=True, wrap=True)
    else:
        fmt_c = '#,##0' if carry and abs(carry) > 1 else "0.00%"
        input_cell(wd, r, 3, carry, fmt=fmt_c)
        cell(wd, r, 4, f"{factor*100:.0f}%" if factor is not None else "—",
             bold=True, color=C["mid_blue"], size=10, bg=C["light_blue"], h="center")
        input_cell(wd, r, 5, wt, fmt='#,##0')
        cell(wd, r, 6, note or "", color="595959", size=9, bg=C["white"], italic=True, wrap=True)
    wd.row_dimensions[r].height = 18
    r += 1


# ══════════════════════════════════════════════════════════════════════════════
# SAVE
# ══════════════════════════════════════════════════════════════════════════════
wb.save(OUT_FILE)
print(f"Saved: {OUT_FILE}")
print(f"Sheets: {[s.title for s in wb.worksheets]}")
