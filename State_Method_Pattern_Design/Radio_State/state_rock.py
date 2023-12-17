import radio_state
import state_off
import state_oldies
#Concrete State: provide their own implementation for the state-specfic methods.
#To avoid duplication of similar code across multiple states, you may provide intermediate abstract classes that
#encapsulate some common behavior

#Both context and concrete states can set the next state of the context and perform the
#actual state transition by replacing the state object linked to the context.
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