

class Measurement:
    def __init__(self):
        self._inches = 0
        self._observers = []

    @property
    def inches(self):
        return self._inches

    @inches.setter
    def inches(self, new_inches):
        self._inches = new_inches
        self._notify_observers()

    def attach(self, observer):
        self._observers.append(observer)

    def _notify_observers(self):
        for obs in self._observers:
            obs.update()