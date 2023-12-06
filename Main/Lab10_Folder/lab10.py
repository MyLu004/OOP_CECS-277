import copy
import check_input
from hero import Hero
from map import Map
from enemy import Enemy

def checking_area(checking_location):
    if myMap[checking_location[0]][checking_location[1]] == 'n':
        print("there is nothing here")
        return 'n'
    elif myMap[checking_location[0]][checking_location[1]] == 'm':
        print('------------------------')
        print("There is a monster")
        return 'm'
    elif myMap[checking_location[0]][checking_location[1]] == 'i':
        return 'i'

    elif myMap[checking_location[0]][checking_location[1]] == 'f':
        return 'f'

def go_direction(hero_choice):
    if hero_choice == 1:
        myHero.go_north()
    elif hero_choice == 2:
        myHero.go_south()
    elif hero_choice == 3:
        myHero.go_east()
    elif hero_choice == 4:
        myHero.go_west()

def counter_Enemy(myHero,hero_dir):
    myEnemy = Enemy()
    print(f"you counter a {myEnemy}")
    print(f'1. Attack {myEnemy.name}\n2.Run Away')
    #asking for the hero choice [fighting or running]
    hero_choice = check_input.get_int_range("Enter the choice counter the enemy: ",1,2)

    if hero_choice == 1:
        while myEnemy.hp != 0 and hero_choice == 1:
            myHero.attack(myEnemy)
            myEnemy.attack(myHero)

            if myEnemy.hp > 0:
                hero_choice = check_input.get_int_range("Enter the choice counter the enemy: ",1,2)
            else:
                myMap.reveal(myHero.location)
                myMap.remove_at_loc(myHero.location)
                go_direction(hero_dir)
                print(f"You have slain a {myEnemy.name}")
                print('------------------------')
                break
    elif hero_choice == 2:
        myMap.reveal(myHero.location)
        print("You ran away!")
        print('------------------------')

if __name__ == "__main__":
    heroName = input("What is your name, traveler? ")
    myHero = Hero(heroName)
    myMap = Map()
    game_cond = True
    while myHero.hp != 0 and game_cond is True:
        print(myHero)
        print(myMap.show_map(myHero.location))

        print('--------------------------------------------')
        print(f'1.North\n2.South\n3.East\n4.West\n5.Quit')
        myHeroChoice = check_input.get_int_range("Enter the choice for the direction: ",1,5)
        myVal = "#"

        checking_location = copy.deepcopy(myHero.location) #hero location
        #get the location value from hero to predict the move

        if myHeroChoice == 1:
            if checking_location[0] - 1 < 0: #GO NORTH [y-1,x] | UP
                #go outside the boundary, will return cannot go that way
                myVal = myHero.go_north()
            else:
                checking_location[0] = checking_location[0] - 1
                myVal = checking_area(checking_location)

        elif myHeroChoice == 2: #GO SOUTH [y,x+1] | DOWN
            if checking_location[0] + 1 > len(myMap[0])-1:
                #go outside the boundary, will return cannot go that way
                myVal = myHero.go_south()
            else:
                checking_location[0] = checking_location[0] + 1
                myVal = checking_area(checking_location)

        elif myHeroChoice == 3:  #GO EAST [y,x+1] | RIGHT
            if checking_location[1] + 1 > len(myMap[0]) - 1:
                myVal = myHero.go_east()
            else:
                checking_location[1] = checking_location[1] + 1
                myVal = checking_area(checking_location)

        elif myHeroChoice == 4: #GO WEST [y,x-1] | LEFT
            if checking_location[1] - 1 < 0:
                myVal = myHero.go_west()
            else:
                checking_location[1] = checking_location[1] - 1
                myVal = checking_area(checking_location)

        elif myHeroChoice == 5: #GO WEST [y,x-1] | LEFT
            myVal = "#"
            game_cond = False

        #checking the myVal
        if myVal == 'n':
            myMap.reveal(myHero.location)
            go_direction(myHeroChoice)
        elif myVal == 'm':
            counter_Enemy(myHero,myHeroChoice)

        elif myVal == 'o':
            print("You cannot go that way")

        elif myVal == 'i':
            print("You found a Health Potion!, You drink it to restore your health.")
            myHero.heal()
            go_direction(myHeroChoice)
            myMap.remove_at_loc(myHero.location)
            myMap.reveal(myHero.location)

        elif myVal == 'f': #update the location and switch the map
            print("Congrat, you win")
            game_cond = False

    '''when existing the while loop, there is 2 cases happen   
    1. Player Dead
    2. Player Win
    '''
    if myHero.hp <= 0:
        print("Player dead")

    print("END OF THE GAME")

