from soft import rock_logger as log


class Item:
    """item class"""

    def __init__(self,
                 name,
                 level=None,
                 back=False,
                 path=None):
        self._name = name
        self._level = level
        self._back = back
        self._path = path

    def __repr__(self):
        return f"Item: {self.name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self.name = name
        
    @property
    def level(self):
        return self._level

    def set_command(self, func, *args):
        self._func = func
        self._args = args

    def command(self):
        log.WARN("CALL COMMAND")
        self._func(*self._args)
