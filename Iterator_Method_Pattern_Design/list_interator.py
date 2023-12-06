
class ListInterator:
    def __init__(self, num_list):
        '''numlist = the attribute [self] from numlist2'''
        self._num_list = num_list
        #alway reset the init after the nested loop
        self._i = -1

    def __next__(self):
        self._i += 1
        if self._i >= len(self._num_list._nums):
            raise StopIteration
        else:
            return self._num_list._nums[self._i]
