#!/usr/bin/env python3

import subprocess as sp
from pathlib import Path

diry = '.'
path = Path(diry).resolve()
path = path / Path('test.sh')

#arg = path._str
# print(arg)
print(dir(path))
proc = sp.Popen([path])
