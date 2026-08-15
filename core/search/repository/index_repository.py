from core.search.index.index import SearchIndex
from core.search.models.document import SearchDocument
from core.search.models.metadata import DocumentMetadata


class IndexRepository:
    """Repository abstraction for search index storage."""

    def __init__(self) -> None:
        self.index = SearchIndex()
        self._documents: dict[str, SearchDocument] = {}

    def save(
        self,
        document_id: str,
        content: str,
        title: str = "",
        metadata: DocumentMetadata | None = None,
    ) -> None:
        document_metadata = metadata or DocumentMetadata()

        self.index.add(
            document_id,
            content,
        )

        self._documents[document_id] = SearchDocument(
            document_id=document_id,
            title=title,
            content=content,
            metadata=document_metadata,
        )

    def find(
        self,
        document_id: str,
    ) -> str | None:
        return self.index.get(document_id)

    def get_document(
        self,
        document_id: str,
    ) -> SearchDocument | None:
        return self._documents.get(document_id)

    def all_documents(self) -> list[str]:
        return self.index.all()

    def clear(self) -> None:
        self.index.clear()
        self._documents.clear()
