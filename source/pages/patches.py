from soft.entities import ItemMenu
from common import rock_logger as log

log.config(__name__)

PIN_FORWARD = 8
PIN_BACKWARD = 10
PIN_ROTARY_1 = 11
PIN_ROTARY_2 = 13

# routines


def forward_routine(state_obj):
    log.info("pressed patches forward")
    item = state_obj.item

    if item.chidren[0]:
        state_obj.previous = item
        state_obj.current = item.chidren[0]


def backward_routine(state_obj):
    log.info("pressed patches backward")
    item = state_obj.item

    if item.parent:
        state_obj.previous = item
        state_obj.current = item.parent


PATCHES = ItemMenu('MAIN')
PATCHES.register_right_routine(PIN_FORWARD, forward_routine)
PATCHES.register_left_routine(PIN_BACKWARD, backward_routine)
PATCHES.register_rotary(PIN_ROTARY_1, PIN_ROTARY_2)