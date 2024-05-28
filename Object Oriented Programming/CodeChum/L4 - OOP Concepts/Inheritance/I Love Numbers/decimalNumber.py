from number import Number

class DecimalNumber(Number):
    def __init__(self, value, decimal_places):
        super().__init__(value)
        self.__decimal_places = decimal_places

    def get_decimal_places(self):
        return self.__decimal_places

    def set_decimal_places(self, decimal_places):
        self.__decimal_places = decimal_places

    def multiply(self, decimal_number):
        self.set_value(self.get_value() * decimal_number.get_value())
        self.__decimal_places += decimal_number.get_decimal_places()

    def __str__(self):
        return f"{self.get_value() / 10 ** self.get_decimal_places():.{self.get_decimal_places()}f}"