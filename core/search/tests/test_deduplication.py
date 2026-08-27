from core.search.deduplication.default import SearchResultDeduplicator
from core.search.models.query import SearchResult


def test_deduplicator_removes_duplicate_documents() -> None:
    deduplicator = SearchResultDeduplicator()

    results = deduplicator.deduplicate(
        [
            SearchResult("law-1", 2.0, "tax"),
            SearchResult("law-1", 2.0, "tax law"),
            SearchResult("law-2", 1.0, "income tax"),
        ]
    )

    assert [result.document_id for result in results] == [
        "law-1",
        "law-2",
    ]


def test_deduplicator_keeps_highest_score() -> None:
    deduplicator = SearchResultDeduplicator()

    results = deduplicator.deduplicate(
        [
            SearchResult("law-1", 1.0, "tax"),
            SearchResult("law-1", 4.0, "tax law"),
            SearchResult("law-1", 2.0, "tax regulation"),
        ]
    )

    assert len(results) == 1
    assert results[0].score == 4.0
    assert results[0].snippet == "tax law"


def test_deduplicator_is_deterministic() -> None:
    deduplicator = SearchResultDeduplicator()

    results = deduplicator.deduplicate(
        [
            SearchResult("law-3", 2.0, "tax"),
            SearchResult("law-1", 2.0, "tax"),
            SearchResult("law-2", 2.0, "tax"),
        ]
    )

    assert [result.document_id for result in results] == [
        "law-1",
        "law-2",
        "law-3",
    ]


def test_deduplicator_handles_empty_results() -> None:
    deduplicator = SearchResultDeduplicator()

    assert deduplicator.deduplicate([]) == []
