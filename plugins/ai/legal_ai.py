from sdk.contracts.plugin import PluginContract


class LegalAIPlugin(PluginContract):
    @property
    def name(self):

        return "legal-ai"

    def initialize(self):

        pass

    def execute(self, payload: dict):

        return {"analysis": payload}
