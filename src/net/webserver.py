#!/usr/bin/env python3

import subprocess as sproc
from common import rock_logger as log
from common import services as serv
from pathlib import Path

log.config(__name__)

SERVICE = 'rock_serverweb'


def is_active():
    response = serv.is_active(SERVICE)
    return response == True
