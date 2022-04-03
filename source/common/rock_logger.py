import logging
import coloredlogs


def config(name):
    global logger
    logger = logging.getLogger(name)
    coloredlogs.install(
        level='DEBUG',
        fmt='%(asctime)s,%(msecs)03d %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s')


DISABLE = 0


def info(msg):
    if not DISABLE:
        logger.info(msg)


def warn(msg):
    if not DISABLE:
        logger.warning(msg)


def debug(msg):
    if not DISABLE:
        logger.debug(msg)


def error(msg):
    if not DISABLE:
        logger.error(bold(msg))


def bold(msg):
    return f'\033[1m{msg}\033[0m'
