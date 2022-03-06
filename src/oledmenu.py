#!/usr/bin/env python3

from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306

STEP = 8

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)
font = 'arial.ttf'


def drawmenu(items, selected):
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="white")
        for i in items:
            draw.text((0, i * STEP), i, fill="white")


drawmenu(['HOTPOST', 'PATCHES'])
input('premi un tasto')
