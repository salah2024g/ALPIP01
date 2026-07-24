from pathlib import Path

from pypdf import PdfReader

from core.document.models.document import Document
from core.document.models.result import ProcessingResult
from core.document.processors.base import DocumentProcessor


class PDFProcessor(DocumentProcessor):

    def supports(
        self,
        document: Document
    ) -> bool:

        return document.media_type == "application/pdf"


    def process(
        self,
        document: Document
    ) -> ProcessingResult:

        try:

            reader = PdfReader(
                str(document.path)
            )

            pages = []

            for page in reader.pages:

                pages.append(
                    page.extract_text() or ""
                )

            document.metadata["pages"] = len(reader.pages)

            return ProcessingResult(
                success=True,
                text="\n".join(pages)
            )

        except Exception as exc:

            return ProcessingResult(
                success=False,
                errors=[str(exc)]
            )
