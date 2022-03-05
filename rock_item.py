"""menu item class"""


class Item:
    """menu item class"""
    count = 0

    def __init__(self, name: str) -> None:
        Item.count += 1
        self._name = name
        self._child_page = None

    @property
    def name(self) -> str:
        """return name of Item"""
        return self._name

    @property
    def order(self) -> int:
        """get order num"""
        return self._order

    @order.setter
    def order(self, value: int) -> None:
        """set order num"""
        self._order = value


class Page:
    """page of items"""

    def __init__(self, name: str) -> None:
        self._name = name
        self._items = []

    def append(self, item: Item) -> None:
        """append item"""
        self._items.append(item)

    @property
    def name(self) -> str:
        """return name of Item"""
        return self._name

    def get_item(self, n_ord: int) -> Item:
        return self._items[n_ord]

    def get_items(self) -> list:
        return self._items

    def get_item_names(self) -> list:
        return [x.name for x in self._items]
