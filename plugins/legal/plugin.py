from sdk.contracts.plugin import PluginContract


class LegalPlugin(PluginContract):

    @property
    def name(self):

        return "legal-domain"


    def initialize(self):

        pass


    def execute(
        self,
        payload: dict
    ):

        return {
            "status": "processed",
            "payload": payload
        }
