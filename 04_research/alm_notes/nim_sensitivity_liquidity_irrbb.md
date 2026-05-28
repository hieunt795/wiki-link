# NIM Sensitivity: Liquidity Risk & IRRBB — Giải thích thực hành

**Date:** 2026-05-26

---

## Q1

> "Phân tích độ nhạy cảm rủi ro thanh khoản, rủi ro lãi suất trên sổ ngân hàng để lượng hóa tác động đến NII, NIM"

Câu này đang nói về **hai việc gộp lại thành một output**:

**1. Rủi ro lãi suất sổ ngân hàng (IRRBB) → NII sensitivity**

Đây là phần chính. Khi lãi suất thị trường thay đổi, tài sản và nợ phải trả tái định giá ở các thời điểm khác nhau (repricing gap). Phân tích độ nhạy cảm ở đây là:

```
Scenario: lãi suất tăng/giảm Xbps
→ Tính lại NII dự kiến 12 tháng tới
→ ΔNII = NII_stressed - NII_baseline
→ ΔNIM = ΔNII / earning assets
```

Output là một con số như: "nếu lãi suất tăng 200bps, NII giảm 150 tỷ VND, NIM giảm 12bps."

**2. Rủi ro thanh khoản → NII qua cost of funds**

Liquidity risk không trực tiếp tạo ra một "sensitivity NII" độc lập. Nó ảnh hưởng NIM qua:

- **Liquidity spread** trong FTP: nếu ngân hàng thiếu funding dài hạn, phải huy động ngắn hạn giá cao hơn → cost of funds tăng → NIM thu hẹp
- **Structural funding gap**: tỷ lệ huy động ngắn hạn/dài hạn thay đổi → bình quân gia quyền lãi suất đầu vào thay đổi

Hai rủi ro giao nhau qua **FTP rate** — liquidity spread là một thành phần của FTP, nên khi thanh khoản thị trường thắt chặt, FTP curve dịch lên, cost toàn hệ thống tăng, NIM bị ăn vào.

**Tóm lại:** Câu đó yêu cầu chạy stress test / sensitivity analysis theo các scenario lãi suất (và funding) → output là NII thay đổi bao nhiêu VND và NIM thay đổi bao nhiêu bps. Rủi ro thanh khoản là context bổ sung (ảnh hưởng cost of funds phía liability); IRRBB là phần chính.

---

## Q2

> "Giải thích như sau đúng không? Chi phí thanh khoản trong các case như thế nào, tác động lên NIM. Ví dụ khách hàng rút tiền thì trám vào nguồn giá bao nhiêu, nóng hay gấp như thế nào sẽ tăng chi phí, tác động bảng cân đối như thế nào, NIM giảm bao nhiêu. Tương tự lãi suất cũng thế."

**Đúng**, và đây là cách hiểu rất thực tế. Cụ thể:

**Phần rủi ro thanh khoản:**

```
Khách hàng rút tiền
  → ngân hàng thiếu nguồn
  → phải "trám" = vay liên ngân hàng / phát hành CD / vay SBV
  → giá của nguồn trám đó = cost of funds mới
  → càng nóng / gấp → lãi suất thị trường liên ngân hàng bị đẩy lên
     (VD: overnight lên 5% thay vì 3%)
  → chi phí huy động toàn danh mục tăng
  → NIM bị ăn vào phía liability
```

"Nóng hay gấp" chính là **liquidity premium** — ngân hàng phải trả thêm để hút vốn gấp, không thể chờ kênh rẻ hơn.

**Tác động bảng cân đối:** Asset side giữ nguyên (vẫn cho vay), nhưng liability side đổi cơ cấu — tiền gửi KH thấp chi phí bị thay bằng vay liên ngân hàng/CD cao chi phí → weighted average cost of funds tăng → NIM giảm.

**IRRBB — "tương tự":**

```
Lãi suất thị trường tăng
  → asset tái định giá nhanh hay chậm so với liability?
  → nếu liability tái định giá nhanh hơn (VD: tiền gửi ngắn hạn nhiều)
     → cost of funds tăng trước khi thu nhập lãi tăng kịp
     → NIM giảm tạm thời
```

**So sánh hai rủi ro:**

| | Rủi ro thanh khoản | IRRBB |
|---|---|---|
| Trigger | Outflow / funding gap | Lãi suất thay đổi |
| Cơ chế | Phải thay nguồn, giá phụ thuộc urgency | Repricing gap asset vs liability |
| Output | NIM bị ăn phía cost of funds | NIM thay đổi theo chiều gap dương/âm |

**Key insight:** Nguồn trám giá bao nhiêu không phải ngẫu nhiên — nó được tính trước qua FTP curve (mỗi tenor có liquidity spread riêng), nên ngân hàng biết trước "nếu thiếu 1000 tỷ 3 tháng thì chi phí trám là X bps."

---

## Q3

> "Phân tích sâu hơn kỹ thuật xử lý câu trả lời cho câu hỏi này như nào?"

Có **3 lớp kỹ thuật** cần giải quyết theo thứ tự:

```
Lớp 1: Xác định funding gap (thiếu bao nhiêu, tenor nào)
Lớp 2: Định giá nguồn trám (X bps = bao nhiêu)
Lớp 3: Tính NIM impact (Y bps = bao nhiêu)
```

**Lớp 1 — Funding Gap: thiếu bao nhiêu, tenor nào?**

Input: Bảng cashflow theo time bucket (behavioral, không phải contractual)

```
Time bucket    Assets maturing    Liabilities maturing    Gap
Overnight      500 tỷ             800 tỷ                  -300 tỷ
1W–1M          1,200 tỷ           2,000 tỷ                -800 tỷ
1M–3M          3,000 tỷ           2,500 tỷ                +500 tỷ
```

