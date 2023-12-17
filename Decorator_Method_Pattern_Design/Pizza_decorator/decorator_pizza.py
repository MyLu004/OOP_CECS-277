import pizza
import abc

#the abstract decorator class: which implement the component interface and override its methods.
#These act as the base objects that are then decorated
#   The decorator's overridden methods are then called on this object
#act as the pointer
class Decorator(pizza.Pizza, abc.ABC):
    def __init__(self,p):
        self._pizza = p

    # def get_price(self): #storing the next layers
    #     return self._pizza.get_price()

    def get_price(self):
        return self._pizza.get_price()

    def get_description(self): #storing the next layers
        return self._pizza.get_description()

