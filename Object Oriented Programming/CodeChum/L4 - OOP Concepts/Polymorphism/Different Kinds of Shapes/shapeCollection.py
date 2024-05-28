from rectangle import Rectangle
from triangle import Triangle

class ShapeCollection:
    def __init__(self, shapes):
        self.shapes = shapes

    def calculate_and_print_area_and_perimeter(self):
        for shape in self.shapes:
            area = shape.get_area()
            perimeter = shape.get_perimeter()
            print(f"Area: {area:.2f}\nPerimeter: {perimeter:.2f}\n")