"""menu item class"""

class Item:
    """menu item class"""
    count = 0
    def __init__(self, name: str, page: str) -> None:
        Item.count += 1
        self._name = name
        self._page = page

    @property
    def name(self) -> str:
        """return name of Item"""
        return self._name

    @property
    def page(self) -> str:
        """return page of Item"""
        return self._page

    @page.setter
    def page(self, value) -> str:
        """set page name"""
        self._page = value

    @property
    def order(self) -> int:
        """get order num"""
        return self._order

    @order.setter
    def order(self, value: int) -> None:
        """set order num"""
        self._order = value

class OledPage:
    """build page of items"""
    def __init__(self, name: str) -> None:
        self._name = name
        self._items = []

    def append_item(self, item: Item) -> None:
        """append item"""
        self._items.append(item)
