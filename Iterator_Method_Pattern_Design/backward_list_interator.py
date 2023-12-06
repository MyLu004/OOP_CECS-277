
class BackwardsListInterator():
    def __init__(self, num_list):
        self._num_list = num_list #pass the numlist to alble access the list
        '''initialize my starting point is the len(list) to go backward'''
        self._i = len(self._num_list._nums)

    def __iter__(self):
        '''to re-define the for loop???'''
        return self

    def __next__(self):
        self._i -= 1
        if self._i <= 0:
            raise StopIteration
        else:
            return self._num_list._nums[self._i]
