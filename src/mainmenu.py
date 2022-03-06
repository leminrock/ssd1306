#!/usr/bin/env python3

import mraa
import rock_menu as menu
import rock_hardware as rhard
import rotary_encoder as renc

PIN1 = 11
PIN2 = 13
PIN3 = 8


encoder = rhard.EncoderEC11()


def rotary_routine(gpio):
    encoder.tick()


def button_routine(gpio):
    print('released')


if __name__ == '__main__':
    pin3 = mraa.Gpio(PIN3)
    pin3.dir(mraa.DIR_IN)
    pin3.isr(mraa.EDGE_RISING, button_routine, pin3)

    encoder.encode(PIN1, PIN2)
    encoder.isr()

    pos = 0
    menu_item = 0

    while True:
        encoder.tick()
        new_pos = encoder.position
        if pos != new_pos:
            #print(f"pos: {new_pos}\tdir: {int(encoder._enc.get_direction())}")
            #direction = encoder._enc.get_direction()
            direction = encoder.direction
            menu_item = min(4, max(0, menu_item + direction))
            print(menu_item)
            pos = new_pos
