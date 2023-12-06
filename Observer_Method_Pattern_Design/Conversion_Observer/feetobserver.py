import conversionObserver

class FeetObserver(conversionObserver.Conversion_Observer):
    def __init__(self, subject):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        feet = self._subject.inches /12
        print("Feet = ", str(feet))
