import abc

class AbstractProductA(abc.ABC):
    @abc.abstractmethod
    def func_a(self):
        pass