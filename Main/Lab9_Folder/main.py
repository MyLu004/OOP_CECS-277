import random
import check_input
from basic_door import BasicDoor
from locked_door import LockedDoor
from deadbolt_door import DeadBolt
from combo_door import ComboDoor
from code_door import CodeDoor


def open_door(myListDoorChoice):
    print(myListDoorChoice[round].examine_door())

    # print the menu option
    print(myListDoorChoice[round].menu_option())

    # base on the get_menu_max: the limit of the choice
    userChoice = check_input.get_int_range("", 1, myListDoorChoice[round].get_menu_max())
    player_cont_choice = True  # set True to loop the attempt

    while player_cont_choice:  # if True-> continue
        myListDoorChoice[round].attempt(userChoice)  # user_input into the attempt method

        if myListDoorChoice[round].is_unlocked() is False:  # if fail
            print(myListDoorChoice[round].clue())
            userChoice = check_input.get_int_range("", 1, myListDoorChoice[round].get_menu_max())  # asking input again
        else:  # if true -> success
            print(myListDoorChoice[round].success())  # success prompt
            player_cont_choice = False  # set False to exit the while loop
    return True

if __name__ == "__main__":
    #creating door object
    myBasicDoor = BasicDoor()
    myLockedDoor = LockedDoor()
    myDeadboltDoor = DeadBolt()
    myComboDoor = ComboDoor()
    myCodeDoor = CodeDoor()

    #list of all door
    myDoorList = [myBasicDoor,myLockedDoor,myComboDoor]

    #random choose 3 door
    myListDoorChoice = random.choices(myDoorList, k = 3)

    #shuffer the list
    random.shuffle(myListDoorChoice)


    #welcome prompt
    print("---------------------------------")
    print(f"Welcome to the Escape Room. "
          f"\nYou must unlock {len(myListDoorChoice)} doors to escape... ")
    print("---------------------------------")

    #for range: go through 3 doors [3 times]
    for round in range(len(myListDoorChoice)):
        open_door(myListDoorChoice)
        print("-----------------------------------------")

    print("Congratulations! You escaped .... this time")
    print("---END OF THE GAME---")

