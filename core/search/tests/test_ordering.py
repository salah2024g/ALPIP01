from core.search.models.query import SearchResult
from core.search.ordering.default import SearchResultOrdering


def test_search_result_ordering_by_score() -> None:
    ordering = SearchResultOrdering()

    results = [
        SearchResult("law-1", 1.0, "tax"),
        SearchResult("law-2", 3.0, "tax tax tax"),
        SearchResult("law-3", 2.0, "tax tax"),
    ]

    ordered = ordering.order(results)

    assert [result.document_id for result in ordered] == [
        "law-2",
        "law-3",
        "law-1",
    ]


def test_search_result_ordering_uses_document_id_as_tiebreaker() -> None:
    ordering = SearchResultOrdering()

    results = [
        SearchResult("law-3", 2.0, "tax"),
        SearchResult("law-1", 2.0, "tax"),
        SearchResult("law-2", 2.0, "tax"),
    ]

    ordered = ordering.order(results)

    assert [result.document_id for result in ordered] == [
        "law-1",
        "law-2",
        "law-3",
    ]


def test_search_result_ordering_does_not_mutate_input() -> None:
    ordering = SearchResultOrdering()

    results = [
        SearchResult("law-2", 2.0, "tax"),
        SearchResult("law-1", 3.0, "tax"),
    ]

    original_ids = [result.document_id for result in results]

    ordered = ordering.order(results)

    assert [result.document_id for result in results] == original_ids
    assert [result.document_id for result in ordered] == [
        "law-1",
        "law-2",
    ]


def test_search_result_ordering_empty() -> None:
    ordering = SearchResultOrdering()

    assert ordering.order([]) == []
