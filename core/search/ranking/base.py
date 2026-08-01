from abc import ABC, abstractmethod

from core.search.models.query import SearchResult


class RankingStrategy(ABC):
    """
    Interface for search result ranking.
    """

    @abstractmethod
    def rank(
        self,
        results: list[SearchResult],
    ) -> list[SearchResult]:
        """
        Rank search results.
        """
        ...
