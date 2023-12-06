import user_interface
import adaptee

#OBJECT ADAPTER : using composition
#adapts the adaptee into a usable object by using composition
class Adapter(user_interface.UseableInterface):
    def __init__(self):
        self._adapt = adaptee.Adaptee() #composition the adaptee

    def usable_method(self):
        return self._adapt.unsable_method()

    def calculate_method(self):
        return self._adapt.calculate_method_for_user()