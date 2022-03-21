from pathlib import Path
from soft.entities import Item, ItemMenu
from soft.graph_menu import GraphMenu
from patcher.patch import set_patch
# from net.hotspot import

"""
# pages
MAINMENU = Item('ROOT')
HOTSPOT = Item('HOTSPOT')
PATCHES = Item('PATCHES')

# HOTSPOT items
#ACTIVATE = Item('ACTIVATE')
#DEACTIVATE = Item('DEACTIVATE')

NETWORKSTATE = Item('ENABLE')

# patch path
PATCHESPATH = Path('../patches').resolve()
JACKDSERVICE = 'rock_jackd'
PDSERVICE = 'rock_puredata'

# build graph
Graph = GraphMenu()

dirs = list(PATCHESPATH.glob('*'))

for _dir in sorted(dirs):
    path = _dir / Path('main.pd')
    patch = Item(_dir.stem, 2, path=path)
    patch.set_command(set_patch, path, JACKDSERVICE, PDSERVICE)
    Graph.one_to_one(PATCHES, patch)

Graph.one_to_many(MAINMENU, [HOTSPOT, PATCHES])
#Graph.one_to_many(HOTSPOT, [ACTIVATE, DEACTIVATE])
Graph.one_to_one(HOTSPOT, NETWORKSTATE)
"""

MAINMENU = ItemMenu('MAIN')
SUBMENU1 = ItemMenu('SUB1', parent=MAINMENU)
SUBMENU2 = ItemMenu('SUB2', parent=SUBMENU1)

MAINMENU.children = SUBMENU1
SUBMENU1.children = SUBMENU2
