'''
Create a Rectangle class with the following in Python:
1. Attributes – x, y, width, height

2. __init__(self, w, h) – pass in w and h (not x and y), assign
them to width and height, set the x and y attributes to 0.

3. get_coords(self) – returns the x and y values as a pair (either a tuple or a list).

4. get_dimensions(self) – returns the rectangle’s width and height as a pair.

5. move_up(self) – moves the rectangle up one row.

6. move_down(self) – moves the rectangle down one row.

7. move_left(self) – moves the rectangle left one column.

8. move_right(self) – moves the rectangle right one column.
'''

class Rectangle():
    def __init__(self, w, h):
        self.x = 0
        self.y = 0
        self.w = w
        self.h = h


    def get_coords(self):
        return (self.x, self.y) #return them as the tuples

    def get_dimensions(self):
        return (self.w, self.h) #return them as the tuples

    def move_up(self):
        self.y -= 1
        # a - 1

    def move_down(self):
        self.y += 1
        # a + 1

    def move_left(self):
        self.x -= 1
        # b - 1

    def move_right(self):
        self.x += 1
        # b + 1