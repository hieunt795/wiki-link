---
finding_id: ma_fx_005
title: "OIN — Thành Phần, Cơ Chế Di Chuyển và Vai Trò Absorber Trong MA Balance Sheet"
topic_slug: ma_fx_target_balance_sheet
type: mechanism_analysis
confidence: 4
status: stable
created: "2026-05-26"
updated: "2026-05-26"
sources_used:
  - "[[IMF Monetary Survey And Reserve Money Identity Framework]]"
  - "[[IMF Monetary Survey — Valuation Adjustment and Transaction Flow Decomposition]]"
  - "[[CB FX Target — Five-Entity Combined Balance Sheet Trace (T-Account Scenarios)]]"
  - "[[CB Quasi-Fiscal Mechanism — Sterilization Costs, Seigniorage, and the Fiscal-Monetary Nexus]]"
raw_source_passages:
  - "[RAW-BOOK IMF Macro Box 5.2 p.4336–4353] OINm = physical assets, capital accounts, valuation adjustments, unclassified items"
  - "[RAW-BOOK IMF Macro Box 5.7 p.4546–4580] OINb = residual; absorbs valuation adjustments, capital accounts, unclassified interbank items"
  - "[RAW-BOOK IMF Macro Box 5.8 p.4651] 'valuation adjustments should be reflected in other items (net) to ensure that the balance sheet remains in balance'"
  - "[RAW-BOOK Lipschitz p.2720] sterilization losses accumulate in OINm via declining CB profit"
  - "[RAW-BOOK IMF Macro p.4572–4578] M2 decomposition: ΔOINb/OINb × OINb/M2 = QF loss / valuation weight"
---

## Vị Trí OIN Trong Balance Sheet MA

OIN là thành phần thứ tư và cuối cùng trong identity cốt lõi:

```
RM = NFA + NCG + Cb + OIN
          ↑         ↑
    (can điều chỉnh  (absorber — nhận
     bằng policy)    mọi thứ còn lại)
```

Vì đây là identity kế toán phải luôn bằng 0, bất kỳ thay đổi nào ở NFA, NCG, Cb mà không khớp với ΔRM đều phải đổ vào ΔOIN. OIN là **số dư bắt buộc** của balance sheet.

---

## OINm — Nội Dung Chi Tiết

```
OINm (Monetary Authority level):

PHẦN LÀM OINm TĂNG (+):
  Physical assets          — cơ sở vật chất, trang thiết bị CB
  Paid-in capital          — vốn điều lệ từ chính phủ khi thành lập
  Retained earnings        — lợi nhuận tích lũy chưa phân phối
  Revaluation surplus      — NFA (FC) × (e_new − e_old): khi nội tệ yếu,
                             giá trị LCU của FX reserves tăng → surplus vào đây

PHẦN LÀM OINm GIẢM (−):
  Provisions               — dự phòng tổn thất
  Accumulated QF losses    — tổn thất từ sterilization, subsidized lending
  Revaluation deficit      — khi nội tệ mạnh, NFA giảm giá trị LCU
  Suspense/unclassified    — items chờ phân loại
```

Hai tầng OIN tương ứng với hai cấp độ hợp nhất:

```
MA level:      RM  = NFA   + NCG + Cb + OINm
Survey level:  M2  = NFA   + NDC       + OINb
                             NDC = NCG + CPS
               OINb = OINm_cb + Σ OIN_dmb_i
```

---

## Ba Cơ Chế Làm OIN Di Chuyển

### Cơ chế 1 — Valuation Adjustment (Quan trọng nhất)

Khi tỷ giá thay đổi, NFA tính bằng LCU thay đổi dù không có giao dịch nào:

```
NFA_LCU = NFA_FC × e   (e = tỷ giá, LCU/FC)

Khi nội tệ yếu (e↑):
  NFA_LCU ↑ (cùng FC nhưng LCU nhiều hơn)
  RM không tự tăng (không có giao dịch thực)
  → ΔOIN phải ↑ để identity còn bằng:
    ΔRM = ΔNFA_LCU + ΔOIN → 0 = +VAj + ΔOIN → ΔOIN = −VAj

Khi nội tệ mạnh (e↓): ngược lại, ΔOIN âm.
```

