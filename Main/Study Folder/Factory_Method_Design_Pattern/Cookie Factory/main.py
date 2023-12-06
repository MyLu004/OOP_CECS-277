import sandwichFactory
import dropFactory

def main():
    myfact = dropFactory.DropFactory()
    print(myfact.process_cookie("CC"))
    print(myfact.process_cookie("PB"))

    mySandwichFact = sandwichFactory.SandwichFactory()
    print(mySandwichFact.process_cookie("OR"))
    print(mySandwichFact.process_cookie("TE"))

main()