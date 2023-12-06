import csv

from task import Task
#CLASS TASKLIST [CLASS A]

class Tasklist:
    '''
    Read in the list of tasks from the file and store them in the tasklist by opening the file
    reading in each line that consists of the task description, due date, and time separated by commas, then construct
    the Task object and appending it ot the list, then sort the list
    '''
    def __init__(self): #storing the task from the file
        self.Tasklist = [] #A list of Task Object

        with open("file_test.txt","r") as file:
            #TaskFile = file.readlines()
            TaskFile = file.read().split('\n')

            for line in TaskFile: #append the value to the tasklist
                val = line.split(",")
                self.Tasklist.append(Task(val[0],val[1],val[2]))

        self.Tasklist.sort()

    '''construct a new task using the parameters, list, then sort the list'''
    def add_task(self, desc, date, time):
        self.Tasklist.append(Task(desc,date,time))
        self.Tasklist.sort()
         #??? How they sort

    '''remove the current task from the tasklist'''
    def mark_complete(self):
        self.Tasklist.pop(0)

    '''write the contents of the tasklist back to the file using the Task's'''
    def save_file(self):
        with open("file_test.txt","w+",newline='') as file:
            for i in range(len(self.Tasklist)):
                file.write(repr(self.Tasklist[i]))

    '''return the Task from the list at the specified index'''
    def __getitem__(self, index):
        #return task from the list the specific index
        return self.Tasklist[index]

    '''return the number of items in the tasklist'''
    def __len__(self):
        #return the number of items in the tasklist
        return len(self.Tasklist)

    '''initilize the interator attribute (n) and return self'''
    def __iter__(self):
        self._n = -1
        return self

    '''
    iterate the iterator one position at a time. Raise a StopInteration when the iterator reaches the end of the
    tasklist, otherwise return the Task object at the iterator's current position
    '''
    def __next__(self):
        self._n += 1
        if self._n >= len(self.Tasklist):
            raise StopIteration
        else:
            return self.Tasklist[self._n]

# if __name__ == "__main__":
#     print("This is new list")
#
#     Newlist = Tasklist()
#     Newlist.add_task('mathHW','12/02/2004','11:59')
#     Newlist.add_task('Essay', '12/03/2004', '11:59')
#     Newlist.add_task('Physics', '12/04/2005', '11:59')
#     Newlist.add_task('Discrete Math', '11/27/2004', '11:59')
#
#     for i in Newlist:
#         print(Newlist[i], end=' ')
#
#
#     #(repr(Newlist[0]))
