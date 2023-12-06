#LOCKED DOOR : INTERFACE [DOOR]
import random
import door

class LockedDoor(door.Door):
    def __init__(self):
        self._key_location = random.randrange(1,4) #random: 1,2,3
        self._input = 0

        #print("key: ",self._key_location)

    def examine_door(self):
        '''return the description of the door'''
        return "You encounter a Locked door\n" \
               "Look around for the key. "

    def menu_option(self):
        ''':return a string of the menu options that user can choose
                from when attempting to unlock the door'''
        return "1.Look under the mat.\n" \
               "2.Look under flower pot.\n" \
               "3.Look under fake rock."

    def get_menu_max(self):
        ''' return the number of options in the above menu'''
        return 3

    def attempt(self,option):
        '''Return a string of the user's attempt to unlock the door'''
        self._input = option
        if option == 1:
            print("You choose option 1. You look under the mat")
        elif option == 2:
            print("You choose option 2. Yo look under the flower pot")
        else:
            print("You choose option 3. You look under the mat")


    def is_unlocked(self):
        """Return whether the door is unlocked or not"""
        if self._input == self._key_location:
            return True
        else:
            return False
    def clue(self):
        '''return the hint that is reurned if the user was unsuccessful at their attempt'''
        return "Look somewhere else."

    def success(self):
        '''returns the cngratualarory message if the user was successful'''
        return "Congratulations, you opened the locked door."

