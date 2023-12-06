import player
class Dealer(player.Player): #inherited from the player

    def play(self):
        myDealerScore = self.score() #the score from the player
        while myDealerScore < 16: #if more than 16 -> draw one card
            print('Dealer Hit!')
            self.hit()
            myDealerScore = self.score() #update the score

        ''' Keep hit until it larger than 16'''

        print(self.__str__()) #print str, the list card

        if myDealerScore >= 22: #if more than 22, then burst
            print('Score: ', myDealerScore)
            myDealerScore = -1 #update the into -1
            print('Brust!')

        else:
            print('Score: ', myDealerScore)

        return myDealerScore

# if __name__ == "__main__": #local testing
#     myDealer = Dealer(Deck())
#     print(myDealer.play())