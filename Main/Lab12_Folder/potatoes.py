import plate_decorator

class Potatoes(plate_decorator.PlateDecorator):
    def description(self):
        '''call the superclass's description and addiitonal description'''
        return super().description() + "Potatoes and "

    def area(self):
        '''call the superclass's method and subtract the food's item area'''
        return super().area() - 18

    def weight(self):
        '''call the superclass's method and subtract the food's item weight'''
        return super().weight() - 6

    def count(self):
        '''call the supperclass's method and add 1 to increment the counter'''
        return super().count() + 1