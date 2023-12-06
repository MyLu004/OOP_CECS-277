import plate

class LargePlate(plate.Plate):
    def description(self):
        ''' returns a string dessription of the plate and what is on it'''
        return "Filmsy 12 inch paper plate with "

    def area(self):
        ''' returns the remaining square inches the plate can hold'''
        return 113

    def weight(self):
        ''' returns the remaining number of ounces the plate can hold '''
        return 24

    def count(self):
        ''' returns the number of food items the plate is current holding
        :return 0: no item in the place yet
        '''
        return 0