from Main.Lab9_Folder import testing


class Cat(testing.Animal):
    """representation of a cat"""
    def speak(self):
        """Meow the cat"""
        return super().speak() + "Meow!"