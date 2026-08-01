from core.plugins.registry import PluginRegistry


class DemoPlugin:
    name = "demo"


def test_register_plugin():

    registry = PluginRegistry()

    registry.register(DemoPlugin())

    assert registry.get("demo") is not None
