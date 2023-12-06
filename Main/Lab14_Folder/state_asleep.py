import puppy_state
import state_eat

class StateSleep(puppy_state.PuppyState):
    def feed(self,puppy):
        '''increment the fed, and change the state to eat when the feed method call'''
        puppy.inc_feed()
        puppy.change_state(state_eat.StateEat())
        return "The puppy wakes up and comes running to eat."

    def play(self,puppy):
        '''can't not play when in sleep state'''
        return "The puppy is asleep. It doesn't want to play right now"