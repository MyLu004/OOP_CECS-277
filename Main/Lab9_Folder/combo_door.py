#COMBO : INTERFACE [DOOR]
import random
import door

class ComboDoor(door.Door):
    def __init__(self):
        self._correct_value = random.randrange(1,11)
        self._input = 0


    def examine_door(self):
        return "You encounter Combo Door\nA door with a combination lock. You can spin the dial to a number 1-10"

    def menu_option(self):
        return "Enter #1-10: "

    def get_menu_max(self):
        return 10

    def attempt(self,option):
        self._input = option

    def is_unlocked(self):

        if self._input == self._correct_value:
            return True
        else:
            return False

    def clue(self):
        if self._input > self._correct_value:
            return "Too High"
        elif self._input < self._correct_value:
            return "Too Low"

    def success(self):
        return "Congratulations, you opened the combo door."

