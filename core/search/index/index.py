class SearchIndex:
    """
    Basic in-memory search index.

    This is the first implementation layer.
    Storage backend can be replaced later
    without changing the search interface.
    """

    def __init__(self) -> None:
        self._documents: dict[str, str] = {}

    def add(self, document_id: str, content: str = "") -> None:
        self._documents[document_id] = content

    def get(self, document_id: str) -> str | None:
        return self._documents.get(document_id)

    def all(self) -> list[str]:
        return list(self._documents.keys())

    def count(self) -> int:
        return len(self._documents)

    def clear(self) -> None:
        self._documents.clear()
