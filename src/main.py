#!/usr/bin/env python3

from soft.pager import PagerShort, PagerLong
from soft import menu_builder as menu
from soft.menu_builder import Graph
from common import rock_logger as log
from hard.hardware import EncoderEC11, RockButton

PIN1 = 11
PIN2 = 13
PIN3 = 10
PIN4 = 8
SHORT_LONG = 4

encoder = EncoderEC11(PIN1, PIN2)
button1 = RockButton(PIN3)
button2 = RockButton(PIN4)
shortpage = PagerShort(pos=0)
longpage = PagerLong(pos=2)
current_page = shortpage


def set_page_type(length):
    if length <= SHORT_LONG:
        page = shortpage
        pos = 0
    else:
        page = longpage
        pos = 2
    return page, pos


def button_routine(gpio):
    global current_page
    sel = current_page.get_selected()

    if gpio == PIN3:
        if not Graph.is_leaf(sel):
            log.INFO("NOT LEAF")
            nodes = Graph.get_nodes(sel)
            current_page, pos = set_page_type(len(nodes))
            log.INFO(f"{current_page}")
            current_page.populate(nodes, pos)
            current_page.draw()
        else:
            log.INFO("LEAF")
            sel.command()
    elif gpio == PIN4:
        previous_node = Graph.get_back(sel)
        nodes = Graph.get_nodes(Graph.get_back(previous_node))
        current_page, pos = set_page_type(len(nodes))
        current_page.populate(nodes, pos)
        current_page.draw()


if __name__ == '__main__':
    button1.isr(button_routine)
    button2.isr(button_routine)
    encoder.isr()

    current_page.populate(Graph.get_nodes(menu.MAINMENU))
    current_page.draw()

    while True:
        direction = encoder.refresh()

        if direction:
            current_page.update(direction)
            log.INFO(f"direction:\t{direction}")
