#!/usr/bin/env python3

import time
from pathlib import Path
from soft.entities import ItemMenu, ItemPatch, ItemApp
from common import rock_logger as log

log.config(__name__)

PIN_FORWARD = 8
PIN_BACKWARD = 10
PIN_ROTARY_1 = 11
PIN_ROTARY_2 = 13

PATCHESPATH = Path('../patches').resolve()


# routines

def forward_routine(item):
    global current
    global previous

    log.info("pressed forward")

    if item.children[0]:
        previous = item
        current = item.children[0]


def backward_routine(item):
    global current
    global previous

    if item.parent:
        previous = item
        current = item.parent


# Nodes
MAINMENU = ItemMenu('MAIN')
WEBSERVER = ItemMenu('ACTIVE WEBSERVER', parent=MAINMENU)
MIDI = ItemApp('MIDI', parent=MAINMENU)
HOTSPOT = ItemApp('ACTIVE HOTSPOT', parent=MAINMENU)
WIFI = ItemApp('START WIFI', parent=MAINMENU)
PATCHES = ItemPatch('PATCHES', parent=MAINMENU)

# Relations
MAINMENU.children = [PATCHES, WEBSERVER, MIDI, HOTSPOT, WIFI]

# ISR routines registration
MAINMENU.register_right_routine(PIN_FORWARD, forward_routine)
MAINMENU.register_left_routine(PIN_BACKWARD, backward_routine)

# current Node
current = MAINMENU
previous = None

current.isr_enter()

if __name__ == '__main__':
    while True:
        if previous and (previous != current):
            previous.isr_exit()
            current.register_right_routine(PIN_FORWARD, forward_routine)
            current.register_left_routine(PIN_BACKWARD, backward_routine)
            log.info(
                f"CHANGED!\tprevious: {previous.name}\tcurrent: {current.name}")
            previous = current
