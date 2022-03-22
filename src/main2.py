#!/usr/bin/env python3

import time
from soft import menu_builder as mb


def test_routine(item):
    global CURRENT
    global PREVIOUS
    PREVIOUS = item
    CURRENT = item.children[0]
    #CURRENT.routine(test_routine, item._pin)


mb.MAINMENU.routine(test_routine, 10)
CURRENT = mb.MAINMENU
PREVIOUS = None


while True:
    if PREVIOUS:
        print("previous:", PREVIOUS.name)
    print(CURRENT.name)
    if PREVIOUS != CURRENT:
        PREVIOUS.isr_exit()
        CURRENT.routine(test_routine, 10)
    time.sleep(0.5)
