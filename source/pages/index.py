# Nodes
from common.cfg import MAINSTATUS
#from common import graph
from pages import mainmenu, patch, webserver, hotspot, wifi, midi

#graph.init()

# nodes
MAINMENU = mainmenu.MAINMENU
WEBSERVER = webserver.WEBSERVER
HOTSPOT = hotspot.HOTSPOT
WIFI = wifi.WIFI
MIDI = midi.MIDI
PATCH = patch.PATCH

# relations
mainmenu = [PATCH, HOTSPOT, WIFI, WEBSERVER, MIDI]

MAINMENU.children = mainmenu
PATCH.children = patch.ITEMPATCH

#graph.add_children(MAINMENU, [PATCH, HOTSPOT, WIFI, WEBSERVER, MIDI])

for item in mainmenu:
    item.parent = MAINMENU

for item in patch.ITEMPATCH:
    item.parent = PATCH

# set initial state
MAINSTATUS.current = MAINMENU
MAINSTATUS.current.isr_enter()
MAINSTATUS.current.rotary_isr_enter()
