from core.search.matching.default import SearchTermMatcher
from core.search.matching.phrase import PhraseMatcher


class BooleanMatcher:
    """Deterministic boolean matching for legal search."""

    def __init__(self) -> None:
        self._terms = SearchTermMatcher()
        self._phrases = PhraseMatcher()

    def matches_all(
        self,
        query_text: str,
        content: str,
    ) -> bool:
        return self._terms.matches_all(query_text, content)

    def matches_phrase(
        self,
        phrase: str,
        content: str,
    ) -> bool:
        return self._phrases.matches(phrase, content)

    def matches_any(
        self,
        query_text: str,
        content: str,
    ) -> bool:
        tokens = query_text.split()

        if not tokens:
            return False

        return any(self._terms.match(token, content) for token in tokens)
