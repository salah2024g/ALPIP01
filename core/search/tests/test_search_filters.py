from core.search.models.query import SearchQuery


def test_search_query_filters() -> None:
    query = SearchQuery(
        text="tax",
        filters={"document_type": "law"},
    )

    assert query.filters["document_type"] == "law"
