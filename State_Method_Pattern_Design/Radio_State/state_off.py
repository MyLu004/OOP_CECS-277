import radio_state
import state_rock
#off radio method [class]

class StateOff(radio_state.RadioState):
    def turn_on(self,radio):
        #changing to state rock
        radio.change_state(state_rock.StateRock())
        return "Turning radio on....\nStation -> Rock."

    def turn_off(self,radio):
        return "Radio already off..."

    def change_station(self,radio):
        return "Radio must be on change station."