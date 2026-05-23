---
node_id: fed_policy_rate_shift_effr_to_secured_rate_tgcr_001
type: mechanism
title: Fed Policy Rate Shift EFFR to Secured Rate TGCR
aliases:
- TGCR targeting
- EFFR to TGCR shift
- Logan rate reform
- secured policy rate
- muc lai luat chinh sach co bao dam
domain:
  primary: monetary_policy
tags:
- fed
- effr
- tgcr
- sofr
- policy_rate
- money_market
- floor_system
- operating_framework
confidence: 1
stability: evolving
thesis: A structural debate is emerging over whether the Federal Reserve should shift
  its policy rate target from EFFR (unsecured Fed Funds, dominated by FHLB arbitrage)
  to TGCR (Tri-Party GC Rate, secured overnight lending between dealers and money
  funds), reflecting the post-LIBOR reality where secured markets dominate and EFFR
  is increasingly a technical artifact of FHLB-bank arbitrage rather than genuine
  interbank demand.
source_refs:
- path: 02_sources/books/conks/Conks - Plumping note (Money market.md
  pages: ''
  weight: primary
related:
- node: '[[Central Bank Monetary Policy Operational Framework Typology]]'
  relation: shared_tag:fed
- node: '[[Currency as a Central Bank Liability]]'
  relation: shared_tag:fed
- node: '[[Fedwire Payment System Reserve Demand And LSM Policy]]'
  relation: shared_tag:fed
- node: '[[Fed Ample Reserves Rate Control Framework]]'
  relation: shared_tag:fed
- node: '[[QT Reserve Drain Effectiveness And Deposit Funding Condition]]'
  relation: shared_tag:fed
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Historical Context
[LLM] Pre-2019: Fed targeted EFFR (unsecured overnight interbank rate, dominated by FHLB-bank transactions).
Post-LIBOR transition: SOFR (secured overnight repo rate, ~$1trn+ depth) replaced LIBOR as market benchmark.
Anomaly: Fed continued using EFFR as its policy target rate even after SOFR became dominant market benchmark.

## Logan Proposal (Dallas Fed, ~2025)
[LLM] Dallas Fed President Lorie Logan proposed shifting the Fed's policy rate target from EFFR (unsecured interbank) to TGCR (Tri-Party General Collateral Rate, the Fed's measure of secured overnight lending between dealers and money funds).
Rationale: TGCR better reflects actual secured money market conditions; SOFR is broader (includes cleared repo) while TGCR is the most policy-relevant segment.

## Implications
[LLM] If adopted: the Fed's upper boundary effectively becomes TGCR rather than IORB. Rate corridor logic shifts toward secured funding markets. Discount window and SRF roles may need recalibration. SOFR-TGCR basis becomes a new policy-relevant spread.

## Rate Reference Glossary
[LLM] EFFR = effective Fed Funds rate (unsecured). OBFR = overnight bank funding rate (broader unsecured + eurodollar). SOFR = secured overnight financing rate (all repo). TGCR = tri-party GC rate (dealer-to-money-fund repo only). BGCR = broad GC rate (TGCR + GCF repo).


