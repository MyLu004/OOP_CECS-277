import user_interface
import adaptee

#CLASS ADAPTER : using inheritance
#adapts the adaptee into a usable ojbect by using inheritance
class Adapter(adaptee.Adaptee,user_interface.UseableInterface):
    def usable_method(self):
        return self.unsable_method()

    def calculate_method(self):
        return self.calculate_method_for_user()