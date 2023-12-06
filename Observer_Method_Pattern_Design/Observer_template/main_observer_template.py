import subject
import observer_A

def main():
    mySubject = subject.Subject()
    myObsA = observer_A.ObserverA(mySubject)

    mySubject.state = "B" #ObsA -> subject state: B
    mySubject.state = "C" #ObsA -> subject state: C

main()