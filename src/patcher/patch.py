#!/usr/bin/env python3

from soft import rock_logger as log
import subprocess as sproc
from pathlib import Path

COMMAND = "puredata -nogui -jack"
SERVICESCRIPT = "setpatch.sh"
SHEBANG = "#!/usr/bin/env bash\n\n"
SYSTEMD_COMMAND = "systemctl"


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
    if proc.returncode:
        log.ERROR(proc.stderr.decode('utf-8').strip('\n').upper())
        return 1
    else:
        return 0


def set_patch(*args):
    res = 0
    if len(args) == 3:
        patchname, jackdservice, pdservice = args
        res += _set(patchname)
        res += _service(pdservice, 'stop')
        res += _service(jackdservice, 'restart')
        res += _service(pdservice, 'restart')
    else:
        log.ERROR(f"FUNCTION set_patch NEEDS 3 ARGS, BUT {len(args)} PROVIDED")
        res += 1

    if not res:
        return 0
    else:
        log.ERROR("task executed with errors")
        return 1
