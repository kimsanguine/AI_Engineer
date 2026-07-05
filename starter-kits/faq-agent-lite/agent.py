#!/usr/bin/env python3
"""Tiny public-safe FAQ retrieval agent.

This example intentionally uses only Python standard library code and synthetic
data so non-engineers can inspect the whole loop.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DATA_PATH = Path(__file__).parent / "sample_data" / "faqs.json"
MIN_CONFIDENCE = 0.28
STOPWORDS = {
    "a",
    "an",
    "and",
    "can",
    "do",
    "i",
    "in",
    "is",
    "my",
    "the",
    "to",
    "what",
    "where",
}


@dataclass(frozen=True)
class Match:
    faq_id: str
    question: str
    answer: str
    category: str
    confidence: float


def tokenize(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9가-힣]+", text.lower())
        if len(token) > 1 and token not in STOPWORDS
    }


def load_faqs(path: Path = DATA_PATH) -> list[dict[str, object]]:
    with path.open(encoding="utf-8") as file:
        data = json.load(file)
    return list(data["faqs"])


def score_question(query: str, faq: dict[str, object]) -> float:
    query_tokens = tokenize(query)
    searchable = " ".join(
        [
            str(faq["question"]),
            str(faq["answer"]),
            " ".join(str(tag) for tag in faq.get("tags", [])),
        ]
    )
    faq_tokens = tokenize(searchable)
    if not query_tokens or not faq_tokens:
        return 0.0

    overlap = len(query_tokens & faq_tokens) / len(query_tokens)
    tag_tokens = tokenize(" ".join(str(tag) for tag in faq.get("tags", [])))
    tag_bonus = 0.15 if query_tokens & tag_tokens else 0.0
    return min(overlap + tag_bonus, 1.0)


def answer_question(query: str, faqs: list[dict[str, object]] | None = None) -> Match | None:
    faqs = faqs if faqs is not None else load_faqs()
    ranked = sorted(((score_question(query, faq), faq) for faq in faqs), reverse=True, key=lambda item: item[0])
    confidence, best = ranked[0]
    if confidence < MIN_CONFIDENCE:
        return None
    return Match(
        faq_id=str(best["id"]),
        question=str(best["question"]),
        answer=str(best["answer"]),
        category=str(best["category"]),
        confidence=round(confidence, 2),
    )


def format_response(query: str) -> str:
    match = answer_question(query)
    if match is None:
        return (
            "I do not know based on the public synthetic FAQ set.\n"
            "Handoff: ask an operator to add a sourced FAQ before using this answer."
        )
    return (
        f"Q: {query}\n"
        f"A: {match.answer}\n"
        f"Source: {match.faq_id} | Category: {match.category} | Confidence: {match.confidence:.2f}"
    )


def main() -> int:
    if len(sys.argv) < 2:
        print('Usage: python3 agent.py "Can I change my billing date?"')
        return 2
    print(format_response(" ".join(sys.argv[1:])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
