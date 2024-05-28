# I Love Numbers - Python
# by CodeChum Admin
# 
# For this program, you are tasked to implement the following classes with the following details:
# Base Class - Number:
# Private Property:
# value (type: int): Represents the numerical value.
# Constructor:
# __init__(self, value: int): Initializes the value property.
# Getter and Setter Methods:
# 
# Subclass - WholeNumber (extends Number):
# Constructor:
# __init__(self, value: int): Calls the constructor of Number.
# Methods:
# multiply(self, whole_number: WholeNumber) -> None: Updates value to the product of its current value and the value of the passed WholeNumber object.
# __str__(self) -> str: Returns the value as a string.
#  
# Subclass - DecimalNumber (extends Number):
# Additional Private Property:
# decimal_places (type: int): Represents the number of decimal places.
# Constructor:
# __init__(self, value: int, decimal_places: int): Calls the constructor of Number and initializes decimal_places.
# Getter and Setter Methods
# Methods:
# multiply(self, decimal_number: DecimalNumber) -> None: Multiplies the value with that of the passed DecimalNumber object and updates decimal_places accordingly (recall that when you multiply 2 decimal numbers, their decimal places are added up).
# __str__(self) -> str: Returns a string representation of the value formatted as "0.{value}", considering the number of decimal places.

class Number:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value