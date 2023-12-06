import radio_state
import state_off
import state_rock

class StatePop(radio_state.RadioState):
    def turn_on(self,radio):
        return "Radio is already turn on...."

    def turn_off(self,radio):
        radio.change_state(state_off.StateOff())
        return "tunring off the radio..."

    def change_station(self,radio):
        radio.change_state(state_rock.StateRock())
        return "Station -> Rock"