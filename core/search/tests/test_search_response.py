from core.search.models.query import SearchResult
from core.search.response.default import SearchResponse


def test_search_response_from_results() -> None:
    results = [
        SearchResult(
            document_id="law-1",
            score=2.0,
            snippet="tax law",
        ),
        SearchResult(
            document_id="law-2",
            score=1.0,
            snippet="income tax",
        ),
    ]

    response = SearchResponse.from_results(results)

    assert response.results == results
    assert response.total == 2
    assert response.is_empty() is False


def test_search_response_empty() -> None:
    response = SearchResponse.from_results([])

    assert response.results == []
    assert response.total == 0
    assert response.is_empty() is True


def test_search_response_copies_results() -> None:
    results = [
        SearchResult(
            document_id="law-1",
            score=1.0,
            snippet="tax law",
        )
    ]

    response = SearchResponse.from_results(results)
    results.clear()

    assert len(response.results) == 1
    assert response.total == 1
