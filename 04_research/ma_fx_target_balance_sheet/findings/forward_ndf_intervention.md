---
finding_id: fxi_002
title: "Forward và NDF — Delivery vs Cash Settlement"
topic_slug: fx_intervention_instruments
type: mechanism_analysis
confidence: 1
status: draft
created: "2026-05-26"
updated: "2026-05-26"
sources_used:
  - "[[CB FX Rate Target Balance Sheet Constraint And Sterilization]]"
gaps_triggered:
  - "outright forward NDF CB intervention — TRUE_GAP, need Cantú et al. IMF WP"
wiki_node_created: "03_wiki/mechanisms/Cb_Fx_Forward_And_Ndf_Intervention_Delivery_Versus_Cash_Settlement.md"
---

## Outright Forward [LLM]

CB cam kết mua/bán FX tại ngày tương lai, giá thỏa thuận hôm nay:

```
Hôm nay ký: không có dòng tiền, không có NFA change → off-balance sheet
Ngày delivery: NFA ↓ (nếu CB bán FX), RM ↓

Dùng khi:
  - CB muốn signal tỷ giá commitment mà không tốn reserves ngay
  - "Announcement effect" — thị trường thấy CB sẵn sàng defend → speculative pressure giảm
  - CB có kỳ vọng tỷ giá sẽ ổn định → có thể không cần deliver thực sự

Rủi ro: delivery risk — đến ngày settlement phải có FX đủ
Thailand 1997: forward commitments vượt gross reserves → vỡ cam kết → khủng hoảng [LLM]
```

## NDF — Non-Deliverable Forward [LLM]

```
Cấu trúc: giống forward nhưng settlement = cash (VND/USD) dựa trên fixing rate
  Không có FX delivery
  NFA không thay đổi
  Chi phí/lợi nhuận = (NDF rate − Fixing rate) × notional → VND settlement

Dùng khi:
  - Currency có capital controls (thị trường onshore hạn chế)
  - CB muốn influence offshore NDF market expectations
  - CB không muốn động đến spot reserves

Offshore NDF market (London, Singapore) phản ánh kỳ vọng tỷ giá độc lập
→ CB can thiệp NDF offshore để anchor kỳ vọng mà không cần spot reserves
```

## So Sánh Balance Sheet Impact

| Instrument | NFA khi ký | NFA khi settle | Hiện reserves? | Delivery risk |
|---|---|---|---|---|
| Spot | Ngay ±100% | N/A | Có (monthly) | Minimal |
| Outright Forward | Không | ±100% | Không | Cao nếu reserves cạn |
| NDF | Không | Không | Không | Chỉ cash P&L |

**Cần ingest:** Cantú et al. IMF WP, IMF BPM6 Ch.6
