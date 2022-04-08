#!/usr/bin/env python3

import time
from pathlib import Path
from soft.entities import ItemMenu, ItemPatch, ItemApp, Status
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
    global mainstatus.previous

    log.info("pressed forward")

    if item.children[0]:
        mainstatus.previous = item
        current = item.children[0]


def backward_routine(item):
    global current
    global mainstatus.previous

    if item.parent:
        mainstatus.previous = item
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
MAINMENU.register_rotary(PIN_ROTARY_1, PIN_ROTARY_2)
PATCHES.register_right_routine(PIN_FORWARD, forward_routine)
PATCHES.register_left_routine(PIN_BACKWARD, backward_routine)
PATCHES.register_rotary(PIN_ROTARY_1, PIN_ROTARY_2)
WEBSERVER.register_right_routine(PIN_FORWARD, forward_routine)
WEBSERVER.register_left_routine(PIN_BACKWARD, backward_routine)
HOTSPOT.register_right_routine(PIN_FORWARD, forward_routine)
HOTSPOT.register_left_routine(PIN_BACKWARD, backward_routine)
WIFI.register_right_routine(PIN_FORWARD, forward_routine)
WIFI.register_left_routine(PIN_BACKWARD, backward_routine)

# current Node
"""
current = MAINMENU
previous = None

current.isr_enter()
current.rotary_isr_enter()
"""

mainstatus = Status(current=MAINMENU)
mainstatus.current.isr_enter()
mainstatus.current.rotary_isr_enter()

if __name__ == '__main__':
    while True:
        if mainstatus.previous and (mainstatus.previous != mainstatus.current):
            mainstatus.previous.isr_exit()
            mainstatus.previous.rotary_isr_exit()
            mainstatus.current.isr_enter()
            mainstatus.current.rotary_isr_enter()
            log.info(
                f"CHANGED!\tmainstatus.previous: {mainstatus.previous.name}\tcurrent: {mainstatus.current.name}")
            mainstatus.previous = mainstatus.current

        direction = mainstatus.current.rotary.refresh()

        if direction:
            # current_page.update(direction)
            log.INFO(f"direction:\t{direction}")
