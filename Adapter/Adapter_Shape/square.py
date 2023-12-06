import shape
class Square(shape.Shape):
    def __init__(self, len):
        self._length = len

    def area(self):
        return self._length * self._length

    def perimeter(self):
        return 4*self._length