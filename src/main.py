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
mainmenu = PagerShort()


def button_routine(gpio):
    global current_page
    sel = current_page.get_selected()
    """
    if not sel.is_leaf():
        current_page.populate(Graph.get_nodes(sel))
        back = False

        if sel.is_child():
            back = True

        current_page.draw(title=sel.name, drawback=back)
    else:
        print(sel.path)
    """
    if not Graph.is_leaf(sel):
        nodes = Graph.get_nodes(sel)
        if len(nodes) <= SHORT_LONG:
            current_page = PageShort(nodes)
            print("pageshort")
        else:
            current_page = PageLong(nodes)
            print("pagelong")
    else:
        print("leaf")


if __name__ == '__main__':
    button1.isr(button_routine)
    button2.isr(button_routine)
    encoder.isr()

    mainmenu.populate(Graph.get_nodes(menu.MAINMENU))

    mainmenu.draw()
    current_page = mainmenu

    # hostspotmenu.draw()
    #current_page = hostspotmenu

    while True:
        direction = encoder.refresh()

        if direction:
            current_page.update(direction)
            print(direction)
