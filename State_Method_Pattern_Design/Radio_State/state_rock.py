import radio_state
import state_off
import state_oldies

class StateRock(radio_state.RadioState):
    def turn_on(self,radio):
        #turn on the rock
        return "Radio already turn on..."

    def turn_off(self,radio):
        #turn off the radio off
        radio.change_state(state_off.StateOff())
        return "Turning radio off..."

    def change_station(self,radio):
        #change to radio from Rock to Oldies
        radio.change_state(state_oldies.StateOldies())
        return "Station -> Oldies"