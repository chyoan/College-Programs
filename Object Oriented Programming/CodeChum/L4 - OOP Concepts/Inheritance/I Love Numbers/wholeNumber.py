from number import Number

class WholeNumber(Number):
    def __init__(self, value):
        super().__init__(value)

    def multiply(self, whole_number):
        self.set_value(self.get_value() * whole_number.get_value())

    def __str__(self):
        return f"{self.get_value()}"