Gap âm = liquidity shortfall — phần này phải "trám."

Cashflow phải là **behavioral cashflow**, không phải contractual:
- Tiền gửi KKH không tính là overnight hoàn toàn — phần core stable được kéo dài (2–5 năm theo replicating portfolio)
- Tiền gửi có kỳ hạn: có xác suất rút trước hạn → điều chỉnh xuống
- Hạn mức tín dụng chưa giải ngân (OD/credit line): có xác suất drawdown → tính vào outflow

Đây là lý do cần behavioral model trước khi tính gap.

**Lớp 2 — Định giá nguồn trám: X bps đến từ đâu?**

X không cố định — phụ thuộc 3 yếu tố:

*2a. Base rate theo tenor:*
```
Nguồn trám          Tenor       Base rate (VN ~)
SBV OMO             7–14 ngày   4.0–4.5%
VNIBOR              1M          4.5–5.0%
VNIBOR              3M          5.0–5.5%
CD phát hành        3M          5.5–6.0%
CD phát hành        6M          6.0–6.5%
```

*2b. Liquidity spread on top — phụ thuộc urgency:*

| Mức độ | Điều kiện | Spread thêm |
|--------|-----------|-------------|
| Normal | Chủ động plan trước, thị trường bình thường | +0–20bps |
| Stressed | Cần trong vài ngày, thị trường có áp lực | +50–100bps |
| Severe | Cần ngay hôm nay, thị trường freeze | +150–300bps |

*2c. Volume effect:* Vay 200 tỷ trên liên ngân hàng — market không để ý. Vay 5,000 tỷ trong 1 ngày — thị trường biết, spread bị đẩy lên.

FTP curve tổng hợp 2a + 2b thành 1 số: `FTP_rate(tenor) = Base_rate(tenor) + Liquidity_spread(tenor)`

**Lớp 3 — Tính NIM impact:**

```
Incremental interest cost = Funding_gap × (Replacement_rate - Original_rate) × (Tenor_days / 365)

NIM impact (annualized, bps) = (Funding_gap / Earning_assets) × Liquidity_spread_bps
```

Ví dụ số:
```
Funding gap:        1,000 tỷ, tenor 3 tháng
Original rate:      VNIBOR 3M = 5.0%
Replacement rate:   VNIBOR 3M + 80bps = 5.8%  (stressed scenario)
Incremental cost:   1,000 tỷ × 0.8% × 90/365 = ~1.97 tỷ
Earning assets:     100,000 tỷ
NIM impact (annual): 1,000/100,000 × 80bps = 0.8bps
```

**Tương tự với IRRBB:**

```
NII_impact = Σ_i [ Repricing_gap_i × Δrate × Days_i/365 ]
NIM_impact_bps = NII_impact / Earning_assets × 10,000
```

Ví dụ: Gap âm 5,000 tỷ ở bucket 3–6M, lãi suất tăng 100bps:
```
NII_impact = -5,000 tỷ × 1% × 0.375 = -18.75 tỷ
NIM_impact = -18.75 / 100,000 × 10,000 = -1.875bps
```

**Interaction effect — hai rủi ro cộng hưởng:**

Khi cả hai xảy ra đồng thời (vừa outflow vừa lãi suất tăng):
- Liquidity stressed → phải vay ngắn hạn thay vì dài hạn → liability duration ngắn lại → repricing gap thay đổi → IRRBB exposure tăng
- NIM impact KHÔNG additive (lớn hơn tổng từng phần) → phải chạy combined scenario

**Output format chuẩn:**

```
                        NII (tỷ)    NIM (bps)
Baseline                1,200       3.20%
Rate +200bps            1,050       -15bps
Liquidity stress 10%    1,120       -8bps
Combined shock          950         -25bps   ← không phải -15 + -8 = -23
```

Non-additivity (~2bps) = interaction effect từ funding mix thay đổi kéo theo repricing gap thay đổi.

---

## Q4

> "Nó có phải là scenario analysis không?"

Không hoàn toàn — đây là 3 thứ khác nhau hay bị gộp lại:

**Sensitivity analysis** — cái đang làm ở trên
> Thay đổi **1 biến**, giữ nguyên mọi thứ, đo output.
> "Rate tăng 100bps → NIM thay đổi bao nhiêu?"
> Không có narrative, chỉ có toán.

**Scenario analysis** — phức tạp hơn
> Định nghĩa **1 câu chuyện vĩ mô nhất quán**, từ đó suy ra nhiều biến thay đổi cùng lúc.
> "Kịch bản suy thoái: SBV tăng lãi 150bps + tín dụng chậm lại + tiền gửi rút 15% — tất cả đồng thời → NIM, NII, vốn thay đổi ntn?"
> Narrative-driven, các biến phải coherent với nhau.

**Stress testing** — extreme end
> Scenario cực đoan, thường là regulatory prescribed.
> "Ngân hàng sống sót được bao lâu nếu outflow 20%/ngày trong 30 ngày?" → LCR logic.
> Output không phải NIM mà là survival horizon / capital adequacy.

| | Sensitivity | Scenario | Stress |
|---|---|---|---|
| Biến thay đổi | 1 biến | Nhiều biến nhất quán | Biến cực đoan |
| Narrative | Không | Có | Có (tail risk) |
| Output | ΔNIM/ΔNII | P&L toàn diện | Survival/capital |
| Dùng cho | ALCO tuần | ALCO quý / chiến lược | Regulatory / ICAAP |

