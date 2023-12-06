import testing2
import testing3

class CatDog(testing3.Cat,testing2.Dog):
    def speak(self):
        """Makes teh cat dog speak"""
        return super().speak() + "Meow!"

if __name__ == "__main__":
    myObject = CatDog()
    print(myObject.speak())