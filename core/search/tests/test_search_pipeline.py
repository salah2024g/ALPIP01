from core.search.repository.index_repository import IndexRepository
from core.search.services.chunking import DocumentChunker
from core.search.services.pipeline import SearchPipeline


def test_search_pipeline():

    repository = IndexRepository()

    chunker = DocumentChunker(chunk_size=3)

    pipeline = SearchPipeline(
        repository,
        chunker,
    )

    count = pipeline.index_document(
        "law_001",
        "one two three four five six",
    )

    assert count == 2

    assert len(repository.all_documents()) == 2