Cái đã phân tích ở trên là **sensitivity analysis**. Nó trở thành scenario analysis khi các biến không còn độc lập — VD: "Fed high-for-longer → SBV tăng lãi để giữ tỷ giá → đồng thời deposit flow ra → combined NIM impact là gì?"

---

## Q5

> "Ví dụ nếu đang huy động trên interbank nhưng không huy động được nữa thì phải huy động ở nguồn nào, ở TT1 hay nguồn khác, chi phí bao nhiêu các kịch bản?"

### Waterfall nguồn thay thế (theo thứ tự ưu tiên)

```
TT2 (interbank) đóng băng
          ↓
1. SBV OMO (repo trái phiếu CP với SBV)
          ↓ (nếu hết room collateral)
2. Repo TPCP với đối tác phi ngân hàng (bảo hiểm, quỹ)
          ↓ (nếu không đủ TPCP)
3. Phát hành CD / tăng lãi suất huy động TT1
          ↓ (nếu cần gấp hơn)
4. Bán tài sản thanh khoản (TPCP, tín phiếu SBV)
          ↓ (cực đoan)
5. SBV tái cấp vốn khẩn cấp / ELA
```

### Tốc độ mobilize vs chi phí

| Nguồn | Tốc độ | Chi phí bình thường | Khi TT2 đóng |
|-------|--------|---------------------|--------------|
| SBV OMO | Same day | OMO rate ~4.0–4.5% | Như cũ (SBV vẫn mở) |
| Repo TPCP phi ngân hàng | 1–2 ngày | VNIBOR + 20–30bps | VNIBOR + 50–100bps |
| Phát hành CD TT1 | 1–2 tuần | Thị trường + 0bps | Thị trường + 50–150bps |
| Tăng lãi suất huy động TT1 | 2–4 tuần | — | Toàn bộ danh mục bị repricing |
| Bán TPCP | 1 ngày | Par – haircut nhỏ | Par – haircut lớn hơn (fire sale) |
| SBV ELA / tái cấp vốn | Vài ngày | Phạt cao | Rất cao + stigma |

### 3 kịch bản và chi phí

**Kịch bản 1: TT2 tạm thời thắt (tight nhưng không frozen)**
> VD: căng thẳng thanh khoản hệ thống ngắn hạn, SBV vẫn bơm OMO
```
Nguồn chính: SBV OMO + repo phi ngân hàng
Chi phí trám: OMO rate + 20–50bps
Thời gian xử lý: same day – 2 ngày
NIM impact: nhỏ, ~1–3bps nếu gap không lớn
```

**Kịch bản 2: TT2 suy giảm nghiêm trọng (bank bị nghi ngờ)**
> VD: tin đồn hoặc sự kiện tín dụng → counterparty giảm hạn mức
```
Nguồn chính: SBV OMO (hết room nhanh) + CD phát hành gấp + tăng lãi TT1
Chi phí trám: thị trường + 100–200bps
Thời gian xử lý: 3–7 ngày (TT1 chậm)
NIM impact: đáng kể — cost of funds toàn danh mục bị kéo lên
Rủi ro thêm: TT1 cũng bắt đầu rút → gap tăng → vòng xoáy
```

**Kịch bản 3: TT2 đóng băng hoàn toàn (systemic hoặc bank-specific crisis)**
> VD: bank run, tin xấu lan rộng
```
Nguồn chính: SBV ELA + bán tài sản gấp
Chi phí trám: ELA rate (phạt) + fire sale haircut
NIM impact: không còn là mục tiêu chính — mục tiêu là survival
```

### Điểm kỹ thuật quan trọng nhất

**Constraint bị bỏ qua nhiều nhất: collateral**

SBV OMO rẻ và nhanh nhất — nhưng chỉ hoạt động nếu ngân hàng có **TPCP/tín phiếu SBV đủ để repo**. Ngân hàng giữ ít TPCP (đã cho vay hết) → room OMO nhỏ → bị đẩy ngay sang CD/TT1 với chi phí cao hơn. Đây là lý do LCR yêu cầu giữ **HQLA buffer** — không phải để "không dùng đến," mà chính là để có collateral trám khi TT2 đóng.

**Stigma effect:**
```
Ngân hàng vay SBV ELA
  → thị trường biết (hoặc đoán)
  → KH TT1 bắt đầu rút tiền
  → gap tăng thêm → phải vay thêm → vòng xoáy tự hủy
```

**Kết luận:**

Phụ thuộc vào 2 biến quyết định:
1. **Lý do TT2 đóng:** hệ thống (SBV vẫn bơm) hay bank-specific (counterparty cắt hạn mức với mình)
2. **Ngân hàng còn bao nhiêu TPCP làm collateral**

- Nếu hệ thống: SBV OMO vẫn mở → chi phí tăng nhẹ (+20–50bps), NIM ảnh hưởng nhỏ
- Nếu bank-specific: phải dùng CD/TT1 gấp (+100–200bps) → NIM bị ăn nghiêm trọng → nếu TT1 cũng rút theo thì đây không còn là bài toán NIM, mà là bài toán sống còn

---

---

## Q6 — Phân tích chi tiết Liquidity Sensitivity

> "Phân tích chi tiết vào liquidity sensitivity"

### 1. Liquidity sensitivity là gì — từ định nghĩa gốc

Nguồn ALM Optimization (p.209):
> "The bank begins to be exposed to liquidity risk when the liability expires and needs to be rolled over.
> Starting from that date, the **funding gap creates the NII sensitivity**."
> [RAW-BOOK A - Asset liability optimization.md p.209]

Liquidity sensitivity = **sự thay đổi của NII/NIM khi chi phí rollover funding thay đổi**.

