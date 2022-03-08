from pathlib import Path
from soft.entities import Item
from soft.graph_menu import GraphMenu

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

Graph = GraphMenu()

files = list(PATCHESPATH.glob('*.pd'))

for file in sorted(files):
    patch = Item(file.stem, 2, path=file, back=False)
    Graph.one_to_one(PATCHES, patch)

Graph.one_to_one(PATCHES, Item('back'))
Graph.one_to_many(MAINMENU, [HOTSPOT, PATCHES])
Graph.one_to_many(HOTSPOT, [ACTIVATE, DEACTIVATE, Item('back')])
