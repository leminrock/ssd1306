"""
['a', 'b', 'c', 'd', 'e', 'f', 'g']

pos = 0     =>        Abc 
pos = -1    =>       aBcd
pos = -2    =>      abCde
pos = -3    =>      bcDef
pos = -4    =>      cdEfg
pos = -5    =>      deFg 
pos = -6    =>      efG 
"""

import inspect
import rock_logger as rlog

rlog.DISABLE = 0

EMPTY = ''
old_pos = 100


class Ciao:
    def __init__(self):
        self.a = 12
        self.b = "istanza"

    def cacca(self):
        print(self.__str__())
        rlog.INFO(self.__dict__)


def roller(elements, pos=2):
    global old_pos
    _max = len(elements) - 1
    _pos = max(0, min(pos, _max))

    if old_pos != _pos:
        items = decorate_list(elements)
        old_pos = _pos
        print(items[old_pos:old_pos+5])
        rlog.WARN("all OK")


def decorate_list(lst):
    double_empty = [EMPTY, EMPTY]
    return double_empty + lst + double_empty
