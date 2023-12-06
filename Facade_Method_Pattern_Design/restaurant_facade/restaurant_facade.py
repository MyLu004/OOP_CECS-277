import menu
import cashier
import cook

class RestaurantFacade:
    def __init__(self):
        self._menu = menu.Menu()
        self._cook = cook.Cook()
        self._cashier = cashier.Cashier(self._cook)

    def get_menu(self):
        s = ""
        for i in range(len(self._menu)):
            s += str(i + 1) + ". " + str(self._menu[i]) + '\n'
        return s

    def order_item(self, item_name):
        item = self._menu.get_item_by_name(item_name)
        self._cashier.add_item(item)
        if item.is_cookable():
            self._cook.add_cookable(item)

    def calc_total(self):
        return self._cashier.calc_total()

    def get_order(self):
        return self._cashier.bag_order()