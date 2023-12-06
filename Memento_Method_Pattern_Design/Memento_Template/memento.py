
#Store the values that represent the previous state of the Originator
#The memento has a construct that passes in the data needed to save its state, and methods to return the value
#of the state when needed

class Memento:
    def __init__(self,s):
        self._state = s

    def get_state(self):
        return self._state

