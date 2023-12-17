import radio_state
import state_off
import state_rock
#Concrete State: provide their own implementation for the state-specfic methods.
#To avoid duplication of similar code across multiple states, you may provide intermediate abstract classes that
#encapsulate some common behavior

#Both context and concrete states can set the next state of the context and perform the
#actual state transition by replacing the state object linked to the context.
class StatePop(radio_state.RadioState):
    def turn_on(self,radio):
        return "Radio is already turn on...."

    def turn_off(self,radio):
        radio.change_state(state_off.StateOff())
        return "tunring off the radio..."

    def change_station(self,radio):
        radio.change_state(state_rock.StateRock())
        return "Station -> Rock"