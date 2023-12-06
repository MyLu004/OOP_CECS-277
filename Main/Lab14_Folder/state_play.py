import puppy_state
import state_asleep
class StatePlay():
    def feed(self, puppy):
        '''can't change back to eat in this state'''
        return "The puppy is too busy playing with the ball to eat right now."

    def play(self, puppy):
        '''increment the plays times'''
        puppy.inc_play() #3 times
        if puppy.play >= 3: #check if it already  play 3 times
            '''If yes, change the state to sleep and reset the fed and play times'''
            puppy.change_state(state_asleep.StateSleep())
            puppy.reset()
            return "You throw the ball again and the puppy excitedly chase it.\n" \
                   "The puppy played so much it fell aslepp!"

        '''if not, return this prompt'''
        return "You throw the ball again and the puppy excitedly chase it."