#!/usr/bin/env python3

#import time
#from pathlib import Path
#from soft.entities import ItemMenu, ItemPatch, ItemApp, Status
from pages import index
from common.cfg import MAINSTATUS
from common import rock_logger as log

log.config(__name__)

"""
PIN_FORWARD = 8
PIN_BACKWARD = 10
PIN_ROTARY_1 = 11
PIN_ROTARY_2 = 13
"""
#PATCHESPATH = Path('../patches').resolve()

# current Node
log.debug(f"current: {MAINSTATUS.current}")
log.debug(f"previous: {MAINSTATUS.previous}")

if __name__ == '__main__':
    while True:
        """
        if MAINSTATUS.previous and (MAINSTATUS.previous != MAINSTATUS.current):
            MAINSTATUS.previous.isr_exit()
            MAINSTATUS.previous.rotary_isr_exit()
            MAINSTATUS.current.isr_enter()
            MAINSTATUS.current.rotary_isr_enter()
            log.info(
                f"CHANGED!\tprevious: {MAINSTATUS.previous.name}\tcurrent: {MAINSTATUS.current.name}")
            MAINSTATUS.previous = MAINSTATUS.current
        """
        if MAINSTATUS.previous:
            log.info(f"{MAINSTATUS.previous}")
        direction = MAINSTATUS.current.rotary.refresh()

        if direction:
            # current_page.update(direction)
            log.info(f"current: {MAINSTATUS.current.name}")
            log.info(f"direction:\t{direction}")
            log.info(f"current children: {MAINSTATUS.current.children_names}")
