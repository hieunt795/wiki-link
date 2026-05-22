# T_MODE_DEEP — Unified Analytical Template
**Version:** 1.0 — 2026-05-20
**Refs:** P1_awareness · P2_epistemic · P3_mechanistic · P4_output · W3_research

> **When to use:** Deep mechanism analysis — plumbing, Treasury desk, T-account tracing.
> Any topic with ≥ 3 sub-questions touching Plumbing or Treasury layers.
> Replaces (does not combine with) research_memo for this type of analysis.

---

## FORMAT DISCIPLINE (read before writing)

**Separators `---`:** Only 3 times — after TOP-DOWN ENTRY, after TREASURY LAYER, after DIAGRAM. Never between sub-sections.

**Tables:** Only when comparing ≥ 3 entities simultaneously. Total column width ≤ 100 characters. If content is long, abbreviate or switch to bullet prose.

**Plumbing sub-components:** No separate heading for each component. Flow naturally: T-Account → Transmission chain → Stakeholder summary → Choke point, in one continuous section.

**Treasury Layer:** Technical prose, no numbered list. End with 2–3 short "Trade implications" bullets.

**DIAGRAM:** One ASCII art only — choose the most important angle, do not force timeline + T-Account + Before/After into the same diagram.

**Visual hierarchy:** Use **bold** to mark the core point in each section. No ALL CAPS in body text.

**Linguistic Sobriety (Rule 11):** No gaming framing, combat metaphors, journalistic labels, wordplay.
```
❌ "Double Kill bóp speculators"  →  ✅ "delayed sterilization creates dual tightening effect"
❌ "Macro trap"                  →  ✅ "policy constraint: monetary tool unavailable, fiscal substitute activated"
❌ "MOF wins the window"         →  ✅ "intervention achieves tactical USD/JPY stabilization within the window"
```
Principle: describe the mechanism, do not label it.

**Source & Claim Discipline (P2 + P3):**
- Every specific number (%, bps, $, date) must carry a label: `[WEB-YYYY-MM-DD]` / `[RAW-BOOK p.X]` / `[LLM-E — estimated range]`
- Direct quotes ("X said Y") must have `[RAW-CLIP]` or `[WEB-URL]` — no quotation marks without verification
- Causal claims must have mechanism A→B→C; never "usually..." or "tends to..." without conditions

---

## TEMPLATE STRUCTURE

---

### TOP-DOWN ENTRY
> Set the frame before the mechanism. No analysis here — only define scope and thesis.

| Field | Value |
|-------|-------|
| Core Question | [The central question to be answered] |
| Asset / Currency | [USD · EUR · VND · Bond · Repo · Equity · ...] |
| Temporal Status | [CURRENT 🟢 / LEGACY 🟡 / DEPRECATED 🔴] |
| Analytical Scope | [System · Market · Specific institution] |
| Thesis | [1 sentence — does not change after this block] |

---

### MACRO LAYER
> Answer: What regime are we in? What anchors the system?

| Dimension | Current Value |
|-----------|--------------|
| Macro Regime | [QT/QE · Hiking/Easing · Ample/Scarce Reserves] |
| Policy Anchor | [Fed Funds · ECB DFR · SBV refi rate + specific level] |
| Fiscal Stance | [Surplus/Deficit · TGA balance · issuance calendar] |
| Institutional Constraint | [What CB can / cannot do under its mandate] |
| Structural Tension | [Conflict between macro regime and policy objective] |

### PLUMBING LAYER
> Answer: Where does money go? Who benefits, who loses, through what mechanism?
> Each step in the chain must pass through at least 1 pillar (P3): Accounting Identity · Contractual Flow · Institutional Constraint.

**Entity + T-Account Tracing**

Every major policy action must appear on the balance sheet of at least 2 entities.

| Entity | Assets (Δ) | Liabilities (Δ) | Net Position |
|--------|-----------|----------------|-------------|
| Central Bank | | | |
| Treasury | | | |
| Commercial Banks | | | |
| MMFs / Shadow Banks | | | |
| End Borrowers | | | |

**Transmission Chain**
```
[Policy Action] → [A] → [B] → [C] → [Asset Price / Real Economy Impact]
```
State the condition at each step: "A → B when [condition]; breaks when [condition]."

**Stakeholder Impact Matrix**

| Stakeholder | Mechanism | Direction | Magnitude |
|------------|-----------|-----------|-----------|
| CB / Fed | | | |
| Banks (ALM desk) | | | |
| MMFs | | | |
| Shadow banks / Hedge funds | | | |
| Corporate borrowers | | | |

