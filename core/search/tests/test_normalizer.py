from core.search.query.normalizer import ArabicQueryNormalizer


def test_arabic_normalizer():
    text = "ضريبة الدخل"
    result = ArabicQueryNormalizer.normalize(text)

    assert result == "ضريبه الدخل"
