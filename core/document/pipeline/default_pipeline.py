from core.document.pipeline.pipeline import DocumentPipeline
from core.document.providers.pdf_processor import PDFProcessor


def build_pipeline():

    pipeline = DocumentPipeline()

    pipeline.register(
        PDFProcessor()
    )

    return pipeline
