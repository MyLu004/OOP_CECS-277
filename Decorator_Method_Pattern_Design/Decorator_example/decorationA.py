import decorator


#concrete decorator class
#inheritance from decorator [extra behavior]
class DecorationA(decorator.Decorator):
    def operation(self):
        return super().operation() + self.additional_operation()

    def additional_operation(self):
        return "DecA"