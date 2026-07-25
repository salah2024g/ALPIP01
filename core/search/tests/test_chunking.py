from core.search.services.chunking import DocumentChunker


def test_document_chunking():

    chunker = DocumentChunker(
        chunk_size=3
    )

    chunks = chunker.split(
        "law_001",
        "one two three four five six"
    )

    assert len(chunks) == 2

    assert chunks[0].document_id == "law_001"
    assert chunks[0].content == "one two three"
