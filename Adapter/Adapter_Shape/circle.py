import shape

class Circle(shape.Shape):
    def __init__(self, rad):
        self._radius = rad

    def area(self):
        return 3.14*self._radius*self._radius

    def perimeter(self):
        return 2* 3.14 * self._radius