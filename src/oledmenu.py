#!/usr/bin/env python3

from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont

STEP = 8
LEFT = 0
RIGHT = 127
TOP = 0
DOWN = 63


serial = i2c(port=1, address=0x3C)
DEVICE = ssd1306(serial)
PATHFONT = '../arial.ttf'

font = ImageFont.truetype(PATHFONT, STEP)


def drawmenu(items, selected=None):
    with canvas(DEVICE) as draw:
        filler = 'white'

        if selected is not None:
            draw.rectangle((LEFT, selected * STEP, RIGHT, (selected + 1) * STEP), outline="white", fill="white")
        
        for n,i in enumerate(items):
            if selected == n:
                filler = 'black'
            else:
                filler = 'white'

            draw.text((0, n * STEP), i, font=font, fill=filler)


drawmenu(['HOTPOST', 'PATCHES'],1)
input('premi un tasto')
