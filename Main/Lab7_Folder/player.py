#class player [class A] aggregation from class deck [class B]
#ckass player [class A] get inherited from class dealer [class B]


class Player():
    def __init__(self, deck):
        self._deck = deck #referred class Card
        self._hand = [] #inital the player hand list
        for i in range(2):
            self._hand.append(deck.draw_card()) #add 2 new card

        self._hand.sort() #sort the card

    def hit(self): #draw one more card
        self._hand.append(self._deck .draw_card())
        self._hand.sort() #sort it

    def score(self):
        mySum = 0
        for value in self._hand: #calculation the score
            # calculatethe Jack,Queen,King value
            if (value.rank == 'Jack') or (value.rank == 'Queen') or (value.rank == 'King') or (value.rank == 'Ace'):
                mySum += 10 #if that the case, just + 10 [include for Ace]
            else:
                mySum += int(value.rank)

        #calculate the amount of Ace card in player hand
        myAce = [value.rank for value in self._hand].count('Ace')

        while myAce > 0: #depend on the sum [if there is Ace in player hand card]
            if mySum <= 22:
                mySum += 1 #Ace value 11 = 10 + 1
            else:
                mySum -= 9 #Ace value 1 = 10 - 9
            myAce -= 1

        #print('this is my sum:' ,mySum)
        return mySum


    def __str__(self): #print the player self.hand list
        mystring = '\n'.join(map(str,self._hand))
        return mystring


# if __name__ == "__main__": #local testing
#     myPlayer = Player(deck.Deck())  #aggregation from deck
#     #put in the deck class into to the player attribute
#     myPlayer.hit()
#     myPlayer.score()
#     print(myPlayer)
#     print(myPlayer.score())

