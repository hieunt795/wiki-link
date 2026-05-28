import sys
sys.path.insert(0, '.')
from ingest import create_wiki_node, _mark_batch_done

SRC2016 = "02_sources/regulator/bcbs/Final report on Guidelines on ICAAP ILAAP (EBA-GL-2016-10).md"
SRC2018 = "02_sources/regulator/bcbs/Guidelines on institutions stress testing (EBA-GL-2018-04).md"

# EBA GL-2016-10 nodes

create_wiki_node("concept",
    "Icaap Ilaap Srep Information Four Category Framework",
    "[LLM] EBA GL/2016/10 organises ICAAP/ILAAP supervisory information into 4 categories: "
    "(1) General -- governance, risk management framework, RAF, stress testing programme, "
    "business model; (2) ICAAP-specific -- risk identification, capital calculation "
    "methodology, internal capital allocation, capital planning, ICAAP stress tests; "
    "(3) ILAAP-specific -- funding strategy, liquidity buffers and collateral policy, "
    "FTP/cost-benefit allocation, intraday liquidity management, liquidity stress tests, "
    "LCP; (4) Conclusions -- ICAAP/ILAAP outcomes, internal validation results, internal "
    "audit reports. All four categories submitted at reference dates proportionate to "
    "SREP category.",
    SRC2016, "alm",
    ["ICAAP ILAAP SREP information categories", "EBA GL/2016/10 four categories",
     "thong tin ICAAP ILAAP cho SREP", "SREP information requirements"],
    ["icaap", "ilaap", "srep", "eba", "information_requirements", "governance"])

create_wiki_node("concept",
    "Ilaap Information Specific Funding Strategy Buffer Lcp Srep",
    "[LLM] EBA GL/2016/10 Section 7 specifies ILAAP information for SREP: "
    "(a) Funding strategy -- multi-year funding plan, currency breakdown, forecast LCR/NSFR; "
    "(b) Liquidity buffers -- internal minimum buffer definition, criteria for asset liquidity "
    "value, time-to-monetise, asset encumbrance policy, collateral location/transferability; "
    "(c) FTP/cost-benefit allocation mechanism; "
    "(d) Intraday liquidity -- monitoring tools, escalation for intraday shortfalls; "
    "(e) Liquidity stress tests -- idiosyncratic, market-wide, combined scenarios; "
    "(f) LCP -- early warning tools, execution strategies, testing procedures. "
    "Quality assurance: independent validation and internal audit results required.",
    SRC2016, "alm",
    ["ILAAP SREP information", "liquidity contingency plan requirements",
     "yeu cau thong tin ILAAP SREP", "EBA GL 2016/10 Section 7"],
    ["ilaap", "srep", "eba", "funding_strategy", "liquidity_buffer", "lcp", "intraday"])

for i in range(34):
    _mark_batch_done(SRC2016, i)
print("EBA GL-2016-10 nodes done + 34 batches marked.")

# EBA GL-2018-04 nodes

create_wiki_node("concept",
    "Stress Testing Eba 2018 Taxonomy Eleven Defined Terms",
    "[LLM] EBA GL/2018/04 defines 11 stress testing terms forming the EU taxonomy: "
    "(1) Solvency stress test -- capital position impact; "
    "(2) Liquidity stress test -- liquidity impact; "
    "(3) Bottom-up -- institution runs own models; "
    "(4) Top-down -- supervisory common methodology; "
    "(5) Static balance sheet -- no new business during scenario; "
    "(6) Dynamic balance sheet -- management can change structure; "
    "(7) Portfolio stress test -- individual portfolio/risk level; "
    "(8) Sensitivity analysis -- single or simple multi-factor shock; "
    "(9) Scenario analysis -- multi-factor coherent narrative; "
    "(10) Reverse stress test -- backward from failure outcome; "
    "(11) Second-round/feedback effects -- spillover from collective reactions.",
    SRC2018, "alm",
    ["EBA stress testing taxonomy", "EU stress test definitions",
     "phan loai kiem tra cang thang EU", "EU stress test terminology"],
    ["eba", "stress_testing", "taxonomy", "definitions", "2018"])

