import decorator_pizza

class Pepperoni(decorator_pizza.Decorator):
    def get_price(self):
        return super().get_price() + 1

    def get_description(self):
        return super().get_description() + " Pepperoni"