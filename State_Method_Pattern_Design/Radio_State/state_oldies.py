import state_off
import state_pop
import radio_state

class StateOldies(radio_state.RadioState):
    def turn_on(self,radio):
        #turn on the oldies
        return "State Oldies: Radio already turn on"

    def turn_off(self,radio):
        #turn of the radio Rock
        radio.change_state(state_off.StateOff())
        return "turning radio off..."

    def change_station(self,radio):
        #change radio to from Oldies to Pop
        radio.change_state(state_pop.StatePop())
        return "Station -> Pop"