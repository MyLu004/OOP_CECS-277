# My Lu & Andrea Vidican - CECS 277 Sec:06
# 8/23/2023
# Lab 01 Assignment: Guessing Game

import random
import check_input


def guessing_game():
    count = 0
    target = random.randint(0, 100)

    print("- Guessing Game -")
    user_input = check_input.get_int("I’m thinking of a number. Make a guess (1-100): ")

    while user_input != target:
        # compare the number to the target
        if user_input >= 0 and user_input <= 100:
            if user_input > target:
                print("Too high! Guess again (1-100):")
                count += 1
            elif user_input < target:
                print("Too low! Guess again (1-100):")
                count += 1
        else:
            print("Invalid input - should be within range 1-100. Guess again(1-100)")
        user_input = check_input.get_int("Guess again: ")

    if user_input == target:
        count += 1
        print(f"Correct! You got it in {count} tries.")


guessing_game()