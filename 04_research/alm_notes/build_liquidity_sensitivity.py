"""
Liquidity Sensitivity NII — Excel Builder
6 sheets: BalanceSheet → BehavioralParams → CashflowLadder → ScenarioMatrix → NIICalc → Dashboard
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter, column_index_from_string
from openpyxl.chart import BarChart, Reference
from openpyxl.chart.series import SeriesLabel

# ─── Palette ─────────────────────────────────────────────────────────────────
C = dict(
    dark_blue="1F3864", mid_blue="2E75B6", light_blue="BDD7EE", very_light="DEEAF1",
    green="375623", light_green="E2EFDA", yellow="7F6000", light_yellow="FFFF99",
    input_bg="FFFACD", orange="833C00", red="C62828", light_red="FFCDD2",
    gray="F2F2F2", white="FFFFFF", purple="4A148C",
)

def _fill(hex_): return PatternFill("solid", fgColor=hex_)
def _font(bold=False, color="000000", size=10, italic=False):
    return Font(bold=bold, color=color, size=size, italic=italic, name="Calibri")
def _align(h="left", v="center", wrap=False):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)
def _border(style="thin", clr="BFBFBF"):
    s = Side(style=style, color=clr)
    return Border(left=s, right=s, top=s, bottom=s)

def cell(ws, r, c_idx, val=None, bold=False, color="000000", size=10, italic=False,
         bg=None, h="left", v="center", wrap=False, fmt=None, border=True):
    cl = ws.cell(row=r, column=c_idx, value=val)
    cl.font = _font(bold=bold, color=color, size=size, italic=italic)
    cl.alignment = _align(h=h, v=v, wrap=wrap)
    if border: cl.border = _border()
    if bg:     cl.fill = _fill(bg)
    if fmt:    cl.number_format = fmt
    return cl

def merge_cell(ws, r, c1, c2, val=None, bold=False, color="000000", size=10, italic=False,
               bg=None, h="left", v="center", wrap=False, fmt=None, border=True):
    ws.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
    cl = cell(ws, r, c1, val, bold=bold, color=color, size=size, italic=italic,
              bg=bg, h=h, v=v, wrap=wrap, fmt=fmt, border=border)
    return cl

def section_bar(ws, r, c1, c2, text, bg=C["dark_blue"], fg="FFFFFF", size=11):
    merge_cell(ws, r, c1, c2, text, bold=True, color=fg, size=size, bg=bg, h="left")
    ws.row_dimensions[r].height = 22

def col_header(ws, r, c_idx, text, bg=C["mid_blue"], fg="FFFFFF", size=10, h="center", wrap=True):
    cl = cell(ws, r, c_idx, text, bold=True, color=fg, size=size, bg=bg, h=h, v="center", wrap=wrap)
    return cl

def input_cell(ws, r, c_idx, val, fmt=None):
    cl = cell(ws, r, c_idx, val, bold=True, color=C["dark_blue"], size=10,
              bg=C["input_bg"], h="right")
    if fmt: cl.number_format = fmt
    return cl

def na_cell(ws, r, c_idx):
    cl = cell(ws, r, c_idx, "N/A", italic=True, color="9E9E9E", size=9, bg="E0E0E0", h="center")
    return cl

# ─── Workbook ─────────────────────────────────────────────────────────────────
wb = openpyxl.Workbook()
wb.remove(wb.active)

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 1 — Balance Sheet (Contractual)
# ══════════════════════════════════════════════════════════════════════════════
ws1 = wb.create_sheet("01_BalanceSheet")
ws1.sheet_view.showGridLines = False
ws1.freeze_panes = "A5"

# Title
merge_cell(ws1, 1, 1, 9, "BẢNG CÂN ĐỐI KẾ TOÁN — DỮ LIỆU CONTRACTUAL (INPUT)",
           bold=True, color="FFFFFF", size=14, bg=C["dark_blue"], h="center")
ws1.row_dimensions[1].height = 32
merge_cell(ws1, 2, 1, 9, "Đơn vị: tỷ VND  |  Ô màu vàng = INPUT có thể chỉnh  |  Dữ liệu mẫu minh họa",
           italic=True, color=C["yellow"], size=10, bg="FFFDE7", h="center")

# Column widths & headers
col_defs = [("A",34), ("B",14), ("C",13), ("D",15), ("E",15), ("F",14), ("G",14), ("H",20), ("I",12)]
for ltr, w in col_defs:
    ws1.column_dimensions[ltr].width = w

hdrs = ["Khoản mục","Số dư (tỷ)","Lãi suất (%)","Bucket contractual",
        "Loại lãi suất","Days to reprice","Bucket (days)","Ghi chú","Nhóm"]
for i, h in enumerate(hdrs, 1):
    col_header(ws1, 4, i, h)
ws1.row_dimensions[4].height = 32

# Balance sheet rows: (name, amount, rate%, bucket_str, rate_type, days_reprice, note, group)
BS_DATA = [
    ("TỔNG TÀI SẢN", None, None, None, None, None, None, "HEADER"),
    ("I. TIỀN & CÁC KHOẢN TƯƠNG ĐƯƠNG TIỀN", None, None, None, None, None, None, "SECTION"),
    ("Tiền mặt & gửi NHNN", 2_000, 0.0, "O/N", "Không lãi", 1, "Dự trữ bắt buộc", "Asset"),
    ("II. TIỀN GỬI VÀ CHO VAY LIÊN NGÂN HÀNG (TT2)", None, None, None, None, None, None, "SECTION"),
    ("Gửi LNH — O/N", 500, 4.2, "O/N", "Thả nổi", 1, "", "Asset"),
    ("Gửi LNH — 1W", 800, 4.4, "1W", "Cố định", 7, "", "Asset"),
    ("Gửi LNH — 1M", 600, 4.6, "1M", "Cố định", 30, "", "Asset"),
    ("III. CHO VAY KHÁCH HÀNG", None, None, None, None, None, None, "SECTION"),
    ("Cho vay thả nổi — repricing 3M", 15_000, 8.5, "3M", "Thả nổi", 90, "Phần lớn vay DN", "Asset"),
    ("Cho vay thả nổi — repricing 6M", 10_000, 9.0, "6M", "Thả nổi", 180, "", "Asset"),
    ("Cho vay cố định — 1Y", 8_000, 9.5, "1Y", "Cố định", 365, "", "Asset"),
    ("Cho vay cố định — >1Y", 20_000, 10.0, ">1Y", "Cố định", 730, "BĐS, dự án", "Asset"),
    ("IV. CHỨNG KHOÁN ĐẦU TƯ (HQLA)", None, None, None, None, None, None, "SECTION"),
    ("TPCP đáo hạn 1Y", 3_000, 5.5, "1Y", "Cố định", 365, "HQLA Level 1", "Asset"),
    ("TPCP đáo hạn 3Y", 5_000, 6.0, ">1Y", "Cố định", 1095, "HQLA Level 1", "Asset"),
    ("TPCP đáo hạn 5Y", 4_000, 6.5, ">1Y", "Cố định", 1825, "HQLA Level 1", "Asset"),
    ("Trái phiếu DN — 2Y", 2_000, 7.5, ">1Y", "Cố định", 730, "HQLA Level 2B", "Asset"),
    ("V. TÀI SẢN KHÁC", None, None, None, None, None, None, "SECTION"),
    ("Tài sản cố định & khác", 1_500, 0.0, ">1Y", "Không lãi", 730, "", "Asset"),
    (None, None, None, None, None, None, None, "SPACER"),
    ("TỔNG NỢ PHẢI TRẢ & VỐN CHỦ SỞ HỮU", None, None, None, None, None, None, "HEADER"),
    ("I. TIỀN GỬI KHÁCH HÀNG (TT1)", None, None, None, None, None, None, "SECTION"),
    ("Tiền gửi KKH — CASA Retail", 6_000, 0.3, "O/N*", "Không kỳ hạn", 1, "Core stable ~65%", "Liability"),
    ("Tiền gửi KKH — CASA Corporate", 4_000, 0.5, "O/N*", "Không kỳ hạn", 1, "Core stable ~40%", "Liability"),
    ("Tiền tiết kiệm — 1M", 5_000, 4.5, "1M", "Cố định", 30, "EWR 5%", "Liability"),
    ("Tiền gửi kỳ hạn — 3M", 8_000, 5.0, "3M", "Cố định", 90, "EWR 8%", "Liability"),
    ("Tiền gửi kỳ hạn — 6M", 12_000, 5.5, "6M", "Cố định", 180, "EWR 6%", "Liability"),
    ("Tiền gửi kỳ hạn — 12M", 10_000, 6.0, "1Y", "Cố định", 365, "EWR 4%", "Liability"),
    ("Tiền gửi kỳ hạn — >12M", 5_000, 6.5, ">1Y", "Cố định", 730, "", "Liability"),
    ("II. VAY LIÊN NGÂN HÀNG (TT2)", None, None, None, None, None, None, "SECTION"),
    ("Vay LNH — O/N", 1_000, 4.3, "O/N", "Thả nổi", 1, "", "Liability"),
    ("Vay LNH — 1W", 2_000, 4.5, "1W", "Cố định", 7, "", "Liability"),
    ("Vay LNH — 1M", 1_500, 4.8, "1M", "Cố định", 30, "", "Liability"),
    ("III. PHÁT HÀNH GIẤY TỜ CÓ GIÁ", None, None, None, None, None, None, "SECTION"),
    ("Trái phiếu phát hành — 2Y", 3_000, 7.0, ">1Y", "Cố định", 730, "", "Liability"),
    ("Chứng chỉ tiền gửi — 3M", 2_000, 5.3, "3M", "Cố định", 90, "", "Liability"),
    ("IV. VỐN CHỦ SỞ HỮU", None, None, None, None, None, None, "SECTION"),
    ("Vốn điều lệ & các quỹ", 8_900, 0.0, ">1Y", "Không lãi", 730, "", "Equity"),
    (None, None, None, None, None, None, None, "SPACER"),
    ("CÁC CAM KẾT NGOẠI BẢNG (OFF-BALANCE SHEET)", None, None, None, None, None, None, "HEADER"),
    ("Hạn mức tín dụng chưa giải ngân — Retail", 1_500, 0.0, "O/N*", "N/A", 1, "Drawdown stressed: 15%", "Off-BS"),
    ("Hạn mức tín dụng chưa giải ngân — Corporate", 3_500, 0.0, "O/N*", "N/A", 1, "Drawdown stressed: 40%", "Off-BS"),
]

GRP_STYLE = {
    "Asset":    ("D9EAD3","2E7D32"), "Liability": ("FCE4EC","C62828"),
    "Equity":   ("E8EAF6","283593"), "Off-BS":    ("FFF3E0","E65100"),
}

r = 5
for row_data in BS_DATA:
    name, amount, rate, bucket, rate_type, days, note, grp = row_data

    if grp == "SPACER":
        ws1.row_dimensions[r].height = 6
        r += 1; continue

    if grp == "HEADER":
        merge_cell(ws1, r, 1, 9, name, bold=True, color="FFFFFF", size=11,
                   bg=C["dark_blue"], h="left")
        ws1.row_dimensions[r].height = 22; r += 1; continue

    if grp == "SECTION":
        merge_cell(ws1, r, 1, 9, name, bold=True, color=C["dark_blue"], size=10,
                   bg=C["light_blue"], h="left")
        ws1.row_dimensions[r].height = 18; r += 1; continue

    bg_row = C["very_light"] if r % 2 == 0 else None

    cell(ws1, r, 1, f"  {name}", size=10, bg=bg_row)
    input_cell(ws1, r, 2, amount).number_format = "#,##0"
    input_cell(ws1, r, 3, rate/100 if rate is not None else 0).number_format = "0.00%"
    cell(ws1, r, 4, bucket, h="center", bg=bg_row)
    cell(ws1, r, 5, rate_type, h="center", bg=bg_row)
    input_cell(ws1, r, 6, days).number_format = "0"
    # bucket_days formula
    cl = ws1.cell(row=r, column=7)
    cl.value = days
    cl.alignment = _align(h="center"); cl.border = _border()
    if bg_row: cl.fill = _fill(bg_row)
    cell(ws1, r, 8, note, italic=True, color="666666", size=9, bg=bg_row)

    # Group badge
    bg_g, fg_g = GRP_STYLE.get(grp, (None, "000000"))
    cell(ws1, r, 9, grp, bold=True, color=fg_g, size=9, bg=bg_g, h="center")

    ws1.row_dimensions[r].height = 18
    r += 1

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 2 — Behavioral Parameters
# ══════════════════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("02_BehavioralParams")
ws2.sheet_view.showGridLines = False

merge_cell(ws2, 1, 1, 6, "BEHAVIORAL PARAMETERS — THAM SỐ ĐIỀU CHỈNH HÀNH VI",
           bold=True, color="FFFFFF", size=14, bg=C["dark_blue"], h="center")
ws2.row_dimensions[1].height = 32
merge_cell(ws2, 2, 1, 6, "Ô màu vàng = INPUT có thể điều chỉnh theo đặc thù ngân hàng",
           italic=True, color=C["yellow"], size=10, bg="FFFDE7", h="center")

for ltr, w in [("A",36),("B",18),("C",18),("D",18),("E",18),("F",28)]:
    ws2.column_dimensions[ltr].width = w

def s2_section(r, title):
    section_bar(ws2, r, 1, 6, title)
    return r + 1

def s2_col_hdrs(r, cols):
    for c_idx, text in cols:
        col_header(ws2, r, c_idx, text)
    ws2.row_dimensions[r].height = 20
    return r + 1

def s2_param_row(r, label, vals, fmt="0%", note=""):
    bg = C["very_light"] if r % 2 == 0 else None
    cell(ws2, r, 1, label, size=10, bg=bg)
    for c_idx, val in vals:
        input_cell(ws2, r, c_idx, val).number_format = fmt
    cell(ws2, r, 6, note, italic=True, color="666666", size=9, bg=bg)
    ws2.row_dimensions[r].height = 18
    return r + 1

r = 4
# ── NMD / CASA ──
r = s2_section(r, "1. NMD — TIỀN GỬI KHÔNG KỲ HẠN / CASA")
r = s2_col_hdrs(r, [(1,"Tham số"),(2,"CASA Retail"),(3,"CASA Corporate"),(4,"Savings NMD"),(6,"Ghi chú")])
NMD = [
    ("Core stable %",         [(2,.65),(3,.40),(4,.55)], "0%",  "% coi là long-term stable"),
    ("Volatile %",             [(2,.35),(3,.60),(4,.45)], "0%",  "Phần có thể rút ngay — overnight"),
    ("Deposit beta",           [(2,.35),(3,.85),(4,.50)], "0%",  "% lãi suất tiền gửi tăng khi lãi suất thị trường +100bps"),
    ("Runoff rate — bình thường (tháng)", [(2,.02),(3,.05),(4,.03)], "0%", "% rút ra mỗi tháng — thông thường"),
    ("Runoff rate — stressed (30 ngày)", [(2,.10),(3,.25),(4,.15)], "0%", "LCR outflow rate stressed"),
]
for label, vals, fmt, note in NMD:
    r = s2_param_row(r, label, vals, fmt, note)

# Replicating portfolio
r += 1
section_bar(ws2, r, 1, 6, "1b. REPLICATING PORTFOLIO — Phân bổ core stable theo tenor", bg=C["mid_blue"], size=10)
r += 1
r = s2_col_hdrs(r, [(1,"Tenor"),(2,"Weight %"),(6,"Ghi chú")])
REP_WEIGHTS = [("1 năm",0.20),("2 năm",0.25),("3 năm",0.30),("4 năm",0.15),("5 năm",0.10)]
rep_start = r
for tenor, wt in REP_WEIGHTS:
    bg = C["very_light"] if r % 2 == 0 else None
    cell(ws2, r, 1, tenor, size=10, bg=bg)
    input_cell(ws2, r, 2, wt).number_format = "0%"
    ws2.row_dimensions[r].height = 18
    r += 1
bg = C["light_blue"]
cell(ws2, r, 1, "TỔNG", bold=True, bg=bg)
cl = ws2.cell(row=r, column=2, value=f"=SUM(B{rep_start}:B{r-1})")
cl.number_format = "0%"; cl.alignment = _align(h="right"); cl.border = _border()
cl.fill = _fill(bg); cl.font = _font(bold=True, size=10)
r += 1

# ── Term deposit ──
r += 1
r = s2_section(r, "2. TIỀN GỬI CÓ KỲ HẠN — Early Withdrawal & Rollover Rates")
r = s2_col_hdrs(r, [(1,"Tenor"),(2,"EWR bình thường"),(3,"EWR stressed"),(4,"Rollover rate"),(6,"Ghi chú")])
TERM = [
    ("1 tháng",  [(2,.05),(3,.20),(4,.65)], "EWR = Early Withdrawal Rate"),
    ("3 tháng",  [(2,.08),(3,.25),(4,.70)], ""),
    ("6 tháng",  [(2,.06),(3,.20),(4,.72)], ""),
    ("12 tháng", [(2,.04),(3,.15),(4,.75)], ""),
    (">12 tháng",[(2,.02),(3,.10),(4,.80)], ""),
]
for label, vals, note in TERM:
    r = s2_param_row(r, label, vals, "0%", note)

# ── Off-BS drawdown ──
r += 1
r = s2_section(r, "3. CAM KẾT NGOẠI BẢNG — Drawdown Rates")
r = s2_col_hdrs(r, [(1,"Loại cam kết"),(2,"Drawdown bình thường"),(3,"Drawdown stressed"),(4,"Drawdown severe"),(6,"Ghi chú")])
OBS = [
    ("Hạn mức OD — Retail",    [(2,.10),(3,.15),(4,.30)], "LCR: 5% committed revolving"),
    ("Hạn mức tín dụng — Corp",[(2,.25),(3,.40),(4,.75)], "LCR: 10% committed"),
    ("Trade finance",           [(2,.15),(3,.20),(4,.40)], ""),
    ("Bảo lãnh phát hành",     [(2,.05),(3,.10),(4,.25)], ""),
]
for label, vals, note in OBS:
    r = s2_param_row(r, label, vals, "0%", note)

# ── Deposit beta note ──
r += 1
merge_cell(ws2, r, 1, 6,
    "SVB 2023: wholesale deposits (VC/PE fund) có beta ~100% — khi lãi suất tăng, toàn bộ outflow gần như ngay lập tức. "
    "Đây là lý do behavioral assumption phải được calibrate theo profile khách hàng thực tế.",
    italic=True, color="C62828", size=9, bg="FFEBEE", h="left", wrap=True)
ws2.row_dimensions[r].height = 40

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 3 — Cashflow Ladder (Funding Gap)
# ══════════════════════════════════════════════════════════════════════════════
ws3 = wb.create_sheet("03_CashflowLadder")
ws3.sheet_view.showGridLines = False
ws3.freeze_panes = "B6"

merge_cell(ws3, 1, 1, 11, "CASHFLOW LADDER — FUNDING GAP (BEHAVIORAL ADJUSTED)",
           bold=True, color="FFFFFF", size=14, bg=C["dark_blue"], h="center")
ws3.row_dimensions[1].height = 32
merge_cell(ws3, 2, 1, 11,
    "[C] = Contractual (trước điều chỉnh)  |  [B] = Behavioral (sau điều chỉnh)  |  "
    "Gap âm = cần trám nguồn  |  Gap dương = thặng dư có thể deploy",
    italic=True, color="404040", size=10, bg="F5F5F5", h="center")

ws3.column_dimensions["A"].width = 40
BUCKETS = ["O/N","1W","1M","3M","6M","1Y",">1Y","TỔNG"]
BUCKET_DAYS = [1, 7, 30, 90, 180, 365, 730, None]
for i, (bkt, col_ltr) in enumerate(zip(BUCKETS, ["B","C","D","E","F","G","H","I"])):
    ws3.column_dimensions[col_ltr].width = 13

# Row 4: bucket headers merged over 2 rows
merge_cell(ws3, 4, 1, 1, "Khoản mục", bold=True, color="FFFFFF", size=10,
           bg=C["dark_blue"], h="center", v="center")
ws3.merge_cells(start_row=4, start_column=1, end_row=5, end_column=1)

for i, bkt in enumerate(BUCKETS):
    col_header(ws3, 4, i+2, bkt, h="center")
ws3.row_dimensions[4].height = 22

# Row 5: days sub-header
for i, d in enumerate(BUCKET_DAYS):
    val = f"({d}d)" if d else ""
    cell(ws3, 5, i+2, val, italic=True, color="FFFFFF", size=8, bg=C["mid_blue"], h="center")
ws3.row_dimensions[5].height = 14

# Cashflow data
# Columns B..H = O/N, 1W, 1M, 3M, 6M, 1Y, >1Y  (7 buckets, cols 2..8)
# Col I = TỔNG (sum formula)
# Each row: (label, [v_on, v_1w, v_1m, v_3m, v_6m, v_1y, v_g1y], style)
# style: CONTRACT | BEHAVIORAL | TOTAL_IN | TOTAL_OUT | GAP | CUM_GAP | NEG_GAP | SECTION | NOTE | SPACER
CF_DATA = [
    ("INFLOWS — TÀI SẢN ĐÁO HẠN / THU LÃI", None, "SECTION"),
    ("[C] Gửi LNH & tiền tương đương",  [2500,800,600,0,0,0,0], "CONTRACT"),
    ("[C] Cho vay đến hạn repricing",   [0,0,0,15000,10000,8000,20000], "CONTRACT"),
    ("[C] Chứng khoán đáo hạn",         [0,0,0,0,0,3000,11000], "CONTRACT"),
    ("[C] Thu lãi dự kiến",             [200,250,800,1800,2000,2500,3000], "CONTRACT"),
    ("  [B] Điều chỉnh behavioral:", None, "NOTE"),
    ("[B] CASA core stable kéo dài",    [0,0,0,0,0,2100,4900], "BEHAVIORAL"),
    ("[B] Drawdown hạn mức (outflow âm)",[-225,-350,-350,0,0,0,0], "BEHAVIORAL"),
    ("TỔNG INFLOWS [Behavioral]",       [2475,700,1050,16800,12000,15600,38900], "TOTAL_IN"),
    (None, None, "SPACER"),
    ("OUTFLOWS — NỢ ĐÁO HẠN / TRẢ LÃI", None, "SECTION"),
    ("[C] Tiền gửi CASA — contractual O/N",[10000,0,0,0,0,0,0], "CONTRACT"),
    ("[C] Tiền gửi có kỳ hạn đáo hạn", [0,0,5000,8000,12000,10000,5000], "CONTRACT"),
    ("[C] Vay LNH đáo hạn",            [1000,2000,1500,0,0,0,0], "CONTRACT"),
    ("[C] Trả lãi dự kiến",            [80,120,450,800,1200,1500,1000], "CONTRACT"),
    ("  [B] Điều chỉnh behavioral:", None, "NOTE"),
    ("[B] Trừ CASA core stable (kéo dài)",[-6500,0,0,0,0,0,0], "BEHAVIORAL"),
    ("[B] Trừ rollover tiền gửi (70%)", [0,0,-3500,-5600,-8400,-7000,-3500], "BEHAVIORAL"),
    ("[B] Cộng EWR (rút trước hạn)",   [0,0,400,600,720,400,100], "BEHAVIORAL"),
    ("TỔNG OUTFLOWS [Behavioral]",      [4580,2120,3850,3800,5520,4900,2600], "TOTAL_OUT"),
    (None, None, "SPACER"),
    ("NET FUNDING GAP & CUMULATIVE", None, "SECTION"),
    ("NET GAP mỗi bucket = INFLOWS − OUTFLOWS",[-2105,-1420,-2800,13000,6480,10700,36300], "GAP"),
    ("CUMULATIVE GAP",[-2105,-3525,-6325,6675,13155,23855,60155], "CUM_GAP"),
    (None, None, "SPACER"),
    ("PHẦN GAP ÂM (chỉ lấy số âm) — cần trám nguồn", None, "SECTION"),
    ("Funding gap cần trám",[-2105,-1420,-2800,0,0,0,0], "NEG_GAP"),
]

STYLE_MAP = {
    "CONTRACT":  (C["very_light"], "000000", False),
    "BEHAVIORAL":("FFF8E1",       "8B6914", False),
    "TOTAL_IN":  (C["light_blue"],C["dark_blue"], True),
    "TOTAL_OUT": ("FFCDD2",       C["red"],  True),
    "GAP":       (None,           "000000", True),   # colour per value
    "CUM_GAP":   ("F3E5F5",       "4A148C", True),
    "NEG_GAP":   (C["light_red"], C["red"], True),
}

r = 6
# Track row indices for key rows (for formula references from sheet 5)
gap_neg_row = None

for item in CF_DATA:
    label, vals, style = item

    if style == "SPACER":
        ws3.row_dimensions[r].height = 5; r += 1; continue

    if style == "SECTION":
        section_bar(ws3, r, 1, 9, label); r += 1; continue

    if style == "NOTE":
        merge_cell(ws3, r, 1, 9, label, italic=True, color="888888", size=9,
                   bg=C["gray"], h="left")
        ws3.row_dimensions[r].height = 14; r += 1; continue

    bg_clr, fg_clr, bold_text = STYLE_MAP.get(style, (None, "000000", False))

    cell(ws3, r, 1, label, bold=bold_text, color=fg_clr, size=10, bg=bg_clr)

    total = sum(v for v in vals if isinstance(v, (int, float)))
    all_vals = vals + [total]

    for col_i, v in enumerate(all_vals, 2):
        cl = ws3.cell(row=r, column=col_i, value=v)
        cl.number_format = "#,##0;[Red]\\-#,##0"
        cl.alignment = _align(h="right")
        cl.border = _border()

        if style == "GAP":
            if v < 0:
                cl.fill = _fill("FFCDD2")
                cl.font = _font(bold=True, color=C["red"], size=10)
            else:
                cl.fill = _fill("E8F5E9")
                cl.font = _font(bold=True, color="2E7D32", size=10)
        else:
            if bg_clr: cl.fill = _fill(bg_clr)
            cl.font = _font(bold=bold_text, color=fg_clr, size=10)

    if style == "NEG_GAP":
        gap_neg_row = r

    ws3.row_dimensions[r].height = 18
    r += 1

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 4 — Scenario Matrix (Liquidity Spreads)
# ══════════════════════════════════════════════════════════════════════════════
ws4 = wb.create_sheet("04_ScenarioMatrix")
ws4.sheet_view.showGridLines = False

merge_cell(ws4, 1, 1, 10, "LIQUIDITY SPREAD SCENARIO MATRIX — MA TRẬN KỊCH BẢN",
           bold=True, color="FFFFFF", size=14, bg=C["dark_blue"], h="center")
ws4.row_dimensions[1].height = 32
merge_cell(ws4, 2, 1, 10,
    "Ô màu vàng = INPUT  |  Công thức = tính tự động  |  Spread tính bằng basis points (bps)",
    italic=True, color=C["yellow"], size=10, bg="FFFDE7", h="center")

for ltr, w in [("A",24),("B",14),("C",15),("D",15),("E",15),("F",15),
               ("G",16),("H",16),("I",16),("J",22)]:
    ws4.column_dimensions[ltr].width = w

# Section 1: Base rates
r = 4
section_bar(ws4, r, 1, 10, "1. LÃI SUẤT CƠ SỞ THEO TENOR (Base Rate)"); r += 1
for c_idx, txt in [(1,"Tenor"),(2,"Base Rate %"),(3,"Nguồn tham chiếu")]:
    col_header(ws4, r, c_idx, txt)
for c_idx in range(4, 11):
    col_header(ws4, r, c_idx, "")
ws4.row_dimensions[r].height = 20; r += 1

BASE_RATES = [
    ("O/N",  0.042, "SBV O/N lending rate"),
    ("1W",   0.044, "VNIBOR 1W"),
    ("1M",   0.048, "VNIBOR 1M"),
    ("3M",   0.050, "VNIBOR 3M"),
    ("6M",   0.055, "VNIBOR 6M"),
    ("1Y",   0.060, "VNIBOR 12M"),
    (">1Y",  0.065, "Bond yield / IRS"),
]
base_rate_row = {}
for tenor, rate, src in BASE_RATES:
    bg = C["very_light"] if r % 2 == 0 else None
    cell(ws4, r, 1, tenor, bold=True, bg=bg)
    input_cell(ws4, r, 2, rate).number_format = "0.00%"
    merge_cell(ws4, r, 3, 10, src, italic=True, color="666666", size=9, bg=bg)
    base_rate_row[tenor] = r
    ws4.row_dimensions[r].height = 18; r += 1

# Section 2: Scenario definitions
r += 1
section_bar(ws4, r, 1, 10, "2. ĐỊNH NGHĨA 4 SCENARIOS"); r += 1
for c_idx, txt in [(1,"Scenario"),(2,"Outflow thêm"),(3,"Mô tả điều kiện")]:
    col_header(ws4, r, c_idx, txt)
for c_idx in range(4, 11):
    col_header(ws4, r, c_idx, "")
ws4.row_dimensions[r].height = 20; r += 1

SCEN_DEF = [
    ("Baseline", "0%",  "70AD47", "Thị trường bình thường, ngân hàng funding bình thường"),
    ("Tight",    "+5%", "FFC000", "Hệ thống căng nhẹ, SBV bơm OMO, spread tăng nhẹ"),
    ("Stressed", "+15%","ED7D31", "Bank bị nghi ngờ, counterparty cắt hạn mức, phải phát hành CD gấp"),
    ("Severe",   "+30%","FF4B4B", "Thị trường đóng băng, bán tài sản gấp / SBV ELA"),
]
scen_row = {}
for scen, outflow, color, desc in SCEN_DEF:
    cell(ws4, r, 1, scen, bold=True, color="FFFFFF", bg=color, h="center")
    cell(ws4, r, 2, outflow, bold=True, bg=color, color="FFFFFF", h="center")
    merge_cell(ws4, r, 3, 10, desc, italic=True, color="404040", size=10)
    scen_row[scen] = r
    ws4.row_dimensions[r].height = 18; r += 1

# Section 3: Spread matrix (input)
r += 1
section_bar(ws4, r, 1, 10, "3. LIQUIDITY SPREAD THEO TENOR & SCENARIO (bps)"); r += 1
for c_idx, txt in [(1,"Tenor"),(2,"Base Rate"),(3,"Baseline\n+bps"),(4,"Tight\n+bps"),
                   (5,"Stressed\n+bps"),(6,"Severe\n+bps"),
                   (7,"Replacement\nBaseline"),(8,"Replacement\nTight"),
                   (9,"Replacement\nStressed"),(10,"Ghi chú")]:
    cl = col_header(ws4, r, c_idx, txt, h="center", wrap=True)
ws4.row_dimensions[r].height = 32
spread_hdr_r = r; r += 1

# Spread data: (tenor, sp_base, sp_tight, sp_stressed, sp_severe, note)
SPREAD_DATA = [
    ("O/N",   0,   30,  100, 250, ""),
    ("1W",    5,   35,  110, 260, ""),
    ("1M",   10,   40,  120, None, "Severe: không vay được tenor này"),
    ("3M",   20,   50,  130, None, ""),
    ("6M",   35,   60,  150, None, "Stressed+: chỉ vay đến 1M"),
    ("1Y",   55,   80, None, None, "Tight+: khó vay tenor này"),
    (">1Y",  75,  None, None, None, ""),
]
spread_row = {}
SCEN_COLS = {"Baseline":3,"Tight":4,"Stressed":5,"Severe":6}
REPL_COLS  = {"Baseline":7,"Tight":8,"Stressed":9}

for tenor, sp_b, sp_t, sp_s, sp_sv, note in SPREAD_DATA:
    br = BASE_RATES[[x[0] for x in BASE_RATES].index(tenor)][1]
    bg = C["very_light"] if r % 2 == 0 else None

    cell(ws4, r, 1, tenor, bold=True, bg=bg)
    cl = ws4.cell(row=r, column=2, value=br)
    cl.number_format = "0.00%"; cl.alignment = _align(h="right"); cl.border = _border()
    if bg: cl.fill = _fill(bg)

    for scen, sp in [("Baseline",sp_b),("Tight",sp_t),("Stressed",sp_s),("Severe",sp_sv)]:
        col_i = SCEN_COLS[scen]
        if sp is not None:
            input_cell(ws4, r, col_i, sp).number_format = "0"
        else:
            na_cell(ws4, r, col_i)

    for scen, repl_col in [("Baseline",7),("Tight",8),("Stressed",9)]:
        sp_col = SCEN_COLS[scen]
        sp_val = {"Baseline":sp_b,"Tight":sp_t,"Stressed":sp_s}[scen]
        if sp_val is not None:
            repl = br + sp_val/10000
            cl = ws4.cell(row=r, column=repl_col, value=repl)
            cl.number_format = "0.000%"; cl.alignment = _align(h="right"); cl.border = _border()
            cl.fill = _fill(C["light_blue"]); cl.font = _font(bold=True, size=10)
        else:
            na_cell(ws4, r, repl_col)

    cell(ws4, r, 10, note, italic=True, color="666666", size=9, bg=bg)
    spread_row[tenor] = r
    ws4.row_dimensions[r].height = 18; r += 1

# Section 4: Urgency premium
r += 1
section_bar(ws4, r, 1, 10, "4. URGENCY PREMIUM — Phụ thuộc số ngày chuẩn bị"); r += 1
for c_idx, txt in [(1,"Thời gian chuẩn bị"),(2,"Urgency premium (bps)"),(3,"Ghi chú")]:
    col_header(ws4, r, c_idx, txt)
for c_idx in range(4, 11):
    col_header(ws4, r, c_idx, "")
ws4.row_dimensions[r].height = 20; r += 1

URGENCY = [
    ("> 2 tuần",    "0–10",    "Plan được — chọn kênh tốt nhất"),
    ("3–14 ngày",   "15–30",   "Phải nhanh hơn bình thường"),
    ("1–3 ngày",    "50–100",  "Phải chấp nhận giá thị trường"),
    ("Same day / O/N","100–250","Không còn lựa chọn — market maker biết"),
]
for prep, prem, note in URGENCY:
    bg = C["very_light"] if r % 2 == 0 else None
    cell(ws4, r, 1, prep, bg=bg)
    cell(ws4, r, 2, prem, bold=True, h="center", bg=C["input_bg"])
    merge_cell(ws4, r, 3, 10, note, italic=True, color="666666", size=9, bg=bg)
    ws4.row_dimensions[r].height = 18; r += 1

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 5 — NII / NIM Calculation
# ══════════════════════════════════════════════════════════════════════════════
ws5 = wb.create_sheet("05_NIICalc")
ws5.sheet_view.showGridLines = False
ws5.freeze_panes = "A7"

merge_cell(ws5, 1, 1, 13, "LIQUIDITY SENSITIVITY — TÍNH TOÁN ΔNII / ΔNIM",
           bold=True, color="FFFFFF", size=14, bg=C["dark_blue"], h="center")
ws5.row_dimensions[1].height = 32
merge_cell(ws5, 2, 1, 13,
    "ΔNII (tỷ) = Funding Gap × Incremental Spread (%) × (Days / 365)  |  "
    "ΔNIM (bps) = ΔNII_annual / Earning Assets × 10,000",
    italic=True, color="404040", size=10, bg="F5F5F5", h="center")

for ltr, w in [("A",28),("B",8),("C",14),("D",12),("E",12),("F",12),("G",12),
               ("H",12),("I",12),("J",12),("K",12),("L",12),("M",20)]:
    ws5.column_dimensions[ltr].width = w

# Key inputs
r = 4
section_bar(ws5, r, 1, 13, "THAM SỐ ĐẦU VÀO"); r += 1
KEY_INPUTS = [
    ("Earning Assets (tỷ VND)", 62_000, "#,##0",  "B5"),
    ("NII Baseline (tỷ/năm)",   3_200,  "#,##0",  "B6"),
    ("NIM Baseline (%)",        0.052,  "0.000%", "B7"),
    ("ΔNIM Limit (bps) — internal limit", -3.5, "0.00", "B8"),
]
for label, val, fmt, ref in KEY_INPUTS:
    cell(ws5, r, 1, label, bold=True, bg=C["very_light"])
    input_cell(ws5, r, 2, val).number_format = fmt
    ws5.row_dimensions[r].height = 18; r += 1

earning_assets_cell = "B5"  # row 5 sheet 5

# Column layout for calc table:
# A=Bucket B=Days C=Gap D=OrigRate E=sp_base F=ΔNII_base G=sp_tight H=ΔNII_tight
# I=sp_stressed J=ΔNII_stressed K=sp_severe L=ΔNII_severe M=note

r += 1
section_bar(ws5, r, 1, 13, "BẢNG TÍNH ΔNII THEO SCENARIO VÀ TIME BUCKET"); r += 1

# Scenario header band
SCEN_LAYOUT = [
    ("Baseline", "70AD47", 5, 6),
    ("Tight",    "FFC000", 7, 8),
    ("Stressed", "ED7D31", 9, 10),
    ("Severe",   "FF4B4B", 11, 12),
]
for c_idx, txt in [(1,"Bucket"),(2,"Days"),(3,"Funding Gap\n(tỷ — âm = cần trám)"),(4,"Original\nRate %")]:
    cl = col_header(ws5, r, c_idx, txt, h="center", wrap=True)
ws5.merge_cells(start_row=r, start_column=1, end_row=r+1, end_column=1)
ws5.merge_cells(start_row=r, start_column=2, end_row=r+1, end_column=2)
ws5.merge_cells(start_row=r, start_column=3, end_row=r+1, end_column=3)
ws5.merge_cells(start_row=r, start_column=4, end_row=r+1, end_column=4)

for scen, color, c1, c2 in SCEN_LAYOUT:
    ws5.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
    cl = ws5.cell(row=r, column=c1, value=scen)
    cl.fill = _fill(color); cl.font = _font(bold=True, color="FFFFFF", size=11)
    cl.alignment = _align(h="center"); cl.border = _border()

cell(ws5, r, 13, "Ghi chú", bold=True, color="FFFFFF", bg=C["dark_blue"], h="center")
ws5.merge_cells(start_row=r, start_column=13, end_row=r+1, end_column=13)
ws5.row_dimensions[r].height = 20; r += 1

for scen, color, c1, c2 in SCEN_LAYOUT:
    for col_i, sub in [(c1,"Sp (bps)"),(c2,"ΔNII (tỷ)")]:
        cl = ws5.cell(row=r, column=col_i, value=sub)
        cl.fill = _fill(color); cl.font = _font(bold=True, color="FFFFFF", size=9)
        cl.alignment = _align(h="center"); cl.border = _border()
ws5.row_dimensions[r].height = 16; r += 1

# Calc rows
# (bucket, days, gap, orig_rate, sp_base, sp_tight, sp_stressed, sp_severe, note)
CALC_ROWS = [
    ("O/N",  1,  -2105, 0.043, 0,   30,  100, 250, ""),
    ("1W",   7,  -1420, 0.045, 5,   35,  110, 260, ""),
    ("1M",  30,  -2800, 0.049, 10,  40,  120, None, "Severe: không huy động được"),
    ("3M",  90,      0, 0.050, 20,  50,  130, None, "Gap dương → không phát sinh chi phí trám"),
    ("6M", 180,      0, 0.055, 35,  60,  150, None, ""),
    ("1Y", 365,      0, 0.060, 55,  80, None, None, "Stressed+: chỉ vay đến 3M"),
    (">1Y",730,      0, 0.065, 75, None, None, None, "Tight+: không vay được tenor dài"),
]

nii_totals = {"Baseline":0.0,"Tight":0.0,"Stressed":0.0,"Severe":0.0}
scen_sp = {"Baseline":4,"Tight":6,"Stressed":8,"Severe":10}

data_start_r = r
for bkt, days, gap, orig, sp_b, sp_t, sp_s, sp_sv in [x[:8] for x in CALC_ROWS]:
    pass  # just to get last values
# real loop:
for row_data in CALC_ROWS:
    bkt, days, gap, orig, sp_b, sp_t, sp_s, sp_sv, note = row_data
    bg = C["very_light"] if r % 2 == 0 else None
    needs_funding = gap < 0

    cell(ws5, r, 1, bkt, bold=True, h="center", bg=bg)
    cell(ws5, r, 2, days, h="center", bg=bg)

    # Gap cell
    cl = ws5.cell(row=r, column=3, value=gap)
    cl.number_format = "#,##0;[Red]\\-#,##0"; cl.alignment = _align(h="right"); cl.border = _border()
    if needs_funding: cl.fill = _fill("FFCDD2"); cl.font = _font(bold=True, color=C["red"], size=10)
    else:             cl.fill = _fill("E8F5E9"); cl.font = _font(color="2E7D32", size=10)

    # Original rate
    cl = ws5.cell(row=r, column=4, value=orig)
    cl.number_format = "0.00%"; cl.alignment = _align(h="right"); cl.border = _border()
    if bg: cl.fill = _fill(bg)

    # 4 scenarios
    for scen, sp, c_sp, c_nii, color in [
        ("Baseline", sp_b,  5,  6, "70AD47"),
        ("Tight",    sp_t,  7,  8, "FFC000"),
        ("Stressed", sp_s,  9, 10, "ED7D31"),
        ("Severe",   sp_sv,11, 12, "FF4B4B"),
    ]:
        if sp is not None:
            input_cell(ws5, r, c_sp, sp).number_format = "0"
            if needs_funding:
                delta = gap * (sp/10000) * (days/365)
                cl = ws5.cell(row=r, column=c_nii, value=round(delta,3))
                cl.number_format = "#,##0.000;[Red]\\-#,##0.000"
                cl.alignment = _align(h="right"); cl.border = _border()
                cl.fill = _fill("FFCDD2"); cl.font = _font(bold=True, color=C["red"], size=10)
                nii_totals[scen] += delta
            else:
                cl = ws5.cell(row=r, column=c_nii, value=0)
                cl.number_format = "0.000"; cl.alignment = _align(h="right"); cl.border = _border()
                if bg: cl.fill = _fill(bg); cl.font = _font(color="999999", size=9)
        else:
            na_cell(ws5, r, c_sp)
            na_cell(ws5, r, c_nii)

    cell(ws5, r, 13, note, italic=True, color="666666", size=9, bg=bg)
    ws5.row_dimensions[r].height = 18
    r += 1

# Summary rows
def summary_row(ws, r, label, vals_dict, fmt, scen_nii_cols, bold=True, height=22):
    merge_cell(ws, r, 1, 4, label, bold=True, color="FFFFFF", size=10, bg=C["dark_blue"])
    for scen, color, c_sp, c_nii in [("Baseline","70AD47",5,6),("Tight","FFC000",7,8),
                                      ("Stressed","ED7D31",9,10),("Severe","FF4B4B",11,12)]:
        val = vals_dict.get(scen, 0)
        cl = ws.cell(row=r, column=c_nii, value=round(val,3) if isinstance(val,float) else val)
        cl.number_format = fmt; cl.alignment = _align(h="center"); cl.border = _border()
        cl.fill = _fill(color); cl.font = _font(bold=True, color="FFFFFF", size=11)
        cl = ws.cell(row=r, column=c_sp); cl.fill = _fill(color); cl.border = _border()
    merge_cell(ws, r, 13, 13, "", bg=C["dark_blue"])
    ws.row_dimensions[r].height = height

# ΔNII point-in-time
summary_row(ws5, r, "TỔNG ΔNII — point-in-time (tỷ VND)",
            nii_totals, '#,##0.00;[Red]\\-#,##0.00', None); r += 1

# Annualized (×12 for monthly avg, simplified)
nii_annual = {k: v*12 for k,v in nii_totals.items()}
summary_row(ws5, r, "ΔNII Annualized ≈ ×12 (tỷ VND/năm) — nếu gap tồn tại cả năm",
            nii_annual, '#,##0.00;[Red]\\-#,##0.00', None); r += 1

# ΔNIM bps
ea = 62_000
nim_bps = {k: v/ea*10000 for k,v in nii_annual.items()}
summary_row(ws5, r, "ΔNIM (bps) = ΔNII_annual / Earning Assets × 10,000",
            nim_bps, '0.00" bps"', None); r += 1

# NIM after shock
nim_base = 0.052
nim_after = {k: nim_base + v/10000 for k,v in nim_bps.items()}
summary_row(ws5, r, "NIM sau shock (%)",
            nim_after, '0.000%', None); r += 1

# Limit check
limit_bps = -3.5
r += 1
section_bar(ws5, r, 1, 13, "LIMIT CHECK — so sánh với internal limit"); r += 1
for c_idx, txt in [(1,"Scenario"),(2,""),(3,"ΔNIM (bps)"),(4,""),(5,"Limit (bps)"),(6,""),(7,"Status"),(8,"")]:
    col_header(ws5, r, c_idx, txt)
for c_idx in range(9,14):
    col_header(ws5, r, c_idx, "")
ws5.row_dimensions[r].height = 18; r += 1

STATUS_COLOR = {"OK":("E8F5E9","2E7D32"),"WATCH":("FFFDE7","8B6914"),"BREACH":("FFEBEE","C62828")}
for scen, color in [("Baseline","70AD47"),("Tight","FFC000"),("Stressed","ED7D31"),("Severe","FF4B4B")]:
    nim = nim_bps[scen]
    if nim >= -1:   status = "OK"
    elif nim >= -2: status = "WATCH"
    else:           status = "BREACH"
    bg_s, fg_s = STATUS_COLOR[status]

    cell(ws5, r, 1, scen, bold=True, color="FFFFFF", bg=color, h="center")
    ws5.merge_cells(start_row=r, start_column=2, end_row=r, end_column=2)
    cl = ws5.cell(row=r, column=3, value=round(nim,2))
    cl.number_format = '0.00" bps"'; cl.alignment = _align(h="center"); cl.border = _border()
    if nim < 0: cl.fill = _fill("FFCDD2"); cl.font = _font(bold=True, color=C["red"], size=10)
    ws5.merge_cells(start_row=r, start_column=4, end_row=r, end_column=4)
    cl = ws5.cell(row=r, column=5, value=limit_bps)
    cl.number_format = '0.00" bps"'; cl.alignment = _align(h="center"); cl.border = _border()
    cl.fill = _fill("FFEBEE"); cl.font = _font(bold=True, color=C["red"], size=10)
    ws5.merge_cells(start_row=r, start_column=6, end_row=r, end_column=6)
    cl = ws5.cell(row=r, column=7, value=status)
    cl.fill = _fill(bg_s); cl.font = _font(bold=True, color=fg_s, size=12)
    cl.alignment = _align(h="center"); cl.border = _border()
    ws5.merge_cells(start_row=r, start_column=8, end_row=r, end_column=13)
    ws5.row_dimensions[r].height = 20; r += 1

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 6 — Dashboard (ALCO)
# ══════════════════════════════════════════════════════════════════════════════
ws6 = wb.create_sheet("06_Dashboard")
ws6.sheet_view.showGridLines = False

for ltr, w in [("A",30),("B",14),("C",14),("D",14),("E",14),("F",14),
               ("G",14),("H",14),("I",14),("J",14),("K",14),("L",14)]:
    ws6.column_dimensions[ltr].width = w

merge_cell(ws6, 1, 1, 12, "LIQUIDITY SENSITIVITY DASHBOARD — BÁO CÁO ALCO",
           bold=True, color="FFFFFF", size=16, bg=C["dark_blue"], h="center")
ws6.row_dimensions[1].height = 42
merge_cell(ws6, 2, 1, 12, "Ngân hàng XYZ  |  Tháng 05/2026  |  Tài liệu nội bộ ALCO",
           italic=True, color="FFFFFF", size=11, bg=C["mid_blue"], h="center")
ws6.row_dimensions[2].height = 22

# ── KPI cards ──
r = 4
KPI = [
    ("Earning Assets","62,000 tỷ", C["dark_blue"]),
    ("NII Baseline",  "3,200 tỷ/năm", C["mid_blue"]),
    ("NIM Baseline",  "5.20%", C["mid_blue"]),
    ("HQLA Buffer",   "9,000 tỷ", C["green"]),
]
kpi_spans = [(1,3),(4,6),(7,9),(10,12)]
for (c1,c2),(label,val,color) in zip(kpi_spans,KPI):
    merge_cell(ws6, r,   c1, c2, label, bold=True, color="FFFFFF", size=10, bg=color, h="center")
    merge_cell(ws6, r+1, c1, c2, val,   bold=True, color="FFFFFF", size=16, bg=color, h="center", v="center")
    ws6.row_dimensions[r+1].height = 38
ws6.row_dimensions[r].height = 20; r += 3

# ── Funding Gap summary ──
section_bar(ws6, r, 1, 12, "FUNDING GAP — BEHAVIORAL ADJUSTED"); r += 1
for c_idx, txt in [(1,"Bucket"),(2,"Gap (tỷ)"),(4,"Cumulative"),(6,"Status"),(7,"Hành động khuyến nghị")]:
    col_header(ws6, r, c_idx, txt)
for c_idx in [3,5]: col_header(ws6, r, c_idx, "")
for c_idx in range(8,13): col_header(ws6, r, c_idx, "")
ws6.row_dimensions[r].height = 20; r += 1

GAP_SUMMARY = [
    ("O/N",  -2105, -2105,  "BREACH", "Trám bằng SBV OMO (cần đủ TPCP collateral)"),
    ("1W",   -1420, -3525,  "BREACH", "Rollover LNH 1W — monitor daily"),
    ("1M",   -2800, -6325,  "BREACH", "Phát hành CD / tăng lãi huy động TT1"),
    ("3M",  +13000,  +6675, "OK",     "Thặng dư — có thể deploy vào TPCP ngắn hạn"),
    ("6M",   +6480, +13155, "OK",     ""),
    ("1Y",  +10700, +23855, "OK",     ""),
    (">1Y", +36300, +60155, "OK",     ""),
]
STATUS_BG = {"OK":"E8F5E9","WATCH":"FFFDE7","BREACH":"FFCDD2"}
STATUS_FG = {"OK":"2E7D32","WATCH":"8B6914","BREACH":"C62828"}

for bkt, gap, cum, status, action in GAP_SUMMARY:
    cell(ws6, r, 1, bkt, bold=True, h="center")

    ws6.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
    cl = ws6.cell(row=r, column=2, value=gap)
    cl.number_format = "#,##0;[Red]\\-#,##0"; cl.alignment = _align(h="right"); cl.border = _border()
    cl.fill = _fill("FFCDD2" if gap<0 else "E8F5E9")
    cl.font = _font(bold=True, color=(C["red"] if gap<0 else "2E7D32"), size=10)

    ws6.merge_cells(start_row=r, start_column=4, end_row=r, end_column=5)
    cl = ws6.cell(row=r, column=4, value=cum)
    cl.number_format = "#,##0;[Red]\\-#,##0"; cl.alignment = _align(h="right"); cl.border = _border()
    cl.fill = _fill("FFCDD2" if cum<0 else "E8F5E9")
    cl.font = _font(bold=True, color=(C["red"] if cum<0 else "2E7D32"), size=10)

    cl = ws6.cell(row=r, column=6, value=status)
    cl.fill = _fill(STATUS_BG[status]); cl.font = _font(bold=True, color=STATUS_FG[status], size=10)
    cl.alignment = _align(h="center"); cl.border = _border()

    ws6.merge_cells(start_row=r, start_column=7, end_row=r, end_column=12)
    cell(ws6, r, 7, action, italic=True, color="404040", size=9)

    ws6.row_dimensions[r].height = 18; r += 1

# ── NII/NIM Sensitivity table ──
r += 1
section_bar(ws6, r, 1, 12, "NII / NIM SENSITIVITY — TÓM TẮT 4 SCENARIOS"); r += 1

# Headers
cell(ws6, r, 1, "Chỉ tiêu", bold=True, color="FFFFFF", bg=C["dark_blue"])
for scen, color, c1 in [("Baseline","70AD47",2),("Tight","FFC000",4),
                          ("Stressed","ED7D31",6),("Severe","FF4B4B",8)]:
    ws6.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c1+1)
    cl = ws6.cell(row=r, column=c1, value=scen)
    cl.fill = _fill(color); cl.font = _font(bold=True, color="FFFFFF", size=10)
    cl.alignment = _align(h="center"); cl.border = _border()
ws6.merge_cells(start_row=r, start_column=10, end_row=r, end_column=11)
cell(ws6, r, 10, "Limit (internal)", bold=True, color="FFFFFF", bg=C["red"], h="center")
cell(ws6, r, 12, "Status max", bold=True, color="FFFFFF", bg=C["dark_blue"], h="center")
ws6.row_dimensions[r].height = 20; r += 1

NIM_ROWS = [
    ("ΔNII — point-in-time (tỷ)",   {k:round(nii_totals[k],1) for k in nii_totals}, "#,##0.0", "—"),
    ("ΔNII — annualized (tỷ/năm)",  {k:round(nii_annual[k],1) for k in nii_annual}, "#,##0.0", "—"),
    ("ΔNIM — annualized (bps)",     {k:round(nim_bps[k],2)   for k in nim_bps},    '0.00" bps"', "-3.5 bps"),
    ("NIM sau shock (%)",           {k:round(nim_after[k],4) for k in nim_after},  "0.000%",    "—"),
]
for metric, vals, fmt, limit in NIM_ROWS:
    bg = C["very_light"] if r % 2 == 0 else None
    cell(ws6, r, 1, metric, bold=True, bg=bg)

    worst = min(vals.values())
    for scen, color, c1 in [("Baseline","70AD47",2),("Tight","FFC000",4),
                              ("Stressed","ED7D31",6),("Severe","FF4B4B",8)]:
        ws6.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c1+1)
        cl = ws6.cell(row=r, column=c1, value=vals[scen])
        cl.number_format = fmt; cl.alignment = _align(h="center"); cl.border = _border()
        cl.fill = _fill(color); cl.font = _font(bold=True, color="FFFFFF", size=10)

    ws6.merge_cells(start_row=r, start_column=10, end_row=r, end_column=11)
    cl = ws6.cell(row=r, column=10, value=limit)
    cl.fill = _fill("FFEBEE"); cl.font = _font(bold=True, color=C["red"], size=10)
    cl.alignment = _align(h="center"); cl.border = _border()

    # Overall status
    if metric.endswith("(bps)"):
        w_s = min(nim_bps.values())
        st = "OK" if w_s >= -1 else ("WATCH" if w_s >= -2 else "BREACH")
        cell(ws6, r, 12, st, bold=True, color=STATUS_FG[st], bg=STATUS_BG[st], h="center")
    else:
        cell(ws6, r, 12, "", bg=bg)
    ws6.row_dimensions[r].height = 22; r += 1

# ── Traffic light ──
r += 1
section_bar(ws6, r, 1, 12, "TRAFFIC LIGHT — ĐÁNH GIÁ TỔNG THỂ"); r += 1

TRAFFIC = [
    ("Baseline", "OK",     "70AD47", "Trong giới hạn — không cần hành động ngay"),
    ("Tight",    "OK",     "70AD47", "Trong giới hạn — theo dõi hàng tuần"),
    ("Stressed", "WATCH",  "FFC000", "Tiếp cận limit — chuẩn bị Contingency Funding Plan"),
    ("Severe",   "BREACH", "FF4B4B", "Vượt limit — kích hoạt CLMP (Contingency Liquidity Management Plan)"),
]
for scen, status, color, action in TRAFFIC:
    ws6.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
    cell(ws6, r, 1, scen, bold=True, color="FFFFFF", bg=color, h="center")
    ws6.merge_cells(start_row=r, start_column=3, end_row=r, end_column=4)
    cl = ws6.cell(row=r, column=3, value=status)
    cl.fill = _fill(color); cl.font = _font(bold=True, color="FFFFFF", size=13)
    cl.alignment = _align(h="center"); cl.border = _border()
    ws6.merge_cells(start_row=r, start_column=5, end_row=r, end_column=12)
    cell(ws6, r, 5, action, bold=(status=="BREACH"), size=10)
    ws6.row_dimensions[r].height = 22; r += 1

# ── Recommended actions ──
r += 1
section_bar(ws6, r, 1, 12, "KHUYẾN NGHỊ HÀNH ĐỘNG CHO ALCO"); r += 1
ACTIONS = [
    ("SHORT-TERM\n(0–30 ngày)",    C["red"],      "Bổ sung HQLA buffer +1,000 tỷ TPCP → mở rộng room SBV OMO cho O/N & 1W gap"),
    ("MEDIUM-TERM\n(1–3 tháng)",   C["orange"],   "Kéo dài tenor huy động TT1: target 30% danh mục >6M (hiện ~20%)"),
    ("STRUCTURAL\n(quarterly)",     C["mid_blue"], "Calibrate lại deposit beta theo profile KH thực tế. Review NMD core stable %"),
    ("MONITORING\n(ongoing)",       C["green"],    "Daily: LCR, intraday gap  |  Weekly: deposit runoff  |  Monthly: NSFR, structural funding ratio"),
]
for horizon, color, action in ACTIONS:
    ws6.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
    cell(ws6, r, 1, horizon, bold=True, color="FFFFFF", bg=color, h="center", v="center", wrap=True)
    ws6.merge_cells(start_row=r, start_column=3, end_row=r, end_column=12)
    cell(ws6, r, 3, action, size=10, wrap=True)
    ws6.row_dimensions[r].height = 34; r += 1

# ── Chart: ΔNIM by scenario ──
r += 2
chart = BarChart()
chart.type = "col"
chart.title = "ΔNIM (bps) — Liquidity Sensitivity by Scenario"
chart.y_axis.title = "bps"
chart.x_axis.title = "Scenario"
chart.style = 10
chart.width = 18; chart.height = 12

scen_labels = ["Baseline","Tight","Stressed","Severe"]
nim_vals_list = [round(nim_bps[s],2) for s in scen_labels]

# Write data for chart
chart_data_start = r
for i, (scen, val) in enumerate(zip(scen_labels, nim_vals_list)):
    ws6.cell(row=r+i, column=1, value=scen)
    ws6.cell(row=r+i, column=2, value=val)

data = Reference(ws6, min_col=2, min_row=r, max_row=r+3)
cats = Reference(ws6, min_col=1, min_row=r, max_row=r+3)
chart.add_data(data)
chart.set_categories(cats)
chart.series[0].title = SeriesLabel(v="ΔNIM (bps)")

# Color bars manually via graphical properties is limited in openpyxl; leave default
ws6.add_chart(chart, f"D{r}")

# ── Tab colors ──
TAB_COLORS = {
    "01_BalanceSheet":   "1F3864",
    "02_BehavioralParams":"375623",
    "03_CashflowLadder": "833C00",
    "04_ScenarioMatrix": "7F6000",
    "05_NIICalc":        "C62828",
    "06_Dashboard":      "4A148C",
}
for name, color in TAB_COLORS.items():
    if name in wb.sheetnames:
        wb[name].sheet_properties.tabColor = color

# ── Save ──────────────────────────────────────────────────────────────────────
OUT = r"D:\AI\Wiki-agentic\04_research\alm_notes\liquidity_sensitivity_NII.xlsx"
wb.save(OUT)
print(f"OK Saved: {OUT}")
print(f"  Sheets: {wb.sheetnames}")
