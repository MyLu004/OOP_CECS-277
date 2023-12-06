import copy

from hero import Hero
from map import Map
from enemy import Enemy

def checking_area(checking_location):

    if myMap[checking_location[0]][checking_location[1]] == 'n':
        print("there is nothing here")
        return 'n'

    elif myMap[checking_location[0]][checking_location[1]] == 'm':
        print("There is a monster")
        return 'm'
    elif myMap[checking_location[0]][checking_location[1]] == 'i':
        return 'i'

    elif myMap[checking_location[0]][checking_location[1]] == 'f':
        return 'f'

    else:
        return 'o'



if __name__ == "__main__":

    myHero = Hero('Kinoko')
    myMap = Map()


    game_cond = True

    while myHero.hp != 0 and game_cond is True:
        print('\n-----------------------------------------')
        print(myHero)
        print(myMap.show_map(myHero.location))
        print(f'1.N | 2.S | 3.E | 4.W | 5.Quit')

        myHeroChoice = int(input("Chose the direction: "))
        myVal = "#"
        checking_location = copy.deepcopy(myHero.location)


        if myHeroChoice == 1:

            if checking_location[0] - 1 < 0: #will print you cannot go this way
                myVal = myHero.go_north()
            else:
                checking_location[0] = checking_location[0] - 1
                myVal = checking_area(checking_location)

            print('my Val: ',myVal)
            if myVal == 'n':
                myMap.reveal(myHero.location)
                myHero.go_north()

            elif myVal == 'm':
                myEnemy = Enemy()
                print(f"You encounter a {myEnemy}")
                print(f'1.Attack {myEnemy.name}\n2.Run Away')
                heroOption = int(input("Enter choice: "))

                if heroOption == 1:
                    while myEnemy.hp != 0 and heroOption == 1:

                        myHero.attack(myEnemy)
                        myEnemy.attack(myHero)
                        print("\n---------------------------")
                        print(f'1.Attack {myEnemy.name}\n2.Run Away')
                        print('my enemy HP: ', myEnemy.hp)
                        if myEnemy.hp == 0:
                            break
                        else:
                            heroOption = int(input("Enter choice: "))

                    if myEnemy.hp == 0:
                        myMap.reveal(myHero.location)
                        myMap.remove_at_loc(myHero.location)
                        myHero.go_north()
                        print(f"You have slain a {myEnemy.name}")

                elif heroOption == 2:
                    myMap.reveal(myHero.location)
                    print("You running away")

            elif myVal == 'o':
                print("*You cannot go there")

            elif myVal == 'i':
                myHero.heal()

            elif myVal == 'f':
                game_cond = False

        elif myHeroChoice == 2: #Go South [Go down]
            if checking_location[0] + 1 > len(myMap[0])-1:
                myVal = myHero.go_south()
            else:
                checking_location[0] = checking_location[0] + 1
                myVal = checking_area(checking_location)


            if myVal == 'n':
                myMap.reveal(myHero.location)
                myHero.go_south()

            elif myVal == 'm':
                myEnemy = Enemy()
                print(f"You encounter a {myEnemy}")
                print(f'1.Attack {myEnemy.name}\n2.Run Away')
                heroOption = int(input("Enter choice: "))

                if heroOption == 1:
                    while myEnemy.hp != 0 and heroOption == 1:

                        myHero.attack(myEnemy)
                        myEnemy.attack(myHero)
                        print("\n---------------------------")
                        print(f'1.Attack {myEnemy.name}\n2.Run Away')
                        print('my enemy HP: ', myEnemy.hp)
                        if myEnemy.hp == 0:
                            break
                        else:
                            heroOption = int(input("Enter choice: "))

                    if myEnemy.hp == 0:
                        myMap.reveal(myHero.location)
                        myMap.remove_at_loc(myHero.location)
                        myHero.go_south()
                        print(f"You have slain a {myEnemy.name}")

                elif heroOption == 2:
                    myMap.reveal(myHero.location)
                    print("You running away")


            elif myVal == 'o':
                print("You cannot go there")

            elif myVal == 'i':
                myHero.heal()

            elif myVal == 'f':
                game_cond = False

        elif myHeroChoice == 3: #move East [to the right]
            if checking_location[1] + 1 > len(myMap[0])-1:
                myVal = myHero.go_east()
            else:
                checking_location[1] = checking_location[1] + 1
                myVal = checking_area(checking_location)

            print('my Val: ', myVal)
            if myVal == 'n':
                myMap.reveal(myHero.location)
                myHero.go_east()

            elif myVal == 'm':
                myEnemy = Enemy()
                print(f"You encounter a {myEnemy}")
                print(f'1.Attack {myEnemy.name}\n2.Run Away')
                heroOption = int(input("Enter choice: "))

                if heroOption == 1:
                    while myEnemy.hp != 0 and heroOption == 1:

                        myHero.attack(myEnemy)
                        myEnemy.attack(myHero)
                        print("\n---------------------------")
                        print(f'1.Attack {myEnemy.name}\n2.Run Away')
                        print('my enemy HP: ', myEnemy.hp)
                        if myEnemy.hp == 0:
                            break
                        else:
                            heroOption = int(input("Enter choice: "))

                    if myEnemy.hp == 0:
                        myMap.reveal(myHero.location)
                        myMap.remove_at_loc(myHero.location)
                        myHero.go_east()
                        print(f"You have slain a {myEnemy.name}")

                elif heroOption == 2:
                    myMap.reveal(myHero.location)
                    print("You running away")

            elif myVal == 'o':
                print("*You cannot go there")

            elif myVal == 'i':
                myHero.heal()

            elif myVal == 'f':
                game_cond = False

        elif myHeroChoice == 4: #Go to West [go to the left]
            if checking_location[1] - 1 < 0:
                myVal = myHero.go_west()
            else:
                checking_location[1] = checking_location[1] - 1
                myVal = checking_area(checking_location)

            print('my Val: ', myVal)
            if myVal == 'n':
                myMap.reveal(myHero.location)
                myHero.go_west()

            elif myVal == 'm':
                myEnemy = Enemy()
                print(f"You encounter a {myEnemy}")
                print(f'1.Attack {myEnemy.name}\n2.Run Away')
                heroOption = int(input("Enter choice: "))

                if heroOption == 1:
                    while myEnemy.hp != 0 and heroOption == 1:

                        myHero.attack(myEnemy)
                        myEnemy.attack(myHero)
                        print("\n---------------------------")
                        print(f'1.Attack {myEnemy.name}\n2.Run Away')
                        print('my enemy HP: ', myEnemy.hp)
                        if myEnemy.hp == 0:
                            break
                        else:
                            heroOption = int(input("Enter choice: "))

                    if myEnemy.hp == 0:
                        myMap.reveal(myHero.location)
                        myMap.remove_at_loc(myHero.location)
                        myHero.go_west()
                        print(f"You have slain a {myEnemy.name}")

                elif heroOption == 2:
                    myMap.reveal(myHero.location)
                    print("You running away")

            elif myVal == 'o':
                print("*You cannot go there")

            elif myVal == 'i':
                myHero.heal()

            elif myVal == 'f':
                game_cond = False



    if myHero.hp <= 0:
        print("YOU DEAD")
    else:
        print("YOU WINNN")

