from core.search.backends.base import SearchBackend
from core.search.models.query import SearchQuery, SearchResult
from core.search.ranking.base import RankingStrategy


class SearchService:
    """
    Search service using backend and ranking abstractions.
    """

    def __init__(
        self,
        backend: SearchBackend,
        ranking: RankingStrategy,
    ) -> None:
        self._backend = backend
        self._ranking = ranking

    def search(
        self,
        query: SearchQuery,
    ) -> list[SearchResult]:
        results = self._backend.search(query)

        return self._ranking.rank(results)
