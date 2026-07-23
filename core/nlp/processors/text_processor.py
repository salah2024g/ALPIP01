from core.nlp.arabic.normalizer import ArabicTextNormalizer
from core.nlp.tokenizers.arabic_tokenizer import ArabicTokenizer


class TextProcessor:


    def __init__(self):

        self.normalizer = ArabicTextNormalizer()
        self.tokenizer = ArabicTokenizer()


    def process(
        self,
        text: str
    ) -> dict:

        normalized = self.normalizer.normalize(
            text
        )

        tokens = self.tokenizer.tokenize(
            normalized
        )

        return {
            "text": normalized,
            "tokens": tokens
        }
