import abc

class UseableInterface(abc.ABC):
    @abc.abstractmethod
    def usable_method(self):
        pass

    def calculate_method(self):
        pass