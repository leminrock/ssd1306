from hard import oled as roled


class Pager:
    def __init__(self, items=[]):
        self._items = items
        self._length = len(items)
        self._max = self._length - 1
        print(
            f"items:\t{self._items}\nlength:\t{self._length}\nmax:\t{self._max}")

    def get_items(self):
        return self._items

    def get_selected(self):
        """get selected item"""
        return self._items[self._pos]

    @property
    def pos(self):
        return self._pos


class PagerShort(Pager):
    def __init__(self, items=[]):
        super().__init__(items)
        self._pos = 0

    def populate(self, items):
        self._items = items
        self._length = len(self._items)
        self._max = self._length - 1
        self._pos = 0

    def update(self, direction):
        newpos = max(0, min(self._max, self._pos + direction))

        if self._pos != newpos:
            self._pos = newpos
            self.draw(self._pos)

    def draw(self, selected=0, title='main title', drawback=False):
        items = [x.name for x in self._items]
        print("position:", self.pos)
        print("items:", items)
        print("selected:", self.get_selected())
        #roled.drawmenu(items, selected, title, drawback)


class PagerLong(Pager):
    def __init__(self, items=[]):
        super().__init__(items)
        self._pos = 1

    def populate(self, items):
        self._items = items
        self._length = len(self._items)
        self._max = self._length - 1
        self._pos = 2

    def draw(self, selected=0, title='patches', drawback=True):
        pass
