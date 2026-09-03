from core.search.models.query import SearchQuery, SearchResult
from core.search.query.normalizer import ArabicQueryNormalizer
from core.search.services.search import SearchService


class SearchPipeline:
    """
    Search execution pipeline.

    Flow:
    Query
      |
    Normalize
      |
    SearchService
      |
    Results
    """

    def __init__(
        self,
        service: SearchService,
    ) -> None:
        self._service = service

    def execute(
        self,
        query: SearchQuery,
    ) -> list[SearchResult]:
        normalized_text = ArabicQueryNormalizer.normalize(query.text)

        normalized_query = SearchQuery(
            text=normalized_text,
            filters=dict(query.filters),
            limit=query.limit,
        )

        return self._service.search(normalized_query)
