import right_triangle
import shape

#OBJECT ADAPTER
#inherritance the interface
class Triangle(shape.Shape):
    def __init__(self, base1, height1):
        self._triangle = right_triangle.RightTriangle(base1,height1)

    def area(self): #interface the method from shape
        return self._triangle.calc_area()

    def perimeter(self): #sum of 3 side
        return self._triangle.base + self._triangle.height + self._triangle.calc_hypotenuse()