#CLASS OBSERVER

import abc

class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self):
        pass