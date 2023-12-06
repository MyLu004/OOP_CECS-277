import abc
#Interface class

class RadioState(abc.ABC):
    @abc.abstractmethod
    def turn_on(self,radio):
        pass

    @abc.abstractmethod
    def turn_off(self,radio):
        pass

    @abc.abstractmethod
    def change_station(self,radio):
        pass