---
finding_id: ma_fx_001
title: "MA Balance Sheet Identity và Causality Reversal Dưới FX Target"
topic_slug: ma_fx_target_balance_sheet
type: mechanism_analysis
confidence: 4
status: stable
created: "2026-05-26"
updated: "2026-05-26"
sources_used:
  - "[[IMF FX Regime Balance Sheet — Monetary Accounts Perspective (Chapter 5)]]"
  - "[[IMF Monetary Survey And Reserve Money Identity Framework]]"
  - "[[CB FX Rate Target Balance Sheet Constraint And Sterilization]]"
raw_source_passages:
  - "[RAW-BOOK IMF Macro p.4794] 'the monetary base and money supply adjust in line with net foreign assets... The monetary authorities are therefore unable to control the money supply'"
  - "[RAW-BOOK IMF Macro p.4810] 'Under a fixed exchange rate regime, the money supply is rendered endogenous — that is, it is determined by the system — rather than being an instrument of policy'"
  - "[RAW-BOOK Lipschitz lines 2665–2730] Section 4a: Monetary Policy and External Shocks; Box 4.7: Intervention and Sterilization"
---

## Identity Gốc

Bảng cân đối monetary authority được tóm gọn qua identity:

```
RM  =  NFA  +  NDA

  RM  = Reserve Money (monetary base) — LIABILITIES side
  NFA = Net Foreign Assets            — ASSETS side
  NDA = Net Domestic Assets = NCG + Cb + OIN
        NCG = Net Claims on Government
        Cb  = Claims on Banks (discount window)
        OIN = Other Items Net (capital, valuation)
```

Đây là accounting identity — luôn đúng. Câu hỏi là **chiều nhân quả** chạy theo hướng nào.

---

## Causality Reversal — Cơ Chế Cốt Lõi

### Chế độ bình thường (không có FX target)

```
CB lựa chọn NDA (NCG, Cb) → điều tiết RM
NFA = biến phụ chọn tùy ý (CB mua/bán FX discretionary)
RM  = target chính sách
```

### Khi cam kết FX rate target

```
BOP flows → NFA [endogenous, driven by intervention obligation]
         → RM [bắt buộc adjust để clear FX market]

NDA = chỉ còn chức năng sterilization — không phải công cụ chính sách độc lập
RM  = residual, không phải target
```

**Causality đảo hoàn toàn:** NFA từ biến chính sách → biến phụ thuộc. RM từ target → residual.

[RAW-BOOK IMF Macro p.4794]: *"Adopting a fixed exchange rate regime therefore dedicates monetary policy to the goal of ensuring that the officially fixed level of the exchange rate is also the equilibrium level. The central bank is then committed to adjusting the money supply to the level needed to ensure that the exchange market clears at the predetermined fixed exchange rate."*

---

## Năm Công Cụ Kiểm Soát RM (IMF Box 5.2)

| Công cụ | Cơ chế | Balance Sheet |
|---|---|---|
| FX Intervention | Mua/bán FX reserves | NFA ↑↓, RM ↑↓ (1:1) |
| Open Market Operations | Mua/bán T-bills thứ cấp | NCG ↑↓, RM ↑↓ (1:1) |
| Deficit Financing | CB cho chính phủ vay | NCG ↑, RM ↑ khi chính phủ chi |
| Discount Window | CB cho vay ngân hàng | Cb ↑↓, RM ↑↓ |
| Reserve Requirements | Thay đổi tỷ lệ DTBB | RM ↑ (RRR tăng); multiplier ↓ |

Dưới FX target: công cụ FX Intervention bị ràng buộc bởi BOP. CB chỉ còn NDA (OMO, NCG, Cb) để sterilize — không phải để chọn stance độc lập. [RAW-BOOK IMF Macro p.4382–4402]