Không phải lãi suất thị trường thay đổi (đó là IRRBB). Mà là: **khi ngân hàng phải gia hạn/thay thế một khoản nợ, họ phải trả bao nhiêu cho khoản nợ mới đó?**

```
ALM locked-in margin  = liquidity spread(asset) - liquidity spread(liability hiện tại)
ALM margin at risk    = phụ thuộc vào liquidity spread của liability khi rollover
                       → đây chính là liquidity sensitivity
[RAW-BOOK A - Asset liability optimization.md p.211]
```

---

### 2. Năm thành phần của Liquidity Risk tác động đến NIM

ALM Optimization phân loại 5 loại, chỉ 3 cái đầu tác động trực tiếp đến NIM:

```
① Funding risk (tác động NIM trực tiếp)
   → Cost of funding tăng do creditworthiness xấu đi hoặc market spread tăng
   → Idiosyncratic: chỉ ngân hàng đó bị ảnh hưởng
   → Cơ chế: counterparty giảm limit → phải vay gấp → premium cao hơn
   [RAW-BOOK A - Asset liability optimization.md p.987]

② Liquidity mismatch risk (tác động NIM qua cơ cấu funding)
   → Mismatch amount/maturity giữa inflows và outflows trong từng time bucket
   → Phần mismatch âm → phải rollover → gặp funding risk ở ①
   [RAW-BOOK A - Asset liability optimization.md p.989]

③ Liquidity contingency risk (tác động NIM trong stress)
   → Unexpected events: non-repayment of loans, drawdown credit lines, khó bán assets
   → Phát sinh funding need đột ngột → không có thời gian tìm nguồn rẻ
   [RAW-BOOK A - Asset liability optimization.md p.990]

④ Market liquidity risk (tác động NIM gián tiếp qua fire sale)
   → Không bán được asset để trám → phải vay thay thế
   → Hoặc bán được nhưng at a loss → P&L hit, không phải NIM hit trực tiếp

⑤ Operational liquidity risk
   → Không tác động NIM — đây là failure-to-pay do lỗi vận hành
```

---

### 3. Cơ chế truyền dẫn: Funding Gap → NIM

**Bước 1 — Xác định structural funding gap:**

```
Structural gap = Asset (tenor T) - Liability (tenor T)
                                    theo từng time bucket

Nếu gap âm tại bucket [3M–6M]:
  → Có 1,000 tỷ asset cần được fund đến 6M
  → Nhưng chỉ có 800 tỷ liability đến 6M
  → 200 tỷ phải được rollover hoặc tìm nguồn mới
```

**Bước 2 — Contractual vs Behavioral cashflow:**

Đây là điểm kỹ thuật quan trọng nhất. Cashflow không thể dùng contractual raw:

```
Contractual view:          Behavioral adjusted:
Tiền gửi KKH → overnight   Tiền gửi KKH → core stable ~2-5Y
                            (replicating portfolio)
Tiền gửi kỳ hạn → T ngày  Tiền gửi kỳ hạn → T - xác suất rút sớm
Hạn mức tín dụng → 0       Hạn mức tín dụng → drawdown probability × amount
```

Nếu dùng contractual, gap ở overnight bucket sẽ âm khổng lồ (toàn bộ CASA).
Nếu dùng behavioral, tiền gửi CASA có duration dài hơn → gap thực tế nhỏ hơn.

**Bước 3 — Định giá funding gap (liquidity spread):**

```
FTP rate(tenor) = Base rate(tenor) + Liquidity spread(tenor) + Credit spread + Optionality cost
                                     ↑
                         Đây là phần tạo ra liquidity sensitivity
[RAW-BOOK ftp_transmission_analysis.md.md]

Liquidity spread phụ thuộc:
  a. Tenor của nguồn thay thế (dài hơn → spread cao hơn)
  b. Urgency (normal +0–20bps, stressed +50–100bps, severe +150–300bps)
  c. Volume (vay càng nhiều trong 1 ngày → spread bị đẩy lên)
  d. Trạng thái thị trường (systemic vs idiosyncratic)
```

**Bước 4 — Tính NIM impact:**

```
Incremental funding cost = Funding_gap × Liquidity_spread × (Tenor_days/365)

NIM impact (bps, annualized) = (Funding_gap / Earning_assets) × Liquidity_spread_bps

Ví dụ:
  Funding gap = 2,000 tỷ, tenor 6M
  Liquidity spread = 80bps (stressed scenario)
  Earning assets = 100,000 tỷ

  Incremental cost = 2,000 × 0.8% × 180/365 = 7.89 tỷ
  NIM impact       = (2,000/100,000) × 80bps = 1.6bps (annualized)
```

---

### 4. Chiều của Liquidity Sensitivity

**Luôn âm** — không có kịch bản nào mà liquidity stress cải thiện NIM.

Nhưng mức độ phụ thuộc vào:

| Yếu tố | Ảnh hưởng |
|---|---|
| Size of funding gap | Gap lớn hơn → NIM impact lớn hơn |
| Tenor của gap | Gap ở bucket dài hơn → spread cao hơn |
| Nguyên nhân outflow | Systemic: SBV vẫn bơm → spread thấp; Idiosyncratic: counterparty cắt → spread cao |
| Collateral sẵn có | Nhiều TPCP → tiếp cận OMO giá rẻ; ít TPCP → phải dùng CD/TT1 giá cao |
| Thời điểm rollover | Cuối quý/cuối năm → thanh khoản hệ thống thắt → spread cao hơn bình thường |

---

### 5. Structural Liquidity vs Short-term Liquidity Sensitivity

