import abc

class Spicy(abc.ABC):
    @abc.abstractmethod
    def eat_fries(self):
        pass