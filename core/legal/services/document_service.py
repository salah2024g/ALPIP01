from core.legal.extractors.pdf import PDFExtractor


class LegalDocumentService:

    def __init__(self):

        self.extractor = PDFExtractor()


    def process(
        self,
        file_path: str
    ) -> dict:

        text = self.extractor.extract(
            file_path
        )

        return {
            "file": file_path,
            "text": text
        }