Có hai lớp khác nhau:

```
SHORT-TERM liquidity sensitivity (daily/weekly/monthly):
  → Funding gap trong LCR horizon (30 ngày)
  → Quản lý bởi Treasury desk hàng ngày
  → Đo bằng: survival horizon, daily funding requirement
  → Impact NIM: nhỏ nếu gap được plan trước; lớn nếu bị surprise

STRUCTURAL liquidity sensitivity (medium-term, 1–5 năm):
  → Funding gap theo NSFR horizon
  → Tỷ lệ short-term vs long-term funding của toàn danh mục
  → Đo bằng: maturity mismatch report, structural funding ratio
  → Impact NIM: ổn định hơn nhưng thay đổi khi chu kỳ lãi suất thay đổi

"Medium long-term liquidity — principles of structural liquidity management"
[RAW-BOOK A - Asset liability optimization.md ToC p.82]
```

---

### 6. Behavioral Dimension — phần thường bị bỏ qua

**Vấn đề lớn nhất của liquidity sensitivity analysis là behavioral assumptions:**

```
NMDs (Non-Maturity Deposits = tiền gửi KKH và tiết kiệm không kỳ hạn):
  → Chiếm 30–60% total deposits ở ngân hàng bán lẻ VN
  → Contractual maturity: overnight
  → Behavioral maturity: 1–5 năm (phần core stable)
  → Nếu model sai → funding gap sai → liquidity sensitivity sai hoàn toàn

Replicating portfolio approach (Tata ALM §2.2, Fig 2.21–2.31):
  → Chia CASA thành: core stable (kéo dài theo rolling portfolio) + volatile (overnight)
  → Core stable được assign tenor theo lịch sử hành vi khách hàng
  → FTP rate cho core stable = weighted average của FTP theo tenor profile

Deposit beta (Tata ALM Fig 2.37):
  → Khi lãi suất thị trường tăng, lãi suất tiền gửi tăng bao nhiêu?
  → Retail deposits: beta ~30–50% (chậm phản ứng)
  → Wholesale deposits: beta ~80–100% (phản ứng gần như ngay lập tức)
  → Beta cao → khi lãi suất tăng, cost of funds tăng nhanh → NIM bị ăn nhiều hơn
```

SVB 2023 thất bại vì behavioral assumption sai: tiền gửi VC/PE fund có beta ~100% và không có core stable component — khi lãi suất tăng, toàn bộ outflow gần như ngay lập tức.

---

### 7. FTP như công cụ đo và phân bổ Liquidity Sensitivity

BCBS bcbs144 Principle 4 yêu cầu:
> "A bank should incorporate **liquidity costs, benefits and risks** in internal pricing
> for all significant business activities."
> [RAW-BOOK bcbs144 Principle 4]

Trong thực tế qua FTP:

```
Mỗi giao dịch được assign FTP rate = base rate + liquidity spread(tenor)

Liquidity spread theo tenor phản ánh:
  → Chi phí thực tế để funding asset/liability đó đến maturity
  → Được ALM tính toán dựa trên funding curve thực của ngân hàng

Ý nghĩa cho liquidity sensitivity:
  → Business Unit chỉ thấy (Customer rate - FTP rate) = customer margin
  → ALM absorb toàn bộ liquidity mismatch risk
  → Khi thị trường stress → ALM tăng liquidity spread trong FTP curve
  → BU bị charge cao hơn cho funding gap → tự động giảm mismatch

Feedback loop:
  LCR thấp → ALM tăng liquidity spread short end → BU giảm cho vay ngắn hạn
           → Liquidity sensitivity giảm dần về equilibrium
[RAW-BOOK ftp_transmission_analysis.md.md §2.1–2.2]
```

---

### 8. Framework đo Liquidity Sensitivity — Output chuẩn

```
Input:
  → Behavioral cashflow ladder (7 time buckets: O/N, 1W, 1M, 3M, 6M, 1Y, >1Y)
  → FTP liquidity spread curve (theo tenor + stress scenario)
  → HQLA buffer có sẵn (giới hạn trên của funding gap có thể tự xử lý)

Process:
  → Tính funding gap âm từng bucket (sau behavioral adjustment)
  → Assign replacement rate cho từng bucket (FTP spread × scenario)
  → Tính incremental cost = Σ [gap_i × spread_i × days_i/365]

Output:
  → NIM impact (bps) cho từng scenario

Scenario framework chuẩn:
┌─────────────────────────┬──────────────┬────────────────────────────┐
│ Scenario                │ Spread thêm  │ Giả định                   │
├─────────────────────────┼──────────────┼────────────────────────────┤
│ Baseline                │ +0bps        │ Thị trường bình thường      │
│ Liquidity tight         │ +30–50bps    │ Hệ thống căng, SBV bơm OMO  │
│ Idiosyncratic stressed  │ +80–150bps   │ Bank bị nghi ngờ, CD gấp    │
│ Severe / systemic       │ +200–300bps  │ Thị trường đóng băng        │
└─────────────────────────┴──────────────┴────────────────────────────┘
```

---

### 9. ILAAP vs ICAAP — Khung quản trị

```
IRRBB sensitivity → ICAAP (Internal Capital Adequacy Assessment Process)
                  → Limit: ΔEVE ≤ 15% Tier 1; ΔNII ≤ X% (internal)
                  → Regulated by: BCBS d368

Liquidity sensitivity → ILAAP (Internal Liquidity Adequacy Assessment Process)
                      → Limit: LCR ≥ 100%, NSFR ≥ 100%, survival horizon ≥ X days
                      → Regulated by: BCBS bcbs144 (17 Principles)
[RAW-BOOK A - Asset liability optimization.md p.306]
```

