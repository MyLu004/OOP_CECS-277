

class Cat:
    def __init__(self):
        self.age = 0
        self.mass = 0

    def description(self):
        return f'the cat is {self.age} and {self.mass} kg'

    def play(self):
        return "the cat is playing"


if __name__ == "__main__":
    myCat = Cat(2,5)