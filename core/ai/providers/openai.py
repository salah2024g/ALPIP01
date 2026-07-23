from core.ai.providers.base import LLMProvider


class OpenAIProvider(LLMProvider):


    def generate(
        self,
        prompt: str,
        context: dict | None = None
    ) -> str:

        return (
            "OpenAI provider placeholder: "
            + prompt
        )
