import networkx as nx


class GraphMenu:
    def __init__(self):
        self.Graph = nx.DiGraph()

    def one_to_one(self, _from, _to):
        self.Graph.add_edge(_from, _to)

    def one_to_many(self, _from, _to):
        links = [(_from, x) for x in _to]
        self.Graph.add_edges_from(links)

    def get_nodes(self, node):
        return list(self.Graph.successors(node))

    def get_names(self, node):
        return [x.name for x in self.get_nodes(node)]

    def is_leaf(self, node):
        return len(self.Graph.out_edges(node)) == 0

    def is_child(self, node):
        return len(self.Graph.in_edges(node)) > 0

    def get_back(self, node):
        pred = list(self.Graph.predecessors(node))
        return pred[0]
