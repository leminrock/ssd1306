#!/usr/bin/env python3

import time
from soft import menu_builder as mb


PIN_FORWARD = 8
PIN_BACKWARD = 10


def forward_routine(item):
    global CURRENT
    global PREVIOUS
    PREVIOUS = item
    CURRENT = item.children[0]


def backward_routine(item):
    global CURRENT
    global PREVIOUS
    PREVIOUS = item
    CURRENT = item.parent


mb.MAINMENU.routine_forward(forward_routine, PIN_FORWARD)
mb.MAINMENU.routine_backward(backward_routine, PIN_BACKWARD)
CURRENT = mb.MAINMENU
PREVIOUS = None


while True:
    if PREVIOUS:
        print("previous:", PREVIOUS.name, end='\t')

    print("current:", CURRENT.name)

    if PREVIOUS and PREVIOUS != CURRENT:
        CURRENT.routine_forward(forward_routine, PIN_FORWARD)
        CURRENT.routine_backward(backward_routine, PIN_BACKWARD)
        PREVIOUS.isr_exit()
        PREVIOUS = CURRENT

    time.sleep(0.5)
