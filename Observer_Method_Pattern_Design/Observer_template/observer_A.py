#CONCRETE OBSERVER
import observer
class ObserverA(observer.Observer):
    def __init__(self, subject):
        self._subject = subject
        self._subject.attach(self) #append to the observer list, when the state change

    def update(self):
        print("objA -> subject state: " + self._subject.state)