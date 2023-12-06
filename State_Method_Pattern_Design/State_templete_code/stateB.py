import state
import stateA

class StateB(state.State):
    def handler(self,context):
        context.change_state(stateA.StateA())
        return "state B"