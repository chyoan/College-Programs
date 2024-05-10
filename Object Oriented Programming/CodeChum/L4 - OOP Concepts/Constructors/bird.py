# Two Kinds of Birds - Python
# by CodeChum Admin

# Create a class called Bird with the following details:
# Class - Bird:
# Public Properties:
# breed (type: str): Represents the breed of the bird.
# is_nocturnal (type: bool): Indicates whether the bird is nocturnal (active during the night).
# Constructor:
# __init__(self, breed: str = "Unknown", is_nocturnal: bool = False): This constructor can be used in two ways:
# When called with no parameters, it initializes the breed property to "Unknown" and the is_nocturnal property to False.
# When called with parameters, it sets the breed and is_nocturnal properties to the values passed in these parameters.

class Bird:
    def __init__(self, breed = "Unknown", is_nocturnal = False):
        self.breed = breed
        self.is_nocturnal = is_nocturnal