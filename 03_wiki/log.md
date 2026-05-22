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