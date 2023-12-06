#CLASS TASK [CLASS B]

class Task:
    def __init__(self, desc = "", date = "MM/DD/YYYY", time = "HH:MM"):
        self.desc = desc
        self.date = date
        self.time = time

    def __str__(self):
        return self.desc + " - Due: " + self.date + " at " + self.time

    def __repr__(self):
        #return a string used to write the task to the file
        return f'{self.desc},{self.date},{self.time}\n'


    def __lt__(self, other): #comparing
        #return True if the self task is less than the other task

        selfYear, otherYear = self.date[6:],other.date[6:]
        selfMonth,otherMonth = self.date[0:2],other.date[0:2]
        selfDate, otherDate = self.date[3:5],other.date[3:5]
        selfHour, otherHour = self.time[0:2],other.time[0:2]
        selfMinute,otherMinute =  self.time[3:],other.time[3:]
        selfDesc, otherDesc = self.desc,other.desc

        return (selfYear,selfMonth,selfDate,selfHour,selfMinute,selfDesc) < (otherYear,otherMonth,otherDate,otherHour,otherMinute,otherDesc)

# if __name__ == "__main__":
#
#
#     Newtask1 = Task('MathHW','02/22/2023','11:59')
#     Newtask2 = Task('ZZZ', '02/22/2023', '11:59')
#     print(Newtask1 < Newtask2)