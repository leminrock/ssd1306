# Nodes
from pages import mainmenu, webserver
#from soft.entities import Status
from common.cfg import MAINSTATUS


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

MAINSTATUS.current = MAINMENU
