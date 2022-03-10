#!/usr/bin/env python3

import subprocess as sp
from pathlib import Path

diry = '.'
path = Path(diry).resolve()
path = path / Path('test.sh')


with open(path, 'w') as f:
    f.write("#!/usr/bin/env bash\n")
    f.write("echo ciao\n")

sp.run(str(path))
