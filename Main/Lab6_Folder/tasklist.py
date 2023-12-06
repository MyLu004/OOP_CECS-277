import csv

from task import Task
#CLASS TASKLIST [CLASS A]

class Tasklist:

    def __init__(self): #storing the task from the file
        self.Tasklist = []

        with open("tasklistfile.txt","r") as file:
            #TaskFile = file.readlines()
            TaskFile = file.read().split('\n')

            for line in TaskFile:
                val = line.split(",")
                self.Tasklist.append(Task(val[0],val[1],val[2]))

        self.Tasklist.sort()


    def add_task(self, desc, date, time):
        self.Tasklist.append(Task(desc,date,time))
        self.Tasklist.sort()
         #??? How they sort

    def mark_complete(self): #remove the currrent task from the tasklist
        self.Tasklist.pop(0)

    def save_file(self): #do later
        with open("file_test.txt","w+",newline='') as file:
            file.write(" ".join(repr(self.Tasklist)))


    def __getitem__(self, index):
        #return task from the list the specific index
        return self.Tasklist[index]

    def __len__(self):
        #return the number of items in the tasklist
        return len(self.Tasklist)

# if __name__ == "__main__":
#     print("This is new list")
#
#     Newlist = Tasklist()
#     Newlist.add_task('mathHW','12/02/2004','11:59')
#     Newlist.add_task('Essay', '12/03/2004', '11:59')
#
#     print(Newlist[0])
#     #(repr(Newlist[0]))
