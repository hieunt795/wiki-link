---
node_id: private_credit_pik_and_hidden_leverage_mechanisms_001
type: mechanism
title: Private Credit PIK and Hidden Leverage Mechanisms
aliases:
- PIK private credit
- NAV lending
- subscription facility
- hidden leverage private credit
- PIK lãi suất trả bằng vốn
- đòn bẩy ẩn tín dụng tư nhân
domain:
  primary: financial_markets
tags:
- private_credit
- pik
- nav_lending
- subscription_facility
- leverage
- credit_risk
- nbfi
confidence: 1
stability: evolving
thesis: 'Private credit funds employ two hidden leverage mechanisms: (1) Payment-in-Kind
  (PIK), which allows borrowers to defer cash interest by accruing more principal
  — keeping defaults optically low while leverage rises; and (2) subscription facilities
  (secured against unfunded LP commitments) and NAV lending (borrowing against fund
  portfolio value) — both instruments create a structure where a "hold-to-maturity,
  illiquid loan book" is paired with financing whose availability is contingent on
  lender confidence and collateral valuation. [LLM]'
source_refs:
- path: 02_sources/deep-research/Deep Dive_ Private Credit.md
  pages: ''
  weight: primary
parent_node: null
related:
- node: '[[PIK_Payment_In_Kind_Credit_Masking]]'
  relation: canonical_detail_for_pik_channel
- node: '[[Private_Credit_Subscription_Nav_Lending_Hidden_Leverage]]'
  relation: canonical_detail_for_fund_finance_channel
- node: '[[Bank_NBFI_Leverage_Loop]]'
  relation: systemic_feedback_channel
date_created: '2026-05-23'
date_updated: '2026-05-24'
steps:
- 'Step 1: Payment-in-Kind (PIK), which allows borrowers to defer cash interest by accruing more principal — keeping defaults optically low while leverage rises; and'
- 'Step 2: subscription facilities (secured against unfunded LP commitments) and NAV lending (borrowing against fund portfolio value) — both instruments create a structure where a "hold-to-maturity, illiquid loan book" is paired with financing whose availability is contingent on lender confidence and collateral valuation. [LLM]'

---

## Scope Boundary

[LLM] This node is an umbrella/router for the two private-credit hidden-leverage channels in the source: borrower-level PIK accrual and fund-level subscription/NAV borrowing.

[LLM] For borrower cash-flow masking, use [[PIK_Payment_In_Kind_Credit_Masking]] as the canonical detailed mechanism.

[LLM] For fund-level leverage from subscription lines and NAV loans, use [[Private_Credit_Subscription_Nav_Lending_Hidden_Leverage]] as the canonical instrument taxonomy.

[LLM] For the systemic bank feedback loop created by those facilities, use [[Bank_NBFI_Leverage_Loop]] rather than this umbrella node.

## Overlap Control

| Sub-mechanism | Canonical node | This node's role |
|---|---|---|
| PIK interest accrual | [[PIK_Payment_In_Kind_Credit_Masking]] | Route only |
| Subscription facilities | [[Private_Credit_Subscription_Nav_Lending_Hidden_Leverage]] | Route only |
| NAV lending | [[Private_Credit_Subscription_Nav_Lending_Hidden_Leverage]] | Route only |
| Bank/NBFI liquidity feedback | [[Bank_NBFI_Leverage_Loop]] | Context only |

[LLM] Do not expand this file with detailed mechanics unless the canonical nodes are later merged or archived.

