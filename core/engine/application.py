class ApplicationEngine:
    def __init__(self):
        self.plugins = []

    def register_plugin(self, plugin):
        self.plugins.append(plugin)

    def list_plugins(self):
        return [plugin.name for plugin in self.plugins]
