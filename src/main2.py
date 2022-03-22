#!/usr/bin/env python3

import time
from soft import menu_builder as mb


def test_routine(item):
    global CURRENT
    old_item = item
    print("cedo il comando a", old_item.children[0], old_item.children[0].name)
    #item.isr_exit()
    CURRENT = old_item.children[0]
    #CURRENT.routine(test_routine, item._pin)


mb.MAINMENU.routine(test_routine, 10)
CURRENT = mb.MAINMENU


while True:
    print(CURRENT.name)
    time.sleep(0.5)
