import check_input
import puppy

if __name__ == "__main__":

    myPuppy = puppy.Puppy() #create the instance of the Puppy object

    '''welcome prompt'''
    print("Congratulations on your new puppy!")
    myInput = check_input.get_int_range("What would you like to do? \n1.Feed the puppy \n2.Play with the puppy \n3.Quit \nEnter Choice: ",1,3)

    while myInput != 3: #if not quit
        print()
        if myInput == 1: #fedding option
            print(myPuppy.give_food())
        elif myInput == 2: #playing option
            print(myPuppy.throw_ball())

        #get the user_input again
        myInput = check_input.get_int_range("What would you like to do? \n1.Feed the puppy \n2.Play with the puppy \n3.Quit \nEnter Choice: ",1,3)

    print("END OF THE GAME")