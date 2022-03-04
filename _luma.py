#!/usr/bin/env python3

"""test oled simulation"""

import time

#from luma.core.interface.serial import i2c, spi, pcf8574
#from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
#from luma.oled.device import ssd1306
from luma.emulator.device import pygame
from PIL import Image, ImageDraw, ImageFont

#serial = i2c(port=1, address=0x3C)

#device = ssd1306(serial)

STEP = 10

device = pygame(mode='1')
voices = ['alfa','beta','gamma','delta','epsilon','zeta','eta','theta','lambda','ki','']

for pos in range(100):
    with canvas(device) as draw:
        fnt = ImageFont.truetype("Fleftex_M.ttf", STEP - 1)

        for i,v in enumerate(voices):
            y = i + pos
            if y % len(voices) == 3:
                txt = f">> {v.upper()}"
            else:
                txt = f"   {v.upper()}"
            draw.text((0,(i+pos) % len(voices) * STEP), txt, fill='white', font=fnt)

        time.sleep(0.1)

time.sleep(3)