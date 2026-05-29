---
node_id: nmd_decay_model_volume_segmentation_001
type: mechanism
title: NMD Decay Model and Volume Segmentation
aliases:
- NMD decay model
- non-maturity deposit behavioralization
- deposit average life estimation
- deposit volume segmentation
- mô hình suy giảm tiền gửi không kỳ hạn
- phân khúc khối lượng tiền gửi NMD
- tuổi thọ trung bình tiền gửi
domain:
  primary: alm
  secondary: []
tags:
- node: '[[NMD]]'
  relation: related_to
- non-maturity-deposits
- decay-model
- behavioralization
- deposit-segmentation
- average-life
- logistic-regression
- node: '[[IRRBB]]'
  relation: related_to
- node: '[[ALM]]'
  relation: related_to
confidence: 1
stability: stable
thesis: 'Deposit decay modeling estimates the expected outflow rate of non-maturity
  deposits (NMDs) by defining "end of life" via logistic regression on threshold-breach
  variables, computing average life via midpoint or monthly granular techniques, and
  segmenting the portfolio to maximize cross-segment behavioral variance so that each
  segment can be independently modeled and replicated. [LLM]

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'Chapter 5: Non-Maturity Deposits — A Decay Model Approach (Soulellis)'
parent_node: null
related:
- node: '[[NMD_Stochastic_Three_Factor_Model]]'
  relation: related_to
- node: '[[IRRBB_Standardised_Versus_Internal_Model_Approach]]'
  relation: related_to
- node: '[[ALM_Low_Negative_Interest_Rate_Environment]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Thesis

Deposit decay modeling estimates the expected outflow rate of non-maturity deposits (NMDs) by defining "end of life" via logistic regression on threshold-breach variables, computing average life via midpoint or monthly granular techniques, and segmenting the portfolio to maximize cross-segment behavioral variance so that each segment can be independently modeled and replicated. [LLM]

## Four Philosophical Drivers of Deposit Behavior

Soulellis identifies four underlying motivations that drive depositor behavior and therefore determine deposit stability: [LLM]

1. **Rate of return** — depositors compare the bank's offered rate to available alternatives (money market funds, competing banks); rate-sensitive depositors exit when the spread narrows beyond a threshold. [LLM]
2. **Liquidity / access** — current accounts and savings accounts provide payment functionality; even rate-insensitive depositors may not shift because they need the operational utility. [LLM]
3. **Institutional safety** — depositor confidence in the bank's solvency; in stress scenarios this becomes the dominant behavioral driver (deposit flight). [LLM]
4. **Service level** — branch proximity, digital platform quality, relationship banking: these create switching costs that dampen deposit outflows. [LLM]

These four drivers map to different customer segments and must be quantified separately in a segmentation model. [LLM]

## Defining "End of Life" for a Deposit Cohort

The decay model requires a binary definition of when a deposit unit is considered "run off" (end of life). [LLM] The Soulellis approach uses **logistic regression** on threshold-breach variables: [LLM]

- Define a set of trigger variables: rate spread below threshold, account dormancy, balance below minimum, competitor rate above threshold. [LLM]
- Run logistic regression to estimate the probability of outflow conditional on the combination of trigger states. [LLM]
- The logistic function produces a probability-of-survival curve S(t) that declines monotonically from 1 at origination toward 0. [LLM]

This approach is preferable to simple exponential decay because it captures non-linearities in depositor response (e.g., threshold effects when rate differentials cross zero). [LLM]

## Average Life Calculation Methods

Two methods are used to convert the survival curve S(t) into a single average life number: [LLM]

### Midpoint Technique (Annual Buckets)

- Divide the deposit portfolio into annual cohorts. [LLM]
- For each annual bucket, the portion that runs off during year k has an average life of k − 0.5 years (midpoint of the bucket). [LLM]
- Average life = Σ (outflow_fraction_k × (k − 0.5)) for k = 1, 2, …, N. [LLM]
- Simple and widely used for regulatory reporting; loses within-year timing information. [LLM]

### Monthly Granular Method

- Use monthly survival curve estimates: S(1), S(2), …, S(M). [LLM]
- Outflow in month m = S(m−1) − S(m). [LLM]
- Average life = Σ (outflow_m × m / 12) for m = 1, …, M (expressed in years). [LLM]
- More precise; required when the replicating portfolio uses instruments with sub-annual maturities. [LLM]

## Segmentation Principle: Maximize Cross-Segment Variance

The portfolio is segmented so that behavior within each segment is homogeneous while behavior **between** segments is maximally different. [LLM] This ensures: [LLM]

- Each segment has a distinct average life and rate sensitivity, justifying separate modeling. [LLM]
- The aggregated model does not average out extreme behaviors (high-rate-sensitivity vs sticky depositors). [LLM]

Typical segmentation dimensions include: [LLM]

| Dimension | Rationale |
|-----------|-----------|
| Product type (current account, savings, call deposit) | Different liquidity / operational utility |
| Client segment (retail, SME, corporate) | Different sophistication and rate sensitivity |
| Balance tier (micro, small, large) | Large balances more rate-sensitive |
| Channel (branch, digital-only) | Digital depositors more mobile |
| Geographic / regulatory jurisdiction | Different deposit guarantee levels |

[LLM]

## Multivariate Rate Sensitivity Regression

Within each segment, the rate index (bank_rate / market_rate) is regressed on macro and market variables: [LLM]

> **rate_index(t) = α + β₁ × rate_index(t−1) + β₂ × Δbase_rate(t) + β₃ × unemployment(t) + β₄ × GDP_growth(t) + ε** [LLM]

Key modeling requirements: [LLM]
- **R² validation** — model must explain sufficient variance in historical rate pass-through. [LLM]
- **p-values** — each predictor must be statistically significant. [LLM]
- **Multicollinearity check** — Variance Inflation Factor (VIF) must remain below 5–10 for each predictor. [LLM]
- **Residual homoscedasticity** — residuals must not exhibit systematic patterns (no heteroscedasticity). [LLM]
- **Out-of-time test** — model is validated on a holdout period not used in estimation to confirm generalizability. [LLM]

## Regulatory Compliance Note

BCBS IRRBB Principle 6 requires that NMD behavioral assumptions be documented, justified, and regularly validated. [LLM] The decay model and segmentation approach satisfies P6 by providing an auditable, data-driven methodology that can be stress-tested and backtested. [LLM]

---
*Source: Chapter 5 of Elkenbracht-Huizing, "The Handbook of ALM in Banking" (2nd ed., Risk Books 2017). All body sentences tagged [LLM] are synthesized from source material. Confidence: 1.*
