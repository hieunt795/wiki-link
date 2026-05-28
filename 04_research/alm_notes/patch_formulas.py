"""
Patch formulas — targeted với row numbers chính xác từ scan.
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

PATH = r"D:\AI\Wiki-agentic\04_research\alm_notes\liquidity_sensitivity_NII_v2.xlsx"
wb   = openpyxl.load_workbook(PATH)
ws3  = wb["03_CashflowLadder"]
ws4  = wb["04_ScenarioMatrix"]
ws5  = wb["05_NIICalc"]

def _f(h): return PatternFill("solid", fgColor=h)
def _ft(bold=False, col="000000", sz=10):
    return Font(bold=bold, color=col, size=sz, name="Calibri")
def _bd():
    s = Side(style="thin", color="BFBFBF")
    return Border(left=s, right=s, top=s, bottom=s)

def put(ws, r, ci, formula, fmt="#,##0", bold=False, bg=None, col="000000"):
    cl = ws.cell(row=r, column=ci, value=formula)
    cl.font = _ft(bold=bold, col=col, sz=10)
    cl.alignment = Alignment(horizontal="right", vertical="center")
    cl.border = _bd()
    cl.number_format = fmt
    if bg: cl.fill = _f(bg)

# ─────────────────────────────────────────────────────────────────────────────
# SHEET 03 — CashflowLadder
# Row 14 = TONG INFLOWS  (data: r7..r13, cols B..H)
# Row 25 = TONG OUTFLOWS (data: r17..r24)
# Row 28 = NET GAP
# Row 29 = CUMULATIVE GAP
# Row 32 = NEG GAP (funding gap cần trám)
# ─────────────────────────────────────────────────────────────────────────────
BCOLS = list(range(2, 9))   # B..H = bucket cols
TCOL  = 9                   # I = TONG

C_IN   = {"bg":"BDD7EE", "fg":"1F3864"}
C_OUT  = {"bg":"FFCDD2", "fg":"C62828"}
C_GAP  = {"bg":"DEEAF1", "fg":"000000"}
C_NEG  = {"bg":"FFCDD2", "fg":"C62828"}

# INFLOW total: SUM rows 7..13 per bucket
for ci in BCOLS:
    ltr = chr(64 + ci)
    put(ws3, 14, ci, f"=SUM({ltr}7:{ltr}13)",
        bold=True, bg=C_IN["bg"], col=C_IN["fg"])
put(ws3, 14, TCOL, f"=SUM(B14:H14)", bold=True, bg=C_IN["bg"], col=C_IN["fg"])

# OUTFLOW total: SUM rows 17..24 per bucket
for ci in BCOLS:
    ltr = chr(64 + ci)
    put(ws3, 25, ci, f"=SUM({ltr}17:{ltr}24)",
        bold=True, bg=C_OUT["bg"], col=C_OUT["fg"])
put(ws3, 25, TCOL, f"=SUM(B25:H25)", bold=True, bg=C_OUT["bg"], col=C_OUT["fg"])

# NET GAP = row 14 - row 25  per bucket
for ci in BCOLS:
    ltr = chr(64 + ci)
    put(ws3, 28, ci, f"={ltr}14-{ltr}25",
        fmt="#,##0;[Red]-#,##0", bold=True)
    # apply colour via static format (positive=green, negative=red not possible via openpyxl without CF)
put(ws3, 28, TCOL, f"=SUM(B28:H28)", bold=True)

# CUMULATIVE GAP: running sum of NET GAP
prev_cum = None
for i, ci in enumerate(BCOLS):
    ltr = chr(64 + ci)
    if i == 0:
        formula = f"={ltr}28"
    else:
        pltr = chr(64 + BCOLS[i-1])
        formula = f"={pltr}29+{ltr}28"
    put(ws3, 29, ci, formula, fmt="#,##0;[Red]-#,##0", bold=True,
        bg="F3E5F5", col="4A148C")
put(ws3, 29, TCOL, "=H29", bold=True, bg="F3E5F5", col="4A148C")

# NEG GAP = MIN(0, net_gap)
for ci in BCOLS:
    ltr = chr(64 + ci)
    put(ws3, 32, ci, f"=MIN(0,{ltr}28)",
        fmt="#,##0;[Red]-#,##0", bold=True,
        bg=C_NEG["bg"], col=C_NEG["fg"])
put(ws3, 32, TCOL, "=SUM(B32:H32)", bold=True, bg=C_NEG["bg"], col=C_NEG["fg"])

print("Sheet 03: formulas written for rows 14, 25, 28, 29, 32")

# ─────────────────────────────────────────────────────────────────────────────
# SHEET 04 — ScenarioMatrix
# Spread data rows: scan from row 22 downward for 7 tenors
# Col layout: A=tenor  B=base_rate  C=sp_baseline  D=sp_tight  E=sp_stressed
#             F=sp_severe  G=repl_baseline  H=repl_tight  I=repl_stressed
# ─────────────────────────────────────────────────────────────────────────────
TENORS = ["O/N","1W","1M","3M","6M","1Y",">1Y"]
# Find spread data rows: look for tenor names in col A starting around row 22
spread_rows = {}
for row in ws4.iter_rows(min_row=20, max_row=45, min_col=1, max_col=1):
    v = row[0].value
    if v and str(v).strip() in TENORS:
        spread_rows[str(v).strip()] = row[0].row

print(f"Sheet04 spread rows: {spread_rows}")

for tenor, r in spread_rows.items():
    # G = B + C/10000  (baseline replacement rate)
    # H = B + D/10000  (tight)
    # I = B + E/10000  (stressed)
    for repl_col, sp_col in [(7,"C"), (8,"D"), (9,"E")]:
        sp_val = ws4.cell(row=r, column=ord(sp_col)-64).value
        if sp_val not in (None, "N/A"):
            put(ws4, r, repl_col, f"=B{r}+{sp_col}{r}/10000",
                fmt="0.000%", bg="BDD7EE", col="1F3864")
        else:
            cl = ws4.cell(row=r, column=repl_col, value="N/A")
            cl.font = _ft(col="9E9E9E"); cl.border = _bd()
            cl.alignment = Alignment(horizontal="center")
            cl.fill = _f("E0E0E0")

print("Sheet 04: replacement rate formulas written (cols G, H, I)")

# ─────────────────────────────────────────────────────────────────────────────
# SHEET 05 — NIICalc
# Data rows: 13..19  (O/N, 1W, 1M, 3M, 6M, 1Y, >1Y)
# Col layout:
#   A=bucket  B=days  C=gap  D=orig_rate
#   E=sp_baseline  F=DNII_baseline
#   G=sp_tight     H=DNII_tight
#   I=sp_stressed  J=DNII_stressed
#   K=sp_severe    L=DNII_severe
# Summary rows:
#   20 = TONG DNII point-in-time
#   21 = DNII Annualized ×12
#   22 = DNIM bps
#   23 = NIM sau shock
# Key input cells: B5=earning_assets  B7=NIM_baseline
# ─────────────────────────────────────────────────────────────────────────────
DATA_ROWS = list(range(13, 20))  # rows 13..19

SCEN_COLS = [
    ("Baseline", 5,  6,  "70AD47"),
    ("Tight",    7,  8,  "FFC000"),
    ("Stressed", 9,  10, "ED7D31"),
    ("Severe",   11, 12, "FF4B4B"),
]

# ΔNII per bucket × scenario
for r in DATA_ROWS:
    for scen, sp_col, nii_col, color in SCEN_COLS:
        sp_ltr  = chr(64 + sp_col)
        nii_ltr = chr(64 + nii_col)
        sp_val  = ws5.cell(row=r, column=sp_col).value
        if sp_val not in (None, "N/A"):
            # ΔNII = gap × (spread_bps/10000) × (days/365)
            formula = f"=C{r}*({sp_ltr}{r}/10000)*(B{r}/365)"
            put(ws5, r, nii_col, formula,
                fmt="#,##0.000;[Red]-#,##0.000",
                bold=True, bg="FFCDD2", col="C62828")
        # else: leave N/A as-is

# TONG DNII row 20: SUM of data rows (skip N/A via IFERROR)
for scen, sp_col, nii_col, color in SCEN_COLS:
    col_ltr = chr(64 + nii_col)
    formula = f"=SUMPRODUCT(IFERROR({col_ltr}13:{col_ltr}19,0))"
    put(ws5, 20, nii_col, formula,
        fmt="#,##0.00;[Red]-#,##0.00",
        bold=True, bg=color, col="FFFFFF")

# ΔNII Annualized row 21: total × 12
for scen, sp_col, nii_col, color in SCEN_COLS:
    col_ltr = chr(64 + nii_col)
    put(ws5, 21, nii_col, f"={col_ltr}20*12",
        fmt="#,##0.00;[Red]-#,##0.00",
        bold=True, bg=color, col="FFFFFF")

# ΔNIM bps row 22: annualized / EA × 10000
for scen, sp_col, nii_col, color in SCEN_COLS:
    col_ltr = chr(64 + nii_col)
    put(ws5, 22, nii_col, f"=IFERROR({col_ltr}21/B5*10000,0)",
        fmt='0.00" bps"',
        bold=True, bg=color, col="FFFFFF")

# NIM sau shock row 23: NIM_baseline + ΔNIM/10000
for scen, sp_col, nii_col, color in SCEN_COLS:
    col_ltr = chr(64 + nii_col)
    put(ws5, 23, nii_col, f"=B7+{col_ltr}22/10000",
        fmt="0.000%",
        bold=True, bg=color, col="FFFFFF")

print("Sheet 05: DNII formulas written for rows 13-19, summary rows 20-23")

# ── Save ──────────────────────────────────────────────────────────────────────
wb.save(PATH)
print(f"OK Saved: {PATH}")
