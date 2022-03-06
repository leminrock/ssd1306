#!/usr/bin/env python3

import mraa
import rock_hardware as rhard
import rotary_encoder as renc
import rock_pager as rpager
import rock_menu as rmenu

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

if __name__ == '__main__':
    button1.encode(PIN3)
    button1.isr()
    button2.encode(PIN4)
    button2.isr()
    encoder.encode(PIN1, PIN2)
    encoder.isr()

    mainmenu.populate(rmenu.get_names(rmenu.Graph, rmenu.MAINMENU))
    hostspotmenu.populate(rmenu.get_names(rmenu.Graph, rmenu.HOTSPOT))
    patchesmenu.populate(rmenu.get_names(rmenu.Graph, rmenu.PATCHES))

    mainmenu.draw()

    while True:
        direction = encoder.refresh()
        if direction:
            mainmenu.update(direction)
            print(direction)
