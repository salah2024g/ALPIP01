from core.search.tokenization.default import SearchTokenizer


def test_tokenizer_splits_terms() -> None:
    tokenizer = SearchTokenizer()

    assert tokenizer.tokenize("tax income law") == [
        "tax",
        "income",
        "law",
    ]


def test_tokenizer_normalizes_case() -> None:
    tokenizer = SearchTokenizer()

    assert tokenizer.tokenize("Tax LAW") == [
        "tax",
        "law",
    ]


def test_tokenizer_handles_repeated_whitespace() -> None:
    tokenizer = SearchTokenizer()

    assert tokenizer.tokenize("tax   income\tlaw") == [
        "tax",
        "income",
        "law",
    ]


def test_tokenizer_handles_empty_text() -> None:
    tokenizer = SearchTokenizer()

    assert tokenizer.tokenize("") == []


def test_tokenizer_handles_whitespace_only_text() -> None:
    tokenizer = SearchTokenizer()

    assert tokenizer.tokenize("   \t\n ") == []
