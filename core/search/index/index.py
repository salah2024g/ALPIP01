class SearchIndex:


    def __init__(self):

        self.documents = []


    def add(
        self,
        document
    ):

        self.documents.append(
            document
        )


    def all(self):

        return self.documents
