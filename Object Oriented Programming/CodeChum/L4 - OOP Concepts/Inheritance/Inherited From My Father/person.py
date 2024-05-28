# Inherited From My Father - Python
# by CodeChum Admin
# 
# For this program, you are tasked to create a class called Person.
# Base Class - Person:
# Private Properties:
# name (type: str): Holds the person's name.
# age (type: int): Represents the person's age.
# gender (type: str): Indicates the gender ('M' for male, 'F' for female).
# Constructors:
# __init__(self, name: str, age: int, gender: str): Initializes name, age, and gender.
# Methods
# Getter and Setter Methods for each of the properties
# is_minor Method:
# is_minor(self) -> bool: Returns True if age is less than 18, otherwise False.
# __str__ Method:
# __str__(self) -> str: Returns a string in the format "{name - age - gender}".
#  
# Subclass - Father (extends Person):
# Constructor:
# __init__(self, name: str, age: int): Calls the constructor of Person with gender set to 'M'.
# introduce_with_style Method:
# introduce_with_style(self, n: int) -> None: Prints "I am your father" n times, with each line having an increasing number of spaces.
# For example, if n is 4 then the printed message would be:
# I am your father
#  I am your father
#   I am your father
#    I am your father
# 
# Subclass - Son (extends Father):
# Constructors:
# __init__(self, name: str, age: int): Calls the constructor of Father. Default value oif name is "Unknown".
# introduce_with_style Method:
# introduce_with_style(self, n: int) -> None: Overridden method. Prints "I am your son" n times with decreasing numbers of spaces.
# For example, if n is 4 then the printed message would be:
#    I am your son
#   I am your son
#  I am your son
# I am your son

class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_gender(self, gender):
        self.__gender = gender

    def is_minor(self):
        return self.__age < 18

    def __str__(self):
        return f"{self.__name} - {self.__age} - {self.__gender}"