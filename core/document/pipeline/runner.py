from core.document.models.aldf import ALDFDocument
from core.document.pipeline.default_pipeline import build_pipeline
from core.document.logger import logger


def process_document(document):

    pipeline = build_pipeline()

    result = pipeline.run(document)

    if result.success:

        logger.info("Document processed successfully")

        return ALDFDocument(
            id=document.id,
            text=result.text,
            metadata=document.metadata
        )

    logger.error(result.errors)

    return None
