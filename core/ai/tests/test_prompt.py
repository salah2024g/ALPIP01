from core.ai.prompts.template import PromptTemplate


def test_prompt_render():

    prompt = PromptTemplate(name="test", content="Hello {name}")

    result = prompt.render({"name": "ALPIP"})

    assert result == "Hello ALPIP"
