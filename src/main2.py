#!/usr/bin/env python3

import time
from soft import menu_builder as mb


def test_routine(item):
    print("cedo il comando")
    item.isr_exit()
    CURRENT = item.children[0]
    CURRENT.routine(item._pin)


mb.MAINMENU.routine(test_routine, 10)
# mb.MAINMENU.loop()

CURRENT = mb.MAINMENU


while True():
    print(CURRENT.name)
    time.sleep(0.5)
