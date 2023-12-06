import copy
import check_input
from hero import Hero
from map import Map
import beg_factory
import exp_factory

# My Lu & Andrea Vidican - CECS 277 Sec:06 & Sec:08
# 11/07/2023
# Lab 011: Dungeons and Monster Part 2


def checking_area(checking_location): #checking the value and return the symbol
    if myMap[checking_location[0]][checking_location[1]] == 'n':
        print("there is nothing here")
        return 'n'
    elif myMap[checking_location[0]][checking_location[1]] == 's':
        #print("there is nothing here")
        return 's'
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

def counter_Enemy(myHero,hero_dir,level,checking):
    #creating Enemy base on the level_input
    if level == 1: #beginner factory
        myFactory = beg_factory.BegFactory()
    elif level == 2: #expert factory
        myFactory = exp_factory.ExpFactory()

    #creating random base on the factory
    myEnemy = myFactory.create_random()

    print(f"you counter a {myEnemy}")
    print(f'1. Attack {myEnemy.name}\n2.Run Away')
    #asking for the hero choice [fighting or running]
    hero_choice = check_input.get_int_range("Enter the choice counter the enemy: ",1,2)

    #chose to fight
    if hero_choice == 1:
        while myEnemy.hp != 0 and hero_choice == 1: #if the player not dead and if the player still chose to fight
            myHero.attack(myEnemy)
            myEnemy.attack(myHero)

            if myEnemy.hp > 0: #check the enemy hp
                print(f'1. Attack {myEnemy.name}\n2.Run Away')
                hero_choice = check_input.get_int_range("Enter the choice counter the enemy: ",1,2)
                #asking the player again

            else: #defeated the enemy
                myMap.remove_at_loc(checking)
                myMap.reveal(myHero.location)
                go_direction(hero_dir)
                print(f"You have slain a {myEnemy.name}")
                print('------------------------')
                break

    elif hero_choice == 2: #chose running away
        myMap.reveal(checking) #reveal the monster location
        print("You ran away!")
        print('------------------------')

if __name__ == "__main__":
    heroName = input("What is your name, traveler? ")

    #level to creating the enemy
    level = check_input.get_int_range("Difficulty: \n1.Beginner \n2.Expert\n", 1, 2)

    #map counter to loading the map
    map_counter = 1
    myHero = Hero(heroName)

    #creating the map
    myMap = Map()

    #game condition
    game_cond = True

    #either the hero.hp > 0 or the player quit
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
            game_cond = False

        #checking the myVal
        if myVal == 'n': #if the destination is n, return nothing
            go_direction(myHeroChoice)
            myMap.reveal(myHero.location)
        elif myVal == 'm': #if the destination is m, go into counter_enemy function
            myMap.reveal(checking_location)
            counter_Enemy(myHero, myHeroChoice, level,checking_location)

        elif myVal == 'o': #if the destination is o, print out the statement cannot go that way
            print("You cannot go that way")

        elif myVal == 'i': #if i, you got the item
            print("You found a Health Potion!, You drink it to restore your health.")
            myHero.heal() #heal the hp to max
            go_direction(myHeroChoice) #make the hero go to that locaiton
            myMap.remove_at_loc(myHero.location) #remove the "i" symbol and replace with n
            myMap.reveal(myHero.location) #reveal it

        elif myVal == 's': #if s, then just move back to the starting point
            go_direction(myHeroChoice)

        elif myVal == 'f': #if f, then load the new map
            print("Congratulation, you found the stair to the next dungeon")
            go_direction(myHeroChoice)
            map_counter += 1
            if map_counter > 3: #if map_counter is greater than 3, then reset to 1 [1,2,3,...,1,2,3]
                map_counter = 1

            myMap.load_map(map_counter) #load the new map
            myMap.reveal(myHero.location) #reveal the locaiton


    '''when existing the while loop, there is 2 cases happen   
    1. Player Dead
    2. Player Win
    '''
    if myHero.hp <= 0:
        print("Player dead")

    print("END OF THE GAME")

