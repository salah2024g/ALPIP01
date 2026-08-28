from dataclasses import dataclass

from core.search.matching.advanced import AdvancedMatcher
from core.search.models.query import SearchQuery
from core.search.repository.index_repository import IndexRepository


@dataclass(slots=True)
class Candidate:
    document_id: str
    score: float


class CandidateGenerator:
    """Deterministic bounded candidate generation for legal search."""

    def __init__(self, repository: IndexRepository) -> None:
        self._repository = repository
        self._matcher = AdvancedMatcher()

    def _matches_filters(
        self,
        document_id: str,
        query: SearchQuery,
    ) -> bool:
        if not query.filters:
            return True

        document = self._repository.get_document(document_id)

        if document is None:
            return False

        for key, expected in query.filters.items():
            value = getattr(document.metadata, key, None)

            if value != expected:
                return False

        return True

    def generate(
        self,
        query: SearchQuery,
    ) -> list[Candidate]:
        if not query.text.strip():
            return []

        candidates: list[Candidate] = []

        for document_id in self._repository.all_documents():
            if not self._matches_filters(document_id, query):
                continue

            content = self._repository.find(document_id)

            if content is None:
                continue

            result = self._matcher.match(
                query.text,
                content,
            )

            if not result.matched:
                continue

            candidates.append(
                Candidate(
                    document_id=document_id,
                    score=result.score,
                )
            )

        candidates.sort(
            key=lambda candidate: (
                -candidate.score,
                candidate.document_id,
            )
        )

        return candidates[: query.limit]
