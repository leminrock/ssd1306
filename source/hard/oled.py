#!/usr/bin/env python3

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont
from common import rock_logger as log

log.config(__name__)

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
PATHFONT = 'data/arial.ttf'
FONT = ImageFont.truetype(PATHFONT, STEP)


########################### - API - ###########################

def drawmenu(items, selected=None, title='main menu', drawback=False):
    log.info(f"CALL drawmenu() with items {items}")
    with canvas(DEVICE) as draw:
        filler = 'white'

        if selected is not None:
            draw.rectangle((
                LEFT,
                selected * STEP + OFFSET,
                RIGHT,
                (selected + 1) * STEP + OFFSET),
                outline="white", fill="white")

        _drawskeleton(draw, title, drawback)

        for n, item in enumerate(items):
            filler = _get_filler(selected, n)
            draw.text((0, n * STEP + OFFSET), item, font=FONT, fill=filler)


######################## - INTERNALS - ########################

def _drawskeleton(draw, title, drawback=False):
    text = 'back'
    titlesize = FONT.getsize(title)
    size = FONT.getsize(text)

    draw.text(
        (int(RIGHT / 2 - titlesize[0] / 2), TOP), title, font=FONT, fill='white')

    if drawback:
        draw.text((RIGHT - size[0], DOWN - size[1]),
                  text, font=FONT, fill='white')


def _get_filler(selected, n):
    # return selected == n ? 'black': 'white'
    return 'black' if selected == n else 'white'
