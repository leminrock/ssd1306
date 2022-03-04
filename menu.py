#!/usr/bin/env python3

import time
from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont
import rock_common as rcom

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

font = ImageFont.truetype('arial.ttf', size=rcom.MAINMENU_STEP)
font2 = ImageFont.truetype('arial.ttf', size=int(rcom.MAINMENU_STEP/2))

def draw_mask(dev,v_pos,height):
    dev.rectangle((0, v_pos*height, 127, (v_pos*height)+height), outline="black", fill="white")

with canvas(device) as draw:
    selected = 1
    draw_mask(draw, selected, rcom.MAINMENU_STEP)

    for n,item in enumerate(rcom.MAINMENU_ITEMS):
        if n == selected:
            c_mask = 'black'
        else:
            c_mask = 'white'
        draw.text((10, item[1] * rcom.MAINMENU_STEP), item[0].upper(), font=font, fill=c_mask)

    draw.text((100, 8 * 7), "back".upper(), font=font2, fill='white')

input("premi un tasto")
