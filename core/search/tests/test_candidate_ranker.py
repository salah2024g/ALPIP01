from core.search.candidates.default import Candidate
from core.search.ranking.candidate_ranker import CandidateRanker


def test_candidate_ranker_orders_by_score() -> None:
    ranker = CandidateRanker()

    candidates = [
        Candidate("law-3", 1.0),
        Candidate("law-1", 3.0),
        Candidate("law-2", 2.0),
    ]

    result = ranker.rank(candidates)

    assert [candidate.document_id for candidate in result] == [
        "law-1",
        "law-2",
        "law-3",
    ]


def test_candidate_ranker_uses_document_id_as_tiebreaker() -> None:
    ranker = CandidateRanker()

    candidates = [
        Candidate("law-3", 2.0),
        Candidate("law-1", 2.0),
        Candidate("law-2", 2.0),
    ]

    result = ranker.rank(candidates)

    assert [candidate.document_id for candidate in result] == [
        "law-1",
        "law-2",
        "law-3",
    ]


def test_candidate_ranker_does_not_modify_input() -> None:
    ranker = CandidateRanker()

    candidates = [
        Candidate("law-2", 1.0),
        Candidate("law-1", 2.0),
    ]

    original = list(candidates)

    ranker.rank(candidates)

    assert candidates == original
