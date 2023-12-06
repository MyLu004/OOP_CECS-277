#DEADBOLT DOOR : INTERFACE [DOOR]
import random
import door

class DeadBolt(door.Door):
    def __init__(self):
        self._bolt1 = random.randrange(1,3) #1: locked | #2: unclocked
        self._bolt2 = random.randrange(1, 3)



    def examine_door(self):
        '''return the description of the door'''
        return "You encounter DeadBolt Door\n" \
               "A door with two DeadBolt." \
               "Both need to be unlocked to open the door, but you " \
               "can't tell if each one is locked or unlocked "


    def menu_option(self):
        ''':return a string of the menu options that user can choose
                from when attempting to unlock the door'''
        return "1. Toggle bolt 1 \n" \
               "2. Toggle bolt 2"

    def get_menu_max(self):
        ''' return the number of options in the above menu'''
        return 2

    def attempt(self,option):
        '''Return a string of the user's attempt to unlock the door'''
        if option == 1: #chosing bolt1
            print("You toggle the first bolt")
            self._bolt1 = -1 #un-clocked it

        if option == 2: #chosing bolt2
            print("You toggle the second bolt")
            self._bolt2 = -1 #true

    def is_unlocked(self):
        """Return whether the door is unlocked or not"""
        if self._bolt1 == -1 and self._bolt2 == -1: #both are unlocked
            return True
        else:
            return False
    def clue(self):
        '''return the hint that is reurned if the user was unsuccessful at their attempt'''
        if self._bolt1 == -1 or self._bolt2 == -1:
            return "You juggle the door ...it seem like one of the bolts is unlocked"
        else:
            return "...it seems like it's completely locked"

    def success(self):
        '''returns the congratualatory message if the user was successful'''
        return "Congratulations, you opened the locked door."

