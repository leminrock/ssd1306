from abc import ABC, abstractmethod
from soft import rock_logger as log
from hard.hardware import RockButton


class Item(ABC):
    def __init__(self, name=None,
                 leaf=False,
                 parent=None):
        self._name = name.upper()
        self._leaf = leaf
        self._parent = parent
        self._children = []

    def is_leaf(self):
        return self._leaf

    def set_leaf(self, leaf=True):
        self._leaf = leaf

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, children):
        if isinstance(children, list):
            self._children = children
        else:
            self._children = [children]

    @property
    def children_names(self):
        return [item.name for item in self._children]

    def add_child(self, item):
        self._children.append(item)

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def isr_routine(self):
        pass

    @abstractmethod
    def isr_routine_start(self):
        pass

    @abstractmethod
    def isr_routine_stop(self):
        pass

    @abstractmethod
    def loop(self):
        pass


def test_routine(gpio):
    print("CIAOOOOOOOO")


class ItemMenu(Item):
    def draw(self):
        pass

    def isr_routine(self, pin):
        self._isr = RockButton(pin)
        #self._isr.isr(test_routine)

    def isr_routine_start(self):
        pass

    def isr_routine_stop(self):
        pass

    def loop(self):
        pass


class ItemPatch(Item):
    def draw(self):
        pass

    def isr_routine(self):
        pass

    def isr_routine_start(self):
        pass

    def isr_routine_stop(self):
        pass

    def loop(self):
        pass

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    def set_command(self, func, *args):
        self._func = func
        self._args = args

    def command(self):
        self._func(*self._args)
