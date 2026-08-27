import re


class SearchTokenizer:
    """Deterministic tokenization for legal search queries."""

    _TOKEN_PATTERN = re.compile(r"\S+")

    def tokenize(self, text: str) -> list[str]:
        return self._TOKEN_PATTERN.findall(text.strip().lower())
