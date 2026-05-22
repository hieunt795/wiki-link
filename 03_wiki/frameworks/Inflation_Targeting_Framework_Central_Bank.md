---
node_id: inflation_targeting_001
type: framework
title: Inflation Targeting Framework (ITF) and Post-GFC Policy Mix
aliases:
  - ITF
  - inflation targeting
  - flexible inflation targeting
  - FIT
  - Inflation Targeting Framework
  - khung mục tiêu lạm phát
  - chính sách tiền tệ mục tiêu lạm phát

domain:
  primary: monetary_policy
  secondary: [macro_outlook]
tags: [inflation-targeting, central-bank, ITF, monetary-framework, macroprudential, policy-mix, EME]

confidence: 3
stability: stable

thesis: >
  The Inflation Targeting Framework (ITF), pioneered by New Zealand (1988), achieved price stability
  through four pillars: a published inflation target, interest-rate consistency (Taylor rule), CB
  independence, and transparency. While successful pre-GFC, the framework proved insufficient alone —
  the post-GFC paradigm adds macroprudential policy, FX market intervention, and capital flow
  management to achieve the dual mandate of price stability AND financial system stability.

source_refs:
  - path: 02_sources/books/central_policy_Perry/Perry Warjiyo and Solikin M. Juhro - Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-2.md
    pages: "Ch.2, Ch.6, Ch.8"
    weight: primary
  - path: 02_sources/books/central_policy_Perry/Perry Warjiyo and Solikin M. Juhro - Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-1.md
    pages: "Table of contents, overview"
    weight: supporting

related:
  - node: "[[Monetary_Policy_Instruments_Operational_Framework]]"
    relation: complements
  - node: "[[Interest_Rate_Corridor_Floor_System_Standing_Facilities]]"
    relation: implemented_via
  - node: "[[Central_Bank_Balance_Sheet_Structure_Liabilities_Assets]]"
    relation: uses

date_created: 2026-05-20
date_updated: 2026-05-20
---

## ITF Core Pillars

| Pillar | Description | Gold Standard Analogy |
|--------|-------------|----------------------|
| Published inflation target | Anchors expectations; central bank commits publicly to inflation level | Currency convertibility to gold |
| Policy consistency | Interest rate set via Taylor rule to hit inflation target 2yr ahead | Monetary targeting tied to gold reserves |
| CB independence | Policy tool (rate) controlled by CB, not government | CB mandate to maintain convertibility |
| Transparency & communication | Inflation projections, minutes, forward guidance published | Price expectations anchored by gold price |

**Taylor rule (simplified):**
```
i = r* + π* + α(π - π*) + β(y - y*)
  i = nominal policy rate
  r* = neutral real rate
  π = current inflation, π* = target
  y - y* = output gap
  α, β = response coefficients (typically α > 1 — Taylor principle)
```

## Historical Evolution

**Pre-GFC success (1988-2007):** ITF reduced inflation volatility sharply across advanced economies and many EMEs. The "Great Moderation" — two decades of low inflation, low rates, robust growth — appeared to validate the framework.

**GFC failure mode:** Price stability + low rates → financial boom → excessive credit growth → asset bubbles → systemic risk. "There is no macrostability without financial stability." ITF did not address financial cycle procyclicality.

**Post-GFC paradigm shift:** Central banks returned to dual mandate: price stability AND financial system stability. [LLM] Bank Indonesia (BI) is cited as a pioneer of this integrated approach since 2010.

## Post-GFC Policy Mix (New Paradigm)

```
Central Bank Policy Mix:
  ┌─────────────────────────────────────────────────┐
  │ MONETARY POLICY                                  │
  │   Interest rate (Taylor rule or forecast-based)  │
  │   + Capital flow management (EME context)        │
  ├─────────────────────────────────────────────────┤
  │ MACROPRUDENTIAL POLICY                           │
  │   LTV ratios, CCyB, G-SIB buffers               │
  │   Lean against financial cycle procyclicality    │
  ├─────────────────────────────────────────────────┤
  │ FX INTERVENTION                                  │
  │   Exchange rate stabilization (non-targeting)    │
  │   Two instruments for two targets                │
  ├─────────────────────────────────────────────────┤
  │ PAYMENT SYSTEM POLICY                            │
  │   Digital/electronic payment regulation          │
  └─────────────────────────────────────────────────┘
```

## EME-Specific Challenges

Emerging market central banks face an additional "policy trilemma":
- Monetary policy independence (price stability)
- Exchange rate stability (external sector)
- Free capital flow mobility

Cannot achieve all three simultaneously. EME central banks typically sacrifice full capital mobility via capital flow management, while using both interest rates AND FX intervention to achieve dual price+exchange rate stability.

## ITF Variants

| Regime | Description | Examples |
|--------|-------------|---------|
| Rigid ITF | Strict inflation target, minimal discretion | New Zealand (early) |
| Flexible ITF (FIT) | Inflation target + weight on output gap | UK, Canada |
| Dual mandate | Inflation + maximum employment | US Federal Reserve |
| Integrated ITF | Inflation + FX + macroprudential (policy mix) | Bank Indonesia, Korea |

## Policy Credibility — Time Inconsistency

Kydland-Prescott / Barro-Gordon: central banks have incentive to inflate ex-post (to boost output) even after committing to price stability. Solution: rules-based framework (ITF + Taylor rule) over pure discretion. CB independence removes government's ability to exploit this temptation.

Rogoff model: delegate monetary policy to a "conservative" (inflation-averse) independent CB to achieve lower equilibrium inflation than a politically motivated government would.