Đây là lý do hai loại sensitivity **báo cáo lên hai track riêng** — ALCO nhận cả hai nhưng chúng được quản lý theo framework khác nhau.

---

*Related wiki nodes:*

> "Trong câu hỏi gốc có đoạn 'độ nhạy thanh khoản' và 'độ nhạy rủi ro lãi suất trên sổ ngân hàng' — giải thích về hai khái niệm này"

Câu hỏi gốc đặt hai khái niệm cạnh nhau nhưng chúng là **hai chiều khác nhau của cùng một bảng cân đối**.

### Độ nhạy IRRBB (NII sensitivity)

**Bản chất:** Đo lường NII/NIM thay đổi bao nhiêu khi **lãi suất thị trường** thay đổi.

```
Lãi suất tăng/giảm Xbps
  → Asset và liability tái định giá ở các thời điểm khác nhau (repricing gap)
  → Repricing gap âm: liability repricing trước → cost of funds tăng trước
  → Repricing gap dương: asset repricing trước → thu nhập tăng trước
  → ΔNII = Σ [Repricing_gap_i × Δrate × Days_i/365]
```

**Biến số thay đổi:** lãi suất thị trường (±100bps, ±200bps…)

Đây là IRRBB chính thức theo BCBS d368 — ngân hàng phải đo và report với regulator. Kết quả có thể dương hoặc âm tùy gap position.

### Độ nhạy thanh khoản (Liquidity sensitivity)

**Bản chất:** Đo lường NII/NIM thay đổi bao nhiêu khi **khả năng và chi phí tiếp cận nguồn vốn** thay đổi.

```
Outflow xảy ra / thị trường funding thắt chặt
  → Ngân hàng phải thay thế nguồn vốn rẻ bằng nguồn đắt hơn
  → Cost of funds tăng qua liquidity spread
  → NIM bị ăn vào phía liability
  → ΔNIM = (Funding_gap / Earning_assets) × Liquidity_spread_bps
```

**Biến số thay đổi:** khả năng và chi phí huy động vốn — không phải lãi suất thị trường chung.

**Lưu ý:** "Độ nhạy thanh khoản" không phải là metric chính thức được Basel đặt tên riêng. Nó là cách diễn đạt thực hành để chỉ phần NIM impact đến từ liquidity risk — phân biệt với phần đến từ interest rate risk.

### Tại sao hai cái này hay bị gộp lại?

Vì chúng tác động vào cùng một chỉ số (NIM) nhưng qua hai kênh khác nhau:

```
                    ┌──────────────────────────────────────┐
                    │               NIM                    │
                    └──────────────┬───────────────────────┘
                                   │
              ┌────────────────────┴─────────────────────┐
              │                                          │
   IRRBB sensitivity                         Liquidity sensitivity
   (asset + liability repricing mismatch)    (liability side: replacement cost)
              │                                          │
   Trigger: lãi suất thị trường thay đổi     Trigger: outflow / funding market thắt
   Đo bằng: repricing gap × Δrate            Đo bằng: funding gap × liquidity spread
   Chiều: dương hoặc âm (phụ thuộc gap)      Chiều: luôn âm (tốn thêm chi phí)
```

### Điểm giao nhau — khi nào chúng cộng hưởng

Hai cái này không độc lập trong stress scenario:

```
Lãi suất tăng cao (IRRBB stress)
  → Khách hàng rút tiền đi tìm lãi suất cao hơn (deposit outflow)
  → Ngân hàng phải trám bằng vay liên ngân hàng / phát hành CD
  → Vay ngắn hạn nhiều hơn → liability duration ngắn lại
  → Repricing gap thay đổi → IRRBB exposure tăng thêm

Kết quả: NIM impact > tổng từng phần riêng lẻ (non-additive)
→ Đây là lý do combined shock = -25bps, không phải -15 + (-8) = -23bps (xem Q3)
```

### Bảng so sánh

| | IRRBB sensitivity | Liquidity sensitivity |
|---|---|---|
| Câu hỏi | Nếu lãi suất thay đổi, NIM thay đổi bao nhiêu? | Nếu funding conditions xấu, NIM thay đổi bao nhiêu? |
| Trigger | Lãi suất thị trường | Outflow / market stress |
| Cơ chế | Repricing gap | Funding gap + replacement cost |
| Chiều | Dương hoặc âm | Luôn âm |
| Tên Basel | NII sensitivity (d368) | Không có tên chính thức — nằm trong Liquidity Risk (bcbs144) |
| Công thức | ΔNII = repricing_gap × Δrate | ΔNIM = funding_gap/earning_assets × spread |

Câu hỏi gốc yêu cầu **đo cả hai và tổng hợp thành một output table** — đó mới là bức tranh đầy đủ về NIM sensitivity của ngân hàng.

---

*Related wiki nodes:*
- `[[Irrbb_Eve_Nii_Dual_Metric_Framework]]`
- `[[Maturity_Gap_Analysis_Interest_Rate_Risk_Banking_Book]]`
- `[[Funds_Transfer_Pricing_Rate_Decomposition_Base_Liquidity_Credit_Optionality_Components]]`
- `[[Bank_Alm_Structural_Liquidity_Management_Nsfr_Lcr_Framework]]`
- `[[Bcbs_Liquidity_Internal_Pricing_Ftp_Principle_4]]`
- `[[Bcbs_Liquidity_Contingency_Funding_Plan_Principle_11]]`
- `[[Bcbs_Hqla_Liquidity_Cushion_Principle_12]]`

---

