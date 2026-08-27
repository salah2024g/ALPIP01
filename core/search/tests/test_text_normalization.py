from core.search.normalization.default import SearchTextNormalizer


def test_normalizer_strips_outer_whitespace() -> None:
    normalizer = SearchTextNormalizer()

    assert normalizer.normalize("  tax law  ") == "tax law"


def test_normalizer_collapses_whitespace() -> None:
    normalizer = SearchTextNormalizer()

    assert normalizer.normalize("tax   income\tlaw") == "tax income law"


def test_normalizer_is_case_insensitive() -> None:
    normalizer = SearchTextNormalizer()

    assert normalizer.normalize("Tax LAW") == "tax law"


def test_normalizer_handles_empty_text() -> None:
    normalizer = SearchTextNormalizer()

    assert normalizer.normalize("") == ""


def test_normalizer_handles_whitespace_only_text() -> None:
    normalizer = SearchTextNormalizer()

    assert normalizer.normalize("   \t\n  ") == ""
