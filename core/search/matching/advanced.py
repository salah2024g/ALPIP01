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
    """Deterministic advanced matcher combining terms and phrases."""

    def __init__(self) -> None:
        self._terms = SearchTermMatcher()
        self._phrases = PhraseMatcher()
        self._boolean = BooleanMatcher()

    def _extract_phrases(self, text: str) -> list[str]:
        return [part.strip() for part in text.split('"')[1::2] if part.strip()]

    def _extract_unquoted_text(self, text: str) -> str:
        return " ".join(text.split('"')[::2]).strip()

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

        unquoted_text = self._extract_unquoted_text(text)
        phrases = self._extract_phrases(text)

        matched_terms = self._terms.match(
            unquoted_text,
            content,
        )

        terms_matched = not unquoted_text or self._boolean.matches_all(
            unquoted_text,
            content,
        )

        matched_phrases = [
            phrase
            for phrase in dict.fromkeys(phrases)
            if self._phrases.matches(phrase, content)
        ]

        phrases_matched = len(matched_phrases) == len(dict.fromkeys(phrases))

        matched = terms_matched and phrases_matched

        term_score = self._terms.count(
            unquoted_text,
            content,
        )

        phrase_score = 2 * len(matched_phrases)

        phrase_match_bonus = 1.0 if matched_phrases and not unquoted_text else 0.0

        score = float(term_score + phrase_score + phrase_match_bonus)

        return AdvancedMatch(
            matched=matched,
            score=score,
            matched_terms=matched_terms,
            matched_phrases=matched_phrases,
        )
