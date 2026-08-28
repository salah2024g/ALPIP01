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

        boolean_matched = self._boolean.matches_any(text, content)

        matched = boolean_matched or bool(matched_terms) or bool(matched_phrases)

        phrase_score = 2 * len(matched_phrases)

        phrase_match_bonus = 1.0 if matched_phrases and not matched_terms else 0.0

        score = float(len(matched_terms) + phrase_score + phrase_match_bonus)

        return AdvancedMatch(
            matched=matched,
            score=score,
            matched_terms=matched_terms,
            matched_phrases=matched_phrases,
        )
