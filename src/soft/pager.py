from hard import oled as roled
from common import rock_logger as log

log.config(__name__)

EMPTY = ''


class Pager:
    def __init__(self, items=[], pos=0):
        self._items = items
        self._length = len(items)
        self._max = self._length - 1
        self._pos = pos

        log.info(self.__str__())
        log.info(self.__dict__)

    def populate(self, items, pos=0):
        self._items = items
        self._length = len(self._items)
        self._max = self._length - 1
        self._pos = pos

    def get_items(self):
        return self._items

    def get_selected(self):
        """get selected item"""
        return self._items[self._pos]

    @property
    def pos(self):
        return self._pos


class PagerShort(Pager):
    def update(self, direction):
        newpos = max(0, min(self._max, self._pos + direction))

        if self._pos != newpos:
            self._pos = newpos
            self.draw(self._pos)

    def draw(self, selected=0, title='main title', drawback=False):
        items = [x.name for x in self._items]

        log.info(f"{self.__str__()}")
        log.info(f"position:\t{self.pos}")
        log.info(f"items:\t{items}")
        log.info(f"position:\t{self.get_selected()}")

        roled.drawmenu(items, selected, title, drawback)


class PagerLong(Pager):
    def update(self, direction):
        newpos = max(0, min(self._max, self._pos + direction))

        if self._pos != newpos:
            self._pos = newpos
            self.draw()
        else:
            log.warn("new pos NOT set")

    def draw(self, title='patches', drawback=False):
        items = [x.name for x in self._items]
        new_items = self.decorate_list(items)
        fragment = new_items[self._pos:self._pos+5]

        log.info(f"{self.__str__()}")
        log.info(f"position:\t{self.pos}")
        log.info(f"items:\t{items}")
        log.info(f"position:\t{self.get_selected()}")

        roled.drawmenu(fragment, 2, title, drawback)

    @staticmethod
    def decorate_list(lst):
        double_empty = [EMPTY, EMPTY]
        return double_empty + lst + double_empty
