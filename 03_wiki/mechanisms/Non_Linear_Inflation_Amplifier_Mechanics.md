---
node_id: nonlinear_inflation_amplifiers_mec_001
type: mechanism
title: Non-Linear Inflation Amplifier Mechanics
aliases:
  - Structural vs Behavioral Amplifiers
  - Cơ chế khuếch đại lạm phát phi tuyến
  - Input-Output Cascade vs Second-Round Effects

domain:
  primary: monetary_policy
  secondary: [macro_outlook]
tags: [inflation, supply_chain, input_output, inflation_expectations, non_linear_dynamics]

confidence: 3
stability: stable

thesis: >
  Inflation propagation in response to supply shocks occurs through two distinct amplifiers: the structural amplifier (automatic input-output cascades through production networks) and the behavioral amplifier (changes in wage- and price-setting behavior driven by expectations). [LLM]

source_refs:
  - path: 02_sources/Inbox/Central Bank Commentary (April 2026)_ Fed, BoJ, and BoE..md
    pages: "Introduction, Taking the Colimit sections"
    weight: primary

related:
  - node: "[[Monetary_Policy_Transmission_Mechanisms_Framework]]"
    relation: extension_of
  - node: "[[Inflation_Targeting_Framework_Central_Bank]]"
    relation: constraint_on

date_created: 2026-05-22
date_updated: 2026-05-22
---

## The Structural Amplifier (Production Network Channel)
The structural amplifier is rooted in the input-output architecture of the global production system. It is triggered by the cascade of cost increases through multi-stage networks once buffer capacity (inventories, margins) is exhausted [RAW-CLIP].
- **Nature:** Automatic and conditional only on shock magnitude and persistence.
- **Mechanism:** Cost-push effects that bypass inflation expectations and wage-price spirals.
- **Indicators:** Sectoral producer price indices (PPI), delivery times, shipping rates, and specific input costs (e.g., fertilizer, petrochemicals) [RAW-CLIP].
- **Non-Linearity:** Threshold effects occur when specific sectors or countries exhaust their buffers, leading to a jump in global indices like the GSCPI [RAW-CLIP].

## The Behavioral Amplifier (Expectations Channel)
The behavioral amplifier is what central banks traditionally define as "second-round effects" [RAW-CLIP].
- **Nature:** Conditional on labor market tightness and the salience of inflation to agents.
- **Mechanism:** Changes in wage-setting and price-setting behavior that outlast the original shock.
- **Indicators:** Inflation expectations surveys, wage settlements, and firms' pricing intentions [RAW-CLIP].
- **Central Bank Bias:** Traditional frameworks (Fed, BoE, BoJ) prioritize this channel, often "looking through" supply shocks unless this behavioral anchor moves [RAW-CLIP].

## Policy Implications
The distinction is critical for policy timing:
1. **Timing Gap:** Waiting for behavioral indicators (wages/expectations) to move may miss the early "structural" phase of a cost shock [RAW-CLIP].
2. **Persistence:** If the production network is transmitting a cost shock through channels that compound rather than attenuate, the "look through" assumption of supply shocks may be incomplete [RAW-CLIP].
3. **Buffer Exhaustion:** Non-linear dynamics suggest that small geographic shocks (e.g., Strait of Hormuz) can propagate through the entire system if they push the network beyond its structural buffer capacity [RAW-CLIP].

