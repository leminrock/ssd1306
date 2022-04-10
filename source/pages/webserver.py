from soft.entities import ItemMenu
from common import rock_logger as log
from common.cfg import *
from common import routines as rtn


log.config(__name__)


# routines:
# backward is common default backward routine -> rtn.backward_routine()
# forward: active/deactive webserver systemd service

def forward_routine(arg):
    """check status of webserver systemd service
    active/deactive the service and set name of instance

    :param arg: instance
    :type arg: ItemWebServer
    """
    pass


WEBSERVER = ItemMenu('START WEBSERVER')

WEBSERVER.register_right_routine(PIN_FORWARD, rtn.forward_routine, MAINSTATUS)
WEBSERVER.register_left_routine(PIN_BACKWARD, rtn.backward_routine, MAINSTATUS)
WEBSERVER.register_rotary(PIN_ROTARY_1, PIN_ROTARY_2)
