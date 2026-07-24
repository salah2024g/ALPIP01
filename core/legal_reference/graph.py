from collections import defaultdict


class ReferenceGraph:

    def __init__(self):

        self.graph = defaultdict(set)


    def add_edge(
        self,
        source: str,
        target: str
    ):

        self.graph[source].add(target)


    def neighbors(
        self,
        node: str
    ):

        return sorted(
            self.graph.get(node, set())
        )
