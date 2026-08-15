from core.search.backends.memory import MemorySearchBackend
from core.search.models.metadata import DocumentMetadata
from core.search.models.query import SearchQuery
from core.search.repository.index_repository import IndexRepository


def test_search_filters_by_document_type() -> None:
    repository = IndexRepository()

    repository.save(
        "law_001",
        "income tax law",
        title="Income Tax Law",
        metadata=DocumentMetadata(
            document_type="law",
            jurisdiction="EG",
        ),
    )

    repository.save(
        "reg_001",
        "income tax regulation",
        title="Income Tax Regulation",
        metadata=DocumentMetadata(
            document_type="regulation",
            jurisdiction="EG",
        ),
    )

    backend = MemorySearchBackend(repository)

    results = backend.search(
        SearchQuery(
            text="tax",
            filters={"document_type": "law"},
        )
    )

    assert len(results) == 1
    assert results[0].document_id == "law_001"


def test_search_filters_by_jurisdiction() -> None:
    repository = IndexRepository()

    repository.save(
        "eg_001",
        "tax law Egypt",
        metadata=DocumentMetadata(
            document_type="law",
            jurisdiction="EG",
        ),
    )

    repository.save(
        "other_001",
        "tax law other jurisdiction",
        metadata=DocumentMetadata(
            document_type="law",
            jurisdiction="OTHER",
        ),
    )

    backend = MemorySearchBackend(repository)

    results = backend.search(
        SearchQuery(
            text="tax",
            filters={"jurisdiction": "EG"},
        )
    )

    assert len(results) == 1
    assert results[0].document_id == "eg_001"


def test_search_respects_limit() -> None:
    repository = IndexRepository()

    for index in range(5):
        repository.save(
            f"law_{index}",
            "tax law",
            metadata=DocumentMetadata(
                document_type="law",
            ),
        )

    backend = MemorySearchBackend(repository)

    results = backend.search(
        SearchQuery(
            text="tax",
            limit=2,
        )
    )

    assert len(results) == 2