create_wiki_node("mechanism",
    "Stress Testing Solvency Liquidity Interaction Icaap Ilaap Integration",
    "[LLM] EBA GL/2018/04 Section 4.8 requires explicit integration of solvency and liquidity "
    "stress tests: capital ratio deterioration can trigger liquidity outflows (market "
    "perception effect), and liquidity crisis can cause capital losses (forced asset sales). "
    "The mapping between these two must be documented. ICAAP stress tests: minimum 2-year "
    "horizon. Both must use consistent management action assumptions -- actions used in ICAAP "
    "cannot be double-counted in ILAAP. Results reported before and after management actions.",
    SRC2018, "alm",
    ["solvency liquidity stress link", "ICAAP ILAAP stress integration",
     "tuong tac von va thanh khoan stress", "capital liquidity feedback"],
    ["eba", "stress_testing", "icaap", "ilaap", "solvency_liquidity_link", "2018"])

create_wiki_node("mechanism",
    "Liquidity Stress Three Scenario Types Idiosyncratic Market Wide Combined Eba",
    "[LLM] EBA GL/2018/04 Section 4.7.6 requires three mandatory liquidity stress scenarios: "
    "(1) Idiosyncratic -- bank-specific event causing institution-specific funding withdrawal "
    "while system functions normally (e.g. credit downgrade, reputational event); "
    "(2) Market-wide -- systemic stress affecting all banks simultaneously "
    "(e.g. interbank market freeze, broad credit spread widening); "
    "(3) Combined -- simultaneous idiosyncratic and market-wide stress (most severe; also "
    "calibration scenario for LCR). Key output metric: lowest cumulative net cash flow "
    "within the assessed time period under each scenario.",
    SRC2018, "alm",
    ["liquidity stress three scenarios", "idiosyncratic market combined scenarios",
     "ba kich ban cang thang thanh khoan", "EBA 2018 liquidity scenarios"],
    ["eba", "stress_testing", "liquidity_risk", "idiosyncratic", "market_wide", "combined"])

create_wiki_node("concept",
    "Stress Testing Management Actions Before After Presentation Conservative Rules",
    "[LLM] EBA GL/2018/04 Section 4.8.2 mandates that stress test results be presented both "
    "before and after management actions -- showing the assumed mitigating impact. Rules: "
    "(1) actions must be consistent with stated strategies/policies (dividend, capital "
    "distribution); (2) must be feasible under the stress scenario -- banks must be "
    "conservative about actions difficult to execute in stressed markets; (3) immediate vs "
    "contingent actions must be distinguished with pre-defined triggers; (4) actions used in "
    "ICAAP stress tests cannot be double-counted in ILAAP management actions and vice versa.",
    SRC2018, "alm",
    ["management actions stress test", "before after management actions ST",
     "hanh dong quan ly kiem tra cang thang", "EBA management actions stress"],
    ["eba", "stress_testing", "management_actions", "icaap", "ilaap", "2018"])

create_wiki_node("mechanism",
    "Reverse Stress Testing Near Default Scenario Recovery Planning Application",
    "[LLM] EBA GL/2018/04 Sections 4.6.5 and 4.7 extend RST to recovery planning: "
    "institutions develop 'near-default' scenarios -- conditions where the business model "
    "becomes unviable UNLESS recovery actions succeed. RST serves dual purpose: "
    "(1) calibrate forward-looking scenario severity (if RST scenario is plausible, forward "
    "scenarios may be too mild); (2) test recovery action effectiveness -- can specific "
    "options restore viability from this near-default state? RST minimum annually; frequency "
    "increases if business model or risk profile changes materially. RST results must be "
    "reported to management body and feed into risk appetite review.",
    SRC2018, "alm",
    ["RST recovery planning", "near-default scenario", "reverse stress test application",
     "kiem tra cang thang nguoc ke hoach phuc hoi"],
    ["eba", "reverse_stress_testing", "recovery_planning", "near_default", "2018"])

for i in range(79):
    _mark_batch_done(SRC2018, i)
print("EBA GL-2018-04 nodes done + 79 batches marked.")
