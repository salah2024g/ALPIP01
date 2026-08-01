from core.search.repository.index_repository import IndexRepository
from core.search.services.chunking import DocumentChunker
from core.search.services.legal_indexer import LegalDocumentIndexer
from core.search.services.pipeline import SearchPipeline


def test_legal_document_indexer():

    repository = IndexRepository()

    pipeline = SearchPipeline(
        repository,
        DocumentChunker(chunk_size=50),
    )

    indexer = LegalDocumentIndexer(pipeline)

    count = indexer.index(
        "tax_law_001",
        "Income Tax Law",
        "Article one contains tax rules",
    )

    assert count == 1

    documents = repository.all_documents()

    assert len(documents) == 1
