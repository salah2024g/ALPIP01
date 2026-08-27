import pytest

from core.search.models.query import SearchQuery
from core.search.validation.default import SearchQueryValidator


def test_query_validator_accepts_valid_query() -> None:
    validator = SearchQueryValidator()

    validator.validate(
        SearchQuery(
            text="tax law",
            filters={"document_type": "law"},
            limit=10,
        )
    )


def test_query_validator_rejects_non_positive_limit() -> None:
    validator = SearchQueryValidator()

    with pytest.raises(ValueError, match="greater than zero"):
        validator.validate(SearchQuery(text="tax", limit=0))


def test_query_validator_rejects_non_string_text() -> None:
    validator = SearchQueryValidator()

    query = SearchQuery(text="tax")
    query.text = 123  # type: ignore[assignment]

    with pytest.raises(TypeError, match="query.text must be a string"):
        validator.validate(query)


def test_query_validator_rejects_non_string_filter_key() -> None:
    validator = SearchQueryValidator()

    query = SearchQuery(
        text="tax",
        filters={"document_type": "law"},
    )
    query.filters[123] = "law"  # type: ignore[index]

    with pytest.raises(TypeError, match="filter keys must be strings"):
        validator.validate(query)


def test_query_validator_rejects_non_string_filter_value() -> None:
    validator = SearchQueryValidator()

    query = SearchQuery(
        text="tax",
        filters={"document_type": "law"},
    )
    query.filters["document_type"] = 123  # type: ignore[assignment]

    with pytest.raises(TypeError, match="filter values must be strings"):
        validator.validate(query)
