#!/usr/bin/env python3

import mraa
from soft.pager import PagerShort, PagerLong
from soft import menu_builder as menu
from soft.menu_builder import Graph
from hard.hardware import EncoderEC11, RockButton
from hard import rotary_encoder as renc

PIN1 = 11
PIN2 = 13
PIN3 = 10
PIN4 = 8

SHORT_LONG = 4

encoder = EncoderEC11(PIN1, PIN2)
button1 = RockButton(PIN3)
button2 = RockButton(PIN4)
current_page = PagerShort()


def button_routine(gpio):
    global current_page
    sel = current_page.get_selected()

    if not Graph.is_leaf(sel):
        print("not leaf")
        nodes = Graph.get_nodes(sel)
        if len(nodes) <= SHORT_LONG:
            print("pageshort")
            current_page = PageShort(nodes)
            print(dir(current_page))
        else:
            print("pagelong")
            current_page = PageLong(nodes)
    else:
        print("leaf")


if __name__ == '__main__':
    button1.isr(button_routine)
    button2.isr(button_routine)
    encoder.isr()

    current_page.populate(Graph.get_nodes(menu.MAINMENU))
    current_page.draw()

    # hostspotmenu.draw()
    #current_page = hostspotmenu

    while True:
        direction = encoder.refresh()

        if direction:
            current_page.update(direction)
            print(direction)
