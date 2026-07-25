from core.search.models.document import DocumentChunk


class DocumentChunker:
    """
    Splits legal documents into searchable chunks.
    """

    def __init__(self, chunk_size: int = 500):
        self.chunk_size = chunk_size

    def split(
        self,
        document_id: str,
        content: str,
    ) -> list[DocumentChunk]:

        chunks = []

        words = content.split()

        for index in range(0, len(words), self.chunk_size):
            chunk_words = words[index:index + self.chunk_size]

            chunks.append(
                DocumentChunk(
                    chunk_id=f"{document_id}_{index}",
                    document_id=document_id,
                    content=" ".join(chunk_words),
                    position=index,
                )
            )

        return chunks
