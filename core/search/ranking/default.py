from core.search.models.query import SearchResult
from core.search.ranking.base import RankingStrategy


class DefaultRankingStrategy(RankingStrategy):
    """
    Default ranking implementation.

    Sorts search results by score in descending order.
    """

    def rank(
        self,
        results: list[SearchResult],
    ) -> list[SearchResult]:
        return sorted(
            results,
            key=lambda item: item.score,
            reverse=True,
        )


DefaultRanking = DefaultRankingStrategy
