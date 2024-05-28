# School Performance - Python
# by CodeChum Admin
# 
# In a school musical performance, different types of performers participate. For this program, we will be implementing the performers.
# Base Class - Performer:
# Properties:
# name (type: str): Represents the name of the performer.
# age (type: int): Represents the age of the performer.
# Constructor:
# __init__(self, name: str, age: int): Initializes the name and age properties.
# Getters
# get_name(self) -> str: Returns the name
# get_age(self) -> int: Returns the age
#  
# Subclass - Singer:
# Inherits From: Performer
# Additional Property:
# vocal range (type: str): Represents the vocal range of the singer.
# Constructor:
# __init__(self, name: str, age: int, vocal_range: str): Initializes the name and age properties by calling the parent class's constructor and sets the vocal_range property.
# Getter:
# get_vocal_range(self) -> str: Returns the vocal range of the singer.
# Method:
# sing(self) -> None: Prints "{name} is singing with a {vocal_range} range."
#  
# Subclass - Dancer:
# Inherits From: Performer
# Additional Property:
# dance_style (type: str): Represents the dance style of the dancer.
# Constructor:
# __init__(self, name: str, age: int, dance_style: str): Initializes the name and age properties by calling the parent class's constructor and sets the dance_style property.
# Getter:
# get_dance_style(self) -> str: Returns the dance style of the dancer.
# Method:
# dance(self) -> None: Prints "{name} is performing {dance_style} dance."

class Performer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age