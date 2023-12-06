import abc

class State(abc.ABC):
    @abc.abstractmethod
    def handler (self,context):
        pass