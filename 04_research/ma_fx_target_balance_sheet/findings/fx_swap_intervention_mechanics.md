---
finding_id: fxi_001
title: "FX Swap — Cấu Trúc Hai Chân và Off-Balance Sheet Exposure"
topic_slug: fx_intervention_instruments
type: mechanism_analysis
confidence: 1
status: draft
created: "2026-05-26"
updated: "2026-05-26"
sources_used:
  - "[[CB FX Rate Target Balance Sheet Constraint And Sterilization]]"
  - "[[FX Swap Basis CIP Deviation Dollar Scarcity]]"
gaps_triggered:
  - "CB FX swap intervention off-balance sheet — TRUE_GAP, need BIS WP 119"
wiki_node_created: "03_wiki/mechanisms/Cb_Fx_Swap_Intervention_Mechanics_And_Off_Balance_Sheet_Exposure.md"
---

## Cấu Trúc FX Swap

FX Swap = hai giao dịch cùng notional, ngược chiều, tại hai thời điểm khác nhau:

```
Buy-Sell Swap (CB muốn inject domestic currency tạm thời):
  Near leg (T+2):  CB bán USD, nhận VND → NFA ↓, RM ↑
  Far leg  (T+n):  CB mua USD lại, trả VND → NFA ↑, RM ↓

Sell-Buy Swap (CB muốn drain domestic currency tạm thời):
  Near leg (T+2):  CB mua USD, trả VND → NFA ↑, RM ↓
  Far leg  (T+n):  CB bán USD lại, nhận VND → NFA ↓, RM ↑
```

Far leg = off-balance sheet tại thời điểm ký. Chỉ ghi nhận khi đến ngày settlement.

## Bốn Lý Do CB Dùng Swap Thay Vì Spot [LLM]

1. **Temporary liquidity without permanent reserve drain** — far leg tự đảo ngược, không phải ra thị trường lần nữa
2. **Reduce intervention visibility** — far leg không xuất hiện trong monthly FX reserve headline
3. **Provide dollar liquidity to commercial banks** — CB swap USD cho bank ngắn hạn để phục vụ nhập khẩu mà không mất reserves vĩnh viễn
4. **Defer sterilization** — near+far leg tự cancel nhau nếu kỳ hạn ngắn, không cần OMO ngay

## Hidden Reserve Problem [LLM]

```
Gross FX Reserves (báo cáo)
  - Far leg obligations của tất cả outstanding swaps
  = Net Effective Reserves (thực tế available for spot intervention)

Khi CB có swap book lớn: Net << Gross
Thị trường không thấy được đến khi swap rolls không được hoặc CB fail to deliver
```

**Cần ingest:** BIS WP 119 (Patel & Cavallino 2019), BIS QR Sep 2022
