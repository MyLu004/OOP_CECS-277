import abc

class AbstractFriesFactory(abc.ABC):
    @abc.abstractmethod
    def make_regular(self):
        pass

    @abc.abstractmethod
    def make_spicy(self):
        pass