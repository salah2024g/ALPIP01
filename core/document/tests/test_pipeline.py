from pathlib import Path

from core.document.models.document import Document
from core.document.pipeline.default_pipeline import build_pipeline


def test_pipeline_creation():

    pipeline = build_pipeline()

    assert pipeline is not None


def test_document_model():

    document = Document(
        id="1",
        path=Path("sample.pdf"),
        media_type="application/pdf"
    )

    assert document.id == "1"
