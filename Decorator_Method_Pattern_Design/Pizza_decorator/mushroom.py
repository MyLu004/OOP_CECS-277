import decorator_pizza


class Mushroom(decorator_pizza.Decorator):
    def get_price(self):
        return super().get_price() + 0.5

    def get_description(self):
        return super().get_description() + " Mushroom"