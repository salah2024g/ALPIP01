from core.search.backends.memory import MemorySearchBackend
from core.search.models.query import SearchQuery
from core.search.pipeline.pipeline import SearchPipeline
from core.search.ranking.default import DefaultRanking
from core.search.repository.index_repository import IndexRepository
from core.search.services.search import SearchService


def test_search_pipeline():

    repository = IndexRepository()

    backend = MemorySearchBackend(repository)

    repository.save(
        "tax_001",
        "ضريبه الدخل",
    )

    service = SearchService(
        backend,
        DefaultRanking(),
    )

    pipeline = SearchPipeline(service)

    results = pipeline.execute(SearchQuery(text="ضريبة الدخل"))

    assert len(results) == 1
    assert results[0].document_id == "tax_001"
