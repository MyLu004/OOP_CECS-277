import check_input
from tasklist import Tasklist

# My Lu & Andrea Vidican - CECS 277 Sec:06 & Sec:08
# 09/18/2023
# Lab 13: Task List Part 2

'''Displays the main menu and returns the user's valid input'''
def main_menu():

    print("\n- TaskList-")
    print('Task to complete: ', myList.__len__())
    print('1.Display current task \n2.Display all tasks \n3.Mark current task complete \n4.Add new task \n5.Search by date \n6.Save and quit')

'''prompts the user to enter the year, month, and day'''
def get_date():
    print('Enter due date: ')

    month = check_input.get_int_range("Enter month: ", 1, 12)
    if month < 10:
        month = "0" + str(month)

    date = check_input.get_int_range("Enter date: ", 1, 31)
    if date < 10:
        date = "0" + str(date)

    year = check_input.get_int_range("Enter year: ", 2000, 2100)

    due_date =  str(month)+'/'+str(date)+'/'+str(year)
    return due_date

'''prompt the user to enter the hour and minutes'''
def get_time():
    print('Enter Time: ')
    hour = check_input.get_int_range("Enter hour: ", 0, 23)
    if hour < 10:
        hour = "0" + str(hour)

    minute = check_input.get_int_range("Enter minute: ", 0, 59)
    if minute < 10:
        minute = "0" + str(minute)

    due_time = str(hour)+':'+str(minute)

    return due_time


def choice_1(myVal): #display all current task
    if myList.__len__() == 0:
        print("All task is complete")
    else:
        print('Current task is:')
        print(myVal.__getitem__(0))

def choice_2(totalTask, myList): #display all the task
    n= 1
    print('Task to complete: ',totalTask)
    if myList.__len__() == 0:
        print("All task is complete")
    else:
        # for amount in range(totalTask):
        #     print(myList[amount], end='\n')
        for amount in myList:
            print(f"{n}.{amount}",end='\n')
            #print(n,'.',amount, end= '\n')
            n += 1

def choice_3(myVal): #marking current task
    print("Marking current task as complete")
    print((myVal.__getitem__(0)))

    myVal.mark_complete() #delete the task in the list

    if myList.__len__() > 0:
        print("New current task is:") #error
        print((myVal.__getitem__(0)))

    #display all current task [depend on get time and date, to check for the attribute]


def choice_4(myList,task,due_date,due_time): #Add new Task
    #date = "MM/DD/YYYY", time = "HH:MM"
    print('New current task is:')
    print(f'{task} - Due: {due_date} at {due_time}')

    task = str(task)

    myList.add_task(task,due_date,due_time)

def choice_5(myList): #search tasks by date


    n = 1
    my_search = get_date()
    for amount in myList: #iterate through the list
        '''comparing the search_date with the date in the list'''
        if my_search == amount.date:
            print(f"{n}.{amount}",end='\n')
            n+=1
        else:
            pass

    if n == 1:
        print(f"There is no task due on {my_search}")

if __name__ == "__main__":
    myList = Tasklist()
    user_input = 0

    totalTask = myList.__len__()

    while user_input != 6 :
        main_menu()
        user_input = check_input.get_int_range("Enter Choice: ",1,6)
        #user_input = 5

        if user_input == 1: #current task
            choice_1(myList)
        elif user_input == 2: #all task
            choice_2(totalTask, myList)
        elif user_input == 3: #task complete
            if totalTask > 0:
                choice_3(myList)
            else:
                print("No task to mark to complete")

        elif user_input == 4: #new task
            task = str(input('Enter a task: '))

            due_date = get_date() #return string due_date [mm/dd/yyyy]

            due_time = get_time() #return string due time [hh:mm]
            choice_4(myList,task,due_date,due_time)

        elif user_input == 5:
            choice_5(myList)

        totalTask = myList.__len__() #updating the len

    myList.save_file()
    print('END OF THE GAME')