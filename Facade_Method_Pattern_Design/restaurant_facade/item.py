#Item

class Item:
    """ represents a restaurant menu item.
    Attributes"
        name(str) : name of the item
        price(int) : price of item
        cookable (bool) : if item is cookable
    """
    def __init__(self,name, price, cookable):
        """initializes the item with a nice, price, and cookability"""
        self._name = name
        self._price = price
        self._cookable = cookable

    @property
    def name(self):
        """returns the name of the item."""
        return self._name

    @property
    def price(self):
        """returns the price of the item"""
        return self._price

    def __str__(self):
        """returns the string representation of the item."""
        return f'{self._name} $ {str(self._price)}'

    def is_cookable(self):
        return self._cookable