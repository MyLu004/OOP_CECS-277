from code_door import CodeDoor

if __name__ == "__main__":
    myCodeDoor = CodeDoor()

    print(myCodeDoor.examine_door())
    print(myCodeDoor.menu_option())

    user_player = int(input("Enter choice: "))
    cont  = True

    while cont:
        myCodeDoor.attempt(user_player)
        if myCodeDoor.is_unlocked() is False:
            print(myCodeDoor.clue())
            user_player = int(input("Enter choice: "))

        else:
            myCodeDoor.success()
            cont = False
