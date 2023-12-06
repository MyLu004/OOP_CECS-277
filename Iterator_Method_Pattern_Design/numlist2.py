from list_interator import ListInterator
from backward_list_interator import BackwardsListInterator

class Numlist:
    def __init__(self):
        self._nums = [1,2,3,4,5]

    def __iter__(self):
        '''initial through ListInterator'''
        return ListInterator(self)

    def get_backwards_iterator(self):
        return BackwardsListInterator(self)



if __name__ == "__main__":
    myList = Numlist()

    #regular iterator
    for n in myList:
        '''call init twice'''
        '''run the default [forward]'''
        for m in myList:
            print(m, end= ' ')
        print('')

    print("\nBack ward iteration")
    #backward iterator
    for a in myList.get_backwards_iterator():
        print(a, end=' ')