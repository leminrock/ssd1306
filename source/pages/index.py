# Nodes
from common.cfg import MAINSTATUS
from pages import mainmenu, webserver

"""
MAINMENU = ItemMenu('MAIN')
WEBSERVER = ItemMenu('ACTIVE WEBSERVER', parent=MAINMENU)
MIDI = ItemApp('MIDI', parent=MAINMENU)
HOTSPOT = ItemApp('ACTIVE HOTSPOT', parent=MAINMENU)
WIFI = ItemApp('START WIFI', parent=MAINMENU)
PATCHES = ItemPatch('PATCHES', parent=MAINMENU)
"""

"""
MAINMENU = mainmenu.MAINMENU
WEBSERVER = webserver.WEBSERVER

MAINMENU.children = WEBSERVER

mainstatus = Status(current=MAINMENU)
"""

MAINMENU = mainmenu.MAINMENU
WEBSERVER = webserver.WEBSERVER

MAINMENU.children = WEBSERVER
WEBSERVER.parent = MAINMENU

MAINSTATUS.current = MAINMENU
