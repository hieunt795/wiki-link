---
finding_id: fxi_004
title: "Hidden Reserves — Gross vs Net Effective Intervention Capacity"
topic_slug: fx_intervention_instruments
type: concept_analysis
confidence: 1
status: draft
created: "2026-05-26"
updated: "2026-05-26"
sources_used:
  - "[[IMF FX Regime Balance Sheet — Monetary Accounts Perspective (Chapter 5)]]"
gaps_triggered:
  - "net effective reserves hidden forward book — TRUE_GAP, need BIS QR Sep 2022, IMF BPM6"
wiki_node_created: "03_wiki/concepts/Cb_Hidden_Fx_Reserves_Net_Effective_Intervention_Capacity.md"
---

## Gross vs Net Effective Reserves [LLM]

```
Gross FX Reserves (officially reported)
  Bao gồm: gold, SDR, reserve position at IMF, FX assets
  KHÔNG trừ: swap far legs, forward delivery obligations, collateral posted

Net Effective Reserves (thực tế có thể dùng để intervene):
  = Gross Reserves
  − Outstanding swap far-leg obligations
  − Outright forward delivery commitments
  − Collateral posted for hedges
  − Minimum operational buffer

Net Effective Reserves là con số thực sự quyết định:
  Bao lâu CB có thể sustain spot intervention?
  Khi nào phải break FX target?
```

## Historical Cases [LLM — cần verify]

**Thailand 1997:**
Gross reserves: ~$30B (appeared adequate)
Forward commitments outstanding: ~$23B+
Net effective reserves: ~$7B → gần như không đủ để defend baht
→ Khi speculators nhận ra net position → attack thành công

**Turkey 2021:**
CB thực hiện FX swap với commercial banks để inject liquidity
Swap far-leg obligations tích lũy → Net reserves âm tại một số thời điểm
Gross reserves vẫn positive → misleading signal

## IMF BPM6 Disclosure Requirements [LLM]

IMF BPM6 yêu cầu khai báo **off-balance sheet FX positions** trong supplementary data:
- Template on International Reserves and Foreign Currency Liquidity
- Section IV: Contingent Short-term Net Drain on Foreign Currency Assets
- Bao gồm: forward, swap, options có FX delivery obligation

Compliance không đồng đều giữa các CB → gap trong international comparability.

## Implications Cho MA Balance Sheet Analysis

```
Khi đọc NFA trong monetary survey:
  NFA = on-balance-sheet net foreign assets
  = Spot positions đã settled
  KHÔNG bao gồm: swap far legs, forwards, options chưa exercised

→ NFA trong monetary survey LUÔN LUÔN overstates true intervention capacity
   nếu CB có off-balance-sheet FX book

Link về parent topic:
  [[CB FX Rate Target Balance Sheet Constraint And Sterilization]]
  → "NFA reaches critical minimum → intervention no longer possible"
  → "Critical minimum" phải tính cả off-BS obligations, không chỉ on-BS NFA
```

**Cần ingest:** BIS QR Sep 2022 (FX swap off-balance sheet EM CBs), IMF BPM6 Ch.6
