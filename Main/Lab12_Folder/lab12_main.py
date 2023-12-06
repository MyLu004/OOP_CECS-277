import check_input
import small_plate
import large_plate
from turkey import Turkey
from stuffing import Stuffing
from potatoes import Potatoes
from beans import Beans
from pies import Pies

# My Lu & Andrea Vidican - CECS 277 Sec:06 & Sec:08
# 11/07/2023
# Lab 012: Thanksgiving Dinner

def examine_plate(myPlate):
    # Sturdiness | Weight
    if myPlate.weight() >= 13:
        Sturdiness = "Strong"
    elif 7 <= myPlate.weight() <= 12:
        Sturdiness = "Weak"
    elif 1 <= myPlate.weight() <= 6:
        Sturdiness = "Bending"
    elif myPlate.weight() <= 0:
        return True

    # Space | Area
    if myPlate.area() >= 41:
        Space = "Plenty"
    elif 21 <= myPlate.area() <= 40:
        Space = "Some"
    elif 1 <= myPlate.area() <= 20:
        Space = "Tiny bit"
    elif myPlate.area() <= 0:
        return True

    print(f'Sturdiness: {Sturdiness}')
    print(f'Space available: {Space}')
    return False

if __name__ == "__main__":
    game_cond = True
    print("- Thanksgiving Dinner -\n"
          "Serve yourself as much food as you like from the buffet, but make sure that your plate"
          "will hold without spilling everywhere!")

    user_plate_choice = check_input.get_int_range("Choose a plate:\n"
                                                  "1.Small sturdy Plate\n"
                                                  "2.Large Flimsy Plate\n",1,2)

    '''asking user choosing plate size'''
    if user_plate_choice == 1:
        myPlate = small_plate.SmallPlate()
    elif user_plate_choice == 2:
        myPlate = large_plate.LargePlate()

    while myPlate.weight() > 0 and myPlate.area() > 0 and game_cond is True:
        '''display the menu'''
        print("1.Turkey \n"
              "2.Stuff \n"
              "3.Potatoes \n"
              "4.Green Beans \n"
              "5.Pie \n"
              "6.Quit")

        "asking user choice for food"
        user_choice = check_input.get_int_range("",1,6)

        #Decorator implement depending on the choice
        if user_choice == 1:
            myPlate = Turkey(myPlate)
        elif user_choice == 2:
            myPlate = Stuffing(myPlate)
        elif user_choice == 3:
            myPlate = Potatoes(myPlate)
        elif user_choice == 4:
            myPlate = Beans(myPlate)
        elif user_choice == 5:
            myPlate = Pies(myPlate)
        elif user_choice == 6:
            game_cond = False
            break

        '''display the description | [:-4] to not incude 'and' at the end'''
        print(myPlate.description()[:-4])

        'execute teh examine_plate method: if True, which is one of the area or weight is 0' \
        'break the loop'
        if examine_plate(myPlate) == True:
            print("Your plate isn't big enough for this much food! Your food spills over the edge.")
            break

    'do nothing'
    if myPlate.area() <= 0 or myPlate.weight() <= 0:
        pass
    else:
        "display the end game prompt, when the player chose quit"
        print(myPlate.description()[:-4])
        print(f"Good Job!, you make it to the table with {myPlate.count()} items")
        print(f"There was still {myPlate.area()} inches left on your plate.")
        print(f"Your plate could have held {myPlate.weight()} more ounces of food")
        print(f"Don't worry, you can always go back for more. Happy Thanksgiving!")

    print("---END OF THE GAME---")