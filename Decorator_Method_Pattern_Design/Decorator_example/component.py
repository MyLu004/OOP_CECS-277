import abc

#Component interface : have everything to call from
class Component(abc.ABC):
    @abc.abstractmethod
    def operation(self): #abstract, get override by concreate component
        pass