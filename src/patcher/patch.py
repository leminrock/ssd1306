#!/usr/bin/env python3

import sys
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
    path = str(patchname.resolve())
    script = Path(SERVICESCRIPT).resolve()

    with open(str(script), 'w') as f:
        f.write(SHEBANG)
        f.write(f"{COMMAND} {path}")

    script.chmod(0o755)


def _service_restart(service):
    sproc.run([SYSTEMD_COMMAND, 'restart', service])


def set_patch(patchname, jackdservice, pdservice):
    _set(patchname)
    _service_restart(jackdservice)
    _service_restart(pdservice)
    sys.exit(0)
