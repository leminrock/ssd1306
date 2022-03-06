#!/usr/bin/env python3

import os
import networkx as nx
from soft.entities import Item, Page

# pages
MAINMENU = Item('ROOT', 0, back=None)
HOTSPOT = Item('HOTSPOT', 1, back=True)
PATCHES = Item('PATCHES', 1, back=True)

# HOTSPOT items
ACTIVATE = Item('ACTIVATE', 2, back=True)
DEACTIVATE = Item('DEACTIVATE', 2, back=True)

# patch path
PATCHESPATH = '../../patches'

# build graph

Graph = nx.DiGraph()

files = os.walk(PATCHESPATH).__next__()[2]
absolute_path = os.path.abspath(PATCHESPATH)

for file in sorted(files):
    patch = Item(file, 2, path=absolute_path + '/' + file, back=False)
    Graph.add_edge(PATCHES, patch)

Graph.add_edges_from([(MAINMENU, HOTSPOT), (MAINMENU, PATCHES)])
Graph.add_edges_from([(HOTSPOT, ACTIVATE), (HOTSPOT, DEACTIVATE)])


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
    return len(graph.in_edgeges(node)) > 0
