class Item:
    """item class"""
    def __init__(self, name, level=None):
        self._name = name
        self._level = level

    def __repr__(self):
        return 'Item: ' + self._name 

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level


class Page:
    def __init__(self, name, level=None):
        self._name = name 
        self._level = level

    def __repr__(self):
        return 'Page: ' + self._name

    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level