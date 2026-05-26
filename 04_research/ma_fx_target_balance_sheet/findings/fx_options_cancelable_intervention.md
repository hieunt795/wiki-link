---
finding_id: fxi_003
title: "FX Options và Cancelable Forward — Quyền Chọn Trong Can Thiệp"
topic_slug: fx_intervention_instruments
type: mechanism_analysis
confidence: 1
status: draft
created: "2026-05-26"
updated: "2026-05-26"
sources_used: []
gaps_triggered:
  - "cancelable forward FX option CB pricing — TRUE_GAP, need BIS Triennial FX Survey, ISDA docs"
wiki_node_created: "03_wiki/mechanisms/Cb_Fx_Options_And_Cancelable_Forward_Intervention_Structures.md"
---

## Vanilla Options — CB Là Buyer, Không Phải Seller [LLM]

```
CB mua USD put (right to sell USD at strike K):
  Premium: trả trước (cost)
  NFA: không thay đổi khi mua
  Exercise: chỉ khi spot < K (nội tệ mạnh hơn K → CB muốn bán USD)
  → CB có "insurance" chống tăng giá nội tệ quá mức

CB KHÔNG nên bán USD call:
  → Đối tác có quyền mua USD từ CB khi nội tệ yếu
  → CB có unlimited downside nếu nội tệ depreciate mạnh
  → Risk profile bất lợi cho CB
```

## Cancelable Forward — Forward Với Embedded Option [LLM]

```
Cấu trúc:
  CB ký forward bán USD, kỳ hạn T+3M, giá K
  + CB có quyền hủy hợp đồng nếu điều kiện X xảy ra

Điều kiện hủy thường là:
  - Spot rate tại delivery khác K quá nhiều (>= barrier)
  - Hoặc thị trường đã ổn định (không cần deliver)

Pricing: rộng hơn plain forward vì counterparty phải hedge quyền chọn hủy
Cost = plain forward spread + option premium ẩn trong spread

Dùng khi:
  CB muốn signal commitment → thị trường thấy forward → pressure giảm
  Nhưng CB không muốn khóa reserves hoàn toàn
  Nếu ổn → cancel → không tốn reserves
  Nếu áp lực lớn → deliver → dùng reserves thực
```

## Zero-Cost Structures [LLM]

```
Range Forward:
  CB cam kết bán USD trong range [K1, K2]
  Spot < K1: CB bán tại K1 (defend floor)
  Spot trong [K1,K2]: market rate
  Spot > K2: CB bán tại K2 (defend ceiling)
  Net premium: 0 (hai legs offset nhau)
  → Tạo semi-automatic corridor, mất discretion ngoài range

Seagull (3 legs):
  Buy USD put + Sell USD put (lower strike) + Sell USD call
  → Net premium ≈ 0
  → CB có limited downside protection với bounded upside risk
```

## Balance Sheet Signature Options

| Structure | NFA khi ký | Premium | Reserves hiện? | Downside |
|---|---|---|---|---|
| Buy vanilla put | Không | -Premium | Không | Bounded (premium only) |
| Sell vanilla call | Không | +Premium | Không | Unlimited |
| Cancelable Forward | Off-BS | Wider spread | Không | Delivery nếu không cancel |
| Range Forward | Off-BS | 0 | Không | Must deliver outside range |
| Seagull | Off-BS | ≈0 | Không | Limited, bounded |

**Cần ingest:** BIS Triennial FX Survey, ISDA FX option documentation
