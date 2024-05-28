# Different Kinds of Shapes - Python
# by CodeChum Admin
# 
# There are different kinds of shapes and in Geometry, each shape has different formulas to get their areas and perimeters. In this program, we will be implementing few of these shapes.
# 
# Class - Shape:
# Methods:
# def get_area(self) -> float: Method with pass as its body.
# def get_perimeter(self) -> float: Method with pass as its body.
#  
# Class - Square (inherits Shape):
# Properties:
# side (type: float): Represents the side length of the square.
# Constructor:
# def __init__(self, side: float): Accepts a single value to initialize side.
# Override Method:
# def get_area(self) -> float: Calculates and returns the area as side * side.
# def get_perimeter(self) -> float: Calculates and returns the perimeter as 4 * side.
#  
# Class - Rectangle (inherits Shape):
# Properties:
# length (type: float): Represents the length of the rectangle.
# width (type: float): Represents the width of the rectangle.
# Constructor:
# def __init__(self, length: float, width: float): Accepts values for length and width.
# Override Method:
# def get_area(self) -> float: Calculates and returns the area as length * width.
# def get_perimeter(self) -> float: Calculates and returns the perimeter as 2 * length + 2 * width.
#  
# Class - Triangle (inherits Shape):
# Properties:
# a (type: float): Represents one side of the triangle.
# b (type: float): Represents another side of the triangle.
# c (type: float): Represents the third side of the triangle.
# Constructor:
# def __init__(self, a: float, b: float, c: float): Accepts values for a, b, and c.
# Override Method:
# def get_area(self) -> float: Calculates and returns the area using Heron's formula.
# def get_perimeter(self) -> float: Calculates and returns the perimeter as a + b + c.
#  
# Class - ShapeCollection:
# Properties:
# shapes (type: List[Shape]): Represents a list of shape objects.
# Constructor:
# def __init__(self, shapes: List[Shape]): Initializes shapes.
# Method
# def calculate_and_print_area_and_perimeter(self) -> None: Loops through each shape in shapes, calculates the area and perimeter, and prints them in two decimal places as:
# Area: {area}
# Perimeter: {perimeter}
# <newline>

class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass