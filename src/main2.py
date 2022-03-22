#!/usr/bin/env python3

import time
from soft import menu_builder as mb


def test_routine(item):
    global CURRENT
    print("cedo il comando a", item.children[0], item.children[0].name)
    CURRENT = item.children[0]
    CURRENT.routine(test_routine, item._pin)
    item.isr_exit()


mb.MAINMENU.routine(test_routine, 10)

CURRENT = mb.MAINMENU


while True:
    print(CURRENT.name)
    time.sleep(0.5)
