from core.search.repository.index_repository import IndexRepository
from core.search.services.chunking import DocumentChunker


class SearchPipeline:
    """
    Converts documents into searchable indexed chunks.
    """

    def __init__(
        self,
        repository: IndexRepository,
        chunker: DocumentChunker,
    ) -> None:
        self.repository = repository
        self.chunker = chunker

    def index_document(
        self,
        document_id: str,
        content: str,
    ) -> int:

        chunks = self.chunker.split(
            document_id,
            content,
        )

        for chunk in chunks:
            self.repository.save(
                chunk.chunk_id,
                chunk.content,
            )

        return len(chunks)
