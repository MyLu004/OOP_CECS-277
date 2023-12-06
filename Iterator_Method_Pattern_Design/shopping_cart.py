
class ShoppingCart:
    def __init__(self):
        self._cart = []

    def add_item(self, item):
        '''append the string [name,price] into the list'''
        self._cart.append(item)

    def __iter__(self):
        self._i = -1
        return self

    def __next__(self):
        '''iterate through the list to display'''
        self._i += 1
        if self._i >= len(self._cart):
            raise StopIteration
        else:
            return self._cart[self._i]