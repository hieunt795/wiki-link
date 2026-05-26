---
finding_id: ma_fx_002
title: "Sterilization — T-Account Mechanics và Hai Giới Hạn Binding"
topic_slug: ma_fx_target_balance_sheet
type: mechanism_analysis
confidence: 4
status: stable
created: "2026-05-26"
updated: "2026-05-26"
sources_used:
  - "[[CB FX Rate Target Balance Sheet Constraint And Sterilization]]"
  - "[[IMF FX Regime Balance Sheet — Monetary Accounts Perspective (Chapter 5)]]"
  - "[[Sterilization Effectiveness — Offset and Sterilization Coefficients in EMEs]]"
raw_source_passages:
  - "[RAW-BOOK IMF Macro p.4828] 'Sterilization can work only for a short period. Its basic weakness is its dependence on the kind of broad and well-functioning securities market that is not available in many transition economies.'"
  - "[RAW-BOOK IMF Macro p.4828] 'sterilization is limited by the cost of interest payments on the government securities purchased, a cost that can escalate rapidly'"
  - "[RAW-BOOK Lipschitz lines 2665–2730] Box 4.7: Intervention and Sterilization; Table 4.8"
---

## T-Account: Ba Tình Huống Can Thiệp

### Tình huống A — Áp lực tăng giá (capital inflows, CA surplus)

CB phải mua FX để giữ tỷ giá không tăng:

```
MONETARY AUTHORITY
Assets                      Liabilities
──────────────────────      ──────────────────────
NFA  +100 (mua FX)     →    RM  +100 (bank reserves↑)
```

Kết quả chưa sterilize: RM tăng → thanh khoản dư thừa → lãi suất liên ngân hàng giảm → nới lỏng tiền tệ ngoài ý muốn.

---

### Tình huống B — Áp lực giảm giá (capital outflows, CA deficit)

CB phải bán FX để giữ tỷ giá không giảm:

```
MONETARY AUTHORITY
Assets                      Liabilities
──────────────────────      ──────────────────────
NFA  -100 (bán FX)     →    RM  -100 (bank reserves↓)
```

Kết quả: RM giảm → thanh khoản thắt → lãi suất tăng → thắt tiền tệ ngoài ý muốn. Tiếp diễn → NFA tiệm cận ngưỡng tối thiểu → mất khả năng defend.

---

### Tình huống C — Sterilized Intervention (giữ RM trung lập)

Sau khi mua FX (Tình huống A), CB bán T-bills để hút RM về:

```
Bước 1 — FX Intervention:
  NFA  +100  →  RM  +100

Bước 2 — Sterilization OMO:
  NCG  -100  →  RM  -100   (CB bán T-bills, hút tiền)

Net result:
  NFA  +100 ↑       (cumulatif)
  NCG  -100 ↓       (NDA giảm)
  RM   = 0          (unchanged)
```

Sterilization "thành công" về mặt RM. Nhưng balance sheet cấu trúc đã thay đổi: NFA cao hơn, NDA thấp hơn — hai giới hạn bắt đầu tích lũy.

---

## Hai Giới Hạn Binding

### Giới hạn 1 — Độ sâu thị trường (Market Depth)

CB bán T-bills để sterilize → cần thị trường thứ cấp đủ sâu để hấp thụ. Tại thị trường mỏng:

```
CB bán T-bills nhiều  →  yield nội địa↑
                      →  r_domestic > r_foreign
                      →  capital inflows thêm
                      →  CB phải mua FX thêm
                      →  cần sterilize thêm
                      →  yield↑ thêm  → loop
```

Vòng lặp tự khuếch đại — sterilization tạo ra chính áp lực mà nó cố triệt tiêu. [RAW-BOOK IMF Macro p.4828]

### Giới hạn 2 — Chi phí lãi suất (Quasi-Fiscal Cost)

CB tích lũy NFA (FX reserves) earn yield thấp (r_foreign), phát hành T-bills sterilization với yield cao hơn (r_domestic):

```
Quasi-fiscal cost/kỳ =  r_domestic × Sterilization_stock
                      −  r_foreign  × NFA_accumulated
                      =  Âm  (net cost, điều kiện thông thường EM)
```

[RAW-BOOK Lipschitz p.2720]: *"buys low-yield FX, sells high-yield domestic → CB profit falls → transfers to budget fall"*

Chi phí tích lũy → CB lỗ → seigniorage transfer về Treasury giảm → fiscal burden tăng gián tiếp.

---

## Sterilization Coefficients (Empirical)

Sterilization coefficient (β) đo mức độ NDA phản ứng bù lại NFA:

```
β = −ΔNDA / ΔNFA

β = 1.0  →  full sterilization (RM unchanged)
β = 0.0  →  no sterilization   (RM moves 1:1 with NFA)
0 < β < 1 → partial sterilization (middle ground)
```

Offset coefficient (α) đo capital inflows phản ứng với monetary tightening:

```
α = ΔCFA / ΔNDA   (CFA = capital flow adjustment)

α → -1  →  full offset (tightening fully offset by inflows)
α → 0   →  no offset   (tightening effective)
```

Với open capital account, α → −1 và β → 1 cùng lúc là impossible sustained equilibrium: sterilization hoàn toàn trong môi trường vốn tự do là không bền vững. [[Sterilization Effectiveness — Offset and Sterilization Coefficients in EMEs]]
