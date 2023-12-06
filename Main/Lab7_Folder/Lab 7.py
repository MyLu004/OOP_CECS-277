import check_input
from Main.Lab7_Folder.deck import Deck
from player import Player
from Main.Lab7_Folder.dealer import Dealer

def displayer_winner(pScore,dScore,point):
    #display the winer
    print('')
    if pScore > dScore: #compare score between player and dealer
        print('Player Wins.')
        point[0] += 1

    elif pScore < dScore:#compare score between player and dealer
        print('Dealer Wins.')
        point[1] += 1

    else: #if tied, then only print
        print('Tied Game.')

    print(f"Player's Point: {point[0]}") #display the score
    print(f"Dealer's Point: {point[1]}")


def GameYN(): #checking if the player still wanna play
    cont_choice = check_input.get_yes_no("Player again? (Y/N)")
    return cont_choice


if __name__ == "__main__":
    gameListPts = [0, 0] #initial the score game list
    cont = True #set the True

    print('-Black Jack-')

    while cont: #while True
        '''
        Create the object in the while loop to able restart the deck_class for the new round if the player still 
        want to play again
        '''
        myPlayer = Player(Deck()) #initial the object for Player
        myDealer = Dealer(Deck()) #initial the object for Dealer

        playerScore = myPlayer.score() #get the playerscore
        #Player turn
        while playerScore < 22: #compare if the score larget than 22
            print("\nPlayer's Cards: ")
            print(myPlayer) #display the player card
            print('Score: ',playerScore) #display the player score

            playerChoice = check_input.get_int_range("1.Hit \n2.Stay\nEnter Choice: ", 1, 2) #asking the option

            if playerChoice == 1: #Hit -> draw one more card
                myPlayer.hit()
                playerScore = myPlayer.score() #update the score

            else: #2.stay break out the while loop
                break

        if playerScore >= 22: #check to print brust
            print("Player's Card: ")
            print(myPlayer)
            print('Score = ',playerScore)
            print('Burst!')
            playerScore = -1 #update the score to -1 [losed]

        #Dealer turn
        print("\nDealer's Card: ")
        myDealer.play() #play the dealer class [will do everything]

        dealerScore = myDealer.score() #get the dealer score

        #Compare the score
        #[player point,dealer point]

        gamePoint = displayer_winner(playerScore, dealerScore, gameListPts) #function display the score

        #ask to contiue the game -> redo everything
        cont = GameYN()

    print("\n\n---End of the Game---")


