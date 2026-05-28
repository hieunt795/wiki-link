"""
LCR Waterfall — Formula-driven rebuild
Mọi cell tính toán dùng =formula Excel; chỉ ô vàng (INPUT) là giá trị tĩnh.

Column layout thống nhất:
  HQLA section  : A=desc  B=balance(in)  C=haircut%(in)  D=adj_formula  E=cap_formula  F=cap_rule  G=note
  Outflow section: A=desc  B=balance(in)  C=basel_runoff(in)  D=vn_runoff(in)  E=outflow_formula  F=note
  Inflow section : A=desc  B=balance(in)  C=rate(in)          D=               E=inflow_formula   F=note
  LCR calc       : A:D merged=label       E=value_formula      F:G merged=note
  Scenario table : A=name  B=out_mult(in) C=obs_add(in)  D=gross_out_f  E=hqla_mult(in)
                   F=nco_f  G=hqla_f  H=lcr_pct_f  I=headroom_f  J=status_f
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import BarChart, Reference
from openpyxl.chart.series import SeriesLabel

# ── Palette ───────────────────────────────────────────────────────────────────
C = dict(
    dk="1F3864", mb="2E75B6", lb="BDD7EE", vl="DEEAF1",
    grn="375623", lgrn="E2EFDA", inp="FFFACD",
    red="C62828", lred="FFCDD2", org="833C00",
    teal="006064", lteal="E0F7FA", gold="F57F17", lgold="FFF9C4",
    gy="F2F2F2", pur="4A148C",
)

def _f(h): return PatternFill("solid", fgColor=h)
def _ft(bold=False, col="000000", sz=10, it=False):
    return Font(bold=bold, color=col, size=sz, italic=it, name="Calibri")
def _al(h="left", v="center", wrap=False):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)
def _bd():
    s = Side(style="thin", color="BFBFBF")
    return Border(left=s, right=s, top=s, bottom=s)

def wc(ws, r, ci, val=None, bold=False, col="000000", sz=10, it=False,
       bg=None, h="left", wrap=False, fmt=None):
    cl = ws.cell(row=r, column=ci, value=val)
    cl.font = _ft(bold=bold, col=col, sz=sz, it=it)
    cl.alignment = _al(h=h, wrap=wrap)
    cl.border = _bd()
    if bg:  cl.fill = _f(bg)
    if fmt: cl.number_format = fmt
    return cl

def mg(ws, r, c1, c2, val=None, bold=False, col="000000", sz=10, it=False,
       bg=None, h="left", wrap=False, fmt=None):
    ws.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
    return wc(ws, r, c1, val, bold=bold, col=col, sz=sz, it=it,
              bg=bg, h=h, wrap=wrap, fmt=fmt)

def sec(ws, r, c1, c2, text, bg=None, sz=11):
    bg = bg or C["dk"]
    mg(ws, r, c1, c2, text, bold=True, col="FFFFFF", sz=sz, bg=bg)
    ws.row_dimensions[r].height = 22
    return r + 1

def hdrs(ws, r, cols):
    for ci, txt in cols:
        wc(ws, r, ci, txt, bold=True, col="FFFFFF", bg=C["mb"], h="center", wrap=True)
    ws.row_dimensions[r].height = 30
    return r + 1

def inp(ws, r, ci, val, fmt="#,##0"):
    cl = wc(ws, r, ci, val, bold=True, col=C["dk"], bg=C["inp"], h="right")
    cl.number_format = fmt
    return cl

def fml(ws, r, ci, formula, fmt="#,##0", bold=False, bg=None, col="000000"):
    """Write a formula string to a cell."""
    cl = wc(ws, r, ci, formula, bold=bold, col=col, bg=bg, h="right")
    cl.number_format = fmt
    return cl

def alt(r): return C["vl"] if r % 2 == 0 else None

# ─── Open workbook ────────────────────────────────────────────────────────────
PATH      = r"D:\AI\Wiki-agentic\04_research\alm_notes\liquidity_sensitivity_NII.xlsx"
PATH_OUT  = r"D:\AI\Wiki-agentic\04_research\alm_notes\liquidity_sensitivity_NII_v2.xlsx"
wb = openpyxl.load_workbook(PATH)
if "07_LCR_Waterfall" in wb.sheetnames:
    del wb["07_LCR_Waterfall"]

ws = wb.create_sheet("07_LCR_Waterfall")
ws.sheet_view.showGridLines = False
ws.freeze_panes = "A5"
ws.sheet_properties.tabColor = "006064"

# Column widths
for ltr, w in [("A",36),("B",14),("C",13),("D",14),("E",16),("F",16),("G",22),
               ("H",13),("I",13),("J",16)]:
    ws.column_dimensions[ltr].width = w

# ── Title ─────────────────────────────────────────────────────────────────────
mg(ws,1,1,10,"LCR WATERFALL — LIQUIDITY COVERAGE RATIO (30-DAY STRESS)",
   bold=True,col="FFFFFF",sz=14,bg=C["teal"],h="center")
ws.row_dimensions[1].height = 34
mg(ws,2,1,10,
   "LCR = HQLA / Net Cash Outflows (30d)  >=  100%  |  Ô vàng = INPUT  |  Ô xanh = Formula tự động tính",
   it=True,col="004D40",sz=10,bg=C["lteal"],h="center")
ws.row_dimensions[2].height = 18

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1 — HQLA STOCK
# col D = adjusted = B*(1-C)
# col E = cap_applied (= D for L1 items; MIN formula for L2 total rows)
# HQLA grand total E = D_l1_total + E_l2a_total + E_l2b_total
# ─────────────────────────────────────────────────────────────────────────────
r = 4
r = sec(ws, r, 1, 10, "SECTION 1 — HQLA STOCK (High Quality Liquid Assets)", bg=C["teal"])
r = hdrs(ws, r, [(1,"Loại tài sản"),(2,"Số dư\n(tỷ VND)"),(3,"Haircut\n%"),
                 (4,"Adj. value\n(tỷ) [formula]"),(5,"Cap applied\n(tỷ) [formula]"),
                 (6,"Quy tắc cap Basel III"),(7,"Ghi chú")])

# ── Level 1 ──
r = sec(ws, r, 1, 10, "Level 1 — Haircut 0%,  không có cap riêng", bg=C["mb"], sz=10)

L1 = [
    ("Tiền mặt + gửi NHNN (excess reserves)", 2_000, 0.00,
     "Không cap", "Dự trữ bắt buộc + tiền mặt"),
    ("TPCP Việt Nam (0% risk weight) — tổng danh mục", 12_000, 0.00,
     "Không cap", "TPCP 1Y / 3Y / 5Y từ HQLA pool"),
    ("Tín phiếu SBV",  0, 0.00, "Không cap", ""),
    ("Gửi SBV vượt DTBB", 500, 0.00, "Không cap", ""),
]
l1_item_rows = []
for name, bal, hcut, cap_rule, note in L1:
    bg = alt(r)
    wc(ws, r, 1, f"  {name}", sz=10, bg=bg)
    inp(ws, r, 2, bal)
    inp(ws, r, 3, hcut, fmt="0.00%")
    # D = B*(1-C)
    fml(ws, r, 4, f"=B{r}*(1-C{r})", bg=C["lteal"], col="004D40")
    # E = D  (no cap for L1 items)
    fml(ws, r, 5, f"=D{r}", bg=C["lteal"], col="004D40")
    wc(ws, r, 6, cap_rule, it=True, col="666666", sz=9, bg=bg)
    mg(ws, r, 7, 7, note, it=True, col="666666", sz=9, bg=bg)
    l1_item_rows.append(r)
    ws.row_dimensions[r].height = 18; r += 1

r_l1_total = r
mg(ws, r, 1, 3, "TỔNG LEVEL 1", bold=True, col="FFFFFF", bg=C["teal"])
fml(ws, r, 4, f"=SUM(D{l1_item_rows[0]}:D{l1_item_rows[-1]})",
    bold=True, bg=C["teal"], col="FFFFFF")
# E = D (no cap needed for L1)
fml(ws, r, 5, f"=D{r}", bold=True, bg=C["teal"], col="FFFFFF")
mg(ws, r, 6, 7, "= 100% của giá trị điều chỉnh", bold=True, col="FFFFFF", bg=C["teal"])
ws.row_dimensions[r].height = 22; r += 1

# ── Level 2A ──
r = sec(ws, r, 1, 10, "Level 2A — Haircut 15%,  cap: <= 40% Adjusted HQLA", bg="1565C0", sz=10)

L2A = [
    ("Agency / GSE securities",           0, 0.15, "Cap 40%", ""),
    ("Covered bonds rated >= AA-",        0, 0.15, "Cap 40%", ""),
    ("TPCP nước ngoài (0% RW, nội tệ)",  0, 0.15, "Cap 40%", ""),
]
l2a_item_rows = []
for name, bal, hcut, cap_rule, note in L2A:
    bg = alt(r)
    wc(ws, r, 1, f"  {name}", sz=10, bg=bg)
    inp(ws, r, 2, bal)
    inp(ws, r, 3, hcut, fmt="0.00%")
    fml(ws, r, 4, f"=B{r}*(1-C{r})", bg=C["lteal"], col="004D40")
    fml(ws, r, 5, f"=D{r}", bg=C["lteal"], col="004D40")
    wc(ws, r, 6, cap_rule, it=True, col="666666", sz=9, bg=bg)
    mg(ws, r, 7, 7, note, it=True, col="666666", sz=9, bg=bg)
    l2a_item_rows.append(r)
    ws.row_dimensions[r].height = 18; r += 1

r_l2a_total = r
mg(ws, r, 1, 3, "TỔNG LEVEL 2A (sau haircut, trước cap)", bold=True, col="FFFFFF", bg="1565C0")
# D = SUM of adjusted items
fml(ws, r, 4, f"=SUM(D{l2a_item_rows[0]}:D{l2a_item_rows[-1]})",
    bold=True, bg="1565C0", col="FFFFFF")
# E = cap applied: MIN(D, 40% × (L1_total_D + D_l2a))
# Basel formula: L2A_cap = MIN(L2A_adj, (2/3)*L1 adjusted) -- simplified as 40% of total
fml(ws, r, 5,
    f"=MIN(D{r}, 0.4*(D{r_l1_total}+D{r}))",
    bold=True, bg="1565C0", col="FFFFFF", fmt="#,##0")
mg(ws, r, 6, 7, "Cap: MIN(L2A_adj, 40% x (L1+L2A))", bold=True, col="FFFFFF", bg="1565C0")
ws.row_dimensions[r].height = 22; r += 1

# ── Level 2B ──
r = sec(ws, r, 1, 10, "Level 2B — Haircut 25-50%,  cap: <= 15% Adjusted HQLA", bg="1976D2", sz=10)

L2B = [
    ("Trái phiếu DN investment grade (BBB-/A+)", 2_000, 0.25, "Cap 15%", "Haircut 25%"),
    ("Cổ phiếu niêm yết (index eligible)",           0, 0.50, "Cap 15%", "Haircut 50%"),
    ("RMBS >= AA-",                                  0, 0.25, "Cap 15%", ""),
]
l2b_item_rows = []
for name, bal, hcut, cap_rule, note in L2B:
    bg = alt(r)
    wc(ws, r, 1, f"  {name}", sz=10, bg=bg)
    inp(ws, r, 2, bal)
    inp(ws, r, 3, hcut, fmt="0.00%")
    fml(ws, r, 4, f"=B{r}*(1-C{r})", bg=C["lteal"], col="004D40")
    fml(ws, r, 5, f"=D{r}", bg=C["lteal"], col="004D40")
    wc(ws, r, 6, cap_rule, it=True, col="666666", sz=9, bg=bg)
    mg(ws, r, 7, 7, note, it=True, col="666666", sz=9, bg=bg)
    l2b_item_rows.append(r)
    ws.row_dimensions[r].height = 18; r += 1

r_l2b_total = r
mg(ws, r, 1, 3, "TỔNG LEVEL 2B (sau haircut, trước cap)", bold=True, col="FFFFFF", bg="1976D2")
fml(ws, r, 4, f"=SUM(D{l2b_item_rows[0]}:D{l2b_item_rows[-1]})",
    bold=True, bg="1976D2", col="FFFFFF")
# E = MIN(L2B_adj, 15% × (L1 + L2A_cap + L2B_adj))
fml(ws, r, 5,
    f"=MIN(D{r}, 0.15*(D{r_l1_total}+E{r_l2a_total}+D{r}))",
    bold=True, bg="1976D2", col="FFFFFF", fmt="#,##0")
mg(ws, r, 6, 7, "Cap: MIN(L2B_adj, 15% x (L1+L2A_cap+L2B))", bold=True, col="FFFFFF", bg="1976D2")
ws.row_dimensions[r].height = 22; r += 1

# ── HQLA Grand Total ──
r_hqla_total = r
mg(ws, r, 1, 3, "TỔNG HQLA ADJUSTED", bold=True, col="FFFFFF", sz=12, bg=C["teal"])
# E = L1_D + L2A_E (cap applied) + L2B_E (cap applied)
fml(ws, r, 5,
    f"=D{r_l1_total}+E{r_l2a_total}+E{r_l2b_total}",
    bold=True, bg=C["teal"], col="FFFFFF", fmt="#,##0")
mg(ws, r, 6, 7,
   f"=\"L1: \"&TEXT(D{r_l1_total},\"#,##0\")&\" + L2A: \"&TEXT(E{r_l2a_total},\"#,##0\")&\" + L2B: \"&TEXT(E{r_l2b_total},\"#,##0\")",
   bold=True, col="FFFFFF", bg=C["teal"])
ws.row_dimensions[r].height = 26; r += 2

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2 — STRESS OUTFLOWS  (kết quả ở col E = B*D)
# ─────────────────────────────────────────────────────────────────────────────
r = sec(ws, r, 1, 10, "SECTION 2 — STRESS OUTFLOWS 30 NGAY  (dong chay ra stressed)")
r = hdrs(ws, r, [(1,"Loại outflow"),(2,"Số dư\n(tỷ)"),(3,"Basel III\nrunoff %"),
                 (4,"VN stressed\nrunoff % [INPUT]"),(5,"Outflow\n(tỷ) [formula]"),
                 (6,"Ghi chú Basel III"),(7,"")])

def outflow_section(ws, r, title, items, bg_color):
    """Write one outflow sub-section. Returns (r_after_rows, r_total, section_outflow_items)."""
    r = sec(ws, r, 1, 10, title, bg=bg_color, sz=10)
    item_rows = []
    for name, bal, r_basel, r_vn, note in items:
        bg = alt(r)
        wc(ws, r, 1, f"  {name}", sz=10, bg=bg)
        inp(ws, r, 2, bal)
        inp(ws, r, 3, r_basel, fmt="0%")
        inp(ws, r, 4, r_vn,   fmt="0%")
        # E = B * D  (VN stressed runoff rate)
        fml(ws, r, 5, f"=B{r}*D{r}", bg=C["lred"], col=C["red"], bold=True)
        mg(ws, r, 6, 7, note, it=True, col="666666", sz=9, bg=bg)
        item_rows.append(r)
        ws.row_dimensions[r].height = 18; r += 1
    # Section total
    r_tot = r
    mg(ws, r, 1, 4, f"Tổng outflow — {title.split('—')[-1].strip()}", bold=True, col="FFFFFF", bg=bg_color)
    fml(ws, r, 5, f"=SUM(E{item_rows[0]}:E{item_rows[-1]})", bold=True, col="FFFFFF", bg=bg_color)
    mg(ws, r, 6, 7, "", bg=bg_color)
    ws.row_dimensions[r].height = 20; r += 1
    return r, r_tot

RETAIL_ITEMS = [
    ("Tiền gửi KKH retail — core stable (65%)",  3_900, 0.03, 0.05, "Stable deposits: 3%"),
    ("Tiền gửi KKH retail — volatile (35%)",     2_100, 0.10, 0.10, "Less stable: 10%"),
    ("Tiền tiết kiệm 1M (retail)",               5_000, 0.10, 0.10, "Less stable retail: 10%"),
    ("Tiền gửi kỳ hạn 3M (retail)",             4_000, 0.10, 0.08, ""),
    ("Tiền gửi kỳ hạn 6M (retail)",             6_000, 0.05, 0.05, "Tenor dài — runoff thấp"),
    ("Tiền gửi kỳ hạn 12M+ (retail)",           7_500, 0.03, 0.03, ""),
]
r, r_retail_total = outflow_section(ws, r, "2.1 Tiền gửi bán lẻ — Retail Deposits", RETAIL_ITEMS, C["mb"])

WHOLESALE_ITEMS = [
    ("Tiền gửi KKH corporate — operational",  2_400, 0.25, 0.25, "Operational deposits = 25%"),
    ("Tiền gửi KKH corporate — non-operational",1_600,0.40,0.40, "Non-operational = 40%"),
    ("Tiền gửi kỳ hạn 3M corporate",         4_000, 0.20, 0.20, "Non-financial wholesale: 20%"),
    ("Tiền gửi kỳ hạn 6M corporate",         6_000, 0.10, 0.10, ""),
    ("Tiền gửi kỳ hạn 12M corporate",        2_500, 0.05, 0.05, ""),
    ("Tiền gửi tổ chức tài chính",               0, 1.00, 1.00, "Financial entity non-op: 100%"),
]
r, r_wholesale_total = outflow_section(ws, r, "2.2 Tiền gửi tổ chức — Wholesale Deposits", WHOLESALE_ITEMS, "37474F")

SECURED_ITEMS = [
    ("Repo TPCP với SBV OMO đáo hạn",         0, 0.00, 0.00, "Backed by L1, CB counterparty: 0%"),
    ("Repo TPCP với LNH đáo hạn",         2_000, 0.15, 0.15, "Backed by L1, non-CB: 15%"),
    ("Vay LNH unsecured — O/N",           1_000, 1.00, 1.00, "Unsecured wholesale: 100%"),
    ("Vay LNH unsecured — 1W",            2_000, 1.00, 1.00, "Unsecured wholesale: 100%"),
    ("Vay LNH unsecured — 1M",            1_500, 1.00, 1.00, "Unsecured wholesale: 100%"),
]
r, r_secured_total = outflow_section(ws, r, "2.3 Secured Funding / Vay có bảo đảm", SECURED_ITEMS, "4E342E")

OBS_ITEMS = [
    ("Hạn mức tín dụng retail chưa giải ngân",     1_500, 0.05, 0.05, "Committed revolving retail: 5%"),
    ("Hạn mức tín dụng corporate non-financial",   2_500, 0.10, 0.10, "Committed credit lines: 10%"),
    ("Hạn mức tín dụng financial entities",        1_000, 0.40, 0.40, "Financial entity facilities: 40%"),
    ("Bảo lãnh & L/C có thể bị call",               500, 0.05, 0.05, "Trade finance: 5%"),
]
r, r_obs_total = outflow_section(ws, r, "2.4 Cam kết ngoại bảng — Off-Balance Sheet", OBS_ITEMS, "4A148C")

# Grand total outflows
r += 1
r_gross_outflow = r
mg(ws, r, 1, 4, "TỔNG GROSS OUTFLOWS (30 ngày)", bold=True, col="FFFFFF", sz=12, bg=C["red"])
fml(ws, r, 5,
    f"=E{r_retail_total}+E{r_wholesale_total}+E{r_secured_total}+E{r_obs_total}",
    bold=True, col="FFFFFF", bg=C["red"], fmt="#,##0")
mg(ws, r, 6, 7,
   f"=\"Retail \"&TEXT(E{r_retail_total},\"#,##0\")&\" + WS \"&TEXT(E{r_wholesale_total},\"#,##0\")&\" + Sec \"&TEXT(E{r_secured_total},\"#,##0\")&\" + OBS \"&TEXT(E{r_obs_total},\"#,##0\")",
   bold=True, col="FFFFFF", bg=C["red"])
ws.row_dimensions[r].height = 26; r += 2

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3 — STRESS INFLOWS  (kết quả col E = B*C,  cap = gross*75%)
# ─────────────────────────────────────────────────────────────────────────────
r = sec(ws, r, 1, 10, "SECTION 3 — STRESS INFLOWS 30 NGAY  (cap 75% of Gross Outflows)")
r = hdrs(ws, r, [(1,"Loại inflow"),(2,"Số dư / hạn mức\n(tỷ)"),(3,"Inflow\nrate %"),
                 (4,""),(5,"Inflow amount\n(tỷ) [formula]"),(6,"Ghi chú Basel III"),(7,"")])

INFLOW_ITEMS = [
    ("Cho vay LNH secured (L1) đáo hạn",  500, 1.00, "Secured by L1: 100%"),
    ("Cho vay LNH unsecured đáo hạn",     800, 1.00, "Unsecured to financial: 100%"),
    ("Cho vay retail đáo hạn",            400, 0.50, "Retail loans: 50% (50% roll giả định)"),
    ("Cho vay non-financial corp đáo hạn",600, 1.00, "Performing loans: 100%"),
    ("Thu lãi chứng khoán trong 30d",     300, 1.00, "Bond coupons: 100%"),
    ("Inflow hợp đồng khác",              200, 1.00, "Other contractual: 100%"),
]
inflow_item_rows = []
for name, bal, rate, note in INFLOW_ITEMS:
    bg = alt(r)
    wc(ws, r, 1, f"  {name}", sz=10, bg=bg)
    inp(ws, r, 2, bal)
    inp(ws, r, 3, rate, fmt="0%")
    wc(ws, r, 4, "", bg=bg)
    # E = B * C
    fml(ws, r, 5, f"=B{r}*C{r}", bg=C["lgrn"], col=C["grn"], bold=True)
    mg(ws, r, 6, 7, note, it=True, col="666666", sz=9, bg=bg)
    inflow_item_rows.append(r)
    ws.row_dimensions[r].height = 18; r += 1

r_inflow_before_cap = r
mg(ws, r, 1, 4, "Tổng inflows trước cap", bold=True, bg=C["lgrn"])
fml(ws, r, 5, f"=SUM(E{inflow_item_rows[0]}:E{inflow_item_rows[-1]})",
    bg=C["lgrn"], col=C["grn"], bold=True)
mg(ws, r, 6, 7, "", bg=C["lgrn"])
ws.row_dimensions[r].height = 20; r += 1

r_cap_75 = r
mg(ws, r, 1, 4, "75% CAP = 75% × Gross Outflows  [công thức]", bold=True, bg=C["lgold"], col=C["gold"])
fml(ws, r, 5, f"=E{r_gross_outflow}*0.75", bold=True, bg=C["lgold"], col=C["gold"])
mg(ws, r, 6, 7, "Basel III: inflows cannot exceed 75% of gross outflows", it=True, col=C["gold"])
ws.row_dimensions[r].height = 20; r += 1

r_inflow_capped = r
mg(ws, r, 1, 4, "TỔNG STRESS INFLOWS (sau cap 75%)  [công thức]", bold=True, col="FFFFFF", sz=12, bg=C["grn"])
fml(ws, r, 5, f"=MIN(E{r_inflow_before_cap},E{r_cap_75})",
    bold=True, col="FFFFFF", bg=C["grn"])
mg(ws, r, 6, 7,
   f"=IF(E{r_inflow_before_cap}>E{r_cap_75},\"Cap da ap dung\",\"Duoi cap — full inflow\")",
   bold=True, col="FFFFFF", bg=C["grn"])
ws.row_dimensions[r].height = 26; r += 2

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4 — LCR CALCULATION  (mọi thứ là công thức, tham chiếu các row trên)
# ─────────────────────────────────────────────────────────────────────────────
r = sec(ws, r, 1, 10, "SECTION 4 — LCR CALCULATION & RATIO  [tat ca la cong thuc]")

def lcr_row(ws, r, label, formula, fmt, bg, col="FFFFFF", sz=11):
    mg(ws, r, 1, 4, label, bold=True, col=col, sz=sz, bg=bg)
    fml(ws, r, 5, formula, bold=True, col=col, bg=bg, fmt=fmt)
    mg(ws, r, 6, 7, "", bg=bg)
    ws.row_dimensions[r].height = 28
    return r + 1

r = lcr_row(ws, r, "HQLA Adjusted (Section 1)",
            f"=E{r_hqla_total}", "#,##0", C["teal"])

r_gross_ref = r
r = lcr_row(ws, r, "Gross Cash Outflows (Section 2)",
            f"=E{r_gross_outflow}", "#,##0", C["red"])

r_inflow_ref = r
r = lcr_row(ws, r, "Stress Inflows (Section 3, sau cap 75%)",
            f"=E{r_inflow_capped}", "#,##0", C["grn"])

r_nco = r
r = lcr_row(ws, r, "Net Cash Outflows (NCO) = Outflows − Inflows",
            f"=E{r_gross_outflow}-E{r_inflow_capped}", "#,##0", "37474F")

r_lcr_ratio = r
r = lcr_row(ws, r, "LCR = HQLA / NCO",
            f"=IFERROR(E{r_hqla_total}/E{r_nco},\"ERR\")", "0.00%", "1B5E20", sz=12)

r_lcr_pct = r
r = lcr_row(ws, r, "LCR (%)",
            f"=IFERROR(E{r_hqla_total}/E{r_nco}*100,0)", '0.00"%"', "1B5E20", sz=13)

r_surplus = r
r = lcr_row(ws, r, "HQLA Surplus / (Shortfall)",
            f"=E{r_hqla_total}-E{r_nco}", "#,##0;[Red]-#,##0", C["teal"])

r_headroom = r
r = lcr_row(ws, r, "Headroom above 100% minimum",
            f"=IFERROR(E{r_lcr_pct}-100,0)", '0.00" pp"', C["mb"])

# Status (IF formula)
r_status = r
mg(ws, r, 1, 4, "STATUS", bold=True, col="FFFFFF", sz=12, bg=C["dk"])
cl = ws.cell(row=r, column=5,
             value=f'=IF(E{r_lcr_pct}>=120,"STRONG -- buffer tot",'
                   f'IF(E{r_lcr_pct}>=100,"OK -- tuan thu",'
                   f'IF(E{r_lcr_pct}>=85,"WATCH -- duoi minimum","BREACH -- hanh dong ngay")))')
cl.font = _ft(bold=True, col="FFFFFF", sz=12)
cl.alignment = _al(h="center")
cl.border = _bd()
cl.fill = _f(C["teal"])
mg(ws, r, 6, 7, "", bg=C["dk"])
ws.row_dimensions[r].height = 28; r += 2

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5 — WATERFALL TABLE  (step-by-step HQLA vs Outflow stacking)
# ─────────────────────────────────────────────────────────────────────────────
r = sec(ws, r, 1, 10, "SECTION 5 — WATERFALL: HQLA CONSUMPTION vs OUTFLOW STACK")
r = hdrs(ws, r, [(1,"Lớp / Thành phần"),(2,"Giá trị\n(tỷ)"),(3,"Cum. HQLA\n(tỷ) [f]"),
                 (4,"Cum. Outflow\n(tỷ) [f]"),(5,"Gap = HQLA−Out\n(tỷ) [f]"),
                 (6,"Status [f]"),(7,"Ghi chú")])

# Waterfall rows: (label, value_formula, is_hqla, note)
WF = [
    ("HQLA Level 1",            f"=D{r_l1_total}",    True,  "Tien mat + TPCP + SBV"),
    ("HQLA Level 2A (cap)",     f"=E{r_l2a_total}",   True,  "Sau haircut 15% + cap 40%"),
    ("HQLA Level 2B (cap)",     f"=E{r_l2b_total}",   True,  "Sau haircut 25% + cap 15%"),
    ("Outflow: LNH unsecured",  f"=E{r_secured_total}",False,"100% runoff"),
    ("Outflow: Wholesale",      f"=E{r_wholesale_total}",False,"25–100% runoff"),
    ("Outflow: Retail",         f"=E{r_retail_total}",  False,"3–10% runoff"),
    ("Outflow: OBS",            f"=E{r_obs_total}",     False,"5–40% runoff"),
    ("(−) Inflows deducted",    f"=-E{r_inflow_capped}",False,"Cap 75% applied"),
]

wf_rows = []
prev_cum_hqla_col  = None
prev_cum_out_col   = None
cum_hqla_start = None
cum_out_start  = None

for i, (label, val_f, is_hqla, note) in enumerate(WF):
    bg = alt(r)
    wc(ws, r, 1, f"  {label}", sz=10, bg=bg)

    if is_hqla:
        fml(ws, r, 2, val_f, bg="E8F5E9", col="1B5E20", bold=True)
    else:
        fml(ws, r, 2, val_f, bg=C["lred"], col=C["red"], bold=True)

    # Cumulative HQLA (col C): adds only HQLA rows
    if i == 0:
        fml(ws, r, 3, f"=B{r}" if is_hqla else "=0", bg=C["vl"])
        cum_hqla_start = r
    else:
        prev_c = wf_rows[-1]
        if is_hqla:
            fml(ws, r, 3, f"=C{prev_c}+B{r}", bg=C["vl"])
        else:
            fml(ws, r, 3, f"=C{prev_c}", bg=C["vl"])

    # Cumulative Outflow (col D): adds only outflow rows (negative sign in val_f for inflows)
    if i == 0:
        fml(ws, r, 4, "=0" if is_hqla else f"=ABS(B{r})", bg=C["vl"])
    else:
        prev_c = wf_rows[-1]
        if is_hqla:
            fml(ws, r, 4, f"=D{prev_c}", bg=C["vl"])
        else:
            fml(ws, r, 4, f"=D{prev_c}+ABS(B{r})", bg=C["vl"])

    # Gap = cumHQLA - cumOutflow (col E)
    fml(ws, r, 5, f"=C{r}-D{r}", bg=C["vl"], bold=True, fmt="#,##0;[Red]-#,##0")

    # Status (col F): IF formula
    cl = ws.cell(row=r, column=6,
                 value=f'=IF(E{r}>0,"COVERED","SHORTFALL")')
    cl.font = _ft(bold=True, sz=9)
    cl.alignment = _al(h="center")
    cl.border = _bd()
    cl.fill = _f(bg or C["gy"])

    mg(ws, r, 7, 7, note, it=True, col="666666", sz=9, bg=bg)
    wf_rows.append(r)
    ws.row_dimensions[r].height = 18; r += 1

# Final waterfall summary
mg(ws, r, 1, 4, "NET: HQLA Surplus / (Shortfall) [cong thuc]",
   bold=True, col="FFFFFF", sz=11, bg=C["teal"])
fml(ws, r, 5, f"=E{r_hqla_total}-E{r_nco}",
    bold=True, col="FFFFFF", bg=C["teal"], fmt="#,##0;[Red]-#,##0")
mg(ws, r, 6, 7, f"=IFERROR(\"LCR = \"&TEXT(E{r_lcr_pct},\"0.0\")&\"%\",\"\")",
   bold=True, col="FFFFFF", bg=C["teal"])
ws.row_dimensions[r].height = 26; r += 2

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 6 — SCENARIO SENSITIVITY  (mọi thứ là công thức)
# ─────────────────────────────────────────────────────────────────────────────
r = sec(ws, r, 1, 10, "SECTION 6 — SCENARIO SENSITIVITY  [tat ca la cong thuc]")
r = hdrs(ws, r, [(1,"Kịch bản"),(2,"Outflow\nmult [INPUT]"),(3,"Add OBS\n(tỷ) [INPUT]"),
                 (4,"Gross Out\nstressed [f]"),(5,"HQLA\nmult [INPUT]"),
                 (6,"NCO\nstressed [f]"),(7,"HQLA\nstressed [f]"),
                 (8,"LCR\n% [f]"),(9,"Headroom\n[f]"),(10,"Status [f]")])

SCENARIOS = [
    ("Baseline",  1.00, 0,     1.00, "70AD47"),
    ("Tight",     1.15, 200,   1.00, "FFC000"),
    ("Stressed",  1.35, 500,   0.95, "ED7D31"),
    ("Severe",    1.60, 1_000, 0.80, "FF4B4B"),
]
scen_rows = []
for scen, out_mult, obs_add, hqla_mult, color in SCENARIOS:
    wc(ws, r, 1, scen, bold=True, col="FFFFFF", bg=color, h="center")
    inp(ws, r, 2, out_mult, fmt="0.00")
    inp(ws, r, 3, obs_add)

    # D = Gross outflows stressed = base_gross × multiplier + additional OBS
    fml(ws, r, 4, f"=E{r_gross_outflow}*B{r}+C{r}", bg=C["lred"], col=C["red"], bold=True)

    inp(ws, r, 5, hqla_mult, fmt="0.00")

    # F = NCO stressed = D - MIN(inflow_before_cap × 80%, D × 75%)
    # (inflows also stressed: reduce to 80% of base, then re-apply 75% cap)
    fml(ws, r, 6,
        f"=D{r}-MIN(E{r_inflow_before_cap}*0.8, D{r}*0.75)",
        bg="37474F", col="FFFFFF", bold=True)

    # G = HQLA stressed = base HQLA × HQLA multiplier (fire-sale / haircut worsening)
    fml(ws, r, 7, f"=E{r_hqla_total}*E{r}", bg=C["teal"], col="FFFFFF", bold=True)

    # H = LCR stressed %
    fml(ws, r, 8, f"=IFERROR(G{r}/F{r}*100,0)",
        fmt='0.0"%"', bold=True, col="FFFFFF", bg=color)

    # I = Headroom vs 100%
    fml(ws, r, 9, f"=H{r}-100",
        fmt='0.0" pp"', bold=True,
        col="1B5E20" if out_mult == 1.0 else C["red"])

    # J = Status IF formula
    cl = ws.cell(row=r, column=10,
                 value=f'=IF(H{r}>=120,"STRONG",IF(H{r}>=100,"OK",IF(H{r}>=85,"WATCH","BREACH")))')
    cl.font = _ft(bold=True, col="FFFFFF", sz=10)
    cl.alignment = _al(h="center"); cl.border = _bd(); cl.fill = _f(color)

    scen_rows.append(r)
    ws.row_dimensions[r].height = 22; r += 1

# Key insight (formula-driven text)
r += 1
mg(ws, r, 1, 10,
   f"=IFERROR(\"HQLA Baseline: \"&TEXT(E{r_hqla_total},\"#,##0\")&\" ty"
   f"  |  NCO Baseline: \"&TEXT(E{r_nco},\"#,##0\")&\" ty"
   f"  |  LCR Baseline: \"&TEXT(E{r_lcr_pct},\"0.0\")&\"%"
   f"  |  Surplus: \"&TEXT(E{r_surplus},\"#,##0\")&\" ty\",\"\")",
   bold=True, col="004D40", sz=10, bg=C["lteal"], h="center")
ws.row_dimensions[r].height = 22; r += 2

# ── Chart data + chart ────────────────────────────────────────────────────────
chart_data_r = r
for i, scen_r in enumerate(scen_rows):
    # Pull scenario name and LCR% via formula
    ws.cell(row=chart_data_r + i, column=1).value = f"=A{scen_r}"
    ws.cell(row=chart_data_r + i, column=2).value = f"=H{scen_r}"
    ws.cell(row=chart_data_r + i, column=3).value = 100  # minimum line

chart = BarChart()
chart.type   = "col"
chart.title  = "LCR (%) by Scenario vs Minimum 100%"
chart.y_axis.title = "LCR (%)"
chart.x_axis.title = "Scenario"
chart.style  = 10
chart.width  = 20; chart.height = 13
chart.y_axis.scaling.min = 0

data_lcr = Reference(ws, min_col=2, min_row=chart_data_r, max_row=chart_data_r + 3)
data_min = Reference(ws, min_col=3, min_row=chart_data_r, max_row=chart_data_r + 3)
cats     = Reference(ws, min_col=1, min_row=chart_data_r, max_row=chart_data_r + 3)
chart.add_data(data_lcr)
chart.add_data(data_min)
chart.set_categories(cats)
chart.series[0].title = SeriesLabel(v="LCR %")
chart.series[1].title = SeriesLabel(v="Minimum 100%")
ws.add_chart(chart, f"E{chart_data_r}")

# ── Save ──────────────────────────────────────────────────────────────────────
wb.save(PATH_OUT)
print("OK Saved with formulas")
print(f"  Key rows: HQLA_total=E{r_hqla_total}  GrossOut=E{r_gross_outflow}  NCO=E{r_nco}  LCR=E{r_lcr_pct}")
print(f"  Sheets: {wb.sheetnames}")
