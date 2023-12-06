import abc
import plate

#the order inheritance matter
class PlateDecorator(plate.Plate, abc.ABC):
    def __init__(self,p):
        ''' pass in the plate p and assign it to the _plate attribute'''
        self._plate = p

    def description(self):
        ''' returns a string dessription of the plate and what is on it'''
        return self._plate.description()

    def area(self):
        ''' returns the remaining square inches the plate can hold'''
        return self._plate.area()

    def weight(self):
        ''' returns the remaining number of ounces the plate can hold '''
        return self._plate.weight()

    def count(self):
        ''' returns the number of food items the plate is current holding'''
        return self._plate.count()
