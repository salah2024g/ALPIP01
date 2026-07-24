from core.legal_reference.parser.parser import (
    LegalReferenceParser,
)


def test_article_reference():

    parser = LegalReferenceParser()

    refs = parser.parse(
        "تطبق أحكام المادة (١٥) مع مراعاة المادة 27."
    )

    assert len(refs) == 2

    assert refs[0].article_number == "15"

    assert refs[1].article_number == "27"
