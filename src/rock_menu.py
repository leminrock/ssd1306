#!/usr/bin/env python3

import os
import networkx as nx
from rock_entities import Item, Page

# pages
MAINMENU = Item('ROOT', 0)
HOTSPOT = Item('HOTSPOT', 1)
PATCHES = Item('PATCHES', 1)

# HOTSPOT items
ACTIVATE = Item('ACTIVATE', 2)
DEACTIVATE = Item('DEACTIVATE', 2)

# patch path
PATCHESPATH = '../../patches'

# build graph

Graph = nx.DiGraph()

for _, _, files in os.walk(PATCHESPATH):
    for file in sorted(files):
        patch = Item(file, 2)
        Graph.add_edge(PATCHES, patch)

Graph.add_edges_from([(MAINMENU, HOTSPOT), (MAINMENU, PATCHES)])
Graph.add_edges_from([(HOTSPOT, ACTIVATE), (HOTSPOT, DEACTIVATE)])


def get_page(graph, node):
    return list(graph.successors(node))


def get_names(graph, node):
    return [x.name for x in get_page(graph, node)]


def get_back(graph, node)
    pred = list(graph.predecessors(node))
    return pred[0]
