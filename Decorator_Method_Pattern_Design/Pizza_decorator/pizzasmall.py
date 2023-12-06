#small pizza
#concrete component [obj]

import pizza

class PizzaSmall(pizza.Pizza):
    def get_price(self):
        return 5

    def get_description(self):
        return "Small Pizza"