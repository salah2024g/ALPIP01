from dataclasses import dataclass

from core.search.models.query import SearchQuery


@dataclass(slots=True)
class Candidate:
    document_id: str
    score: float


class CandidateGenerator:
    """Deterministic bounded candidate generation for legal search."""

    def __init__(self, repository) -> None:
        self._repository = repository

    def generate(
        self,
        query: SearchQuery,
    ) -> list[Candidate]:
        tokens = [
            token.strip().lower()
            for token in query.text.split()
            if token.strip()
        ]

        if not tokens:
            return []

        candidates: list[Candidate] = []

        for document_id in self._repository.all_documents():
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
