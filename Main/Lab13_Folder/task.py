#CLASS TASK [CLASS B]

class Task:
    '''assign the parameters to the attributes'''
    def __init__(self, desc = "", date = "MM/DD/YYYY", time = "HH:MM"):
        self._desc = desc
        self._date = date
        self._time = time

    '''string description of the task'''
    @property
    def desc(self):
        return self._desc

    '''date: due date of the task. A string in the format: MM/DD/YYYY'''
    @property
    def date(self):
        return self._date

    '''time: time the task is due. A string in the format: HH:MM'''
    @property
    def time(self):
        return self._time

    '''returns a string used to display the task information to the user'''
    def __str__(self):
        return self._desc + " - Due: " + self._date + " at " + self._time

    '''returns a string used to write the task to the file'''
    def __repr__(self):
        #return a string used to write the task to the file
        return f'{self._desc},{self._date},{self._time}\n'

    '''returns true if the self task is less than the other task'''
    def __lt__(self, other): #comparing
        #return True if the self task is less than the other task

        selfYear, otherYear = self._date[6:],other._date[6:]
        selfMonth,otherMonth = self._date[0:2],other._date[0:2]
        selfDate, otherDate = self._date[3:5],other._date[3:5]
        selfHour, otherHour = self._time[0:2],other._time[0:2]
        selfMinute,otherMinute =  self._time[3:],other._time[3:]
        selfDesc, otherDesc = self._desc,other._desc

        return (selfYear,selfMonth,selfDate,selfHour,selfMinute,selfDesc) < (otherYear,otherMonth,otherDate,otherHour,otherMinute,otherDesc)
