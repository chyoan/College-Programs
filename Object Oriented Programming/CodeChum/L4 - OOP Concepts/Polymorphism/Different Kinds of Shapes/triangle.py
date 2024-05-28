from shape import Shape

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        s = (self.a + self.b + self.c ) / 2
        return (s*(s - self.a) * (s - self.b) * (s - self.c))**0.5

    def get_perimeter(self):
        return self.a + self.b + self.c