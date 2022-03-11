from pathlib import Path
from soft.entities import Item
from soft.graph_menu import GraphMenu
from patcher.patch import set_patch

# pages
MAINMENU = Item('ROOT')
HOTSPOT = Item('HOTSPOT')
PATCHES = Item('PATCHES')

# HOTSPOT items
ACTIVATE = Item('ACTIVATE')
DEACTIVATE = Item('DEACTIVATE')

# patch path
PATCHESPATH = Path('../../patches').resolve()
JACKDSERVICE = 'rock_jackd'
PDSERVICE = 'rock_puredata'

# build graph
Graph = GraphMenu()

files = list(PATCHESPATH.glob('*.pd'))

for file in sorted(files):
    patch = Item(file.stem, 2, path=file)
    patch.set_command(set_patch, file, JACKDSERVICE, PDSERVICE)
    Graph.one_to_one(PATCHES, patch)

Graph.one_to_many(MAINMENU, [HOTSPOT, PATCHES])
Graph.one_to_many(HOTSPOT, [ACTIVATE, DEACTIVATE])
