from core.ai.providers.base import LLMProvider


class LocalLLMProvider(LLMProvider):


    def generate(
        self,
        prompt: str,
        context: dict | None = None
    ) -> str:

        return (
            "Local model response placeholder: "
            + prompt
        )
