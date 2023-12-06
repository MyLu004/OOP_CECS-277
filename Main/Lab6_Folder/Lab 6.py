import check_input
from tasklist import Tasklist

def main_menu():
    print("\n- TaskList-")
    print('Task to complete: ', myList.__len__())
    print('1.Display current task \n2.Display all tasks \n3.Mark current task complete \n4.Add new task \n5.Save and quit')

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

def choice_1(myVal):
    #display all current task [should work on the sorting here]
    if myList.__len__() == 0:
        print("All task is complete")
    else:
        print('Current task is:')
        print(myVal.__getitem__(0))

def choice_2(totalTask, myList):
    print('Task to complete: ',totalTask)
    if myList.__len__() == 0:
        print("All task is complete")
    else:
        for amount in range(totalTask):
            print(myList[amount], end='\n')

def choice_3(myVal):
    print("Marking current task as complete")
    print((myVal.__getitem__(0)))

    myVal.mark_complete() #delete the task in the list

    if myList.__len__() > 0:
        print("New current task is:") #error
        print((myVal.__getitem__(0)))

    #display all current task [depend on get time and date, to check for the attribute]


def choice_4(myList,task,due_date,due_time):
    #date = "MM/DD/YYYY", time = "HH:MM"
    print('New current task is:')
    print(f'{task} - Due: {due_date} at {due_time}')

    task = str(task)

    myList.add_task(task,due_date,due_time)


if __name__ == "__main__":
    myList = Tasklist()
    user_input = 0

    totalTask = myList.__len__()

    while user_input != 5 :
        main_menu()
        user_input = check_input.get_int_range("Enter Choice: ",1,5)

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

        totalTask = myList.__len__()


    myList.save_file()
    print('END OF THE GAME')