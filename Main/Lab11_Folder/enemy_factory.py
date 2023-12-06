import abc

class EnemyFactory(abc.ABC):
    @abc.abstractmethod
    def create_random(self):
        pass