# Anatomy of a Rectangle - Python
# by CodeChum Admin

# A class Rectangle is already defined in the code editor. Complete the class with the following details:
# Class - Rectangle:
# Implemented Public Properties:
# length (type: float): Represents the length of the rectangle.
# width (type: float): Represents the width of the rectangle.
# Public Method:
# get_area(self) -> float: This method takes no parameters. It calculates the area of the rectangle using the formula Area = length x width and returns the result as a floating-point value.

class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0

    def get_area(self):
        return float(self.length * self.width)