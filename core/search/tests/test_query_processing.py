import pytest

from core.search.query.normalizer import ArabicQueryNormalizer
from core.search.query.parser import LegalQueryParser


def test_arabic_query_normalizer_normalizes_arabic_forms() -> None:
    result = ArabicQueryNormalizer.normalize("  أإآ ى ة ـ ضريبة  ")

    assert result == "ااا ي ه  ضريبه"


def test_query_parser_normalizes_arabic_text() -> None:
    parser = LegalQueryParser()

    query = parser.parse("  ضريبة الدخل  ")

    assert query.text == "ضريبه الدخل"


def test_query_parser_normalizes_arabic_variants() -> None:
    parser = LegalQueryParser()

    query = parser.parse("  ضريبة الدخل وآخر مدة  ")

    assert query.text == "ضريبه الدخل واخر مده"


def test_query_parser_preserves_phrase_structure() -> None:
    parser = LegalQueryParser()

    query = parser.parse('  "ضريبة الدخل"  ')

    assert query.text == '"ضريبه الدخل"'


def test_query_parser_supports_mixed_term_and_phrase() -> None:
    parser = LegalQueryParser()

    query = parser.parse(' ضريبة "الدخل العام" ')

    assert query.text == 'ضريبه "الدخل العام"'


def test_query_parser_preserves_filters() -> None:
    parser = LegalQueryParser()

    filters = {
        "document_type": "law",
        "jurisdiction": "EG",
    }

    query = parser.parse(
        "ضريبة الدخل",
        filters=filters,
    )

    assert query.filters == filters


def test_query_parser_preserves_limit() -> None:
    parser = LegalQueryParser()

    query = parser.parse(
        "ضريبة",
        limit=25,
    )

    assert query.limit == 25


def test_query_parser_rejects_invalid_limit() -> None:
    parser = LegalQueryParser()

    with pytest.raises(ValueError, match="greater than zero"):
        parser.parse("ضريبة", limit=0)


def test_query_parser_rejects_invalid_filter_key() -> None:
    parser = LegalQueryParser()

    with pytest.raises(TypeError, match="filter keys must be strings"):
        parser.parse(
            "ضريبة",
            filters={123: "law"},  # type: ignore[dict-item]
        )


def test_query_parser_rejects_invalid_filter_value() -> None:
    parser = LegalQueryParser()

    with pytest.raises(
        TypeError,
        match="filter values must be strings",
    ):
        parser.parse(
            "ضريبة",
            filters={"document_type": 123},  # type: ignore[dict-item]
        )


def test_query_parser_empty_text_remains_empty() -> None:
    parser = LegalQueryParser()

    query = parser.parse("   ")

    assert query.text == ""