[RAW-BOOK IMF Macro Box 5.8 p.4651]: *"valuation adjustments should be reflected in 'other items (net)' to ensure that the balance sheet remains in balance."*

Đây là lý do tại sao OIN trong monetary survey của EM thường dao động mạnh xung quanh các đợt phá giá — không phải CB làm gì khác, chỉ là revaluation.

### Cơ chế 2 — Quasi-Fiscal Loss Accumulation

Mỗi kỳ CB sterilize, có chi phí lãi suất ròng:

```
CB P&L mỗi kỳ:
  Thu:  r_f × NFA_stock   (yield thấp trên FX reserves)
  Chi:  r_d × Sterilization_stock  (yield cao trên T-bills phát hành)
  Net:  (r_f − r_d) × stock = NEGATIVE

→ Lợi nhuận CB giảm → retained earnings giảm → OINm ↓

Sequence:
  Kỳ 1: OINm = +100 (capital ban đầu)
  Kỳ 2: OINm = +85  (−15 QF loss)
  Kỳ 3: OINm = +65  (−20 QF loss, sterilization lớn hơn)
  Kỳ 4: OINm = +30
  Kỳ 5: OINm = 0    → CB hết vốn, seigniorage về Treasury = 0
  Kỳ 6: OINm = −20  → CB insolvent về mặt kế toán
```

[RAW-BOOK Lipschitz p.2720 + p.2728]

### Cơ chế 3 — Recapitalization (Đảo ngược QF losses)

Khi OINm quá âm, chính phủ phải bơm vốn:

```
Chính phủ phát hành trái phiếu recap NB → CB nhận:

CB:      NCG ↑ NB  │ OINm ↑ NB  (equity restored)
         (nắm giữ   (vốn tăng)
          trái phiếu
          recap)

Gov:     Debt ↑ NB  │ (nợ tăng, ghi nhận trong GFS)

Fiscal treatment [RAW-BOOK IMF Macro p.1841]:
  Conventional deficit: chỉ ghi lãi suất hàng năm trên NB
  True cost: toàn bộ NB = present value của tất cả lãi tương lai
  → Recap che giấu trong headline deficit, chỉ lộ dần qua interest expense
```

---

## OIN Là Diagnostic Lens — Đọc Sức Khỏe CB

```
M2 decomposition weight:
  ΔM2/M2 = (ΔNFA/NFA)×(NFA/M2) + (ΔNDC/NDC)×(NDC/M2) + (ΔOINb/OINb)×(OINb/M2)
                                                            ↑
                                              OIN weight = QF + valuation signal

[RAW-BOOK IMF Macro p.4572–4578]
```

| OINm signal | Diễn giải |
|---|---|
| OINm tăng đều | CB profitable, seigniorage transfer dương, vốn tích lũy |
| OINm đi ngang dù NFA↑ | Valuation gains bị offset bởi QF losses — net zero |
| OINm giảm chậm | Sterilization costs > earnings: QF loss tích lũy |
| OINm = 0 | CB hết vốn; seigniorage transfer về Treasury = 0 |
| OINm âm | CB insolvent kế toán; cần recap; fiscal contingency đang hiện thực hóa |
| OINm jump lớn đột ngột ↑ | Recapitalization vừa xảy ra — tìm phát hành trái phiếu recap |
| OINb âm (survey level) | Capital erosion toàn hệ thống ngân hàng — tiền thân banking crisis |

---

## Kết Nối Với Hai Research Workspace Kia

```
ma_fx_target_balance_sheet:
  NFA endogeneity → sterilization → OINm↓ (Cơ chế 2 ở trên)
  OINm âm → fiscal cost latent → fiscal dominance endgame

fx_intervention_instruments:
  FX Swap far-leg settle → NFA thay đổi thực → OINm nhận valuation adjustment
  Forward delivery → NFA change tại T+n → OINm absorbs at settlement
  Options exercise → NFA change → OINm absorbs
  → Off-balance-sheet instruments tạo contingent OIN exposure chỉ lộ khi settled
```
