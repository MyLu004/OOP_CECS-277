#CODE DOOR : INTERFACE [DOOR]
import random
import door

class CodeDoor(door.Door):
    def __init__(self):
        myranChoice = ['X','O']
        myCodeList = []

        for i in range(3):
            i = random.choice(myranChoice)
            #print(i)
            myCodeList.append(i)

        self._correct_code = myCodeList
        self._input = None

    def examine_door(self):
        return "You encounter a code door\n" \
               "A door with a coded keypad with three characters" \
               "Each key toggles a value with an 'X' or an 'O'"

    def menu_option(self):
        return "1.Press Key 1 \n2.Press Key 2 \n3.Press Key 3 "

    def get_menu_max(self):
        return 3

    def attempt(self,option):
        self._input = option #X -> O
        if self._correct_code[self._input-1] == "X":
            self._correct_code[self._input - 1] = "O"
        else: #O -> X
            self._correct_code[self._input - 1] = "X"

    def is_unlocked(self):
        if len(set(self._correct_code)) == 1:
            return True
        else:
            return False

    def clue(self):
        print(self._correct_code)

        X_amount = self._correct_code.count("X")
        O_amount = self._correct_code.count("O")


        if X_amount > O_amount:
            return f"There is {X_amount} of correct character"
        else:
            return f"There is {O_amount} of correct character"

    def success(self):
        return "Congratulations, you opened the code door."

