import abc

class Conversion_Observer(abc.ABC):
    @abc.abstractmethod
    def update(self):
        pass