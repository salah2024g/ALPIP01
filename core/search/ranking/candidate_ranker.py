from core.search.candidates.default import Candidate


class CandidateRanker:
    """Deterministic ranking of search candidates."""

    def rank(
        self,
        candidates: list[Candidate],
    ) -> list[Candidate]:
        return sorted(
            candidates,
            key=lambda candidate: (
                -candidate.score,
                candidate.document_id,
            ),
        )
