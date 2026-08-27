import re


class SearchTextNormalizer:
    """Deterministic normalization for legal search text."""

    _WHITESPACE = re.compile(r"\s+")

    def normalize(self, text: str) -> str:
        normalized = text.strip().lower()
        normalized = self._WHITESPACE.sub(" ", normalized)
        return normalized
