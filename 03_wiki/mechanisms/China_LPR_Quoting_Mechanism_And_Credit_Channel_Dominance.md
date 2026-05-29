---
node_id: china_lpr_quoting_mechanism_credit_channel_001
type: mechanism
title: China LPR Quoting Mechanism And Credit Channel Dominance
aliases:
- LPR Quoting System
- China Credit Transmission Channel
- Cơ chế báo giá LPR Trung Quốc
- Kênh tín dụng truyền dẫn chính sách tiền tệ PBOC
domain:
  primary: monetary_policy
tags:
- pboc
- lpr
- mlf
- credit_channel
- interest_rate_transmission
- china
- market_segmentation
confidence: 1
stability: evolving
thesis: The LPR is formed monthly by 20 quoting banks submitting spreads over the
  OMO (primarily MLF) rate to the National Interbank Funding Center, with the arithmetic
  mean after excluding outliers published for 1Y and 5Y+ maturities; China's monetary
  transmission is primarily driven by the credit channel (affecting credit availability)
  rather than the interest rate channel, and cross-market transmission between the
  money market (DR007), credit market (LPR), and bond market (Treasury yield) is structurally
  blocked.
source_refs:
- path: 02_sources/academic/Guo_Chinas_Monetary_Policy_Framework_2025.md
  pages: batch 2 (chars ~7840-16051)
  weight: primary
parent_node: '[[PBOC Monetary Policy Framework And Interest Rate Transmission]]'
related:
- node: '[[PBC Interest Rate Transmission DR007 to LPR]]'
  relation: extends
- node: '[[PBOC Monetary Policy Framework And Interest Rate Transmission]]'
  relation: component_of
- node: '[[PBC Dual-Track Monetary Policy Framework]]'
  relation: context
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## LPR Quoting Mechanism

**Participants:** 20 commercial banks submit LPR quotes to the National Interbank Funding Center (NIFC), authorized by PBOC.

**Process:**
1. Banks submit by 9:00 a.m. on the 20th of each month (postponed if holiday)
2. Method: spread added to the open market operation rate (primarily MLF rate)
3. NIFC calculates arithmetic mean after removing highest and lowest quotes
4. LPR published in two maturities: **1-year** and **over 5-year**

**Rate determination at bank level:** Individual lending rates = LPR ± adjustment for borrower credit risk, collateral, loan term, interest rate fluctuation mechanism, and loan type. [RAW-CLIP]

## Transmission Chain (Pre-July 2024)

```
PBC OMO (7-day reverse repo)
    ↓
DR007 (money market operational target)
    ↓
MLF rate (medium-term policy rate, mid-month operations)
    ↓
LPR (20-bank quote, spread over MLF)
    ↓
Retail loan rates (LPR ± borrower spread)
```

Post-July 2024: MLF decoupled; LPR anchors to 7-day OMO rate directly. [LLM - see [[PBOC Monetary Policy Framework And Interest Rate Transmission]]]

## Credit Channel Dominance

China's monetary policy transmission is **primarily through the credit channel** (asset side: affecting credit availability to economic entities), not the interest rate channel (debt side: affecting funding cost of financial institutions). [RAW-CLIP — Sun Wei & Zhang Nan, 2020]

This contrasts with advanced economies where the interest rate channel is primary.

## Market Segmentation Problem

Each segment has its own benchmark rate:
- **Money market:** DR007 (effective within segment)
- **Credit market:** LPR (effectively prices loans)
- **Bond market:** Treasury yield (effectively prices bonds)

**However:** cross-segment transmission is structurally blocked — changes in DR007 do not cleanly translate to LPR changes or Treasury yield movements. [RAW-CLIP — Yi Gang, 2021]

This segmentation is the structural constraint driving continued reform pressure toward a more integrated price-based framework. [LLM]
