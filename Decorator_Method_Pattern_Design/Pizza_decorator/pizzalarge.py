#large pizza
#concreate component (obj)

import pizza

class PizzaLarge(pizza.Pizza):
    def get_price(self):
        return 7

    def get_description(self):
        return "Large Pizza"