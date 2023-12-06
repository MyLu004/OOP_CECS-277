
class Cashier:
    def __init__(self,cook):
        self._order_item = []
        self._cook = cook

    def add_item(self, item):
        self._order_item.append(item)

    def calc_total(self):
        total = 0
        for item in self._order_item:
            total+= item.price
        return total

    def get_non_cookable_item(self, item):
        return "Getitng " + item.name

    def bag_order(self):
        s = ''
        for item in self._order_item:
            if item.is_cookable():
                s += self._cook.make_item(item) + "\n"
            else:
                s += self.get_non_cookable_item(item) + "\n"
        return s
