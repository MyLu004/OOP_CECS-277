import context

def main():
    myContext = context.Context()
    print(myContext.request()) #state A
    print(myContext.request()) #state B
    print(myContext.request()) #state A

main()