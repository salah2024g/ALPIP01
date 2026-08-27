from core.search.matching.advanced import AdvancedMatcher


def test_advanced_match_combines_terms() -> None:
    matcher = AdvancedMatcher()

    result = matcher.match(
        "tax income",
        "Income tax law",
    )

    assert result.matched is True
    assert result.matched_terms == ["tax", "income"]
    assert result.score == 2.0


def test_advanced_match_detects_phrase() -> None:
    matcher = AdvancedMatcher()

    result = matcher.match(
        '"income tax"',
        "The income tax law applies.",
    )

    assert result.matched is True
    assert result.matched_phrases == ["income tax"]
    assert result.score == 3.0


def test_advanced_match_is_deterministic() -> None:
    matcher = AdvancedMatcher()

    first = matcher.match(
        "tax income",
        "income tax law",
    )
    second = matcher.match(
        "tax income",
        "income tax law",
    )

    assert first == second


def test_advanced_match_rejects_empty_query() -> None:
    matcher = AdvancedMatcher()

    result = matcher.match(
        "",
        "tax law",
    )

    assert result.matched is False
    assert result.score == 0.0
    assert result.matched_terms == []
    assert result.matched_phrases == []
