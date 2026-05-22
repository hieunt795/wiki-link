# Confidence Scale — Wiki Knowledge Trust Hierarchy

Every wiki node carries a `confidence` field (1–5). This score governs reranker weighting
and determines how the system treats a node during retrieval and promotion.

---

## Scale Definition

| Score | Label | Meaning | Source type | Reranker multiplier |
|-------|-------|---------|-------------|---------------------|
| 5 | Authoritative | Multiple primary textbooks + peer-reviewed papers agree. Core established theory. | Multiple academic textbooks | ×1.25 |
| 4 | Reliable | Single primary textbook OR multiple reliable secondary sources. Well-cited. | One primary textbook, or IMF/BIS/Fed research paper | ×1.20 |
| 3 | Corroborated | Reliable secondary sources OR credible institutional reports. | IMF WP, BIS QR, Fed staff note, ECB WP | ×1.15 |
| 2 | Provisional | LLM synthesis backed by at least one source. Not fully verified. Mark `[LLM]` in body. | Synthesis of clipping/secondary sources | ×1.10 |
| 1 | Stub | LLM-generated without source verification. Placeholder only. | Auto-generated during ingest | ×1.05, then ×0.4 LLM penalty |

---

## Operational Rules

**Setting confidence at ingest:**
- Newly ingested nodes start at `confidence: 1` regardless of source quality.
- Raise to 2 after agent reads and summarizes the source with partial verification.
- Raise to 3+ only after reading the primary source passage and verifying the claim.
- Agent must not self-promote above 3 without citing a specific page/section.

**LLM penalty (reranker):**
- Any node with `[LLM]` in thesis or first 200 characters of body receives an additional ×0.4 multiplier during Phase 4 reranking.
- This means a confidence=1 stub with [LLM] effectively scores at ×(1.05 × 0.4) = ×0.42 vs a confidence=5 node at ×1.25 — a 3× trust gap by design.

**Promotion gate:**
- Findings in `04_research/` cannot be promoted to `03_wiki/` if `confidence < 3`.
- Confidence 3 requires citing a specific IMF/BIS/Fed document or peer-reviewed paper.

**Downgrade triggers:**
- If a newer source contradicts a node: lower confidence by 1 until contradiction is resolved.
- If `stability: stale` is set: lower confidence by 1.
- If `source_refs` point to deleted or moved files: lower confidence to 1 until refs are fixed.

---

## Examples by Domain

### Monetary Policy
- conf=5: IS-LM model core mechanics (multiple textbooks, Bindseil + Woodford + Mishkin agree)
- conf=4: QE transmission channels per Bindseil (single primary textbook, detailed treatment)
- conf=3: Forward guidance effectiveness (multiple IMF/BIS staff papers)
- conf=2: LLM synthesis of BOJ clippings on YCC dynamics
- conf=1: Auto-stub created during ingest of new Clipping article

### Basel / Capital
- conf=5: CET1 definition under BCBS Basel III text (regulatory primary source)
- conf=4: LCR calibration rationale (BCBS consultative paper + BIS QR)
- conf=3: G-SIB buffer methodology (FSB/BCBS guidance)
- conf=2: Private credit Basel treatment synthesis from research notes

### Fixed Income / Markets
- conf=5: Duration and convexity mechanics (Tuckman/Serrat + Homer/Leibowitz)
- conf=4: Repo market dynamics (Singh Collateral Plumbing + Choudhry)
- conf=3: SOFR transition mechanism (Fed staff notes + ISDA)
