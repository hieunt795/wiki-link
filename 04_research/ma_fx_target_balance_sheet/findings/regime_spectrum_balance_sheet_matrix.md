---
finding_id: ma_fx_004
title: "Phổ Chế Độ — Balance Sheet Matrix và Diagnostic Signals"
topic_slug: ma_fx_target_balance_sheet
type: synthesis
confidence: 3
status: stable
created: "2026-05-26"
updated: "2026-05-26"
sources_used:
  - "[[IMF FX Regime Balance Sheet — Monetary Accounts Perspective (Chapter 5)]]"
  - "[[CB FX Target — Five-Entity Combined Balance Sheet Trace (T-Account Scenarios)]]"
  - "[[FX Rate Target + Quasi-Fiscal Operations — Stagflation Trap Mechanism]]"
raw_source_passages:
  - "[RAW-BOOK IMF Macro p.4850] Currency board: 'reserve money can be created only if it is fully backed by holdings of foreign exchange... Sterilization is ruled out'"
  - "[RAW-BOOK IMF Macro p.4852] Float: 'monetary authorities have full control over the domestic money supply... The link between the money supply and the balance of payments is broken'"
  - "[RAW-BOOK IMF Macro p.4862] Perfect capital mobility + fixed rate: 'central bank cannot hope to influence the level of domestic interest rates'"
  - "[RAW-BOOK IMF Macro p.4864] Three-component response: partial intervention + partial sterilization + accept some monetary expansion"
---

## Phổ Chế Độ — Balance Sheet Instrument Matrix

```
                  Fixed Peg    Currency Board   Managed Float   Pure Float
────────────────────────────────────────────────────────────────────────────
NFA               Endogenous   Fully endogenous  Discretionary   Discretionary
NDA (sterilize)   Available    NOT available     Available       Available
RM                Endogenous   = NFA × 1.0       Partial ctrl    Full ctrl
Monetary auton.   None         Zero              Partial         Full
Sterilization     Possible     Impossible        Possible        N/A
Quasi-fiscal      Yes          N/A               Yes (smaller)   No
Adjustment mech.  Reserve ↓↑   Prices/wages      Mix             Exchange rate
```

---

## Fixed Peg — Defend Obligatory

NFA hoàn toàn endogenous. CB phải intervene bất cứ khi nào tỷ giá lệch khỏi parity.

Với open capital account, monetary policy bị vô hiệu hóa hoàn toàn:

```
CB tăng lãi suất  →  r_domestic > r_foreign
                  →  capital inflows
                  →  CB phải mua FX (defend peg)
                  →  NFA ↑ → RM ↑ → offset tightening
                  →  r_domestic trở về r_foreign

Net: tightening 0% effective. [RAW-BOOK IMF Macro p.4862]
```

---

## Currency Board — Zero Monetary Autonomy

Ràng buộc pháp lý: RM chỉ được tạo ra nếu NFA tăng tương đương 1:1. NDA bị lock.

```
Currency Board balance sheet:
  NFA / RM ≥ 1.0  (100% backing requirement)
  NDA = 0 (fixed by law, cannot be used for sterilization)

Adjustment mechanism (không có sterilization):
  BOP deficit  →  NFA ↓  →  RM ↓
              →  thanh khoản thắt  →  r_domestic ↑
              →  áp lực giảm giá/tiền lương (nếu flexible)
              →  hoặc thất nghiệp tăng (nếu rigid)
```

[RAW-BOOK IMF Macro p.4850]: *"Adjustment will eventually raise nominal and real interest rates and put downward pressure on prices: if prices, and especially wages, are not flexible, output and employment fall."*

---

## Managed Float — Middle Ground Thực Tế

Phản ứng ba thành phần khi có capital inflows lớn [RAW-BOOK IMF Macro p.4864]:

```
(i)  Partial FX intervention:
     CB mua một phần FX → NFA ↑ (không đủ giữ tỷ giá cố định)
     → Nội tệ tăng giá một phần (nominal appreciation)

(ii) Partial sterilization:
     CB bán T-bills → NDA ↓, hút bớt RM
     → Bị giới hạn bởi market depth + quasi-fiscal cost

(iii) Accept một phần monetary expansion:
     Phần NFA không sterilize → RM ↑ → lạm phát
     → Real appreciation qua giá thay vì nominal rate

Outcome: triangulation giữa tỷ giá, dự trữ ngoại hối, và lạm phát
```

---

## Pure Float — Monetary Autonomy Đầy Đủ

CB không có nghĩa vụ intervene → NFA discretionary → RM fully controlled.

```
BOP deficit  →  excess FX demand  →  nội tệ giảm giá tự nhiên
            →  CB không intervene  →  NFA unchanged
            →  depreciation phục hồi cạnh tranh thương mại tự động

Monetary tightening:
  CB tăng NDA↓ → r_domestic ↑
  Capital inflows → nội tệ appreciate (không phải CB mua FX)
  Appreciation → nhập khẩu rẻ hơn → thêm kênh kiểm soát lạm phát
  Net: monetary policy fully effective + exchange rate là thêm transmission channel
```

---

## Diagnostic Signals — Đọc Balance Sheet

| Pattern quan sát | Diễn giải |
|---|---|
| NFA ↓ + NCG ↑ + RM ổn định | CB defend depreciation bằng sterilized intervention. Kiểm tra: NCG room còn bao nhiêu? |
| NFA ↑ + NDA ↓ + RM ổn định | Sterilizing appreciation pressure. Quasi-fiscal cost đang tích lũy. |
| NFA ↑ + NDA không giảm đủ + RM ↑ | Partial sterilization — monetary expansion leak qua kênh FX. |
| M2 ↑ nhưng NFA + NDA không giải thích đủ | Kiểm tra OIN và valuation — FX deposits có thể bị revalue (dollarization). |
| NFA tiệm cận ngưỡng tối thiểu | Intervention capacity sắp cạn → risk premium spike sắp xảy ra. |
| NCG ↑ liên tục trong khi NFA ↓ | Fiscal dominance đang hình thành — CB đang tài trợ deficit qua monetary channel. |
