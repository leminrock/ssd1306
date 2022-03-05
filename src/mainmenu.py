#!/usr/bin/env python3

import mraa 
import rock_menu as menu 
import rotary_encoder as renc 

PIN1 = 11
PIN2 = 13
PIN3 = 12

class Encoder:
    def __init__(self, p1, p2):
        self._enc = renc.RotaryEncoder(p1, p2, renc.LATCHMODE['FOUR3'])

def rotary_routine(gpio):
    pass

def button_routine(gpio):
    pass


if __name__=='__main__':
    pin1 = mraa.Gpio(PIN1)
    pin2 = mraa.Gpio(PIN2)
    pin3 = mraa.Gpio(PIN3)
    pin1.dir(mraa.DIR_IN)
    pin2.dir(mraa.DIR_IN)
    pin3.dir(mraa.DIR_IN)

    encoder = Encoder(pin1, pin2)

    pin1.isr(mraa.EDGE_BOTH, rotary_routine, pin1)
    pin2.isr(mraa.EDGE_BOTH, rotary_routine, pin2)
    pin3.isr(mraa.RISING, button_routine, pin3)