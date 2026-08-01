from core.legal_reference.parser.external_parser import ExternalReferenceParser


def test_external_references():

    parser = ExternalReferenceParser()

    text = """

يعمل بأحكام القانون رقم 206 لسنة 2020.

وتطبق اللائحة التنفيذية.

ويصدر قرار الوزير رقم 399 لسنة 2021.

"""

    refs = parser.parse(text)

    assert len(refs) == 3

    assert refs[0].reference_type == "law"

    assert refs[0].law_number == "206"

    assert refs[0].year == "2020"

    assert refs[1].reference_type == "regulation"

    assert refs[2].reference_type == "decision"
