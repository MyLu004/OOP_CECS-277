import originator

#The Caretaker : controls the Originator's states and stores the Mementos

def main():
    myHistory = [] #storing the memento object that eventually given back to the Orginator to revert it state
    myOriginator = originator.Originator() #0

    myOriginator.change_state() #1
    myOriginator.change_state() #2

    print("Current State = "+ str(myOriginator.state)) #2

    #saving the state, append the state to the history
    myHistory.append(myOriginator.save()) #save state 2

    myOriginator.change_state() #3
    myOriginator.change_state() #4

    print("Current State = "+ str(myOriginator.state)) #4
    myHistory.append(myOriginator.save()) #save state 4

    myOriginator.change_state() #5
    print("Current State= " + str(myOriginator.state))  #5

    myOriginator.restore(myHistory.pop(len(myHistory)-1)) #restore to state 4
    print("Current State= " + str(myOriginator.state))  #4

    print("myHistory: ",myHistory)

    myOriginator.restore(myHistory.pop(len(myHistory)-1)) #restore to state 2

    print("myHistory: ",myHistory)

    print("Current State= " + str(myOriginator.state))  #2

main()