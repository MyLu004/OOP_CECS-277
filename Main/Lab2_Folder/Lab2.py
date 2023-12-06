import random
import check_input


# My Lu & Andrea Vidican - CECS 277 Sec:06 & Sec:08
# 8/28/2023
# Lab 02 Assignment : Three Card Monte

def get_users_bet(money):
    # get the user_bet_amount
    print(f"You have ${money}")

    # check if the current_money is larger than 50 to set up the range
    if money > 50:
        # if larger than, then the range between 0 and 50 [ the maximum ]
        user_betInfo = check_input.get_int_range(("How much you wanna bet?"), 0, 50)
    else:
        # if less than, then the range between 0 and current_money
        user_betInfo = check_input.get_int_range(("How much you wanna bet?"), 0, money)

    # return the user_bet_amount
    return user_betInfo


def get_users_choice():
    # default map
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print("|  1  | |  2  | |  3  |")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")

    # get the user_choice
    # use check_input to make sure the user enter valid value
    user_choice = check_input.get_int_range(("Find the Queen: "), 1, 3)
    return user_choice


def display_queen_loc(queen_loc, user_bet, user_money):
    # select random from 0 to 1 to display the queen locate
    queen_choice = random.randint(0, 2)
    list = ['K', 'K', 'K']

    # replace the list[random] with 'Q'
    list[queen_choice] = 'Q'

    # compare the user_choice with the queen location
    # add queen_choice with 1 cause it was start with 0
    if queen_loc == queen_choice + 1:
        # if True, then u win
        print("You got lucky this time...")
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print(f"|  {list[0]}  | |  {list[1]}  | |  {list[2]}  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")

        # add the bet amount into the user_money_amount
        user_money += (user_bet * 2)

    else:
        # if False, then you lose
        print('Sorry... you lose.')
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print(f"|  {list[0]}  | |  {list[1]}  | |  {list[2]}  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")

        # minus the bet amount into the user_money_amount
        user_money -= user_bet

    # return the user_money
    return user_money


def GameYN():
    user_cont_choice = check_input.get_yes_no("Play again? (Y/N)")

    return user_cont_choice


if __name__ == "__main__":
    print("- Three card Monte -")
    print("Find the queen to double your bet!")

    # initial value
    user_money = 100

    # continue_Choice initiall = True
    cont_choice = True

    # while loop to checking
    # if the user_money is not empty and decide to continue, then run the while loop
    while cont_choice is True and user_money > 0:

        # get the user_bet_amount
        user_bet = get_users_bet(user_money)

        # get the user_choice
        val = get_users_choice()

        # use val in the function to compare the queen choice
        # user_bet to decide add or subtract with the user_money
        # the display_queen will return user_money
        user_money = display_queen_loc(val, user_bet, user_money)

        # check if the user still have money
        if user_money > 0:
            # if yes, then ask the user to continue the game or not
            cont_choice = GameYN()
        else:
            # if not, then the user unable to continue the game
            print("You're out of money. Beat it loser!")
            # it will break out the loop
            break

    print("END OF THE GAME")