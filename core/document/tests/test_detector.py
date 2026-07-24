from pathlib import Path

from core.document.providers.detector import FileTypeDetector


def test_pdf_detection():

    assert (
        FileTypeDetector.detect(
            Path("law.pdf")
        )
        ==
        "application/pdf"
    )


def test_text_detection():

    assert (
        FileTypeDetector.detect(
            Path("notes.txt")
        )
        ==
        "text/plain"
    )
