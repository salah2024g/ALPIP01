from abc import ABC, abstractmethod

from core.search.models.query import SearchResult


class RankingStrategy(ABC):
    """Base interface for ranking search results."""

    @abstractmethod
    def rank(
        self,
        results: list[SearchResult],
    ) -> list[SearchResult]:
        """Rank search results."""
