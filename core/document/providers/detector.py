from pathlib import Path


class FileTypeDetector:

    @staticmethod
    def detect(path: Path) -> str:

        suffix = path.suffix.lower()

        if suffix == ".pdf":
            return "application/pdf"

        if suffix == ".txt":
            return "text/plain"

        return "application/octet-stream"
