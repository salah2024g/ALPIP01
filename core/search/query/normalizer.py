class ArabicQueryNormalizer:
    """
    Normalize Arabic legal search queries.
    """

    @staticmethod
    def normalize(text: str) -> str:
        text = text.strip()

        replacements = {
            "أ": "ا",
            "إ": "ا",
            "آ": "ا",
            "ى": "ي",
            "ة": "ه",
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        text = text.replace("ـ", "")

        return text.lower()
