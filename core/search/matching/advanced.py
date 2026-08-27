from dataclasses import dataclass

from core.search.matching.boolean import BooleanMatcher
from core.search.matching.default import SearchTermMatcher
from core.search.matching.phrase import PhraseMatcher


@dataclass(slots=True)
class AdvancedMatch:
    matched: bool
    score: float
    matched_terms: list[str]
    matched_phrases: list[str]


class AdvancedMatcher:
    """Deterministic advanced matcher combining terms, phrases, and boolean logic."""

    def __init__(self) -> None:
        self._terms = SearchTermMatcher()
        self._phrases = PhraseMatcher()
        self._boolean = BooleanMatcher()

    def match(
        self,
        query_text: str,
        content: str,
    ) -> AdvancedMatch:
        text = query_text.strip()

        if not text:
            return AdvancedMatch(
                matched=False,
                score=0.0,
                matched_terms=[],
                matched_phrases=[],
            )

        matched_terms = self._terms.match(text, content)

        phrases = [
            part.strip()
            for part in text.split('"')
            if part.strip() and " " in part.strip()
        ]

        matched_phrases = [
            phrase
            for phrase in dict.fromkeys(phrases)
            if self._phrases.matches(phrase, content)
        ]

        matched = self._boolean.matches_any(text, content)

        score = float(len(matched_terms) + (2 * len(matched_phrases)))

        return AdvancedMatch(
            matched=matched,
            score=score,
            matched_terms=matched_terms,
            matched_phrases=matched_phrases,
        )
