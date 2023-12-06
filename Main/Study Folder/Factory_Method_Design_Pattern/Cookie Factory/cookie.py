
import abc

class Cookie(abc.ABC):
    @abc.abstractmethod
    def eat_cookie(self):
        pass