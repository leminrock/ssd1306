#!/usr/bin/env python3

import mraa
#from soft import pager as rpager
from soft.pager import PagerShort, PagerLong
from soft import menu as rmenu
from hard import hardware as rhard
from hard import rotary_encoder as renc

PIN1 = 11
PIN2 = 13
PIN3 = 10
PIN4 = 8


encoder = rhard.EncoderEC11()
button1 = rhard.RockButton()
button2 = rhard.RockButton()
mainmenu = PagerShort()  # rpager.Pager()
#hostspotmenu = rpager.Pager()
#patchesmenu = rpager.Pager()


def button_routine(gpio):
    global current_page
    sel = current_page.get_selected()
    if not sel.is_leave():
        current_page.populate(rmenu.get_nodes(rmenu.Graph, sel))
        back = False

        if sel.is_child():
            back = True

        current_page.draw(title=sel.name, drawback=back)
    else:
        print(sel.path)


if __name__ == '__main__':
    button1.encode(PIN3)
    button1.isr(button_routine)
    button2.encode(PIN4)
    button2.isr(button_routine)
    encoder.encode(PIN1, PIN2)
    encoder.isr()

    mainmenu.populate(rmenu.get_nodes(rmenu.Graph, rmenu.MAINMENU))
    #hostspotmenu.populate(rmenu.get_nodes(rmenu.Graph, rmenu.HOTSPOT))
    #patchesmenu.populate(rmenu.get_nodes(rmenu.Graph, rmenu.PATCHES))

    mainmenu.draw()
    current_page = mainmenu

    # hostspotmenu.draw()
    #current_page = hostspotmenu

    while True:
        direction = encoder.refresh()

        if direction:
            current_page.update(direction)
            print(direction)
