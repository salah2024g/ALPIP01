from core.search.candidates.default import Candidate
from core.search.limits.default import CandidateLimiter


def test_candidate_limiter_limits_results() -> None:
    limiter = CandidateLimiter()

    candidates = [
        Candidate("law-1", 5.0),
        Candidate("law-2", 4.0),
        Candidate("law-3", 3.0),
    ]

    result = limiter.limit(candidates, 2)

    assert result == [
        Candidate("law-1", 5.0),
        Candidate("law-2", 4.0),
    ]


def test_candidate_limiter_returns_all_when_limit_is_larger() -> None:
    limiter = CandidateLimiter()

    candidates = [
        Candidate("law-1", 2.0),
        Candidate("law-2", 1.0),
    ]

    result = limiter.limit(candidates, 10)

    assert result == candidates


def test_candidate_limiter_rejects_non_positive_limit() -> None:
    limiter = CandidateLimiter()

    candidates = [
        Candidate("law-1", 2.0),
        Candidate("law-2", 1.0),
    ]

    assert limiter.limit(candidates, 0) == []
    assert limiter.limit(candidates, -1) == []


def test_candidate_limiter_does_not_modify_input() -> None:
    limiter = CandidateLimiter()

    candidates = [
        Candidate("law-1", 2.0),
        Candidate("law-2", 1.0),
    ]

    result = limiter.limit(candidates, 1)

    assert candidates == [
        Candidate("law-1", 2.0),
        Candidate("law-2", 1.0),
    ]
    assert result == [Candidate("law-1", 2.0)]
