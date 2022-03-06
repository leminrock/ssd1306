#!/usr/bin/env python3

import mraa
import rock_menu as menu
import rotary_encoder as renc

PIN1 = 11
PIN2 = 13
PIN3 = 8


class Encoder:
    def __init__(self):
        self._enc = None

    @property
    def enc(self):
        return self._enc

    def encode(self, p1, p2):
        self._enc = renc.RotaryEncoder(p1, p2, renc.LATCHMODE['FOUR3'])

    def tick(self):
        self._enc.tick()


encoder = Encoder()


def rotary_routine(gpio):
    encoder.tick()


def button_routine(gpio):
    print('released')


if __name__ == '__main__':
    pin1 = mraa.Gpio(PIN1)
    pin2 = mraa.Gpio(PIN2)
    pin3 = mraa.Gpio(PIN3)
    pin1.dir(mraa.DIR_IN)
    pin2.dir(mraa.DIR_IN)
    pin3.dir(mraa.DIR_IN)

    encoder.encode(pin1, pin2)

    pin1.isr(mraa.EDGE_BOTH, rotary_routine, pin1)
    pin2.isr(mraa.EDGE_BOTH, rotary_routine, pin2)
    pin3.isr(mraa.EDGE_RISING, button_routine, pin3)

    pos = 0
    menu_item = 0

    while True:
        encoder.tick()
        new_pos = encoder._enc.get_position()
        if pos != new_pos:
            #print(f"pos: {new_pos}\tdir: {int(encoder._enc.get_direction())}")
            direction = encoder._enc.get_direction()
            menu_item = min (4, max(0, menu_item + direction))
            print(menu_item)
            pos = new_pos
