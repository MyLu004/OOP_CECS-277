import conversionObserver

class SmoothObserver(conversionObserver.Conversion_Observer):
    def __init__(self, subject):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        smooth = self._subject.inches /67
        print("Smooth = ", str(smooth))
