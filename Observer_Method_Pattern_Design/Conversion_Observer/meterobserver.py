import conversionObserver

class MeterObserver(conversionObserver.Conversion_Observer):
    def __init__(self, subject):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        meters = self._subject.inches /39.97
        print("Meters = ", str(meters))
