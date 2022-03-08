import networkx as nx
from pathlib import Path
from soft.entities import Item

# pages
MAINMENU = Item('ROOT', 0, back=False)
HOTSPOT = Item('HOTSPOT', 1, back=True)
PATCHES = Item('PATCHES', 1, back=True)

# HOTSPOT items
ACTIVATE = Item('ACTIVATE', 2, back=True)
DEACTIVATE = Item('DEACTIVATE', 2, back=True)

# patch path
PATCHESPATH = Path('../../patches').resolve()

# build graph

Graph = nx.DiGraph()
files = list(PATCHESPATH.glob('*.pd'))

for file in sorted(files):
    patch = Item(file.stem, 2, path=file, back=False)
    Graph.add_edge(PATCHES, patch)

Graph.add_edge(PATCHES, Item('back'))


def one_to_many(_from, _to):
    links = [(_from, x) for x in _to]
    Graph.add_edges_from(links)


one_to_many(MAINMENU, [HOTSPOT, PATCHES])
one_to_many(HOTSPOT, [ACTIVATE, DEACTIVATE, Item('back')])


def get_nodes(graph, node):
    return list(graph.successors(node))


def get_names(graph, node):
    return [x.name for x in get_nodes(graph, node)]


def get_back(graph, node):
    pred = list(graph.predecessors(node))
    return pred[0]


def is_leave(graph, node):
    return len(graph.out_edges(node)) == 0


def is_child(graph, node):
    return len(graph.in_edges(node)) > 0
