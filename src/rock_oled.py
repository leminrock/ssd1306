#!/usr/bin/env python3

from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont

WIDTH = 128
HEIGHT = 64
STEP = int(HEIGHT / 7)
LEFT = 0
RIGHT = WIDTH - 1
TOP = 0
DOWN = HEIGHT - 1
OFFSET = STEP * 2
SERIAL = i2c(port=1, address=0x3C)
DEVICE = ssd1306(SERIAL)
PATHFONT = '../arial.ttf'

font = ImageFont.truetype(PATHFONT, STEP)


def drawmenu(items, selected=None):
    with canvas(DEVICE) as draw:
        filler = 'white'

        if selected is not None:
            draw.rectangle((LEFT, selected * STEP + OFFSET, RIGHT,
                            (selected + 1) * STEP + OFFSET), outline="white", fill="white")

        drawskeleton(draw, 'main menu')

        for n, item in enumerate(items):
            if selected == n:
                filler = 'black'
            else:
                filler = 'white'

            draw.text((0, n * STEP + OFFSET), item, font=font, fill=filler)


def drawskeleton(draw, title):
    text = 'back'
    titlesize = font.getsize(title)
    size = font.getsize(text)

    draw.text(
        (int(RIGHT / 2 - titlesize[0] / 2), TOP), title, font=font, fill='white')
    draw.text((RIGHT - size[0], DOWN - size[1]), text, font=font, fill='white')


