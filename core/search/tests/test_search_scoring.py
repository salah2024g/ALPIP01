from core.search.backends.memory import MemorySearchBackend
from core.search.models.query import SearchQuery
from core.search.repository.index_repository import IndexRepository


def test_search_scores_multiple_occurrences() -> None:
    repository = IndexRepository()

    repository.save(
        "law_001",
        "tax law applies to tax income and tax returns",
    )

    backend = MemorySearchBackend(repository)

    results = backend.search(
        SearchQuery(text="tax"),
    )

    assert len(results) == 1
    assert results[0].document_id == "law_001"
    assert results[0].score == 3.0


def test_search_ignores_non_matching_documents() -> None:
    repository = IndexRepository()

    repository.save(
        "law_001",
        "income tax law",
    )

    repository.save(
        "law_002",
        "commercial law",
    )

    backend = MemorySearchBackend(repository)

    results = backend.search(
        SearchQuery(text="tax"),
    )

    assert len(results) == 1
    assert results[0].document_id == "law_001"


def test_search_respects_query_limit() -> None:
    repository = IndexRepository()

    for index in range(5):
        repository.save(
            f"law_{index}",
            "tax tax",
        )

    backend = MemorySearchBackend(repository)

    results = backend.search(
        SearchQuery(
            text="tax",
            limit=2,
        )
    )

    assert len(results) == 2
