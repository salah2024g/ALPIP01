from core.search.backends.exact import ExactSearchBackend
from core.search.models.query import SearchQuery
from core.search.ranking.default import DefaultRankingStrategy
from core.search.repository.index_repository import IndexRepository
from core.search.services.search import SearchService


def test_search_service():
    repository = IndexRepository()

    repository.save(
        "tax_001",
        "income tax law article",
    )

    backend = ExactSearchBackend(repository)
    ranking = DefaultRankingStrategy()

    service = SearchService(
        backend=backend,
        ranking=ranking,
    )

    results = service.search(SearchQuery(text="tax"))

    assert len(results) == 1
    assert results[0].document_id == "tax_001"
