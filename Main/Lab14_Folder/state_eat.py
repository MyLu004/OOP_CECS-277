import puppy_state
import state_play
import state_asleep
class StateEat(puppy_state.PuppyState):
    def feed(self,puppy):
        '''incremenet the fed '''
        puppy.inc_feed() #3 times
        if puppy.feed >= 3: #check if it already  eat 3 times
            '''If yes, change the state to sleep and reset the fed and play times'''
            puppy.change_state(state_asleep.StateSleep())
            puppy.reset() #reset the feed and play
            return "The puppy continues to eat as you add another scoop of kibble to its bowl.\n" \
                   "The puppy ate so much it feel asleep!"

        '''if not, return this prompt'''
        return "The puppy continues to eat as you add another scoop of kibble to its bowl."


    def play(self,puppy):
        '''change the state to play and increment the play times once'''
        puppy.change_state(state_play.StatePlay())
        puppy.inc_play()
        return "The puppy looks up from its food and chases the ball you threw."