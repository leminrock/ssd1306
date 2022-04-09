# Nodes
from common.cfg import MAINSTATUS
from pages import mainmenu, webserver, hotspot, wifi, midi, patches


MAINMENU = mainmenu.MAINMENU
WEBSERVER = webserver.WEBSERVER
HOTSPOT = hotspot.HOTSPOT
WIFI = wifi.WIFI
MIDI = midi.MIDI
PATCHES = patches.PATCHES

mainmenu = [PATCHES, HOTSPOT, WIFI, WEBSERVER, MIDI]
MAINMENU.children = mainmenu
PATCHES.children = patches.ITEMPATCH

for item in mainmenu:
    item.parent = MAINMENU

for item in patches.ITEMPATCH:
    item.parent = PATCHES

# set initial state
MAINSTATUS.current = MAINMENU
MAINSTATUS.current.isr_enter()
MAINSTATUS.current.rotary_isr_enter()
