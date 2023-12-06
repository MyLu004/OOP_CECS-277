
#SUBJECT CLASS: class has state and maintain the list of observers that will be notifies whenever the state change

class Subject:
    def __init__(self):
        self._state = "A"
        self._observers = []

    @property #return the current state [getter]
    def state(self):
        return self._state

    #call this will auto call the getter as well
    #update the value [setter]
    @state.setter
    def state(self, new_state):
        self._state = new_state
        #notify when the state change
        self._notify_observers()

    #append the changeo to the list
    def attach(self,observer):
        self._observers.append(observer)


    def _notify_observers(self):
        for obs in self._observers:
            obs.update()