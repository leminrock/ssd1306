from soft.entities import ItemMenu
from common import rock_logger as log
from common.cfg import MAINSTATUS


log.config(__name__)

PIN_FORWARD = 8
PIN_BACKWARD = 10
PIN_ROTARY_1 = 11
PIN_ROTARY_2 = 13

# routines


def forward_routine(state_obj):
    log.info("pressed webserver forward")
    log.info(f"current: {MAINSTATUS.current.name}")
    item = MAINSTATUS.current

    if item.chidren[0]:
        log.debug(f"select child from: {MAINSTATUS.current.children_names}")
        MAINSTATUS.previous = item
        MAINSTATUS.current = item.chidren[0]
        #log.info(f"previous: {MAINSTATUS.previous.name}")
        #log.info(f"current: {MAINSTATUS.current.name}")


def backward_routine(state_obj):
    log.info("pressed webserver backward")
    log.info(f"current: {MAINSTATUS.current.name}")
    item = MAINSTATUS.current

    if item.parent:
        MAINSTATUS.previous = item
        MAINSTATUS.current = item.parent


WEBSERVER = ItemMenu('START WEBSERVER')
WEBSERVER.register_right_routine(PIN_FORWARD, forward_routine)
WEBSERVER.register_left_routine(PIN_BACKWARD, backward_routine)
WEBSERVER.register_rotary(PIN_ROTARY_1, PIN_ROTARY_2)
