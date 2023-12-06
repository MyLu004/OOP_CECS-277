import stateA

class Context:
    def __init__(self): #compotion : set the stateA is the initial object
        self._state = stateA.StateA()

    def change_state(self,state): #changing state in here
        self._state = state

    def request(self):
        return self._state.handler(self) #return the string