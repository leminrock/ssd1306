import subprocess as sproc
from common import rock_logger as log

COMMAND = 'systemctl'
START = 'start'
RESTART = 'restart'
STOP = 'stop'
ENABLE = 'enable'
DISABLE = 'disable'
SHOW = 'show'


# API


def systemctl(service, action):
    """manage systemctl command

    :param service: service
    :type service: str
    :param action: action to perform
    :type action: str
    :return: exit code
    :rtype: int
    """
    capture = _send_command(service, action)

    if capture.stderr:
        log.warn(capture.stderr)

    if capture.stdout:
        log.debug(capture.stdout)

    return capture.returncode


def is_active(service):
    """get status of a systemd service

    :param service: service to retrieve status
    :type service: str
    :return: response
    :rtype: bool
    """
    capture = _send_command(service, SHOW)
    res = _parse_status(capture.stdout.decode('utf-8'))
    return res == 'active'


# internal functions

def _send_command(service, action):
    return sproc.run([COMMAND, action, service], capture_output=True)


def _parse_status(s):
    splitted = s.split('\n')
    splitted = [x.split('=') for x in splitted]

    for item in splitted:
        if item[0].strip(None) == 'ActiveState':
            return item[1]

    return None
