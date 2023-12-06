#base class: pizza
#function for the pizza class
    #cost
    #description
#base component:
#   size [component / base]
#   topic [decoration]

import abc

class Pizza(abc.ABC):
    @abc.abstractmethod
    def get_price(self):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass