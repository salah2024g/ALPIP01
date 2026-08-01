from core.search.repository.index_repository import IndexRepository


def test_index_repository():

    repository = IndexRepository()

    repository.save(
        "law_001",
        "tax article",
    )

    assert repository.find("law_001") == "tax article"

    assert repository.all_documents() == ["law_001"]
