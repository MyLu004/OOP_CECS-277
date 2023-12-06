#ADPTEE CLASS

import math

class RightTriangle():
    def __init__(self, base, height):
        self._base = base
        self._height = height

    @property
    def base(self):
        return self._base

    @property
    def height(self):
        return self._height

    def calc_area(self):
        return 0.5 * self._base * self._height

    def calc_hypotenuse(self):
        return math.sqrt(self._base**2 + self._height**2)

    def __str__(self):
        return f"B : {str(self._base)} | H : {str(self._height)}\n" \
               f"Hypot : {str(self.calc_hypotenuse())}"