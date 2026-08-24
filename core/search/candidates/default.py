from dataclasses import dataclass

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

    def _tokens(self, text: str) -> list[str]:
        return [token.strip().lower() for token in text.split() if token.strip()]

    def generate(
        self,
        query: SearchQuery,
    ) -> list[Candidate]:
        tokens = self._tokens(query.text)

        if not tokens:
            return []

        candidates: list[Candidate] = []

        for document_id in self._repository.all_documents():
            if not self._matches_filters(document_id, query):
                continue

            content = self._repository.find(document_id)

            if content is None:
                continue

            body = content.lower()

            if not all(token in body for token in tokens):
                continue

            score = sum(body.count(token) for token in tokens)

            candidates.append(
                Candidate(
                    document_id=document_id,
                    score=float(score),
                )
            )

        candidates.sort(
            key=lambda candidate: (
                -candidate.score,
                candidate.document_id,
            )
        )

        return candidates[: query.limit]
