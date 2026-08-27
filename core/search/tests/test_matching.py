from core.search.matching.default import SearchTermMatcher


def test_match_returns_matching_query_terms() -> None:
    matcher = SearchTermMatcher()

    assert matcher.match(
        "tax income",
        "Income tax law",
    ) == ["tax", "income"]


def test_match_is_case_insensitive() -> None:
    matcher = SearchTermMatcher()

    assert matcher.match(
        "Tax LAW",
        "tax law",
    ) == ["tax", "law"]


def test_match_removes_duplicate_query_terms() -> None:
    matcher = SearchTermMatcher()

    assert matcher.match(
        "tax tax income",
        "tax income law",
    ) == ["tax", "income"]


def test_match_ignores_unmatched_terms() -> None:
    matcher = SearchTermMatcher()

    assert matcher.match(
        "tax regulation",
        "tax law",
    ) == ["tax"]


def test_matches_all_requires_all_terms() -> None:
    matcher = SearchTermMatcher()

    assert (
        matcher.matches_all(
            "tax income",
            "income tax law",
        )
        is True
    )

    assert (
        matcher.matches_all(
            "tax regulation",
            "income tax law",
        )
        is False
    )


def test_matches_all_rejects_empty_query() -> None:
    matcher = SearchTermMatcher()

    assert matcher.matches_all("", "tax law") is False
