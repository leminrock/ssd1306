from soft.entities import ItemMenu
from common import rock_logger as log
from source.main3 import WEBSERVER

log.config(__name__)

PIN_FORWARD = 8
PIN_BACKWARD = 10
PIN_ROTARY_1 = 11
PIN_ROTARY_2 = 13

# routines


def forward_routine(state_obj):
    log.info("pressed webserver forward")
    item = state_obj.item

    if item.chidren[0]:
        state_obj.previous = item
        state_obj.current = item.chidren[0]


def backward_routine(state_obj):
    log.info("pressed webserver backward")
    item = state_obj.item

    if item.parent:
        state_obj.previous = item
        state_obj.current = item.parent


WEBSERVER = ItemMenu('START WEBSERVER')
WEBSERVER.register_right_routine(PIN_FORWARD, forward_routine)
WEBSERVER.register_left_routine(PIN_BACKWARD, backward_routine)
WEBSERVER.register_rotary(PIN_ROTARY_1, PIN_ROTARY_2)
