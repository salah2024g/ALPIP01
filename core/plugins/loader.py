from core.plugins.registry import PluginRegistry


class PluginLoader:

    def __init__(self):
        self.registry = PluginRegistry()


    def load(self, plugin):
        plugin.initialize()
        self.registry.register(plugin)
