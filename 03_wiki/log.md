# Wiki Operation Log

Chronological record of all ingest, update, promotion, and audit operations.

---

## 2026-05-25

- **WIKI NODE UPDATED** (IMF Macro Accounting — full balance sheet enrichment):
  - `03_wiki/frameworks/Imf_Monetary_Survey_And_Reserve_Money_Identity_Framework.md` — Added all three analytical balance sheets from source: (1) MA Balance Sheet (Box 5.2): full asset/liability breakdown — NFA (gold, FX, IMF reserve pos., SDRs, less short-term foreign liabilities, less use of IMF credit), NCG, Cb, CPS, OINm on assets; RM (CY, DMB cash in vault, DMB deposits at MA), govt deposits, foreign liabilities, capital+OINm on liabilities; identity: NFA+NCG+Cb+CPS+OINm = RM+Govt deposits+Foreign liabilities; (2) DMB Balance Sheet (Box 5.5): full line items — Reserves, Foreign Assets, Claims on Govt, Claims on NFPEs, CPS, Claims on NMFIs on assets; DD, QM (time/savings/FX deposits), money market instruments, bonds, restricted deposits, foreign liabilities, govt deposits, credit from MA, liabilities to NMFIs, capital accounts on liabilities; (3) Monetary Survey (Box 5.7) consolidated: NFA (MA+DMB net of interbank) + NCG (net of all govt deposits) + CPS + OINb = M2; M2 = M1 (CY+DD) + QM; M2=NFA+NDA shown; (4) M2 Growth Decomposition: ΔM2/M2 = Σ(Δcomponent/component × component/M2) with policy interpretation for isolating FX-driven vs. fiscal vs. private credit sources.

- **WIKI NODES UPDATED** (IMF Macro Accounting — Box 6.4 equations enrichment across 5 nodes):
  - `03_wiki/frameworks/Imf_Flow_Of_Funds_4_Sector_Consistency_Framework.md` — Added Box 6.4 complete formal system: all 8 sector accounting identities in zero-sum form (Eqs. 1–8), cross-sector consistency check, variable definitions, accounting-vs-behavioral limitation caveat
  - `03_wiki/frameworks/Imf_Sna_Real_Sector_Accounting_Gdp_Identities_And_Sectoral_Accounts.md` — Added Eq. 1 formal GNDI zero-sum identity (−GNDI + C + I + X − M + Yt + TRt = 0) and sectoral decomposition (Sp−Ip) + (Sg−Ig) = CAB with explicit variable definitions
  - `03_wiki/frameworks/Imf_Balance_Of_Payments_Framework_And_External_Account_Analysis.md` — Added Eq. 7–8 BOP identity in zero-sum form (−CAB − FDI − NFB + ΔNFA + ΔOINt = 0), sign convention explanation, link to valuation adjustment node
  - `03_wiki/frameworks/Imf_Gfs_Fiscal_Accounting_Framework_Deficit_Measurement_And_Sustainability.md` — Added Eq. 2–3 fiscal sector identities: Sg−Ig = GNDIg−Cg−Ig and financing constraint (Sg−Ig) + NFBg + ΔNDCg + NB = 0 with link to crisis vector modes
  - `03_wiki/frameworks/Imf_Monetary_Survey_And_Reserve_Money_Identity_Framework.md` — Added Eq. 6 monetary survey identity in zero-sum form (ΔM2 − ΔNFA − ΔNDC − ΔOINb = 0) with flow direction interpretation and NDA ceiling derivation
  - `03_wiki/frameworks/Imf_Monetary_Analysis_Quantity_Theory_Velocity_And_Exchange_Rate_Regimes.md` — Added Eq. 4–5 private sector identities: Sp−Ip = GNDIp−Cp−Ip and financing constraint (FDIp + NFBp + ΔNDCp − ΔM2 − NB = 0) with sign convention interpretation and M2 link

- **WIKI NODE CREATED** (IMF Macro Accounting — crisis vector mechanisms research):
  - `03_wiki/frameworks/Imf_Macro_Crisis_Vector_Framework.md` — Confidence 4: synthesizes all crisis transmission mechanisms from IMF Macro Accounting Chs. 3-5; 3 crisis vectors mapped: (1) Fiscal — 4 modes of deficit financing → 4 crisis outcomes (inflation/exchange rate crisis/explosive debt/crowding out) with balance sheet effects per mode; (2) External — speculative attack under fixed peg (Krugman 1979 expectations mechanism, attack before reserves exhausted), current account sustainability/solvency condition (PV(future surpluses) ≥ external debt), Lawson doctrine critique (contamination spillover, real exchange rate reversal risk), financial vulnerability reserve adequacy indicators (M2/FX ratio Calvo 1996, short-term FX liabilities, monetary base threshold, capital account openness), credibility as reserve amplifier (Poland 1991 vs. Mexico 1994); (3) Banking — fractional reserve maturity mismatch → illiquidity → contagion → systemwide confidence freeze → CB LOLR (isolate + guarantee + systemwide liquidity) → balance sheet: Cb↑ → RM↑ + quasi-fiscal recapitalization risk; cross-sector amplification matrix; diagnostic section for all 4 fiscal financing modes + banking + external vectors.

- **WIKI NODE CREATED** (IMF Macro Accounting Ch.5 — deep research session, Box 5.8):
  - `03_wiki/mechanisms/Imf_Monetary_Survey_Valuation_Adjustment_Transaction_Flow_Decomposition.md` — Confidence 4: formal decomposition of monetary survey stock changes into (1) transaction flows (converted at average exchange rate) and (2) valuation adjustments from exchange rate movements; VAj formula and treatment in OIN(net); ΔNFA vs. ΔRES reconciliation methodology; policy application — NDA ceiling calculations must use transaction-only ΔNFA; diagnostic section for analyst use.

- **WIKI NODE UPDATED** (IMF Macro Accounting Ch.5 — confidence upgrade):
  - `03_wiki/mechanisms/Imf_Money_Multiplier_Ratio_Decomposition_Three_Agent.md` — Confidence raised 3→4: core simple mm=(1+c)/(c+r) and extended mm=(1+c+b)/(c+rd+rt·b+re·(1+b)) formulas directly verified from source lines 4708–4754; three-agent framework (MA/banks/public) verified from source lines 4756–4758; [LLM] markers retained only on GFC contextual example and seigniorage section.

- **WIKI NODE UPDATED** (IMF Macro Accounting Ch.6 — enriched with analytical uses):
  - `03_wiki/frameworks/Imf_Flow_Of_Funds_4_Sector_Consistency_Framework.md` — Added external imbalance analysis (CAD origin tracing: private vs. government sector); fiscal imbalance transmission analysis (tax increase vs. CB monetization channels); detailed Table 6.1 column and row structure explanation; banking sector column identity restating ΔM2 = ΔNFA + ΔNDC + ΔOINb.

