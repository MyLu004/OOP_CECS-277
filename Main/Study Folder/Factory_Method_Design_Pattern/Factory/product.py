#Abstract Product [A Product interface : defines what product can do]
import abc

class Product(abc.ABC):
    @abc.abstractmethod
    def use_product(self):
        pass

