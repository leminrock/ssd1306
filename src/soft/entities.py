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

    @property
    def level(self):
        return self._level
