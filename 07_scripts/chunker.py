"""Smart markdown chunker with QMD-style break point scoring.

Splits markdown documents into overlapping chunks optimized for BGE-M3 encoding.
Target: 900 tokens per chunk with 15% overlap, breaking at natural document boundaries.
"""

from __future__ import annotations
import re
from dataclasses import dataclass

# Approximate tokens per character for English/Vietnamese mixed text
_CHARS_PER_TOKEN = 4.0

# Break point scores by markdown element type
_BREAK_SCORES = {
    "h1": 100,
    "h2": 90,
    "h3": 80,
    "h4": 70,
    "code_fence": 80,
    "hr": 60,
    "blank_line": 20,
    "list_item": 5,
    "line_break": 1,
}


@dataclass
class Chunk:
    text:        str
    heading:     str    # nearest heading above this chunk
    position:    int    # character offset in source document
    token_count: int
    source_file: str = ""


def chunk_markdown(
    text: str,
    target_tokens: int = 900,
    overlap_pct: float = 0.15,
    source_file: str = "",
) -> list[Chunk]:
    """Split markdown text into chunks with smart break point detection.

    Algorithm:
    1. Scan all lines for break points with scores
    2. At target_tokens, search a 200-token window before cutoff
    3. Score = baseScore × (1 - (distance/window)^2 × 0.7)
    4. Cut at highest-scoring break point
    5. Overlap is taken from the tail of the previous chunk

    Code fence protection: break points inside ``` blocks are suppressed.
    """
    if not text or not text.strip():
        return []

    lines = text.split("\n")
    target_chars = int(target_tokens * _CHARS_PER_TOKEN)
    overlap_chars = int(target_chars * overlap_pct)
    window_chars = int(200 * _CHARS_PER_TOKEN)

    # Build list of (char_offset, score, heading) for each line
    break_points: list[tuple[int, float, str]] = []
    in_code_fence = False
    current_offset = 0
    current_heading = ""

    for line in lines:
        line_len = len(line) + 1  # +1 for newline
        stripped = line.strip()

        # Track code fences
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_fence = not in_code_fence

        score = 0.0
        if not in_code_fence:
            if re.match(r"^# ", line):
                score = _BREAK_SCORES["h1"]
                current_heading = stripped.lstrip("# ").strip()
            elif re.match(r"^## ", line):
                score = _BREAK_SCORES["h2"]
                current_heading = stripped.lstrip("# ").strip()
            elif re.match(r"^### ", line):
                score = _BREAK_SCORES["h3"]
                current_heading = stripped.lstrip("# ").strip()
            elif re.match(r"^#### ", line):
                score = _BREAK_SCORES["h4"]
                current_heading = stripped.lstrip("# ").strip()
            elif re.match(r"^```|^~~~", stripped):
                score = _BREAK_SCORES["code_fence"]
            elif re.match(r"^---$|^\*\*\*$|^___$", stripped):
                score = _BREAK_SCORES["hr"]
            elif stripped == "":
                score = _BREAK_SCORES["blank_line"]
            elif re.match(r"^[-*+] |^\d+\. ", stripped):
                score = _BREAK_SCORES["list_item"]
            else:
                score = _BREAK_SCORES["line_break"]

        break_points.append((current_offset, score, current_heading))
        current_offset += line_len

    total_chars = current_offset
    chunks: list[Chunk] = []
    start = 0

    while start < total_chars:
        end_target = start + target_chars

        if end_target >= total_chars:
            # Last chunk — take everything remaining
            chunk_text = text[start:]
            if chunk_text.strip():
                heading = _find_heading_at(break_points, start)
                chunks.append(Chunk(
                    text=chunk_text,
                    heading=heading,
                    position=start,
                    token_count=_estimate_tokens(chunk_text),
                    source_file=source_file,
                ))
            break

        # Search for best break point in window before end_target
        window_start = max(start, end_target - window_chars)
        best_offset = end_target
        best_score = -1.0

        for offset, score, heading in break_points:
            if offset < window_start or offset > end_target:
                continue
            # Score decays with distance from ideal cut point
            distance = end_target - offset
            adjusted = score * (1.0 - (distance / window_chars) ** 2 * 0.7)
            if adjusted > best_score:
                best_score = adjusted
                best_offset = offset

        chunk_text = text[start:best_offset].strip()
        if chunk_text:
            heading = _find_heading_at(break_points, start)
            chunks.append(Chunk(
                text=chunk_text,
                heading=heading,
                position=start,
                token_count=_estimate_tokens(chunk_text),
                source_file=source_file,
            ))

        # Overlap: start next chunk overlap_chars before best_offset
        start = max(start + 1, best_offset - overlap_chars)

    return chunks


def _find_heading_at(break_points: list[tuple[int, float, str]], offset: int) -> str:
    """Return the most recent heading at or before the given offset."""
    heading = ""
    for bp_offset, _, bp_heading in break_points:
        if bp_offset > offset:
            break
        if bp_heading:
            heading = bp_heading
    return heading


def _estimate_tokens(text: str) -> int:
    return max(1, int(len(text) / _CHARS_PER_TOKEN))


def iter_source_documents(
    source_dirs: list[str],
    extensions: tuple[str, ...] = (".md",),
) -> list[dict]:
    """Iterate over all markdown files in source directories.

    Returns list of dicts with keys: path, text, frontmatter.
    """
    from pathlib import Path
    import yaml

    docs: list[dict] = []
    for dir_str in source_dirs:
        base = Path(dir_str)
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if path.suffix not in extensions:
                continue
            if path.name.startswith("_"):
                continue  # skip registry files like _source_registry.yaml
            try:
                raw = path.read_text(encoding="utf-8", errors="ignore")
                frontmatter, body = _split_frontmatter(raw)
                docs.append({
                    "path": str(path),
                    "text": raw,
                    "body": body,
                    "frontmatter": frontmatter,
                })
            except Exception:
                pass

    return docs


def _split_frontmatter(text: str) -> tuple[dict, str]:
    """Split YAML frontmatter from markdown body.

    Returns (frontmatter_dict, body_text).
    """
    import yaml

    if not text.startswith("---"):
        return {}, text

    lines = text.split("\n")
    end = -1
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break

    if end == -1:
        return {}, text

    fm_text = "\n".join(lines[1:end])
    body = "\n".join(lines[end + 1:])

    try:
        fm = yaml.safe_load(fm_text) or {}
    except Exception:
        fm = {}

    return fm, body
