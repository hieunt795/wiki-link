# Wiki Operation Log

Chronological record of all ingest, update, promotion, and audit operations.

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
