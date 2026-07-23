from sdk.contracts.plugin import PluginContract


class NLPPlugin(PluginContract):


    @property
    def name(self):

        return "arabic-nlp"


    def initialize(self):

        pass


    def execute(
        self,
        payload: dict
    ):

        return {
            "processed": True,
            "payload": payload
        }
