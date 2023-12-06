
#Iterator - basic counting iterator

class Counter:
    def __init__(self,max):
        self._max = max

    def __iter__(self):
        '''re-initialize the for loop'''
        '''set up the initial value for the foor loop'''
        self._n = 0  #variable [self._n] for the for loop [have nothing to do with the object]
        return self

    def __next__(self):
        '''for-loop'''
        '''moving the counter up'''
        self._n += 1 #increment by 1 for the counter
        if self._n > self._max:
            raise StopIteration
        else:
            return self._n #return the value

if __name__ == "__main__":
    myNumber = Counter(10) #object of counter class
    for n in myNumber:
        #build in function auto call __iter__
        #when going through the loop, auto call __next__
        print(n, end= ' ')
