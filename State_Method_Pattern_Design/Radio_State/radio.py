import state_off
#context class: stores  a reference to one of the conrete state objects and delegates to it all state-specific work
# The context communicates with the state object iva the state interface. The context exposes a setter for passing it a
# new state object

#store the behavior of the state, like what should the method do with the state, behavior are the same, the different is
#which behavior affect to, depend on the state, there target is different.
class Radio:
    def __init__(self):
        self._state = state_off.StateOff() #initial state of radio

    def change_state(self, new_state):
        self._state = new_state

    def off_switch(self):
        return self._state.turn_off(self)

    def on_switch(self):
        return self._state.turn_on(self)

    def channel_switch(self):
        return self._state.change_station(self)