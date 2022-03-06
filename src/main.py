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

if __name__ == '__main__':
    button1.encode(PIN3)
    button1.isr()
    button2.encode(PIN4)
    button2.isr()
    encoder.encode(PIN1, PIN2)
    encoder.isr()

    pos = 0
    menu_item = 0
    
    mainmenu.populate(rmenu.get_page(rmenu.Graph, rmenu.MAINMENU))
    print(mainmenu._items)

    while True:
        ref = encoder.refresh()
        if ref:
            print(ref)
