from abc import ABC, abstractmethod

from core.search.models.query import SearchQuery, SearchResult


class SearchBackend(ABC):
    """Base interface for search execution."""

    @abstractmethod
    def search(self, query: SearchQuery) -> list[SearchResult]:
        """Execute a search."""
