---
node_id: nmd_stochastic_three_factor_model_001
type: mechanism
title: NMD Stochastic Three-Factor Model
aliases:
- NMD stochastic model
- three-factor deposit model
- Vasicek deposit volume model
- NMD Cholesky Monte Carlo
- mô hình ba nhân tố ngẫu nhiên tiền gửi NMD
- Monte Carlo tiền gửi không kỳ hạn
- rủi ro nén biên lãi suất tiền gửi
domain:
  primary: alm
  secondary: []
tags:
- node: '[[NMD]]'
  relation: related_to
- stochastic-model
- node: '[[Vasicek]]'
  relation: related_to
- credit-spread
- Monte-Carlo
- node: '[[Cholesky]]'
  relation: related_to
- margin-compression
- floor-risk
- replicating-portfolio
- node: '[[IRRBB]]'
  relation: related_to
confidence: 1
stability: stable
thesis: 'The Bohn stochastic three-factor NMD model drives deposit value via correlated
  Vasicek short rate, mean-reverting credit spread, and lognormal deposit volume processes;
  a Cholesky decomposition captures their correlations; and the risk appetite confidence
  level φ defines the replicating portfolio as the interest-rate hedge that covers
  deposit funding costs at the φ-percentile, with margin compression risk requiring
  raised hedge ratios before rates fall through the client-rate floor. [LLM]

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'Chapter 6: Non-Maturity Deposits — A Stochastic Model Approach (Bohn)'
parent_node: null
related:
- node: '[[NMD_Decay_Model_Volume_Segmentation]]'
  relation: related_to
- node: '[[ALM_Low_Negative_Interest_Rate_Environment]]'
  relation: related_to
- node: '[[IRRBB_Standardised_Versus_Internal_Model_Approach]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Thesis

The Bohn stochastic three-factor NMD model drives deposit value via correlated Vasicek short rate, mean-reverting credit spread, and lognormal deposit volume processes. [LLM] A Cholesky decomposition captures inter-factor correlations, and the risk appetite confidence level φ defines the replicating portfolio as the hedge covering deposit funding costs at the φ-percentile. [LLM] Margin compression risk requires raising hedge ratios before client rates breach the zero floor. [LLM]

## Three Stochastic Factors

The model state is driven by three correlated stochastic processes: [LLM]

### Factor 1: Short Rate — Vasicek Process

> **dr(t) = κᵣ(θᵣ − r(t)) dt + σᵣ dWᵣ(t)** [LLM]

- κᵣ: mean-reversion speed for interest rates [LLM]
- θᵣ: long-run mean rate level [LLM]
- σᵣ: interest rate volatility [LLM]
- The Vasicek process allows negative rates, which is relevant for EUR environments. [LLM]

### Factor 2: Credit Spread — Mean-Reverting Process

> **dc(t) = κ_c(θ_c − c(t)) dt + σ_c dW_c(t)** [LLM]

- The credit spread represents the bank's funding cost above risk-free; it affects the net margin earned on deposit funding. [LLM]
- Mean-reversion reflects the empirical tendency of credit spreads to normalize after stress. [LLM]

### Factor 3: Deposit Volume — Lognormal Process

> **dD(t) = μ_D D(t) dt + σ_D D(t) dW_D(t)** [LLM]

- D(t) is the total deposit volume; lognormal ensures non-negativity. [LLM]
- μ_D reflects trend growth; σ_D captures volume volatility driven by rate sensitivity and depositor behavior. [LLM]
- Volume is negatively correlated with interest rates in rate-sensitive segments (higher rates → outflows to alternatives). [LLM]

## Correlation Structure — Cholesky Decomposition

The three Brownian motions (Wᵣ, W_c, W_D) are correlated through a 3×3 correlation matrix Σ: [LLM]

> **Σ = [[1, ρ_{rc}, ρ_{rD}], [ρ_{rc}, 1, ρ_{cD}], [ρ_{rD}, ρ_{cD}, 1]]** [LLM]

Cholesky decomposition of Σ gives lower triangular matrix L such that LL^T = Σ. [LLM] Correlated Brownian increments are generated as: [LLM]

> **dW = L × dZ**, where dZ are independent standard normal increments. [LLM]

Typical sign conventions: [LLM]
- ρ_{rD} < 0: higher rates → lower volume (rate-sensitive outflow). [LLM]
- ρ_{rc} > 0: higher rates often coincide with wider credit spreads in stress. [LLM]
- ρ_{cD} < 0: wider credit spreads (bank stress) → deposit outflows. [LLM]

## Risk Appetite Confidence Level φ and the Replicating Portfolio

The model generates a Monte Carlo distribution of future deposit volumes and funding costs. [LLM] The risk appetite parameter φ (e.g., φ = 0.1%, representing the worst 1-in-1000 outcome) defines the **φ-quantile line** of deposit volume: [LLM]

- At each future time point, the φ-percentile of simulated deposit volumes gives a conservative lower bound on stable funding. [LLM]
- The **replicating portfolio** is the fixed-income portfolio (mix of 1Y, 2Y, …, nY bonds) whose maturity profile matches the expected duration of the φ-line. [LLM]
- Only the volume at or below the φ-line is invested in the replicating portfolio; the residual "volatile" volume is kept at overnight rates. [LLM]

The confidence level φ is a board-approved risk appetite parameter: lower φ → longer replicating portfolio maturity → higher NII in normal rates → higher EVE risk in rate up shocks. [LLM]

## Margin Compression Risk

Margin compression occurs when market rates fall toward the client rate floor (typically 0% for retail deposits): [LLM]

- If market rates = 2% and client rates = 1%, the deposit margin = 100bp. [LLM]
- If market rates fall to 0.5%, client rates cannot go below 0%, so the bank earns only 50bp margin. [LLM]
- Below zero market rates, the bank may be unable to pass negative rates to retail depositors, resulting in a negative net carry on the deposit portfolio. [LLM]

**Risk management implication:** [LLM]

- As rates approach zero, the PV01 of the deposit position increases nonlinearly because the floor option becomes increasingly in-the-money. [LLM]
- Static hedge ratios (set at higher rate levels) will underhedge the rate risk near the floor. [LLM]
- **Hedge ratios must be raised before rates reach the floor**, anticipating the nonlinear increase in duration. [LLM]
- Monte Carlo simulation with floor optionality is required to quantify this convexity risk; closed-form gap analysis will underestimate it. [LLM]

## Relation to the Replicating Portfolio

The stochastic model outputs feed into the replicating portfolio construction (the topic of a separate existing wiki node). [LLM] The three-factor model provides the probabilistic distribution of deposit duration at each confidence level; the replicating portfolio implements the interest-rate hedge implied by that distribution. [LLM]

---
*Source: Chapter 6 of Elkenbracht-Huizing, "The Handbook of ALM in Banking" (2nd ed., Risk Books 2017). All body sentences tagged [LLM] are synthesized from source material. Confidence: 1.*
