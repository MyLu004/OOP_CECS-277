import random
from Main.Lab7_Folder.card import Card

#class deck [class A] composition from class Card [class B]
#ckass deck [class B] aggregtion to class Player [class A]

class Deck:
    def __init__(self): #initializes a standard deck of 52 cards
        self._card = [Card(valsuit,valrank) for valsuit in Card.mySuit for valrank in Card.myRank] #Composition from card
            #List comprehension to create the new list base on the existed list
        '''
        calling the Card class with proper arguments [Card(mysuit,myrank)] 
        '''
            #using the List Comprehension to create the list of card
        Deck.shuffer(self._card) #shuffer the card


    def shuffer(self):
        return random.shuffle(self)

    def draw_card(self):
        return self._card.pop(0) #return the value and pop at the same time

    def __len__(self):
        return len(self._card)

# if __name__ == "__main__": #local testing
#     myDeck = Deck() #create an object
#
#     '''
#     we use the print statement that from the card class
#     '''