**Liquidity Choke Points**

Where is liquidity blocked or destroyed in the transmission chain? State the specific node.

---

### TREASURY LAYER
> Answer: If sitting at the Treasury desk, what do I need to know and do?
> TQN Lens — translate operational mechanics into practitioner logic.

**ALM & Funding Impact**

| Dimension | Impact |
|-----------|--------|
| Duration | [Impact on portfolio duration] |
| Funding Cost | [How spread changes] |
| LCR / NSFR | [Regulatory ratio affected?] |
| Collateral | [Haircut, eligibility, scarcity changes] |

**Treasury Insight**
> [Technical prose — "So what for the desk?": what does this mean for the ALM/Treasury manager?
>  No metaphors, no journalism. Pure practitioner logic.]

**Trade & Positioning Implications**
- Relative value: [Which instrument benefits / suffers]
- Hedging: [Duration hedge, basis trade, FX swap if relevant]
- Risk trigger: [Condition that forces closing/opening position]

---

### TIMING LAYER
> Cross-cutting synthesis — Timing is not a sequential step but a layer applied across the full analysis.
> Answer: Where is the Plumbing + Treasury Insight on the time axis?

| | PAST (Precedent) | PRESENT (Current) | FUTURE (Trajectory) |
|-|-----------------|------------------|---------------------|
| Macro Regime | [Previous regime? When did it shift?] | [Current regime + phase in cycle] | [Conditions for regime change] |
| Plumbing | [How did this mechanism work in precedent?] | [Active / Stressed / Breaking?] | [Velocity + Window of Exposure] |
| Treasury | [How did desk respond in similar regimes?] | [Current positioning] | [Triggers to monitor] |

**Timing Dynamics**
- **Velocity:** How fast/slow does the transmission mechanism operate? (days / weeks / quarters)
- **Window of Exposure:** How long does the vulnerable window last?
- **Synchronization:** Are multiple mechanisms activating simultaneously? → amplification risk

### FEEDBACK / BOUNDARY
> Answer: What stops the entire mechanism above from working, or reverses it?

| Signal | Monitoring Indicator | Danger Threshold | Current |
|--------|--------------------|--------------------|---------|
| Stress indicator 1 | | | |
| Stress indicator 2 | | | |
| Breakpoint condition | | | |

**Failure Conditions:** [Boundary conditions — when is this analytical model wrong?]

---

### DIAGRAM
> Choose the ASCII art form that best illustrates the most complex part of this analysis.
> Before drawing: What is most complex in this piece that prose cannot capture? Draw that.

Candidate forms (use, combine, or vary as needed):
- **T-Account parallel:** when comparing balance sheets of 2+ entities simultaneously
- **Transmission chain:** when mechanism is a long A→B→C→D chain
- **Feedback loop:** when there is a self-reinforcing or self-canceling loop
- **Flow diagram:** when money/assets pass through multiple intermediaries in sequence
- **Capital waterfall:** when showing loss absorption order or risk layering
- **Timeline:** when the sequence of events is the core of the mechanism

One clear diagram is better than three complex ones.

```
[ASCII DIAGRAM HERE]
```

---

### CONCLUSION

| Field | Value |
|-------|-------|
| Thesis | [Confirmed / Modified / Rejected — reason in 1 sentence] |
| Net Plumbing Effect | [Direction + Magnitude + Timing] |
| Treasury Action | [What should the desk do specifically?] |
| Confidence | TIER [A/B/C/D] — [reason] |
| Critical Caveat | [The single condition that makes the entire analysis wrong] |

**Confidence Tiers:**
- TIER A: Multiple confidence>=4 sources, no open contradictions, mechanism well-documented
- TIER B: At least one confidence>=3 source, minor uncertainty on 1-2 sub-questions
- TIER C: Primarily confidence<=2 sources, significant inference, use with caution
- TIER D: Largely estimated, TRUE_GAP items unresolved — analytical starting point only

### NEXT STEPS
```bash
# Search before spawning a new node
python 07_scripts/librarian.py search "<concept from analysis>"

# If new concept found → spawn wiki node
# → 03_wiki/mechanisms/<topic>.md

# If source needs ingesting
python 07_scripts/librarian.py ingest 02_sources/path/to/file.md

# After creating node
python 07_scripts/librarian.py sync

# Close session and review TEMPLATE_INSIGHTs
python 07_scripts/librarian.py session-close {topic_slug}
```