- **WIKI NODES CREATED** (IMF Macro Accounting — remaining coverage gaps):
  - `03_wiki/mechanisms/Imf_Real_Interest_Rate_Fisher_Equation_And_Portfolio_Choice.md` — Confidence 4: 4 asset types (money/bonds/equities/real assets) with return-risk-liquidity tradeoffs; rate of return = income + capital gain; Fisher equation (Rr ≈ Rn − Pᵉ approximate; exact discrete form for high inflation); negative real rates in transition → asset substitution → dollarization mechanism; diagnostic (calculate Rr → portfolio substitution signal)
  - `03_wiki/mechanisms/Incomes_Policy_Wage_Controls_Stabilization_Programs.md` — Confidence 4: 3 motivations (inertial inflation / SOE decapitalization / exchange rate credibility); 3 institutional approaches (guidelines / social contract / TIP); 4-step design (norm selection / indexation / coverage / enforcement); wage bill vs. average wage norm tradeoffs; partial forward-looking indexation; Poland popiwek EWT rates (100%–500% progressive, reduced to 300% 1993); private sector coverage exemption; temporary effectiveness profile
  - `03_wiki/frameworks/Labor_Market_Unemployment_Taxonomy_And_NAIRU.md` — Confidence 4: 5 unemployment types (seasonal / frictional / cyclical / structural / disguised); NAIRU definition and its policy implication (cannot reduce unemployment below NAIRU without inflation); discouraged worker effect; labor force participation rate distortions; disguised unemployment dominant form in SOE-heavy transition economies; NAIRU shifts from structural rigidities

---


  - `03_wiki/mechanisms/Imf_Real_Interest_Rate_Fisher_Equation_And_Portfolio_Choice.md` — Confidence 4: 4 asset types (money/bonds/equities/real assets) with return-risk-liquidity tradeoffs; rate of return = income + capital gain; Fisher equation (Rr ≈ Rn − Pᵉ approximate; exact discrete form for high inflation); negative real rates in transition → asset substitution → dollarization mechanism; diagnostic (calculate Rr → portfolio substitution signal)
  - `03_wiki/mechanisms/Incomes_Policy_Wage_Controls_Stabilization_Programs.md` — Confidence 4: 3 motivations (inertial inflation / SOE decapitalization / exchange rate credibility); 3 institutional approaches (guidelines / social contract / TIP); 4-step design (norm selection / indexation / coverage / enforcement); wage bill vs. average wage norm tradeoffs; partial forward-looking indexation; Poland popiwek EWT rates (100%–500% progressive, reduced to 300% 1993); private sector coverage exemption; temporary effectiveness profile
  - `03_wiki/frameworks/Labor_Market_Unemployment_Taxonomy_And_NAIRU.md` — Confidence 4: 5 unemployment types (seasonal / frictional / cyclical / structural / disguised); NAIRU definition and its policy implication (cannot reduce unemployment below NAIRU without inflation); discouraged worker effect; labor force participation rate distortions; disguised unemployment dominant form in SOE-heavy transition economies; NAIRU shifts from structural rigidities

---

## 2026-05-24

- **2026-05-24**: INGEST: Created mechanism node `TGA Volatility And Reserve Buffer Demand` from The Checking Account of the U.S. Federal Government....md
- **2026-05-24**: INGEST: Created framework node `Fed Treasury Operational Choice Space` from The Checking Account of the U.S. Federal Government....md
- **2026-05-24**: INGEST: Created contradiction node `Warsh Balance Sheet Stimulus Swap Vs Structural Demand Neutrality` from Warsh and the Fed's Balance Sheet.md
- **2026-05-24**: INGEST: Created synthesis node `US Macro Constraint Stack Fed Treasury Curve Inflation External Sector` from Lipschitz_Schadler_Macroeconomics.md
- **2026-05-24**: INGEST: Created framework node `Warsh Fed Balance Sheet Operating Doctrine` from Warsh and the Fed's Balance Sheet.md
- **2026-05-24**: INGEST: Created framework node `Warsh Maturity Sovereignty Framework` from A new Fed-Treasury Accord_.md
- **2026-05-24**: INGEST: Created framework node `Warsh Credit Allocation Exit Framework` from A new Fed-Treasury Accord_.md
- **2026-05-24**: INGEST: Created mechanism node `Warsh Reserve Floor And Structural Demand Constraint` from Warsh and the Fed's Balance Sheet.md

- **WIKI EXPANSION**: 10 Core Federal Reserve Nodes Upgraded
  - Topic: Federal Reserve Operational Framework, Liquidity Facilities, and Balance Sheet Mechanics
  - Nodes expanded: `Fed_Ample_Reserves_Rate_Control_Framework`, `Fed_Balance_Sheet_Size_And_Policy_Rate_Independence`, `Fed_Overnight_Reverse_Repo_ON_RRP`, `Fedwire_Payment_System_Reserve_Demand_And_Lsm_Policy`, `Standing_Repo_Facility_SRF_Fed_Backstop`, `Tga_Reserve_Swap_Mechanics_And_Debt_Ceiling_Dynamics`, `Fed_Fiscal_Agent_Treasury_Relationship`, `Fed_Dollar_Swap_Lines_Crisis_Hierarchy_and_Swapper_of_Last_Resort`, `Fed_RMO_Reserve_Management_Operations_Post_QT_Mechanics`, `Fed_Global_Jaws_FRP_FIMA_Public_Dollar_Architecture`.
  - Quality: All nodes promoted to Confidence 4; mechanistic depth added with A->B->C causal chains and verified source citations (Duffie 2026, Conks, ECB/Fed Primer).
  - Status: Metadata synchronized across `index.md`, `log.md`, and `_source_registry.yaml`.

- **REPORT PUBLISHED**: `05_reports/2026-05/us_treasury_curve_2026.md`
  - Topic: US Treasury Yield Curve 2026 — Bear Steepener, Term Premium Regime, RV Implications
  - Mode: T_MODE_DEEP → Research Memo style
  - Source basis: 7 wiki nodes + 7 fresh web fetches (Treasury H.15, FRED TIPS/5y5y, NY Fed ACM, TBAC May 2026, Japan WolfStreet, Ferrante Capital)
  - Audit: 2 blocking fails resolved (C1: RV section added; E1: `---` count reduced to 3); 0 warnings
  - Key findings: 2y=4.13%, 10y=4.56%, 30y=5.07%; ACM term premium 0.68% (Apr); 10y breakeven 2.48%; 5y5y 2.29%; bear steepener driven by fiscal supply ($1.9T deficit) + Fed duration withdrawal + Japan selling ($29.6B Q1); 4 RV trade ideas
  - Connected to: `04_research/fed_framework_2026/` and `05_reports/2026-05/fed_operating_framework_2026.md`

