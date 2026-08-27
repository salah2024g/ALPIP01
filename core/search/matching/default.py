from core.search.tokenization.default import SearchTokenizer


class SearchTermMatcher:
    """Deterministic token matching for legal search."""

    def __init__(self) -> None:
        self._tokenizer = SearchTokenizer()

    def match(
        self,
        query_text: str,
        content: str,
    ) -> list[str]:
        query_tokens = self._tokenizer.tokenize(query_text)
        content_tokens = set(self._tokenizer.tokenize(content))

        return [
            token for token in dict.fromkeys(query_tokens) if token in content_tokens
        ]

    def matches_all(
        self,
        query_text: str,
        content: str,
    ) -> bool:
        query_tokens = self._tokenizer.tokenize(query_text)

        if not query_tokens:
            return False

        content_tokens = set(self._tokenizer.tokenize(content))

        return all(token in content_tokens for token in query_tokens)
