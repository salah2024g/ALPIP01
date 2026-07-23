from core.ai.prompts.template import PromptTemplate


LEGAL_ANALYSIS_PROMPT = PromptTemplate(
    name="legal_analysis",
    content=(
        "Analyze the following legal text:\n"
        "{text}"
    )
)
