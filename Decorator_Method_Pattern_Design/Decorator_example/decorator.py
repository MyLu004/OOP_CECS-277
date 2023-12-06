import abc
import component

#abtract class : [still even w/out abstract method???]
#layering for the concrete component
#recursive part
class Decorator(component.Component, abc.ABC):
    def __init__(self,comp): #_init_: require the attribute when passing the object
        self._component = comp

    def operation(self):
        return self._component.operation()