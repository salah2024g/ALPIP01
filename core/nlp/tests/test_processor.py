from core.nlp.processors.text_processor import TextProcessor


def test_arabic_processing():

    result = TextProcessor().process(
        "نص قانوني"
    )

    assert len(
        result["tokens"]
    ) == 2
