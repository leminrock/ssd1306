#!/usr/bin/env python3

import os
import networkx as nx

G = nx.DiGraph()

class Item:
    def __init__(self, name, level):
        self._name = name
        self._level = level

MAINMENU = 'root'

# main menu items

HOTSPOT = 'HOTSPOT'
PATCHES = 'PATCHES'

# HOTSPOT items

ACTIVATE = 'ACTIVATE'
DEACTIVATE = 'DEACTIVATE'

# PATCHES items

for _,_,files in os.walk('../patches'):
    for file in sorted(files):
        G.add_edge(PATCHES, file)

G.add_edges_from([(MAINMENU, HOTSPOT),(MAINMENU, PATCHES)])
G.add_edges_from([(HOTSPOT, ACTIVATE),(HOTSPOT, DEACTIVATE)])

print(list(G.successors(MAINMENU)))
print(list(G.successors(HOTSPOT)))
print(list(G.successors(PATCHES)))

print(list(G.predecessors('p1.pd')))
