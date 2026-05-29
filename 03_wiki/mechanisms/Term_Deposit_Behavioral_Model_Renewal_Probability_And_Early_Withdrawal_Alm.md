---
node_id: term_deposit_behavioral_model_renewal_probability_and_early_withdrawal_alm_001
type: mechanism
title: Term Deposit Behavioral Model — Renewal Probability And Early Withdrawal ALM
aliases:
- term deposit renewal model
- early withdrawal probability model
- behavioral term deposit ALM
- mô hình hành vi tiền gửi có kỳ hạn
- renewal rate deposit model
- early redemption ALM
- xác suất tái tục tiền gửi
domain:
  primary: alm
tags:
- alm
- behavioral_model
- term_deposit
- renewal_probability
- early_withdrawal
- irrbb
- liquidity_risk
- ftp
- nmd
confidence: 1
stability: evolving
thesis: '[LLM] Term deposit behavioral modeling in ALM estimates two key probabilities:
  (1) renewal probability — the fraction of term deposits that roll over at contractual
  maturity rather than being withdrawn, and (2) early withdrawal probability — the
  fraction that exits before maturity. These probabilities are estimated from historical
  bank data using statistical models and allow ALM to construct a behavioral maturity
  profile that differs from the contractual maturity ladder, improving IRRBB measurement
  accuracy and FTP rate assignment. The PwC framework for ABBank (BC030304) defines
  model parameters, governance procedures, and validation requirements for these behavioral
  assumptions.'
source_refs:
- path: 02_sources/regulator/other/BC030304_Term_Deposit_HDSD_arm_FINAL (1).md
  pages: ''
  weight: primary
parent_node: null
related:
- node: '[[Term_Deposit_Alm_Governance_Policy_Procedure_Limit_Framework]]'
  relation: governance_framework
- node: '[[Term_Deposit_Behavioral_Model_Ppl_Pts_Policy_Specification]]'
  relation: policy_spec
- node: '[[Term_Deposit_Behavioral_Model_Pts_Variant_Parameter_Specification]]'
  relation: parameter_spec
- node: '[[Behavioralization_Non_Maturity_Deposit_Alm_Prepayment_Early_Withdrawal_Modeling]]'
  relation: behavioral_methodology
date_created: '2026-05-26'
date_updated: '2026-05-26'
---

[LLM] Auto-generated stub from BC030304_Term_Deposit_HDSD_arm_FINAL (1).md. Review and expand.

