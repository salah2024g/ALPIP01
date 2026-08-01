from core.search.index.index import SearchIndex


def test_search_index():

    index = SearchIndex()

    index.add("law_001", "tax law article one")

    assert len(index.all()) == 1
    assert index.get("law_001") == "tax law article one"
    assert index.count() == 1
