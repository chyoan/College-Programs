# Pets for Lonely People - Python
# by CodeChum Admin
# 
# If you're a very lonely person, having a pet can usually help you with your situation. For this program, you will create different kinds of Pets.
# 
# Class - Pet:
# Properties:
# type (str): Represents the type of the pet.
# is_friendly (bool): Indicates if the pet is friendly.
# Constructor:
# def __init__(self, pet_type: str, is_friendly: bool): Initializes the type and is_friendly properties with the provided values.
# Methods:
# def make_noise(self) -> None: Abstract method with pass as its body.
# def __str__(self) -> str: Returns a string representation of the pet, including its type and friendliness status, formatted as "Pet {self.type} {'is friendly' if self.is_friendly else 'is not friendly'}".
#  
# Class - Lion (extends Pet):
# Constructor:
# def __init__(self): Calls the constructor of Pet with type "lion" and sets is_friendly to False.
# Methods:
# def make_noise(self) -> None: Prints "Roar!".
#  
# Class - Cat (extends Pet):
# Constructor:
# def __init__(self): Calls the constructor of Pet with type "cat" and sets is_friendly to True.
# Methods:
# def make_noise(self) -> None: Prints "Meow!".
#  
# Class - Dog (extends Pet):
# Properties:
# breed (str): The breed of the dog.
# Constructor:
# def __init__(self, breed: str): Calls the constructor of Pet with type "dog" and sets is_friendly to True. Initializes the breed property with the provided value.
# Methods:
# def make_noise(self) -> None: Prints "Arf!".
# def __str__(self) -> str: Returns a string representation of the dog, including its type, friendliness status, and breed, formatted as "Pet {self.type} {'is friendly' if self.is_friendly else 'is not friendly'} [{self.breed}]".
#  
# Class - PetHouse:
# Methods:
# def make_noise(self, pets: List[Pet]) -> None: Loops through each Pet in the pets list and calls their make_noise method.

class Pet:
    def __init__(self, pet_type, is_friendly):
        self.type = pet_type
        self.is_friendly = is_friendly

    def make_noise(self):
        pass

    def __str__(self):
        return f"Pet {self.type} {'is friendly' if self.is_friendly else 'is not friendly'}"