from abc import ABC, abstractmethod

from core.document.models.document import Document
from core.document.models.result import ProcessingResult


class DocumentProcessor(ABC):
    @abstractmethod
    def supports(self, document: Document) -> bool: ...

    @abstractmethod
    def process(self, document: Document) -> ProcessingResult: ...
