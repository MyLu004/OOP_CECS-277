import state
import stateB

class StateA(state.State):
    def handler(self,context):
        context.change_state(stateB.StateB())
        return "state A"