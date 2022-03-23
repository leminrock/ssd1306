#!/usr/bin/env python3

import time
import subprocess as sproc
from common import rock_logger as log
from pathlib import Path
from hard import oled

log.config(__name__)

COMMAND = "puredata -nogui -jack"
SERVICESCRIPT = "/home/rock/.puredata"
SHEBANG = "#!/usr/bin/env bash\n\n"
SYSTEMD_COMMAND = "systemctl"


########################### - API - ###########################


def set_patch(*args):
    res = 0
    if len(args) == 3:
        patchname, jackdservice, pdservice = args
        res += _set(patchname)
        res += _service(pdservice, 'stop')
        res += _service(jackdservice, 'restart')
        time.sleep(2)
        res += _service(pdservice, 'restart')
    else:
        log.error(
            f"FUNCTION set_patch() NEEDS 3 ARGS, BUT {len(args)} PROVIDED")
        res += 1

    log.info(f"response: {res}")

    if not res:
        name = args[0].parts[-2]
        oled.drawmenu([name.upper()], 0, "PATCH LOADED")
        log.info("OK")
        return 0
    else:
        oled.drawmenu(["ERROR"], 0, "PATCH NOT LOADED")
        log.error("task executed with errors")
        return 1


######################## - INTERNALS - ########################


def _set(patchname):
    """set puredata patch to execute immediately and at boot

    :param patchname: puredata file (with complete path)
    :type patchname: pathlib.PosixPath
    """
    log.info(f"SET PATCH {patchname.stem}")
    path = str(patchname.resolve())
    script = Path(SERVICESCRIPT).resolve()

    try:
        with open(str(script), 'w') as f:
            f.write(SHEBANG)
            f.write(f"{COMMAND} {path}")

        script.chmod(0o755)
        return 0
    except:
        log.error("NON DEFINED ERROR")
        return 1


def _service(service, action):
    log.info(f"{action.upper()} SERVICE {service.upper()}")
    proc = sproc.run([SYSTEMD_COMMAND, action, service],
                     capture_output=True)

    if proc.returncode:
        log.error(proc.stderr.decode('utf-8').strip('\n').upper())
        return 1
    else:
        return 0
