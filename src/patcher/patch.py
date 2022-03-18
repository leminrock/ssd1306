#!/usr/bin/env python3

import time
import subprocess as sproc
from soft import rock_logger as log
from pathlib import Path
from hard import oled

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
        log.ERROR(
            f"FUNCTION set_patch() NEEDS 3 ARGS, BUT {len(args)} PROVIDED")
        res += 1

    if not res:
        oled.drawmenu([args[0]], 0, "PATCH LOADED")
        log.INFO("OK")
        return 0
    else:
        oled.drawmenu(["ERROR"], 0, "PATCH NOT LOADED")
        log.ERROR("task executed with errors")
        return 1


######################## - INTERNALS - ########################


def _set(patchname):
    """set puredata patch to execute immediately and at boot

    :param patchname: puredata file (with complete path)
    :type patchname: pathlib.PosixPath
    """
    log.INFO(f"SET PATCH {patchname.stem}")
    path = str(patchname.resolve())
    script = Path(SERVICESCRIPT).resolve()

    try:
        with open(str(script), 'w') as f:
            f.write(SHEBANG)
            f.write(f"{COMMAND} {path}")

        script.chmod(0o755)
        return 0
    except:
        log.ERROR("NON DEFINED ERROR")
        return 1


def _service(service, action):
    log.INFO(f"{action.upper()} SERVICE {service.upper()}")
    proc = sproc.run([SYSTEMD_COMMAND, action, service],
                     capture_output=True)

    log.INFO(f"call service response: {proc}")

    if proc.returncode:
        log.ERROR(proc.stderr.decode('utf-8').strip('\n').upper())
        return 1
    else:
        return 0
