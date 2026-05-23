---
node_id: tga_target_creep_bill_issuance_001
type: mechanism
title: TGA Target Creep Bill Issuance And Reserve Neutralization
aliases:
- TGA target increase
- Treasury cash buffer creep
- TGA neutralized reserves
- Mục tiêu TGA tăng dần
- Dự trữ bị trung hòa vào TGA
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- tga
- tbills
- reserves
- treasury_issuance
- reserve_neutralization
- rmo
confidence: 1
stability: evolving
thesis: As Treasury shifts debt issuance toward shorter-maturity bills, the frequency of maturities and redemptions rises, requiring a larger cash buffer in the TGA — structurally pushing Treasury to ratchet up its TGA target (e.g. $850B → $900B+), which permanently neutralizes additional reserves in the government's account and must be offset by Fed RMOs.
source_refs:
- path: 02_sources/books/conks/Conks - Plumping note (Money market.md
  pages: batch 10 (chars ~78506-88020)
  weight: primary
related:
- node: '[[TGA Reserve Swap Mechanics And Debt Ceiling Dynamics]]'
  relation: extends
- node: '[[Fed RMO Reserve Management Operations Post QT Mechanics]]'
  relation: creates_demand_for
- node: '[[Treasury T-bill Supply RRP Drain And MMF Cash Routing]]'
  relation: related_mechanism
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## Mechanism

**Step 1 — Bill-heavy issuance strategy:**
Treasury shifts composition toward bills (overnight to 1-year) over coupons (2-30yr) to minimize taxpayer cost and absorb TGA volatility.

**Step 2 — Higher redemption frequency:**
More bills = more frequent maturities = more cash needed on hand to ensure smooth settlement without market disruption.

**Step 3 — TGA target ratchet:**
Treasury is forced to raise its TGA cash target. Example: $850B → at minimum $900B (per Conks estimate for 2026). Each $100B increment in target = $100B of reserves permanently "neutralized" — held in the TGA, unavailable for interbank clearing. [RAW-CLIP]

**Step 4 — Structural reserve drain:**
Neutralized reserves reduce the reserves available to banks for onshore and offshore dollar payments. In the Basel III era, settling via Eurodollar deposits is expensive, so this drain increases banks' appetite for cheap Fed reserves. [RAW-CLIP]

## Implication for RMO Sizing

Each $50B increase in Treasury's TGA target adds $50B to the structural reserve deficit that the Fed must offset via RMOs (reserve management operations — outright bill purchases). This creates a feedback loop: bill-heavy issuance → higher TGA target → larger RMO requirement → Fed buys more bills → supports bill market → enables more bill issuance. [LLM]

## Quantitative Reference (2025-2027)

- QT2 ended December 1, 2025
- TGA target then: ~$850B
- Estimated TGA target 2026 year-end: ~$900-950B
- Total reserve injections needed by end-2027: ~$240B (from RMOs)
[RAW-CLIP — Conks Plumbing Notes: Post-QT Era]
