from core.document.models.document import Document
from core.document.models.result import ProcessingResult
from core.document.processors.base import DocumentProcessor


class DocumentPipeline:

    def __init__(self):

        self._processors: list[DocumentProcessor] = []

    def register(self, processor: DocumentProcessor):

        self._processors.append(processor)

    def run(self, document: Document) -> ProcessingResult:

        for processor in self._processors:

            if processor.supports(document):

                return processor.process(document)

        return ProcessingResult(
            success=False,
            errors=["No processor available"]
        )
