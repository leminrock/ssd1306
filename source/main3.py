#!/usr/bin/env python3

from pages import index
from common.cfg import MAINSTATUS
from common import rock_logger as log

log.config(__name__)

# current Node
log.debug(f"current: {MAINSTATUS.current}")
log.debug(f"previous: {MAINSTATUS.previous}")

if __name__ == '__main__':
    while True:
        if MAINSTATUS.previous and (MAINSTATUS.previous != MAINSTATUS.current):
            MAINSTATUS.previous.isr_exit()
            MAINSTATUS.previous.rotary_isr_exit()
            MAINSTATUS.current.isr_enter()
            MAINSTATUS.current.rotary_isr_enter()
            log.debug(
                f"CHANGED!\tprevious: {MAINSTATUS.previous.name}\tCURRENT: {MAINSTATUS.current.name}")
            MAINSTATUS.previous = MAINSTATUS.current

        # log.debug(f"{MAINSTATUS.current.rotary.direction}")
        #direction = MAINSTATUS.current.rotary_refresh()
        direction = MAINSTATUS.current.rotary.refresh()

        if direction:
            # current_page.update(direction)
            log.info(f"current: {MAINSTATUS.current.name}")
            log.info(f"direction:\t{direction}")
            log.info(f"current children: {MAINSTATUS.current.children_names}")
