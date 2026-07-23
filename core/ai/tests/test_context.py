from core.ai.context.manager import AIContextManager


def test_context_creation():

    context = AIContextManager().build_context(
        ["document"]
    )

    assert "documents" in context
