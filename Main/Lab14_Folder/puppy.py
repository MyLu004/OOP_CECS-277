#CONTEXT CLASS

import state_eat
import state_play
import state_asleep

class Puppy:
    def __init__(self):
        self._puppystate = state_asleep.StateSleep() #set the default state
        self._feed = 0
        self._play = 0

    @property #getter
    def feed(self):
        return self._feed
    @property #getter
    def play(self):
        return self._play

    '''updates the puppy's state to the new state'''
    def change_state(self, new_state):
        self._puppystate = new_state

    '''calls the play method for whichever state the puppy is in'''
    def throw_ball(self):
        return self._puppystate.play(self)

    '''calls the feed method for whichever state the puppy is in'''
    def give_food(self):
        return self._puppystate.feed(self)

    '''increments the number of times the pupy has been fed in a row'''
    def inc_feed(self):
        self._feed += 1

    '''increments the number of times the pupy has been played in a row'''
    def inc_play(self):
        self._play += 1


    def reset(self):
        self._play = 0
        self._feed = 0