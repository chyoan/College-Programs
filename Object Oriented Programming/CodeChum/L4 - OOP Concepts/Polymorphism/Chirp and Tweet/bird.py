# Chirp and Tweet - Python
# by CodeChum Admin
# 
# Create a simple program to demonstrate basic polymorphism with bird sounds.
# 
# Class - Bird:
# Methods:
# def make_sound(self) -> None: An abstract method that represents making a sound. It doesn't have a specific implementation in the base class Bird.
# 
# Class - Sparrow (extends Bird):
# Methods:
# def make_sound(self) -> None: Overrides the make_sound method from the base class Bird. It prints the sound "Chirp Chirp" when called.
#  
# Class - Parrot (extends Bird):
# Methods:
# def make_sound(self) -> None: Overrides the make_sound method from the base class Bird. It prints the sound "Tweet Tweet" when called.
# 
# Class - BirdCage:
# Methods:
# def make_bird_sounds(self, birds: List) -> None: Accepts a list of Bird objects as input. Iterates through the list of birds and calls the make_sound method on each bird to make its sound.

class Bird:
    def make_sound(self):
        pass