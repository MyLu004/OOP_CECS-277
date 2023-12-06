import abc

class AbstractProductB(abc.ABC):
    @abc.abstractmethod
    def func_b(self):
        pass