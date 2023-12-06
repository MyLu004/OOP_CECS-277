import memento

#object that has a state that needs to be saved and eventually reverted back to
class Originator:
    def __init__(self):
        self._state = 0 #inital the state

    @property
    def state(self):
       return self._state

    def change_state(self):
        self._state +=1 #change state, like the counter [from iterate method]

    def save(self): #save the current state, append the val_state that is calle
        return memento.Memento(self._state)

    def restore(self, mem):
        #get the current state through memento
        self._state = mem.get_state()