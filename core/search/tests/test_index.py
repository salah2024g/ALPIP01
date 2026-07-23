from core.search.index.index import SearchIndex


def test_search_index():

    index = SearchIndex()

    index.add(
        "document"
    )

    assert len(
        index.all()
    ) == 1
