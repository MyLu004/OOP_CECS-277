#class card [class B] compostion to class deck [class A]

class Card:
    mySuit = ['Clubs','Diamonds','Hearts','Space']
    myRank = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    def __init__(self, suit , rank):
        self._rank = rank
        self._suit = suit

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f'{self._rank} of {self._suit}'

    def __lt__(self, other):
        #comparing rank '2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace'
        return self.myRank.index(self._rank) < self.myRank.index(other._rank)

#
# if __name__ == "__main__": #local testing
#     pass