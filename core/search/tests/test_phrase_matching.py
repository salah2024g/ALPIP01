from core.search.matching.phrase import PhraseMatcher


def test_phrase_matcher_matches_phrase() -> None:
    matcher = PhraseMatcher()

    assert (
        matcher.matches(
            "income tax",
            "The income tax law applies.",
        )
        is True
    )


def test_phrase_matcher_is_case_insensitive() -> None:
    matcher = PhraseMatcher()

    assert (
        matcher.matches(
            "Income Tax",
            "INCOME TAX LAW",
        )
        is True
    )


def test_phrase_matcher_rejects_missing_phrase() -> None:
    matcher = PhraseMatcher()

    assert (
        matcher.matches(
            "income tax",
            "The corporate law applies.",
        )
        is False
    )


def test_phrase_matcher_empty_phrase() -> None:
    matcher = PhraseMatcher()

    assert matcher.matches("", "income tax law") is False


def test_phrase_matcher_counts_occurrences() -> None:
    matcher = PhraseMatcher()

    assert (
        matcher.count(
            "income tax",
            "income tax law; income tax regulation",
        )
        == 2
    )


def test_phrase_matcher_empty_phrase_count() -> None:
    matcher = PhraseMatcher()

    assert matcher.count("", "income tax law") == 0
