
import random
import check_input
# My Lu & Andrea Vidican - CECS 277 Sec:06 & Sec:08
# 09/06/2023
# Lab 03: Ship, Captain, and Crew!

'''
Create the following functions for your program:
1. roll_dice(dice) – Passes in a list of dice. Randomize the values of each of the
dice 1-6. Sort the values and place them in descending order.

2. display_dice(name, dice) – Passes in the name of the list, and the list of dice.
Display the dice values separated by spaces.

3. find_winner(player_points) – Passes in the two player’s points as a list.
Displays the two player’s points values, and displays who won. If the scores are the
same, then display that it was a tie.
'''

#diceval = the amount of number to generate the random list
def roll_dice(dice_val):  # randomize the list
    #a dice to keep and a dice to roll
    random_list = []

    #the for loop to randomize the list
    for i in range(0,dice_val):
     n = random.randint(1,6)
     random_list.append(n)

    #sorted the list in descending
    random_list.sort(reverse=True)
    print("\nRoll = ", random_list) #display the roll list
    return random_list #return the list

#name: string name | dice = list
def display_dice(name, dice):  # display the the keep or cargo list
    dice.sort(reverse=True)
    return print(f"{name} = {dice}")



def find_winner(player_points): #last step of the game
    print("Score:")
    print(f"Player #1 = {player_points[0]}")
    print(f"Player #2 = {player_points[1]}")

    if player_points[0] > player_points[1]:
        print("Player #1 won!")
    elif player_points[0] < player_points[1]:
        print("Player #2 won!")
    else:
        print("That it was a tie")

def GameYN():
  user_cont_choice = check_input.get_yes_no("Play again? (Y/N)")
  #just return True or False
  return user_cont_choice

if __name__ == "__main__":
    #player data
    player_amount = 2 #fixed value
    player = 1
    player_score = [0, 0]

    print('----Ship, Captain, and Crew!---– \n\n')

    #game start:
    for i in range(player_amount):
        print(f"Player #{player}'s Turn")

        # the amount of dice,roll
        dice_amount = 5
        roll_amount = 3
        keep_list = ['keep', []]

        #conditional statement for continue game
        cont_choice = True

        #value display, [number to compare, and bool condition]
        ship_num = [6, False]
        captain_num = [5, False]
        crew_num = [4, False]

        while cont_choice is True:
            player_list = roll_dice(dice_amount)
            cargo_point = ['cargo', []]
            #checking function and display the string:
            '''
                1.check if there is specific number in the player_list [the random list]
                2.check if that number doesn't exists in the list already
                3.check if they already obtain the number that allow to go to the next state [next condition]
            '''
            if ship_num[0] in player_list and ship_num[0] not in keep_list[1]:
                print('Yo ho ho! Ye secured a ship')
                #reduce the dice amount for generate the play list
                dice_amount -= 1

                #append the value into the list [depend on the index]
                keep_list[1].append(player_list[player_list.index(ship_num[0])])

                #then remove the value from the main list [depend on the index]
                player_list.remove(player_list[player_list.index(ship_num[0])])

                #set the condition is true
                ship_num[1] = True

            if captain_num[0] in player_list and captain_num[0] not in keep_list[1] and ship_num[1] == True:
                print("Shiver me timbers! A Capt'n!")
                dice_amount -= 1
                keep_list[1].append(player_list[player_list.index(captain_num[0])])
                player_list.remove(player_list[player_list.index(captain_num[0])])
                captain_num[1] = True

            if crew_num[0] in player_list and crew_num[0] not in keep_list[1] and captain_num[1] == True:
                print("Ye bribed a crew with Grog!")
                dice_amount -= 1
                keep_list[1].append(player_list[player_list.index(crew_num[0])])
                player_list.remove(player_list[player_list.index(crew_num[0])])
                crew_num[1] = True
                #finally have everything

            #display the keep_list
            display_dice(keep_list[0],keep_list[1])

            #calculate the score when they have everything [when all the condition is met]
            if (ship_num[1] == True) and (captain_num[1] == True) and (crew_num[1] == True):
                #append the value into the cargo list to display and calculate
                cargo_point[1].append(player_list[0])
                cargo_point[1].append(player_list[1])

                #display the cargo_point
                display_dice(cargo_point[0],cargo_point[1])
                print(f"Your cargo points are: {sum(cargo_point[1])}")


            #print('player list', player_list)
            if roll_amount > 0: #if the roll not out yet, then keep asking
                cont_choice = GameYN()
                roll_amount -= 1
            else:
                break

        #update the new value in the player_score list
        player_score[player-1] = (sum(cargo_point[1]))
        #display it
        print(f"Player #{player} points = { player_score[player-1]}\n")
        #then update the player
        player += 1

    #outside the game
    #checking winner
    find_winner(player_score)
    print("---END OF THE GAME---")





