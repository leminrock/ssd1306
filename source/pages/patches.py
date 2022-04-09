# patches page and relative patch pages

from soft.entities import ItemMenu, ItemPatch
from common import rock_logger as log
from common.cfg import *
from common import routines as rtn
from pathlib import Path


log.config(__name__)

PATCHESPATH = Path('../patches').resolve()

PATCHES = ItemMenu('PATCHES')
PATCHES.register_right_routine(PIN_FORWARD, rtn.forward_routine, MAINSTATUS)
PATCHES.register_left_routine(PIN_BACKWARD, rtn.backward_routine, MAINSTATUS)
PATCHES.register_rotary(PIN_ROTARY_1, PIN_ROTARY_2)

ITEMPATCH = []

dirs = list(PATCHESPATH.glob('*'))

for _dir in sorted(dirs):
    path = _dir / Path('main.pd')
    itempatch = ItemPatch(_dir.stem)
    ITEMPATCH.append(itempatch)
    #patch.set_command(set_patch, path, JACKDSERVICE, PDSERVICE)
    #Graph.one_to_one(PATCHES, patch)
