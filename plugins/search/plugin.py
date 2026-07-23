from sdk.contracts.plugin import PluginContract


class SearchPlugin(PluginContract):


    @property
    def name(self):

        return "legal-search"


    def initialize(self):

        pass


    def execute(
        self,
        payload: dict
    ):

        return {
            "search": payload
        }
