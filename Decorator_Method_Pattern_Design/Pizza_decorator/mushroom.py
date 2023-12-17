import decorator_pizza

#The concrete decorator classes: which extend the Decorator and override the Componet's methods.
#They then call the superclass's version of that method along with any additional behaviors that Decoration should do

class Mushroom(decorator_pizza.Decorator):
    def get_price(self):
        return super().get_price() + 0.5

    def get_description(self):
        return super().get_description() + " Mushroom"