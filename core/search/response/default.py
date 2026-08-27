from dataclasses import dataclass, field

from core.search.models.query import SearchResult


@dataclass(slots=True)
class SearchResponse:
    """Deterministic search response container."""

    results: list[SearchResult] = field(default_factory=list)
    total: int = 0

    @classmethod
    def from_results(
        cls,
        results: list[SearchResult],
    ) -> "SearchResponse":
        return cls(
            results=list(results),
            total=len(results),
        )

    def is_empty(self) -> bool:
        return not self.results
