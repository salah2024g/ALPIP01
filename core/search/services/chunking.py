from core.search.models.document_chunk import DocumentChunk


class DocumentChunker:


    def chunk(
        self,
        document_id: int,
        text: str,
        size: int = 200
    ):

        words = text.split()

        chunks = []

        for index in range(
            0,
            len(words),
            size
        ):

            content = " ".join(
                words[index:index + size]
            )

            chunks.append(
                DocumentChunk(
                    document_id=document_id,
                    content=content,
                    position=index
                )
            )

        return chunks
