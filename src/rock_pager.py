class Pager:
    def __init__(self):
        self._length = 0
        self._items = []

    def populate(self, items):
        self._items.extend(items)
        self._length = len(self._items)

    def append(self, item):
        pass