- **RESEARCH WORKSPACE**: `04_research/us_treasury_curve_2026/` created
  - 3 findings files, 1 T_MODE_DEEP draft, 1 approved audit_log.json, 1 data snapshot
  - 5 TRUE_GAPs logged: intermediate yields, ACM May update, Japan demand elasticity, FY2027-28 supply impact, r* level

- **REPORT PUBLISHED**: `05_reports/2026-05/fed_operating_framework_2026.md`
  - Topic: Fed Operating Framework 2026 — Rate Path, QT Halt, Balance Sheet, Reserve Adequacy
  - Mode: T_MODE_DEEP → Research Memo style
  - Source basis: 8 wiki nodes + Duffie BPEA 2026 + 5 fresh web fetches (Fed H.4.1, FOMC Minutes, SEP)
  - Audit: 3 blocking fails resolved; B3 counter-argument added (FHLB/FBO segmentation); T3 warning accepted
  - Key findings: QT halted Dec 2025 ($2.2T total); RMPs $10B/month; reserves $3.13T near LCLoR floor; rate hold 3.5–3.75% on tariff-driven inflation

- **RESEARCH WORKSPACE**: `04_research/fed_framework_2026/` created
  - 3 findings files, 1 T_MODE_DEEP draft, 1 approved audit_log.json
  - 3 TRUE_GAPs logged: SRF usage data, reserve demand elasticity update, Fedwire payment delay index
  - 1 PENDING gap: May 2026 FOMC decision

- **WIKI NODE CREATED**: `03_wiki/mechanisms/CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization.md`
  - Confidence: 4 | Stability: stable
  - T_MODE_DEEP construction: read Lipschitz & Schadler lines 2241–2858 (Box 4.7, Table 4.8, Bulgaria case), IMF Macro Accounting lines 3699–3749 (sterilization, reserve adequacy), Perry Warjiyo lines 212–295 (dual instruments, FIT)
  - Thesis: NFA endogeneity under FX target → CB retains only NDA; sterilization faces reserve depletion (Case A) and quasi-fiscal carrying cost (Case B)
  - Content: T-account mechanics (2 directions), 4-factor sterilization decision matrix, regime comparison (5 regimes), Greenspan-Guidotti rule, Mundell-Fleming ineffectiveness, dual-instrument EME resolution, HEALTHY/STRESS/CRISIS diagnostic pattern

- **WIKI NODES CREATED** (FX rate target deep dive — IMF Macro Accounting source):
  - `03_wiki/mechanisms/Imf_Exchange_Rate_Assessment_And_Crawling_Peg_Design.md` — Confidence 4: Box 4.8 (4-indicator ER assessment), active vs passive crawl design, rate-of-crawl determination, band widening as managed float transition, Poland 1990–1995 case study
  - `03_wiki/frameworks/Imf_Financial_Programming_NDA_Ceiling_And_BOP_Monetary_Approach.md` — Confidence 4: Monetary approach to BOP (excess NDA → NFA loss, one-for-one), NDA ceiling conditionality logic, controllability hierarchy (Cb > NCG > NFA), three monetary survey sector links, indirect monetization mechanism despite legal prohibition

- **WIKI NODES CREATED** (IMF Macro Accounting — Chapter 2 inflation + Chapter 3 tax analysis):
  - `03_wiki/frameworks/Imf_Inflation_Analysis_Cpi_Gdp_Deflator_Four_Types_Core.md` — Confidence 4: 4 inflation types (policy-induced, cost-push, demand-pull, inertial), CPI vs GDP deflator (3 differences: coverage/imports/Laspeyres-Paasche), core vs underlying inflation, NAIRU taxonomy (5 unemployment types), Japan non-accommodation example, inflation diagnostic
  - `03_wiki/frameworks/Imf_Tax_Revenue_Analysis_Elasticity_Buoyancy_Effort_Tanzi.md` — Confidence 4: tax elasticity (unchanged system) vs buoyancy (including discretionary), taxable capacity definition, tax effort = actual/capacity ratio, 3 structural determinants of taxable capacity (openness/income/composition), Tanzi 8-criterion revenue productivity diagnostic test (concentration, dispersion, erosion, collection lags, specificity, objectivity, enforcement, cost), Tanzi effect (inflation–collection lag cycle)

- **WIKI NODE CREATED**: `03_wiki/mechanisms/CB_Quasi_Fiscal_Sterilization_Seigniorage_Fiscal_Monetary_Nexus.md`
  - Confidence: 4 | Stability: stable | T_MODE_DEEP
  - Source basis: Lipschitz & Schadler (Box 4.1, Box 4.6, p.2720-2763, p.2948-2969), IMF Macro Accounting (Box 3.7, GFS CB profit treatment, sterilization exercise), Perry Warjiyo Ch.11 (fiscal-monetary coordination, CB independence under crisis)
  - Thesis: FX target creates 4-channel quasi-fiscal nexus: (1) normal seigniorage transfer (CB profit → Treasury); (2) sterilization inverts this (negative carry → calls on government); (3) NCG expansion = covert monetization; (4) CB recapitalization = deferred fiscal cost
  - Content: IMF QFO taxonomy (3 types), fiscal dominance causal sequence, policy interaction matrix (5 cases), 4-signal diagnostic pattern, true fiscal stance formula

- **RESEARCH WORKSPACE**: `04_research/vietnam_imf_macro_2026/` created
  - Topic: Vietnam macro accounts under IMF accounting framework (SNA + GFS + BOP + Monetary Survey)
  - Key findings: Private surplus +7.6% GDP, Govt deficit -1.5%, CA +6.1% GDP [2024 identity ✓]; Credit/GDP 134%; FX reserves 2.4 months (below IMF adequacy); SBV sold $9.3bn FX 2024
  - 4 TRUE_GAPs: SBV balance sheet detail, fiscal financing breakdown, FX exposure matrix, quasi-fiscal scale
  - Status: in_progress

---

## 2026-05-20

- **INIT**: Wiki structure created. Directories established. Schema files written.
  - 01_schema/: frontmatter.md, node_types.md, confidence_scale.md, vi_en_dictionary.yml
  - 03_wiki/: index.md, log.md, _metadata/ initialized
  - 04_research/: _template/ scaffold created
  - 06_templates/: core and domain templates written
  - CLAUDE.md: root operating manual written
  - Status: 0 wiki nodes. 293 sources awaiting ingest.

