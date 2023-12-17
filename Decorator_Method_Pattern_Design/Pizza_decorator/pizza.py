#base class: pizza
#function for the pizza class
    #cost
    #description
#base component:
#   size [component / base]
#   topic [decoration]

#   the component interface: with methods that the base objects need to override its methods.
#   These act as the base object are then decorated
import abc

class Pizza(abc.ABC):
    @abc.abstractmethod
    def get_price(self):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass