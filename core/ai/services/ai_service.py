class AIService:


    def __init__(
        self,
        provider
    ):

        self.provider = provider


    def ask(
        self,
        prompt: str,
        context: dict | None = None
    ) -> str:

        return self.provider.generate(
            prompt,
            context
        )
