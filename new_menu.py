# pylint: disable=missing-function-docstring
#!/usr/bin/env python3

import os
import networkx as nx

# pages
MAINMENU = 'ROOT'
HOTSPOT = 'HOTSPOT'
PATCHES = 'PATCHES'

# HOTSPOT items
ACTIVATE = 'ACTIVATE'
DEACTIVATE = 'DEACTIVATE'


G = nx.DiGraph()

class Item:
    """item class"""
    def __init__(self, name, level):
        self._name = name
        self._level = level

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level


class Page:
    def __init__(self, name):
        self._name = name 
        self._level = level

    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level


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
