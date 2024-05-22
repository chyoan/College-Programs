# A Car That Works - Python
# by CodeChum Admin
# 
# For this problem, you are tasked to create the class Car:
# Class - Car:
# Private Properties:
# color (type: str): Represents the color of the car.
# price (type: float): Holds the price of the car.
# size (type: str): Indicates the size of the car, where 'S' represents small, 'M' represents medium, and 'L' represents large.
# Constructor:
# __init__(self, color: str, price: float, size: str): Initializes the car's color, price, and size properties. The size is standardized to uppercase using size.upper().
# Methods
# Getter Methods:
# get_color(self) -> str: Returns the car's color.
# get_price(self) -> float: Returns the car's price.
# get_size(self) -> str: Returns the car's size.
# Setter Methods:
# set_color(self, color: str) -> None: Sets the car's color to the specified value.
# set_price(self, price: float) -> None: Sets the car's price to the specified value.
# set_size(self, size: str) -> None: Sets the car's size to the specified value. The size should be one of 'S' for small, 'M' for medium, or 'L' for large. Use conversion of lowercase characters to uppercase using size.upper().
# __str__ Method:
# __str__(self) -> str: Returns a formatted string representing the car, following the format "Car (color) - P(price, formatted to two decimal places) - (size descriptor)". The size descriptor is determined based on the size character ('small' for 'S', 'medium' for 'M', and 'large' for 'L').
# Example Strings:
# For a red car priced at 19999.85 and of medium size: "Car (red) - P19999.85 - medium"
# For a blue car priced at 50000.00 and large: "Car (blue) - P50000.00 - large"

class Car:
    def __init__(self, color, price, size):
        self.__color = color
        self.__price = price
        self.__size = size

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    def get_size(self):
        return self.__size

    def set_color(self, color):
        self.__color = color

    def set_price(self, price):
        self.__price = price

    def set_size(self, size):
        if size.upper() in ['S', 'M', 'L']:
            self.__size = size.upper()

    def __str__(self):
        if self.__size == 'S':
            self.__size = 'small'
        elif self.__size == 'M':
            self.__size = 'medium'
        else:
            self.__size = 'large'
        
        return f"Car ({self.__color}) - P{self.__price:.2f} - {self.__size}"