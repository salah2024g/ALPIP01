from core.legal_structure.parser.normalizer import (
    normalize_number
)


def test_arabic_digits():

    assert normalize_number(
        "١٢٣٤٥"
    ) == "12345"


def test_english_digits():

    assert normalize_number(
        "678"
    ) == "678"
