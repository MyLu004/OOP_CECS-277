#small pizza
#concrete component [obj]
#which implement the component interface and override its methods.
#These act as the base objects that are then decorated

import pizza

class PizzaSmall(pizza.Pizza):
    def get_price(self):
        return 5

    def get_description(self):
        return "Small Pizza"