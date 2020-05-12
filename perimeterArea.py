width = float(input("Please enter the width of the rectangle: "))
lenght = float(input("Please enter the lenght of the rectangle: "))

def rectanglePerimeter():
    perimeter = 2 * (width + lenght)
    return perimeter;
def rectangleArea():
    return width * lenght;

print("The perimeter is", rectanglePerimeter(), "and the area is ", rectangleArea())

"""
Program returns the perimeter and area of a rectangle.
"""
