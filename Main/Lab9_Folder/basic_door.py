#BASIC DOOR : INTERFACE [DOOR]
import random
import door

class BasicDoor(door.Door):
    def __init__(self):
        self._state = random.randrange(1,3) #random: 1,2
        self._input = 0

    def examine_door(self):
        '''return the description of the door'''
        return "You encounter a basic door\n" \
               "you can either push it or pull it to open."

    def menu_option(self):
        ''':return a string of the menu options that user can choose
        from when attempting to unlock the door'''
        return "1.Push \n2.Pull "

    def get_menu_max(self):
        ''' return the number of options in the above menu'''
        return 2

    def attempt(self,option):
        '''Return a string of the user's attempt to unlock the door'''
        self._input = option

        if option == 1:
            print("You push the door")
        else:
            print("You pull the door")

    def is_unlocked(self):
        """Return whether the door is unlocked or not"""
        if self._input == self._state:
            return True
        else:
            return False
    def clue(self):
        '''return the hint that is reurned if the user was unsuccessful at their attempt'''
        return "Try the other way"

    def success(self):
        '''returns the cngratualarory message if the user was successful'''
        return "Congratulations, you opened the basic door."

