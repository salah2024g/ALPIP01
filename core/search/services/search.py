class SearchService:


    def __init__(
        self,
        index
    ):

        self.index = index


    def search(
        self,
        query: str
    ):

        results = []

        for document in self.index.all():

            if query in document.content:

                results.append(
                    document
                )

        return results
