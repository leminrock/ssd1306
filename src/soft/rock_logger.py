import coloredlogs
import logging

coloredlogs.install()


DISABLE = 0


def INFO(msg):
    if not DISABLE:
        logging.info(msg)


def WARN(msg):
    if not DISABLE:
        logging.warning(msg)


def ERROR(msg):
    if not DISABLE:
        logging.error(bold(msg))


def bold(msg):
    return f'\033[1m{msg}\033[0m'
