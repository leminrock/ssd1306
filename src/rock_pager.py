class Pager:
    def __init__(self):
        self._items = []

    def populate(self, items):
        self._items.extend(items)

    def append(self, item):
        pass
