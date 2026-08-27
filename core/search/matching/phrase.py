from core.search.normalization.default import SearchTextNormalizer


class PhraseMatcher:
    """Deterministic phrase matching for legal search."""

    def __init__(self) -> None:
        self._normalizer = SearchTextNormalizer()

    def matches(
        self,
        phrase: str,
        content: str,
    ) -> bool:
        normalized_phrase = self._normalizer.normalize(phrase).strip()
        normalized_content = self._normalizer.normalize(content)

        if not normalized_phrase:
            return False

        return normalized_phrase in normalized_content

    def count(
        self,
        phrase: str,
        content: str,
    ) -> int:
        normalized_phrase = self._normalizer.normalize(phrase).strip()
        normalized_content = self._normalizer.normalize(content)

        if not normalized_phrase:
            return 0

        return normalized_content.count(normalized_phrase)
