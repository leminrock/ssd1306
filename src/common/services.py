import subprocess as sproc
from common import rock_logger as log

COMMAND = 'systemctl'
START = 'start'
RESTART = 'restart'
STOP = 'stop'
ENABLE = 'enable'
DISABLE = 'disable'


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
    capture = sproc.run([COMMAND, action, service], capture_output=True)

    if capture.stderr:
        log.warn(capture.stderr)

    if capture.stdout:
        log.debug(capture.stdout)

    else:
        return capture.returncode


def get_status(service):
    """get status of a systemd service

    :param service: service to retrieve status
    :type service: str
    :return: response
    :rtype: bool
    """
    capture = sproc.run([COMMAND, 'show', service], capture_output=True)
    # return res.stdout.decode('utf-8')
    res = __parse_status(capture.stdout.decode('utf-8'))
    return res == 'active'


# internal functions

def __parse_status(s):
    splitted = s.split('\n')
    splitted = [x.split('=') for x in splitted]

    for item in splitted:
        if item[0].strip(None) == 'ActiveState':
            return item[1]

    return None
