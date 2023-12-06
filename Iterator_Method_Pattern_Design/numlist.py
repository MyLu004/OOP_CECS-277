import list_interator

class Numlist:
    def __init__(self):
        self._nums = [1,2,3,4,5]

    def __iter__(self):
        '''start at -1, so we will start at 0 like self.nums[0]'''
        self._i = -1

        return self

    def __next__(self):
        self._i += 1
        #print('my i:', self._i)
        if self._i >= len(self._nums):
            raise StopIteration
        else:
            #retur n the value in the list
            return self._nums[self._i]

if __name__ == "__main__":
    myList = Numlist()

    for n in myList:
        for m in myList:
            print(m, end= ' ')
    print()