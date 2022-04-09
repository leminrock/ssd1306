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
    global MAINSTATUS
    log.info("pressed mainmenu forward")
    log.info("current:", MAINSTATUS.current.name)
    item = MAINSTATUS.current

    if item.chidren[0]:
        MAINSTATUS.previous = item
        MAINSTATUS.current = item.chidren[0]


def backward_routine(state_obj):
    global MAINSTATUS
    log.info("pressed mainmenu backward")
    item = MAINSTATUS.current

    if item.parent:
        MAINSTATUS.previous = item
        MAINSTATUS.current = item.parent


MAINMENU = ItemMenu('MAIN')
MAINMENU.register_right_routine(PIN_FORWARD, forward_routine)
MAINMENU.register_left_routine(PIN_BACKWARD, backward_routine)
MAINMENU.register_rotary(PIN_ROTARY_1, PIN_ROTARY_2)
