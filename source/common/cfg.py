class Status():
    def __init__(self, current=None, previous=None):
        self._current = current
        self._previous = previous

    @property
    def current(self):
        return self._current

    @property
    def previous(self):
        return self._previous

    @current.setter
    def current(self, item):
        self._current = item

    @previous.setter
    def previous(self, item):
        self._previous = item


MAINSTATUS = Status()
