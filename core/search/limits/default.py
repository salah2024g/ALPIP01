from core.search.candidates.default import Candidate


class CandidateLimiter:
    """Deterministic candidate limiting."""

    def limit(
        self,
        candidates: list[Candidate],
        limit: int,
    ) -> list[Candidate]:
        if limit <= 0:
            return []

        return candidates[:limit]
