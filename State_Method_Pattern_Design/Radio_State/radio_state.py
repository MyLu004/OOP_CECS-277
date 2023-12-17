import abc
#Interface State class: declares the state-specific methods. These methods should make sense for all
#concrete states because you don't want some of your states to have useless methods that will never be called

#interface class: the abstract class contain all the abstract method to overwriten
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