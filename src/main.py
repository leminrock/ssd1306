#!/usr/bin/env python3

import mraa
import rock_pager as rpager
import rock_menu as rmenu
from hardware import hardware as rhard
from hardware import rotary_encoder as renc

PIN1 = 11
PIN2 = 13
PIN3 = 10
PIN4 = 8


encoder = rhard.EncoderEC11()
button1 = rhard.RockButton()
button2 = rhard.RockButton()
mainmenu = rpager.Pager()
hostspotmenu = rpager.Pager()
patchesmenu = rpager.Pager()


def button_routine(gpio):
    global current_page
    sel = current_page.get_selected()

    if sel == 'HOSTSPOT':
        current_page = hostspotmenu
    else:
        current_page = patchesmenu

    current_page.draw()


if __name__ == '__main__':
    button1.encode(PIN3)
    button1.isr(button_routine)
    button2.encode(PIN4)
    button2.isr(button_routine)
    encoder.encode(PIN1, PIN2)
    encoder.isr()

    mainmenu.populate(rmenu.get_nodes(rmenu.Graph, rmenu.MAINMENU))
    hostspotmenu.populate(rmenu.get_nodes(rmenu.Graph, rmenu.HOTSPOT))
    patchesmenu.populate(rmenu.get_nodes(rmenu.Graph, rmenu.PATCHES))

    mainmenu.draw()
    current_page = mainmenu

    # hostspotmenu.draw()
    #current_page = hostspotmenu

    while True:
        direction = encoder.refresh()

        if direction:
            current_page.update(direction)
            print(direction)
