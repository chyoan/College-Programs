# Drinking a Beverage - Python
# by CodeChum Admin
# 
# Implement the Beverage class which has the following details:
# Base Class - Beverage:
# Private Properties:
# name (type: str): The name of the beverage.
# volume (type: int): The volume of the beverage in milliliters.
# is_chilled (type: bool): Indicates if the beverage is chilled.
# Constructor:
# __init__(self, name: str, volume: int, is_chilled: bool): Initializes the name, volume, and is_chilled properties.
# Methods:
# is_empty(self) -> bool: Returns True if volume is 0.
# __str__(self) -> str: Returns a string in the format "{name} ({volume}mL) {is still chilled | is not chilled anymore}".
# Getter Methods:
# get_name(self) -> str: Returns the name of the beverage.
# get_volume(self) -> int: Returns the volume of the beverage.
# get_is_chilled(self) -> bool: Returns True if the beverage is still chilled, otherwise False.
#  
# Subclass - Water (extends Beverage):
# Additional Private Property:
# type (type: str): The type of water, can be "Purified", "Regular", or "Distilled".
# Constructor:
# __init__(self, volume: int, is_chilled: bool, type: str): Calls the Beverage constructor with "Water" as the name and initializes the type property. If type is empty, set the default to "Regular".
# Getter Method:
# get_type(self) -> str: Returns the type of water.
# 
# Subclass - Beer (extends Beverage):
# Additional Private Property:
# alcoholic_content (type: float): The percentage of alcoholic content (0.01 to 1.00).
# Constructor:
# __init__(self, volume: int, is_chilled: bool, alcoholic_content: float): Calls the Beverage constructor with "Beer" as the name and initializes the alcoholic_content property.
# Methods:
# get_type(self) -> str: Returns "Flavored", "Regular", or "Strong" based on the alcoholic_content. Flavored for less than 3%, Regular for less than 6%, and other values greater than that are Strong.
# __str__(self) -> str: Calls the parent's __str__ method and appends the alcoholic percentage. Example: "Beer (249mL) is still chilled (6.0% alcoholic content)". One decimal place for the alcoholic percentage always.
# Getter Method:
# get_alcoholic_content(self) -> float: Returns the alcoholic content.

class Beverage:
    def __init__(self, name, volume, is_chilled):
        self.__name = name
        self.__volume = volume
        self.__is_chilled = is_chilled

    def is_empty(self):
        return self.__volume == 0

    def __str__(self):
        chilled_status = "is still chilled" if self.__is_chilled else "is not chilled anymore"
        return f"{self.__name} ({self.__volume}mL) {chilled_status}"

    def get_name(self):
        return self.__name

    def get_volume(self):
        return self.__volume

    def get_is_chilled(self):
        return self.__is_chilled