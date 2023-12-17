import state_off
import state_pop
import radio_state
#Concrete State: provide their own implementation for the state-specfic methods.
#To avoid duplication of similar code across multiple states, you may provide intermediate abstract classes that
#encapsulate some common behavior

#Both context and concrete states can set the next state of the context and perform the
#actual state transition by replacing the state object linked to the context.
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