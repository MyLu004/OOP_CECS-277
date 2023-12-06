import abc

class AbstractFactory(abc.ABC):
    @abc.abstractmethod
    def create_prod_a(self):
        pass

    def create_prod_b(self):
        pass