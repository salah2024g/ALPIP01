from core.search.index.index import SearchIndex


class IndexRepository:
    """
    Repository abstraction for search index storage.
    """

    def __init__(self) -> None:
        self.index = SearchIndex()

    def save(
        self,
        document_id: str,
        content: str,
    ) -> None:
        self.index.add(
            document_id,
            content,
        )

    def find(
        self,
        document_id: str,
    ) -> str | None:
        return self.index.get(document_id)

    def all_documents(self) -> list[str]:
        return self.index.all()

    def clear(self) -> None:
        self.index.clear()
