from core.search.analysis.facets import SearchFacets
from core.search.models.document import SearchDocument
from core.search.models.metadata import DocumentMetadata


def test_search_facets_counts_metadata() -> None:
    documents = [
        SearchDocument(
            document_id="law-1",
            title="Income Tax Law",
            content="...",
            metadata=DocumentMetadata(
                document_type="law",
                jurisdiction="EG",
                language="ar",
            ),
        ),
        SearchDocument(
            document_id="law-2",
            title="Tax Regulation",
            content="...",
            metadata=DocumentMetadata(
                document_type="law",
                jurisdiction="EG",
                language="ar",
            ),
        ),
        SearchDocument(
            document_id="law-3",
            title="Court Decision",
            content="...",
            metadata=DocumentMetadata(
                document_type="judgment",
                jurisdiction="EG",
                language="ar",
            ),
        ),
    ]

    facets = SearchFacets.from_documents(documents)

    assert facets.get("document_type") == {
        "law": 2,
        "judgment": 1,
    }
    assert facets.get("jurisdiction") == {"EG": 3}
    assert facets.get("language") == {"ar": 3}


def test_search_facets_supports_dict_metadata() -> None:
    documents = [
        SearchDocument(
            document_id="law-1",
            title="Law",
            content="...",
            metadata={"document_type": "law"},
        ),
    ]

    facets = SearchFacets.from_documents(documents)

    assert facets.get("document_type") == {"law": 1}


def test_search_facets_missing_field() -> None:
    facets = SearchFacets.from_documents([])

    assert facets.get("document_type") == {}
