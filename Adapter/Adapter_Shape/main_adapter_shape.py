
import square
import circle
import triangle

def display_shape(shape_val):
    print(f"Area = " + str(shape_val.area()))
    print(f"Perimeter = "+str(shape_val.perimeter()))

def main():
    myName = ['Circle','Square','Triangle']
    myShape = [circle.Circle(2),square.Square(3), triangle.Triangle(2,3)]

    for s_val in myShape:

        display_shape(s_val)

main()