from sdk.contracts.plugin import PluginContract


class SamplePlugin(PluginContract):
    @property
    def name(self):
        return "sample"

    def initialize(self):
        pass

    def execute(self, payload: dict):
        return {"received": payload}
