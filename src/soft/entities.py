from abc import ABC, abstractmethod
from common import rock_logger as log
from hard.hardware import RockButton, EncoderEC11

log.config(__name__)


class Item(ABC):
    def __init__(self, name=None,
                 leaf=False,
                 parent=None,
                 pos=0):
        self._name = name.upper()
        self._leaf = leaf
        self._parent = parent
        self._pos = pos
        self._children = []

    # getter/setter

    @property
    def children(self):
        """
        get children list of instances
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        set children list of instances
        """
        if isinstance(children, list):
            self._children = children
        else:
            self._children = [children]

    @property
    def children_names(self):
        """
        get children names
        """
        return [item.name for item in self._children]

    def add_child(self, item):
        """
        add a child
        """
        self._children.append(item)

    @property
    def parent(self):
        """
        get parent instance
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        set parent instance
        """
        self._parent = parent

    @property
    def name(self):
        """
        get Item name
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        set Item name
        """
        self._name = name

    # methods

    def is_leaf(self):
        return self._leaf

    def set_leaf(self, leaf=True):
        self._leaf = leaf

    def register_right_routine(self, pin, func):
        """
        set isr_routine for right button
        """
        self._right_pin = pin
        self.forward = RockButton(pin)
        self._right_func = func

    def register_left_routine(self, pin, func):
        """
        set isr_routine for left button
        """
        self._left_pin = pin
        self.backward = RockButton(pin)
        self._left_func = func

    def isr_enter(self):
        """
        active button routine interrupts
        """
        self.forward.isr(self._right_func, self)
        self.backward.isr(self._left_func, self)

    def isr_exit(self):
        """
        exit button routine interrupts
        """
        self.forward.isr_exit()
        self.backward.isr_exit()

    def rotary_isr_enter():
        pass

    def rotary_isr_exit():
        pass

    # @abstractmethod
    # def register_rotary_routine(self, pin1=None, pin2=None, func=None):
    #    pass

    @abstractmethod
    def update_name(self):
        """
        update name of the instance based on his status
        """
        pass

    @abstractmethod
    def draw(self):
        pass


class ItemMenu(Item):
    def update_name(self):
        return self.name

    def draw(self):
        pass


class ItemPatch(Item):
    def update_name(self):
        return self.name

    def draw(self):
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


class ItemApp(Item):
    def update_name(self):
        return self.name

    def draw(self):
        pass
