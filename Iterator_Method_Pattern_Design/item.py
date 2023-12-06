
class Item:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def __str__(self):
        return f'{self._name} ${str(self._price)}'
