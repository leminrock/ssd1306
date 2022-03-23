import logging
import coloredlogs


def config(name):
    global logger
    logger = logging.getLogger(name)
    coloredlogs.install(
        level='DEBUG', fmt='%(asctime)s,%(msecs)03d %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s')


DISABLE = 0


def INFO(msg):
    if not DISABLE:
        logger.info(msg)


def WARN(msg):
    if not DISABLE:
        logger.warning(msg)


def DEBUG(msg):
    if not DISABLE:
        logger.debug(msg)


def ERROR(msg):
    if not DISABLE:
        logger.error(bold(msg))


def bold(msg):
    return f'\033[1m{msg}\033[0m'
