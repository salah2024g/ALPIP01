import fitz
from pypdf import PdfReader
from pypdf.errors import PdfReadError

from core.document.models.document import Document
from core.document.models.result import ProcessingResult
from core.document.processors.base import DocumentProcessor


class PDFProcessor(DocumentProcessor):
    def supports(self, document: Document) -> bool:
        return document.media_type == "application/pdf"

    def process(self, document: Document) -> ProcessingResult:
        try:
            pdf = fitz.open(document.path)
            pages = [page.get_text() for page in pdf]

            document.metadata["pages"] = len(pdf)

            return ProcessingResult(
                success=True,
                text="\n".join(pages),
            )

        except (fitz.FileDataError, OSError, ValueError):
            try:
                reader = PdfReader(str(document.path))
                pages = [page.extract_text() or "" for page in reader.pages]

                document.metadata["pages"] = len(reader.pages)

                return ProcessingResult(
                    success=True,
                    text="\n".join(pages),
                )

            except (PdfReadError, OSError, ValueError) as exc:
                return ProcessingResult(
                    success=False,
                    errors=[str(exc)],
                )
