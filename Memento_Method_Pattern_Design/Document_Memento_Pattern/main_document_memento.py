import document

def main():
    myHistory = []
    myDocument = document.Document()

    print("Enter text (Q to quit, B to back up, R to revert): ")

    done = False

    while not done:
        print(myDocument.words)
        user_input = input("> ")

        if user_input == "Q":
            print("Quitting...")
            done = True

        elif user_input == "B": #saving the check point of the state
            myHistory.append(myDocument.back_up())

        elif user_input == "R": #restore to the check point
            myDocument.restore(myHistory.pop(len(myHistory)-1))

        else:
            myDocument.add_words(user_input)

main()