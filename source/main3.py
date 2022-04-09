#!/usr/bin/env python3

#import time
#from pathlib import Path
#from soft.entities import ItemMenu, ItemPatch, ItemApp, Status
from pages import index
from common import rock_logger as log

log.config(__name__)

PIN_FORWARD = 8
PIN_BACKWARD = 10
PIN_ROTARY_1 = 11
PIN_ROTARY_2 = 13

#PATCHESPATH = Path('../patches').resolve()

# current Node
mainstatus = index.mainstatus
mainstatus.current.isr_enter()
mainstatus.current.rotary_isr_enter()

if __name__ == '__main__':
    while True:
        if mainstatus.previous and (mainstatus.previous != mainstatus.current):
            mainstatus.previous.isr_exit()
            mainstatus.previous.rotary_isr_exit()
            mainstatus.current.isr_enter()
            mainstatus.current.rotary_isr_enter()
            log.info(
                f"CHANGED!\tmainstatus.previous: {mainstatus.previous.name}\tcurrent: {mainstatus.current.name}")
            mainstatus.previous = mainstatus.current
        else:
            log.info(
                f"UNCHANGED!\tcurrent: {mainstatus.current.name}")

        direction = mainstatus.current.rotary.refresh()

        if direction:
            # current_page.update(direction)
            log.info(f"direction:\t{direction}")