## Q7 — Tính toán Liquidity Sensitivity Impact lên NII: Phương pháp 7 bước (2026-05-27)

### Tổng quan framework

Liquidity sensitivity impact lên NII đo lường: **khi funding conditions xấu đi (outflow + spread widening), NII giảm bao nhiêu?** Khác với IRRBB (market rate driven), đây là liability-side cost shock.

**Ba kênh truyền dẫn:**

```
1. FUNDING COST CHANNEL
   Trigger: stress scenario → outflow → replacement funding at higher spread
   Formula: ΔNII_funding = −Σ[Lⱼ × ΔLPⱼ × w_rollover_j × t_remaining_j/12]

   Lⱼ        = outstanding balance của liability bucket j
   ΔLPⱼ       = liquidity premium widening (bps) for bucket j
   w_rollover_j = fraction maturing/rolling over in stress horizon
   t_remaining_j = months remaining in horizon

2. HQLA OPPORTUNITY COST CHANNEL
   Trigger: must hold more HQLA → displaces earning assets
   Formula: ΔNII_hqla = −ΔHQLA × (r_loan_avg − r_HQLA)

   ΔHQLA   = incremental HQLA needed to meet LCR buffer post-shock
   r_loan_avg = weighted average loan yield
   r_HQLA  = HQLA portfolio yield (typically OIS + 10-20bps)

3. VOLUME IMPACT CHANNEL
   Trigger: outflow → reduced lending capacity
   Formula: ΔNII_volume = −ΔLoans × NIM_marginal

   ΔLoans      = reduction in loan book due to reduced funding
   NIM_marginal = spread on foregone marginal lending
```

---

### Bước 1 — Định nghĩa stress scenarios

| Scenario | Trigger | Liquidity Premium Shock | Runoff Horizon |
|---|---|---|---|
| **Idiosyncratic** | Credit downgrade / reputational event | +100 bps retail deposits; +200 bps wholesale | 30 ngày |
| **Market-wide** | Interbank market freeze | +50 bps all unsecured funding | 30 ngày |
| **Combined** | Both simultaneously | +150 bps retail; +250 bps wholesale | 30 ngày |

Calibration nguồn: EBA GL/2018/04 Section 4.7.6; bcbs238 run-off rate tables.

---

### Bước 2 — Lập repricing schedule cho liabilities

```
Phân nhóm liability theo:
  - Product type: retail deposits (demand / savings / term), wholesale (repo / CD / senior unsecured)
  - Maturity bucket: O/N, 1W, 1M, 3M, 6M, 1Y, >1Y
  - Behavioral maturity: NMDs → dùng replicating portfolio duration, không phải contractual

Key inputs cần lấy từ ALM system:
  Lⱼ        → balance sheet as of reference date
  w_rollover_j → % maturing within stress horizon (từ maturity ladder)
  ΔLPⱼ       → spread shock per bucket per scenario
```

---

### Bước 3 — Tính Funding Cost Impact (Channel 1)

```
ΔNII_funding = −Σⱼ [ Lⱼ × ΔLPⱼ × w_rollover_j × t_remaining_j / 12 ]

Ví dụ (bank có total liabilities = 10,000 tỷ):

Bucket j               Lⱼ (tỷ)  ΔLP (bps)  w_rollover  t_rem  ΔNII contribution (tỷ)
─────────────────────────────────────────────────────────────────────────────────────
Retail demand deposits   3,000      75 bps      15%        1M    −3,000×0.0075×0.15×(1/12) = −0.28
Retail savings           2,000      50 bps      10%        3M    −2,000×0.0050×0.10×(3/12) = −0.25
Retail term < 1Y         1,500     100 bps      60%        6M    −1,500×0.0100×0.60×(6/12) = −4.50
Wholesale CD             1,000     200 bps      80%        1M    −1,000×0.0200×0.80×(1/12) = −1.33
Wholesale repo             500     150 bps     100%        1M    −500×0.0150×1.00×(1/12)   = −0.63
Senior unsecured           800     250 bps      30%        6M    −800×0.0250×0.30×(6/12)   = −3.00
─────────────────────────────────────────────────────────────────────────────────────
TOTAL ΔNII_funding (idiosyncratic, annualized portion) ≈ −9.99 tỷ → ~−10 tỷ
```

**Lưu ý quan trọng:**
- `t_remaining` = thời gian còn lại trong năm tài chính sau khi stress xảy ra
- Nếu tính full-year impact: t_remaining = 12 tháng cho tất cả buckets
- Nếu tính mid-year stress: dùng t_remaining thực tế của từng bucket

---

### Bước 4 — Tính HQLA Opportunity Cost (Channel 2)

```
ΔNII_hqla = −ΔHQLA × (r_loan_avg − r_HQLA)

Giả sử:
  LCR hiện tại    = 120% (buffer = 20% × HQLA_requirement)
  Post-stress LCR minimum cần giữ = 110% (supervisory expectation)
  ΔHQLA needed    = additional buffer to restore 110% LCR under stress

Ví dụ:
  HQLA_requirement = 5,000 tỷ (từ net outflow calculation)
  Stress outflow tăng 1,200 tỷ → HQLA_requirement mới = 6,200 tỷ
  ΔHQLA = 6,200 − 5,000 = 1,200 tỷ

  r_loan_avg = 8.5% (weighted average earning asset yield)
  r_HQLA     = 4.0% (government bond portfolio yield)
  Spread lost = 4.5%

  ΔNII_hqla = −1,200 × 4.5% = −54 tỷ/năm
```

---

### Bước 5 — Tính Volume Impact (Channel 3)

