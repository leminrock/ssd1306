from soft.entities import ItemMenu
from common import rock_logger as log
from common.cfg import *
from common import routines as rtn


log.config(__name__)


HOTSPOT = ItemMenu('START HOTSPOT')
HOTSPOT.register_right_routine(PIN_FORWARD, rtn.forward_routine, MAINSTATUS)
HOTSPOT.register_left_routine(PIN_BACKWARD, rtn.backward_routine, MAINSTATUS)
HOTSPOT.register_rotary(PIN_ROTARY_1, PIN_ROTARY_2)
