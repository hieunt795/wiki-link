"""Bilingual Vietnamese ↔ English domain dictionary + query augmentation.

Used by synthesis_search probe (FTS5 exact matching) to augment Vietnamese queries
with English equivalents. BGE-M3 dense/sparse search handles VI natively — no
augmentation needed for those paths.
"""

from __future__ import annotations
import re
from pathlib import Path

import yaml

# Vietnamese tone-marked characters for language detection
_VI_CHARS = set(
    "àáâãèéêìíòóôõùúýăđơư"
    "ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝĂĐƠƯ"
    "ắằẳẵặấầẩẫậắằẳẵặếềểễệ"
    "ịỉĩọỏốồổỗộớờởỡợụủũứừửữự"
    "ặếềểễệịỉĩọỏốồổỗộớờởỡợụủũứừửữựỳỷỹỵ"
)

# Default dictionary — loaded from 01_schema/vi_en_dictionary.yml at runtime
_VI_EN: dict[str, list[str]] = {}

# Reverse map: english token → list of vietnamese phrases that map to it
_VI_TOKEN_MAP: dict[str, list[str]] = {}


def load_dictionary(path: Path | None = None) -> None:
    """Load VI↔EN dictionary from YAML file.

    Called once at startup by librarian.py. Falls back to embedded defaults.
    """
    global _VI_EN, _VI_TOKEN_MAP

    if path is None:
        # Default path relative to this file
        path = Path(__file__).parent.parent / "01_schema" / "vi_en_dictionary.yml"

    if path.exists():
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        _VI_EN = data.get("terms", {})
    else:
        # Embedded minimal fallback (avoid hard failure if schema missing)
        _VI_EN = _EMBEDDED_FALLBACK

    # Build reverse map
    _VI_TOKEN_MAP = {}
    for vi_term, en_terms in _VI_EN.items():
        for en in en_terms:
            _VI_TOKEN_MAP.setdefault(en.lower(), []).append(vi_term)


def is_vietnamese(text: str) -> bool:
    """Return True if text contains Vietnamese tone-marked characters.

    Threshold: ≥ 2 tone-marked characters = Vietnamese.
    Single accented chars appear in French/Spanish loanwords in EN text too.
    """
    count = sum(1 for ch in text if ch in _VI_CHARS)
    return count >= 2


def vi_augment(query: str) -> str:
    """Augment a Vietnamese query with English equivalents for FTS5 matching.

    For each VI term found in the dictionary, appends its EN equivalents.
    The augmented query is used ONLY for FTS5 — BGE-M3 dense/sparse work natively.

    Example:
        vi_augment("lãi suất chính sách") →
        "lãi suất chính sách interest rate policy rate monetary policy"
    """
    if not _VI_EN:
        load_dictionary()

    additions: list[str] = []
    query_lower = query.lower()

    # Match multi-word phrases first (longer matches take priority)
    sorted_terms = sorted(_VI_EN.keys(), key=len, reverse=True)
    matched_positions: set[int] = set()

    for vi_term in sorted_terms:
        idx = query_lower.find(vi_term.lower())
        if idx == -1:
            continue
        # Check that position wasn't already matched by a longer phrase
        positions = set(range(idx, idx + len(vi_term)))
        if positions & matched_positions:
            continue
        matched_positions |= positions
        additions.extend(_VI_EN[vi_term])

    if not additions:
        return query

    # Deduplicate additions, preserve order
    seen: set[str] = set()
    unique_additions: list[str] = []
    for term in additions:
        if term.lower() not in seen:
            seen.add(term.lower())
            unique_additions.append(term)

    return query + " " + " ".join(unique_additions)


def get_en_equivalents(vi_term: str) -> list[str]:
    """Return English equivalents for a given Vietnamese term."""
    if not _VI_EN:
        load_dictionary()
    return _VI_EN.get(vi_term.lower(), [])


# Minimal embedded fallback — only the most critical terms
_EMBEDDED_FALLBACK: dict[str, list[str]] = {
    "lãi suất": ["interest rate", "policy rate"],
    "chính sách tiền tệ": ["monetary policy"],
    "ngân hàng trung ương": ["central bank"],
    "lạm phát": ["inflation", "CPI"],
    "đường cong lợi suất": ["yield curve"],
    "thanh khoản": ["liquidity"],
    "nới lỏng định lượng": ["quantitative easing", "QE"],
    "thắt chặt định lượng": ["quantitative tightening", "QT"],
    "tỷ giá": ["exchange rate", "FX rate"],
    "trái phiếu chính phủ": ["government bond", "sovereign bond"],
    "vốn ngân hàng": ["bank capital"],
    "tỷ lệ an toàn vốn": ["capital adequacy ratio", "CAR"],
    "ổn định tài chính": ["financial stability"],
    "cho vay ký quỹ": ["repo", "repurchase agreement"],
    "tài sản thế chấp": ["collateral"],
}
