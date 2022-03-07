from hard import oled as roled


class Pager:
    def __init__(self, length=0):
        self._pos = 0
        self._length = 0
        self._items = []
        self._max = length - 1

    def populate(self, items):
        self._items.extend(items)
        self._length = len(self._items)
        self._max = self._length - 1

    def update(self, direction):
        newpos = max(0, min(self._max, self._pos + direction))

        if self._pos != newpos:
            self.draw(newpos)
            self._pos = newpos

    def draw(self):
        length = self._length
        if (length < 4):
            self.drawshort()
        else:
            self.drawlong()

    def drawshort(self, selected=0, title='main title', drawback=False):
        items = [x.name for x in self._items]
        roled.drawmenu(items, selected, title, drawback)

    def drawlong(self, selected=0, title='patches', drawback=True):
        pass

    def get_selected(self):
        """get selected item"""
        return self._items[self._pos]