```
ΔNII_volume = −ΔLoans × NIM_marginal

Cơ chế:
  Outflow → bank không thể extend credit mới hoặc phải call loans
  → Foregone interest income on loans not made

Ví dụ:
  Funding gap = 1,500 tỷ (sau khi replacement funding + HQLA sourced)
  Residual lending reduction = 500 tỷ (không thể fully replace)
  NIM_marginal = 3.5% (spread on new loans over funding cost)

  ΔNII_volume = −500 × 3.5% = −17.5 tỷ/năm

Lưu ý: channel này thường nhỏ hơn channel 1 và 2.
Channel 3 quan trọng hơn trong kịch bản severe + prolonged (>3 tháng).
```

---

### Bước 6 — FTP Adjustment

```
Khi bank sử dụng FTP framework, liquidity cost đã được allocated:
  → Loan desks trả FTP charge (bao gồm liquidity premium)
  → Deposit desks nhận FTP credit

Trong stress scenario, FTP rates tăng → tác động phụ thuộc vào FTP adjustment timing:

CASE A: FTP adjusted immediately (market FTP)
  → Front book reprices instantly
  → Nhưng back book (existing loans) không reprices → ΔNII tập trung ở back book lag
  → Công thức điều chỉnh: ΔNII_net = ΔNII_funding × (1 − % front book/ total book)

CASE B: FTP uses internal transfer rate with lag
  → Treasury absorbs shock initially
  → Passes through to business lines quarterly
  → ΔNII timing spreads over FTP reset cycle

Cần xác định FTP policy của bank trước khi áp công thức.
```

---

### Bước 7 — Tổng hợp và báo cáo

```
ΔNII_total = ΔNII_funding + ΔNII_hqla + ΔNII_volume

Bảng kết quả (ví dụ bank 10,000 tỷ liabilities):

Scenario         Channel 1       Channel 2       Channel 3       TOTAL      % of NII
                 (Funding cost)  (HQLA opp.)     (Volume)
─────────────────────────────────────────────────────────────────────────────────────
Idiosyncratic    −10.0 tỷ        −54.0 tỷ        −17.5 tỷ       −81.5 tỷ    −4.1%
Market-wide      −5.0 tỷ         −25.0 tỷ        −8.0 tỷ        −38.0 tỷ    −1.9%
Combined         −18.0 tỷ        −72.0 tỷ        −25.0 tỷ       −115.0 tỷ   −5.8%

Giả sử NII baseline = 2,000 tỷ/năm.
Combined scenario không phải tổng idiosyncratic + market-wide vì:
  → Run-off rates under combined < sum of individual (EBA GL/2018/04 calibration)
  → Nhưng spread shock > từng scenario riêng lẻ
```

**Output format cho ILAAP/ALCO reporting:**

```
1. NII sensitivity table by scenario (bảng trên)
2. Waterfall chart: baseline NII → funding cost → HQLA → volume → post-stress NII
3. Sensitivity to key assumptions:
   - Run-off rate ±10% → ΔNII_funding ±X tỷ
   - Spread assumption ±25bps → ΔNII_funding ±Y tỷ
   - HQLA yield assumption ±50bps → ΔNII_hqla ±Z tỷ
4. Recovery actions: management actions available to offset (FTP repricing, deposit campaigns)
5. Link to survival period metrics (time-to-LCR-breach under each scenario)
```

---

### Mối liên hệ với IRRBB NII sensitivity

```
IRRBB NII sensitivity (bcbs d368):
  ΔNII_irrbb = repricing_gap × Δmarket_rate
  Chiều: dương hoặc âm (phụ thuộc gap position)

Liquidity NII sensitivity:
  ΔNII_liq = ΔNII_funding + ΔNII_hqla + ΔNII_volume
  Chiều: LUÔN ÂM (thêm chi phí)

COMBINED SCENARIO (stress với cả hai):
  Hai sensitivity KHÔNG cộng tuyến tính:
  → IRRBB stress (rate tăng) → deposit outflow → liquidity stress cộng hưởng
  → Phải chạy joint scenario, không tổng đơn thuần

Bảng tổng hợp đầy đủ cho ALCO:

Metric                     Baseline    +200bps rate    Idiosyncratic    Combined
                                        (IRRBB)         liq stress       stress
──────────────────────────────────────────────────────────────────────────────────
NII (tỷ)                   2,000        +40             −81.5            −115 + IRRBB
NIM (%)                    2.80%        +0.06%          −0.11%           −0.18%
LCR (%)                    120%         115%            100%             95%*
Survival period (days)     90           75              45               35
──────────────────────────────────────────────────────────────────────────────────
* Below 100% → triggers LCR restoration plan per bcbs238
```

*Nguồn phương pháp:* bcbs238 (run-off rates), bcbs144 Principles 10-12 (stress framework),
EBA GL/2018/04 (3-scenario taxonomy), SSM ILAAP Guide 2018 (P6: adverse scenarios).

*Related wiki nodes (added 2026-05-27):*
- `[[Lcr_Retail_Deposit_Run_Off_Rates_Stable_Less_Stable_Categories]]`
- `[[Lcr_Wholesale_Unsecured_Funding_Run_Off_By_Counterparty_Type]]`
- `[[Liquidity_Stress_Three_Scenario_Types_Idiosyncratic_Market_Wide_Combined_Eba]]`
- `[[Ilaap_Adverse_Scenario_Calibration_Vulnerability_Based_P7]]`
- `[[Stress_Testing_Solvency_Liquidity_Interaction_Icaap_Ilaap_Integration]]`
- `[[Ilaap_Internal_Liquidity_Adequacy_Assessment_Framework]]`
