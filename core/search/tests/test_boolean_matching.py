from core.search.matching.boolean import BooleanMatcher


def test_boolean_matches_all_terms() -> None:
    matcher = BooleanMatcher()

    assert (
        matcher.matches_all(
            "tax income",
            "income tax law",
        )
        is True
    )


def test_boolean_matches_any_term() -> None:
    matcher = BooleanMatcher()

    assert (
        matcher.matches_any(
            "tax regulation",
            "income tax law",
        )
        is True
    )


def test_boolean_rejects_when_no_terms_match() -> None:
    matcher = BooleanMatcher()

    assert (
        matcher.matches_any(
            "regulation statute",
            "income tax law",
        )
        is False
    )


def test_boolean_matches_phrase() -> None:
    matcher = BooleanMatcher()

    assert (
        matcher.matches_phrase(
            "income tax",
            "The income tax law applies.",
        )
        is True
    )


def test_boolean_rejects_empty_query() -> None:
    matcher = BooleanMatcher()

    assert matcher.matches_any("", "tax law") is False
