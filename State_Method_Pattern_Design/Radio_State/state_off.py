import radio_state
import state_rock
#off radio method [class]

#Concrete State: provide their own implementation for the state-specfic methods.
#To avoid duplication of similar code across multiple states, you may provide intermediate abstract classes that
#encapsulate some common behavior

#Both context and concrete states can set the next state of the context and perform the
#actual state transition by replacing the state object linked to the context.
class StateOff(radio_state.RadioState):
    def turn_on(self,radio):
        #changing to state rock
        radio.change_state(state_rock.StateRock())
        return "Turning radio on....\nStation -> Rock."

    def turn_off(self,radio):
        return "Radio already off..."

    def change_station(self,radio):
        return "Radio must be on change station."