---

*New entries are appended above this line by `librarian.py ingest` and `librarian.py sync`.*

- **2026-05-21**: INGEST: Updated mechanism `Treasury General Account TGA Reserve Swap` from TGA Clipping (Armenter 2026)
- **2026-05-21**: INGEST: Created framework node `Fed Fiscal Agent Treasury Relationship` from TGA Clipping (Armenter 2026)
- **2026-05-20**: INGEST: Created concept node `Warsh Balance Sheet Stimulus Swap` from Warsh and the Fed's Balance Sheet.md
- **2026-05-20**: INGEST: Created framework node `Fed Treasury Accord 2026 Proposal` from A new Fed-Treasury Accord_.md
- **2026-05-20**: INGEST: Created framework node `ECB New Operational Framework 2024` from ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
- **2026-05-20**: INGEST: Created framework node `Fed Ample Reserves Range Floor Framework` from ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
- **2026-05-20**: INGEST: Created mechanism node `Standing Repo Facility SRF Fed Backstop` from ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
- **2026-05-20**: INGEST: Created mechanism node `Monetary Policy Transmission Short Long Rate Frictions` from ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
- **2026-05-20**: INGEST: Created mechanism node `Treasury General Account TGA Reserve Swap` from Conks - Shadow Banking and Cash Markets.md
- **2026-05-20**: INGEST: Created mechanism node `Fed Overnight Reverse Repo ON RRP` from Conks - Shadow Banking and Cash Markets.md
- **2026-05-20**: INGEST: Created mechanism node `Quantitative Tightening QT Balance Sheet Runoff` from Conks - Fed's Policies and Facilities.md
- **2026-05-20**: INGEST: Created concept node `Shadow Banking Market Based Finance` from Conks - Shadow Banking and Cash Markets.md
- **2026-05-20**: INGEST: Created framework node `Global Dollar System Eurodollar Architecture` from Conks - Global Dollar and Eurodollar Systems.md
- **2026-05-20**: INGEST: Created mechanism node `Debt Ceiling Extraordinary Measures Treasury` from Conks - Shadow Banking and Cash Markets.md
- **2026-05-20**: INGEST: Created mechanism node `Repo Market Mechanics Triparty Bilateral` from Conk - Repo.md
- **2026-05-20**: INGEST: Created framework node `Monetary Policy Instruments Operational Framework` from Bindseil_Monetary_Policy_Operations.md
- **2026-05-20**: INGEST: Created mechanism node `Interest Rate Corridor Floor System Standing Facilities` from Bindseil_Monetary_Policy_Operations.md
- **2026-05-20**: INGEST: Created mechanism node `Central Bank Intermediation Balance Sheet Autonomous Factors` from Bindseil_Monetary_Policy_Operations.md
- **2026-05-20**: INGEST: Created mechanism node `Collateral Framework Haircuts Central Bank Credit` from Bindseil_Monetary_Policy_Operations.md
- **2026-05-20**: INGEST: Created mechanism node `SLR LCR Balance Sheet Constraints Treasury Market Dealer` from Conks - Liquidity and Market Dynamics.md
- **2026-05-20**: INGEST: Created framework node `Central Bank Balance Sheet Structure Liabilities Assets` from Central_Bank_Balance_Sheet.md
- **2026-05-20**: INGEST: Created mechanism node `Collateral Velocity Rehypothecation` from Singh_Collateral_Financial_Plumbing.md
- **2026-05-20**: INGEST: Created mechanism node `DV01 Duration Convexity Fixed Income` from Tuckman_Serrat_Fixed_Income_2022.md
- **2026-05-20**: INGEST: Created framework node `Inflation Targeting Framework Central Bank` from Perry Warjiyo Central Bank Policy.md
- **2026-05-20**: INGEST: Created mechanism node `Monetary Policy Transmission Collateral Channel` from Singh_Collateral_Financial_Plumbing.md
- **2026-05-20**: BUGFIX: Fixed _encode_all() in librarian.py — replaced broken add()/save() calls with DenseIndex.build(); added encode_batch mode to bge_m3_daemon.py; fixed os.kill() Windows incompatibility; fixed JSON serialization of numpy float32 sparse weights
- **2026-05-20**: SYNC: Running full index rebuild — 11722 docs (13 wiki nodes + 11709 raw chunks) encoding to FAISS + sparse + FTS5
- **2026-05-20**: INGEST: Created mechanism node `Interest Rate Swaps OIS Fixed Floating` from Tuckman_Serrat_Fixed_Income_2022.md Ch.13
- **2026-05-20**: INGEST: Created mechanism node `Reserve Floor Payment System Demand` from Duffie_BPEA_Payments_Liquidity_2026.md
- **2026-05-20**: INGEST: Created framework node `Monetary Policy Transmission Mechanisms Framework` from Perry Warjiyo trang-3.md Ch.5
- **2026-05-20**: INGEST: Created mechanism node `Swap Spreads Balance Sheet Plumbing Frictions` from Huggins_Schaller_Fixed_Income_RV.md Ch.17-18
- **2026-05-20**: INGEST: Created framework node `Basel III Endgame Capital Liquidity Credit Migration` from deep-research/Basel, Ngân hàng, Tín dụng Tư nhân.md
- **2026-05-20**: INGEST: Created mechanism node `Private Credit SRT NAV Loans Bank Partnerships` from deep-research/Basel, Ngân hàng, Tín dụng Tư nhân.md
- **2026-05-20**: REPORT: Published research memo `fed_qt_reserve_scarcity_memo` — Fed QT and Reserve Scarcity (audit approved, confidence floor 3, 5 wiki nodes used)
- **2026-05-20**: BUGFIX: Fixed bge_m3_daemon.py sync crash — removed DAEMON_ANCHOR_PID from _ensure_running() (daemon was dying when sync exited); reduced internal batch_size 12->4; added gc.collect() after encode_batch to prevent tensor OOM accumulation; reverted workaround batch_sizes in dense_index.py (4->16) and librarian.py (8->32)
- **2026-05-20**: PHASE5: Wired agentic + deep commands into librarian.py; wrote test suite 07_scripts/tests/test_phase5.py — 27 tests covering graph_rag, deepdive_search, agentic_search, CLI wiring, wiki node integrity; all 27 PASS
- **2026-05-22**: INGEST: Created mechanism node `QE Duration Extraction from Private Sector` from What about Japan_ (Part II).md
- **2026-05-22**: INGEST: Created mechanism node `Financial Repression via Reserve Creation` from What about Japan_ (Part II).md
- **2026-05-22**: INGEST: Created mechanism node `Japan FILP to QE Structural Succession` from What about Japan_ (Part I).md
- **2026-05-22**: INGEST: Created mechanism node `Financial Repression Distributional Welfare Effects` from What about Japan_ (Part II).md
- **2026-05-22**: INGEST: Created mechanism node `Ample Reserves Buffer Sizing TGA Volatility` from Napkin Math for an Ample Reserves Buffer.md
- **2026-05-22**: INGEST: Created mechanism node `Private Credit Secondary Market Price Discovery` from Deep Dive_ Private Credit.md
- **2026-05-22**: INGEST: Created mechanism node `Private Credit Subscription NAV Lending Hidden Leverage` from Deep Dive_ Private Credit.md
- **2026-05-22**: INGEST: Created mechanism node `Private Credit Insurer Structural Channel` from Deep Dive_ Private Credit.md
- **2026-05-22**: INGEST: Created mechanism node `FHLB EFFR IORB Arbitrage Floor Mechanism` from Conks - Plumping note (Money market.md
- **2026-05-22**: INGEST: Created mechanism node `Fed Policy Rate Shift EFFR to Secured Rate TGCR` from Conks - Plumping note (Money market.md
- **2026-05-22**: INGEST: Created framework node `Duration Targeting Bond Portfolio Framework` from Homer_Leibowitz_Inside_The_Yield_Book.md
- **2026-05-22**: INGEST: Created mechanism node `Duration Targeting Convergence And Yield Trap` from Homer_Leibowitz_Inside_The_Yield_Book.md
- **2026-05-22**: INGEST: Created mechanism node `Bond Accrual Price Effect Interaction` from Homer_Leibowitz_Inside_The_Yield_Book.md
- **2026-05-22**: INGEST: Created framework node `IRRBB EVE NII Dual Metric Framework` from Elkenbracht_Huizing_Handbook_ALM.md
- **2026-05-22**: INGEST: Created mechanism node `Non Maturity Deposit Fair Margin And Replicating Portfolio` from Elkenbracht_Huizing_Handbook_ALM.md
- **2026-05-22**: INGEST: Created mechanism node `Swap Carry And Roll Down Analysis` from Howard_Corb_Interest_Rate_Swaps.md
- **2026-05-22**: INGEST: Created mechanism node `Asset Swap Mechanics And Spread` from Howard_Corb_Interest_Rate_Swaps.md
- **2026-05-22**: INGEST: Created mechanisms node `Fed Ample Reserves Rate Control Framework` from Conks - Fed's Policies and Facilities.md
- **2026-05-22**: INGEST: Created mechanisms node `Triparty Repo Market Structure And Daily Cycle` from Conk - Repo.md
- **2026-05-22**: INGEST: Created mechanisms node `Eurodollar System Mechanics And Post-Reform Decline` from Conks - Global Dollar and Eurodollar Systems.md
- **2026-05-22**: INGEST: Created mechanisms node `QT Reserve Drain Effectiveness And Deposit Funding Condition` from Conks - Fed's Policies and Facilities.md
- **2026-05-22**: INGEST: Created mechanisms node `TGA Reserve Swap Mechanics And Debt Ceiling Dynamics` from Conks - Liquidity and Market Dynamics.md
- **2026-05-22**: INGEST: Created mechanisms node `US Shadow Banking Post-GFC Market Based Finance Structure` from Conks - Shadow Banking and Cash Markets.md
- **2026-05-22**: INGEST: Created frameworks node `Basel III Capital And Liquidity Constraint Mechanics` from Basel, Ngân hàng, Tín dụng Tư nhân.md
- **2026-05-22**: INGEST: Created mechanisms node `Fedwire Payment System Reserve Demand And LSM Policy` from Duffie_BPEA_Payments_Liquidity_2026.md
- **2026-05-22**: INGEST: Created mechanisms node `Basel Driven Credit Migration To Private Markets` from Basel, Ngân hàng, Tín dụng Tư nhân.md
- **2026-05-22**: INGEST: Created mechanisms node `Collateral Velocity And Pledged Collateral Market Mechanics` from Singh_Collateral_Financial_Plumbing.md
- **2026-05-22**: INGEST: Created frameworks node `Central Bank Monetary Policy Operational Framework Typology` from Bindseil_Monetary_Policy_Operations.md
- **2026-05-22**: INGEST: Created framework node `PBOC Monetary Policy Framework And Interest Rate Transmission` from Guo_Chinas_Monetary_Policy_Framework_2025.md
- **2026-05-22**: INGEST: Created mechanisms node `PBOC RMB Fix Counter Cyclical Factor And FX Management` from RMB (part 2) - How the PBOC manages the RMB.md
- **2026-05-22**: INGEST: Created framework node `IMF Monetary Survey And Reserve Money Identity Framework` from Macroeconomic Accounting and Analysis IMF.md
- **2026-05-22**: INGEST: Created framework node `IMF Flow Of Funds 4-Sector Consistency Framework` from Macroeconomic Accounting and Analysis IMF.md
- **2026-05-22**: INGEST: Created framework node `IMF GFS Fiscal Accounting Framework Deficit Measurement And Sustainability` from Macroeconomic Accounting and Analysis IMF.md
- **2026-05-22**: INGEST: Created framework node `IMF SNA Real Sector Accounting GDP Identities And Sectoral Accounts` from Macroeconomic Accounting and Analysis IMF.md
- **2026-05-22**: INGEST: Created framework node `IMF Balance of Payments Framework and External Account Analysis` from Macroeconomic Accounting and Analysis IMF.md
- **2026-05-22**: INGEST: Created framework node `IMF Monetary Analysis Quantity Theory Velocity And Exchange Rate Regimes` from Macroeconomic Accounting and Analysis IMF.md- **2026-05-22**: INGEST: Created concept node Currency as a Central Bank Liability from Why Is Currency a Liability of the Fed_.md
- **2026-05-22**: INGEST: Created mechanism node Non-Linear Inflation Amplifier Mechanics from Central Bank Commentary (April 2026).md
- **2026-05-22**: INGEST: Created framework node Supply Shock Policy Response Scenario Taxonomy from Central Bank Commentary (April 2026).md
- **2026-05-22**: MAINTENANCE: Rebuilt index.md and wiki_graph_data.json (79 nodes, 91 edges)

- **2026-05-23**: INGEST: Created mechanism node `NBFI Sovereign Bond Absorption Post-ECB-QT` from Who Buys When the ECB Doesn't_.md
- **2026-05-23**: INGEST: Created mechanism node `ECB QT Sovereign Yield Volatility Amplification` from Who Buys When the ECB Doesn't_.md
- **2026-05-23**: INGEST: Created mechanism node `Scissors Effect ECB QT and Sovereign Supply` from Who Buys When the ECB Doesn't_.md
- **2026-05-23**: INGEST: Created concept node `Sovereign Basis Trade Repo Leverage` from Who Buys When the ECB Doesn't_.md
- **2026-05-23**: INGEST: Created concept node `NBFI Sovereign Market Supervisory Gap` from Who Buys When the ECB Doesn't_.md
- **2026-05-23**: INGEST: Created framework node `PBC Dual-Track Monetary Policy Framework` from China's Monetary Policy Framework and Financial Market Transmission _ Bulletin.md
- **2026-05-23**: INGEST: Created mechanism node `PBC Reserve Requirement Ratio Liquidity Management` from China's Monetary Policy Framework and Financial Market Transmission _ Bulletin.md
- **2026-05-23**: INGEST: Created mechanism node `PBC Medium-Term Lending Facility Rate Transmission` from China's Monetary Policy Framework and Financial Market Transmission _ Bulletin.md
- **2026-05-23**: INGEST: Created mechanism node `PBC Structural Monetary Policy Targeted Relending` from China's Monetary Policy Framework and Financial Market Transmission _ Bulletin.md
- **2026-05-23**: INGEST: Created mechanism node `PBC Interest Rate Transmission DR007 to LPR` from China's Monetary Policy Framework and Financial Market Transmission _ Bulletin.md
- **2026-05-23**: INGEST: Created mechanism node `Fed USD Swap Line Architecture and Crisis Function` from I need a dollar (through your swap line).md
- **2026-05-23**: INGEST: Created mechanism node `FX Swap Basis CIP Deviation Dollar Scarcity` from I need a dollar (through your swap line).md
- **2026-05-23**: INGEST: Created concept node `USD Swap Lines Geopolitical Dollar Integration Tool` from I need a dollar (through your swap line).md
- **2026-05-23**: INGEST: Created concept node `Policy Trilemma Efficiency Frontier Equivalence` from False Trilemmas.md
- **2026-05-23**: INGEST: Created mechanism node `Discount Window Stigma Self-Reinforcing Equilibrium` from De-Stigmatizing the Discount Window, Part I_ Tomatoes.md
- **2026-05-23**: INGEST: Created mechanism node `Gilt-Treasury Spread Monetary Policy Expectations Driver` from What's Driving the Gilt-Treasury Spread_.md
- **2026-05-23**: INGEST: Created mechanism node `UK Inflation Persistence Structural Drivers` from What's Driving the Gilt-Treasury Spread_.md
- **2026-05-23**: INGEST: Created mechanism node `ECB New Operational Framework Range Floor 2024` from ECB AND FED POLICY OPERATIONAL FRAMEWORKS â A PRIMER.md
- **2026-05-23**: INGEST: Created mechanism node `Floor System Rate Convergence Mechanism` from ECB AND FED POLICY OPERATIONAL FRAMEWORKS â A PRIMER.md
- **2026-05-23**: INGEST: Created mechanism node `Fed Range Floor ON RRP Non-Bank Access Constraint` from ECB AND FED POLICY OPERATIONAL FRAMEWORKS â A PRIMER.md
- **2026-05-23**: INGEST: Created mechanism node `Fed Ample Reserves Buffer Sizing Formula` from Napkin Math for an Ample Reserves Buffer.md
- **2026-05-23**: INGEST: Created mechanism node `TGA Reserve Inverse Relationship Fed Balance Sheet Growth` from The Checking Account of the U.S. Federal Government....md
- **2026-05-23**: INGEST: Created concept node `Fed Balance Sheet Size and Policy Rate Independence` from Warsh and the Fed's Balance Sheet.md
- **2026-05-23**: INGEST: Created mechanism node `Fed QE Debt Maturity Transformation Fiscal Impact` from A new Fed-Treasury Accord_.md
- **2026-05-23**: INGEST: Created framework node `Fed Balance Sheet Trilemma Small-Stable-Minimal` from Breaking Out of the Central Bank Balance Sheet Trilemma.md
- **2026-05-23**: INGEST: Created mechanism node `TGA Reform as Fed Balance Sheet Reduction Tool` from Breaking Out of the Central Bank Balance Sheet Trilemma.md
- **2026-05-23**: INGEST: Created mechanism node `Eurobond Blue-Red Bond Adverse Selection Moral Hazard` from Why Eurobonds won't work.md
- **2026-05-23**: INGEST: Created concept node `Sovereign Debt Market Discipline Price Discovery Role` from Why Eurobonds won't work.md
- **2026-05-23**: INGEST: Created concept node `Central Bank Credibility Supply Shock Policy Space` from Fed, ECB, and BoJ_ A Matter of Credibility.md
- **2026-05-23**: INGEST: Created mechanism node `Japan Consolidated Public Sector Sovereign Wealth Fund Mechanism` from What about Japan_ (Part I).md
- **2026-05-23**: INGEST: Created mechanism node `BoJ QE Duration Extraction Household Wealth Transfer` from What about Japan_ (Part II).md
- **2026-05-23**: INGEST: Created mechanism node `Basel III Capital Requirements Private Credit Migration` from Private Credit, Basel, and Regional Dynamics.md
- **2026-05-23**: INGEST: Created concept node `US vs Europe Private Credit Market Structure Divergence` from Private Credit, Basel, and Regional Dynamics.md
- **2026-05-23**: INGEST: Created mechanism node `Bank Private Credit Partnership Model Post-Basel` from Private Credit, Basel, and Regional Dynamics.md
- **2026-05-23**: INGEST: Created mechanism node `Private Credit Dual Driver Low Rates and Bank Regulation` from Deep Dive_ Private Credit.md
- **2026-05-23**: INGEST: Created concept node `Private Equity Private Credit Integration Nexus` from Deep Dive_ Private Credit.md
- **2026-05-23**: INGEST: Created mechanism node `Private Credit PIK and Hidden Leverage Mechanisms` from Deep Dive_ Private Credit.md
- **2026-05-23**: INGEST: Created mechanism node `Bank Credit Line Private Credit Funds Systemic Channel` from Deep Dive_ Private Credit.md
- **2026-05-23**: INGEST: Created concept node `Insurance Pension Private Credit Structural Investor Role` from Deep Dive_ Private Credit.md
- **2026-05-23**: INGEST: Created mechanism node `Private Credit Systemic Stress Transmission Mechanism` from Deep Dive_ Private Credit.md
- **2026-05-24**: MAINTENANCE: Expanded 5 thin nodes with verified source data: Money Multiplier Myth, CB Credibility, NBFI Supervisory Gap, Scissors Effect, and Sovereign Basis Trade. (System audit complete, 127 thin nodes remaining)
- **2026-05-24**: INGEST: Created framework node `Fed Balance Sheet Recomposition and Net Expansion` from A new Fed-Treasury Accord_.md and Warsh and the Fed's Balance Sheet.md
- **2026-05-24**: INGEST: Created framework node `Stagflation Regime Diagnostic Framework` from Macroeconomic Accounting and Analysis IMF.md and Central Bank Commentary (April 2026)_ Fed, BoJ, and BoE..md
- **2026-05-24**: INGEST: Created mechanism node `Cost Push Inflation Persistence Mechanism` from Macroeconomic Accounting and Analysis IMF.md
- **2026-05-24**: INGEST: Created framework node `Stagflation Policy Response Tradeoff Framework` from Macroeconomic Accounting and Analysis IMF.md, Central Bank Commentary (April 2026)_ Fed, BoJ, and BoE..md, and Fed, ECB, and BoJ_ A Matter of Credibility.md
- **2026-05-24**: INGEST: Created framework node `US 1970s Stagflation And Policy Regime Shift` from Watts_Wray_Macroeconomics.md, Perry Warjiyo and Solikin M. Juhro - Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-2.md, and Macroeconomic Accounting and Analysis IMF.md
- **2026-05-24**: INGEST: Created framework node `Volcker Fed Reaction Function Break` from Perry Warjiyo and Solikin M. Juhro - Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-4.md
- **2026-05-24**: INGEST: Created mechanism node `Volcker Disinflation Sacrifice Ratio Channel` from Watts_Wray_Macroeconomics.md and Perry Warjiyo and Solikin M. Juhro - Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-4.md

- **2026-05-26**: INGEST: Created concept node `Currency As Central Bank Liability` from Why Is Currency a Liability of the Fed_.md
- **2026-05-26**: INGEST: Created mechanism node `Tax Extinguishment As Proof Of Currency Liability Status` from Why Is Currency a Liability of the Fed_.md
- **2026-05-26**: INGEST: Created mechanism node `Supply Shock Production Network Cascade Amplification` from Central Bank Commentary (April 2026)_ Fed, BoJ, and BoE..md
- **2026-05-26**: INGEST: Created framework node `Central Bank Energy Price Shock Three Stage Taxonomy` from Central Bank Commentary (April 2026)_ Fed, BoJ, and BoE..md
- **2026-05-26**: INGEST: Created mechanism node `CB FX Swap Intervention Mechanics And Off Balance Sheet Exposure` from fx_swap_intervention_mechanics.md
- **2026-05-26**: INGEST: Created mechanism node `CB FX Forward And NDF Intervention Delivery Versus Cash Settlement` from forward_ndf_intervention.md
- **2026-05-26**: INGEST: Created mechanism node `CB FX Options And Cancelable Forward Intervention Structures` from fx_options_cancelable_intervention.md
- **2026-05-26**: INGEST: Created concept node `CB Hidden FX Reserves Net Effective Intervention Capacity` from hidden_reserves_net_effective_position.md
- **2026-05-26**: INGEST: Created concept node `MA Balance Sheet OIN Other Items Net Absorber Mechanics` from oin_taxonomy_and_mechanics.md
- **2026-05-26**: INGEST: Created mechanism node `Supply Chain Non-Linear Shock Structural Amplification` from Central Bank Commentary (April 2026)_ Fed, BoJ, and BoE..md
- **2026-05-26**: INGEST: Created framework node `Central Bank Supply Shock Policy Framework — Direct Indirect Second Round Effects` from Central Bank Commentary (April 2026)_ Fed, BoJ, and BoE..md
- **2026-05-26**: INGEST: Created concept node `Central Bank Currency Liability Tax Redemption And Currency Franchise` from Why Is Currency a Liability of the Fed_.md
- **2026-05-26**: INGEST: Created framework node `Bank ALM Banking Book Risk Management Framework` from A - Asset liability optimization.md
- **2026-05-26**: INGEST: Created mechanism node `Behavioralization Non-Maturity Deposit ALM — Prepayment Early Withdrawal Modeling` from A - Asset liability optimization.md
- **2026-05-26**: INGEST: Created mechanism node `Maturity Gap Analysis Interest Rate Risk Banking Book` from A - Asset liability optimization.md
- **2026-05-26**: INGEST: Created concept node `Bank ALM Structural Liquidity Management NSFR LCR Framework` from A - Bank Asset Liability Management Best Practice_ Yesterday, Today and Tomorrow-De Gruyter (2021).md
- **2026-05-26**: INGEST: Created concept node `Funds Transfer Pricing Rate Decomposition — Base Liquidity Credit Optionality Components` from ftp_transmission_analysis.md.md
- **2026-05-26**: INGEST: Created mechanism node `FTP As Unified Balance Sheet Control Mechanism — Transmission To Risk Factors` from ftp_transmission_analysis.md.md
- **2026-05-26**: INGEST: Created concept node `FTP Curve Construction By Tenor — Short Medium Long Term Spread Framework` from ftp_transmission_analysis.md.md
- **2026-05-26**: INGEST: Created concept node `Vietnam Bank FTP Methodology Implementation — VietABank EY Framework` from VAB - Phương pháp luận FTP_sent to client_FORMATTED_011122 ALM_EY rep 21.06 ALM cmt.md
- **2026-05-26**: INGEST: Created mechanism node `Term Deposit Behavioral Model — Renewal Probability And Early Withdrawal ALM` from BC030304_Term_Deposit_HDSD_arm_FINAL (1).md
- **2026-05-26**: INGEST: Created concept node `Term Deposit ALM Governance — Policy Procedure Limit Framework` from BC030304_Term_Deposit_PPL_arm_FINAL (1).md
- **2026-05-26**: INGEST: Created mechanism node `Overdraft Behavioral Model — Utilization Rate And Drawdown ALM Cashflow` from BC030306_OD_HDSD_arm_FINAL (1).md
- **2026-05-26**: INGEST: Created concept node `Non-Maturity Deposit And Revolving Facility Behavioral Assumptions ALCO Governance` from BC030306_OD_PPL_arm_FINAL (1).md
- **2026-05-26**: INGEST: Created concept node `Term Deposit Behavioral Model — PTS Variant Parameter Specification` from BC030304_Term_Deposit_HDSD_pts_FINAL (1).md
- **2026-05-26**: INGEST: Created concept node `Term Deposit Behavioral Model — PPL PTS Policy Specification` from BC030304_Term_Deposit_PPL_pts_FINAL (1).md
- **2026-05-26**: INGEST: Created concept node `Overdraft Behavioral Model — PTS Variant Parameter Specification` from BC030306_OD_HDSD_pts_FINAL (1).md
- **2026-05-26**: INGEST: Created concept node `Overdraft Behavioral Model — PPL PTS Policy Specification` from BC030306_OD_PPL_pts_FINAL (1).md
- **2026-05-27**: INGEST: Created regulation node `Bcbs Stress Testing Sound Practices 21 Principles 2009` from bcbs155.md
- **2026-05-27**: INGEST: Created mechanism node `Stress Testing Governance Integration Bank Risk Framework` from bcbs155.md
- **2026-05-27**: INGEST: Created regulation node `Basel Iii Lcr Liquidity Coverage Ratio Standard 2013` from bcbs238.md
- **2026-05-27**: INGEST: Created concept node `Hqla Classification Level1 Level2a Level2b` from bcbs238.md
- **2026-05-27**: INGEST: Created concept node `Lcr Monitoring Tools Maturity Mismatch Funding Concentration` from bcbs238.md
- **2026-05-27**: INGEST: Created framework node `Liquidity Stress Test Three Supervisory Approaches Fsi 59` from insights59.md
- **2026-05-27**: INGEST: Created mechanism node `Liquidity Stress Contagion Second Round Effects System Wide` from insights59.md
- **2026-05-27**: INGEST: Created regulation node `Ecb Ilaap Guide 2018 Seven Principles Ssm` from ssm.ilaap_guide_201811.en.md
- **2026-05-27**: INGEST: Created concept node `Ilaap Economic And Normative Perspective Dual Pillar` from ssm.ilaap_guide_201811.en.md
- **2026-05-27**: INGEST: Created regulation node `Eba Gl 2016 10 Icaap Ilaap Information For Srep` from Final report on Guidelines on ICAAP ILAAP (EBA-GL-2016-10).md
- **2026-05-27**: INGEST: Created regulation node `Eba Gl 2018 04 Institutions Stress Testing` from Guidelines on institutions stress testing (EBA-GL-2018-04).md
- **2026-05-27**: INGEST: Created concept node `Reverse Stress Testing Failure Point Business Model Viability` from Guidelines on institutions stress testing (EBA-GL-2018-04).md
- **2026-05-27**: INGEST: Created concept node `Stress Testing Methodology Taxonomy Sensitivity Scenario Reverse` from bcbs155.md
- **2026-05-27**: INGEST: Created concept node `Stress Testing Scenario Severity Design Forward Looking` from bcbs155.md
- **2026-05-27**: INGEST: Created mechanism node `Stress Testing Funding Asset Liquidity Joint Shock Interaction` from bcbs155.md
- **2026-05-27**: INGEST: Created concept node `Supervisory Common Scenario Stress Test Systemic Risk Assessment` from bcbs155.md
- **2026-05-27**: INGEST: Created concept node `Ilaap Liquidity Adequacy Statement Board Approved Conclusion` from ssm.ilaap_guide_201811.en.md
- **2026-05-27**: INGEST: Created mechanism node `Ilaap Recovery Plan Management Actions No Double Counting` from ssm.ilaap_guide_201811.en.md
- **2026-05-27**: INGEST: Created mechanism node `Ilaap Adverse Scenario Calibration Vulnerability Based P7` from ssm.ilaap_guide_201811.en.md
- **2026-05-27**: INGEST: Created concept node `Ilaap Cross Border Liquidity Transferability Group Impediments` from ssm.ilaap_guide_201811.en.md
- **2026-05-27**: INGEST: Created mechanism node `Ilaap Risk Identification Gross Approach Mitigants Assessed Separately` from ssm.ilaap_guide_201811.en.md
- **2026-05-27**: INGEST: Created concept node `Ilaap Normative Perspective Regulatory Ratio Multi Year Projection` from ssm.ilaap_guide_201811.en.md
- **2026-05-27**: INGEST: Created concept node `Liquidity Stress Test Three Building Blocks Assets Liabilities Management Response` from insights59.md
- **2026-05-27**: INGEST: Created mechanism node `Bank Nbfi Liquidity Amplification Three Channels Fire Sale Funding Contagion` from insights59.md
- **2026-05-27**: INGEST: Created concept node `Liquidity Stress Test Static Balance Sheet Assumption Shock Isolation` from insights59.md
- **2026-05-27**: INGEST: Created concept node `Liquidity Stress Test Depositor Behaviour Assumptions Key Driver` from insights59.md
- **2026-05-27**: INGEST: Created concept node `Lcr Retail Deposit Run Off Rates Stable Less Stable Categories` from bcbs238.md
- **2026-05-27**: INGEST: Created concept node `Lcr Wholesale Unsecured Funding Run Off By Counterparty Type` from bcbs238.md
- **2026-05-27**: INGEST: Created concept node `Lcr Secured Funding Run Off By Collateral Quality Asset Level` from bcbs238.md
- **2026-05-27**: INGEST: Created concept node `Lcr Derivatives Downgrade Trigger Three Notch Assumption Additional Collateral` from bcbs238.md
- **2026-05-27**: INGEST: Created concept node `Lcr Below 100 Usage Supervisory Response Disclosure Requirements` from bcbs238.md
- **2026-05-27**: INGEST: Created concept node `Icaap Ilaap Srep Information Four Category Framework` from Final report on Guidelines on ICAAP ILAAP (EBA-GL-2016-10).md
- **2026-05-27**: INGEST: Created concept node `Ilaap Information Specific Funding Strategy Buffer Lcp Srep` from Final report on Guidelines on ICAAP ILAAP (EBA-GL-2016-10).md
- **2026-05-27**: INGEST: Created concept node `Stress Testing Eba 2018 Taxonomy Eleven Defined Terms` from Guidelines on institutions stress testing (EBA-GL-2018-04).md
- **2026-05-27**: INGEST: Created mechanism node `Stress Testing Solvency Liquidity Interaction Icaap Ilaap Integration` from Guidelines on institutions stress testing (EBA-GL-2018-04).md
- **2026-05-27**: INGEST: Created mechanism node `Liquidity Stress Three Scenario Types Idiosyncratic Market Wide Combined Eba` from Guidelines on institutions stress testing (EBA-GL-2018-04).md
- **2026-05-27**: INGEST: Created concept node `Stress Testing Management Actions Before After Presentation Conservative Rules` from Guidelines on institutions stress testing (EBA-GL-2018-04).md
- **2026-05-27**: INGEST: Created mechanism node `Reverse Stress Testing Near Default Scenario Recovery Planning Application` from Guidelines on institutions stress testing (EBA-GL-2018-04).md