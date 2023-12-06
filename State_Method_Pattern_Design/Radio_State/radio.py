import state_off

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