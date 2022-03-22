#!/usr/bin/env python3

import time
from soft import menu_builder as mb


def test_routine(item):
    global CURRENT
    global PREVIOUS
    PREVIOUS = item
    CURRENT = item.children[0]


mb.MAINMENU.routine(test_routine, 10)
CURRENT = mb.MAINMENU
PREVIOUS = None


while True:
    if PREVIOUS:
        print("previous:", PREVIOUS.name, end='\t')

    print("current:", CURRENT.name)

    if PREVIOUS and (PREVIOUS != CURRENT):
        PREVIOUS.isr_exit()
        CURRENT.routine(test_routine, 10)
        PREVIOUS = CURRENT

    time.sleep(0.5)
