# Making a Smoothie - Python
# by CodeChum Admin

# A class named Blender is provided, which represents a blender. The class has the following details to implement:
# Class - Blender:
# Public Methods:
# blend(fruit1: str = None, fruit2: str = None, n: int = 1)
# This method accepts three parameters, fruit1, fruit2, and n, with default values of None and 1.
# If no fruits are provided (both fruit1 and fruit2 are None), it prints "There's nothing to blend here, boss."
# If fruit1 and fruit2 are provided, it prints "Blending {fruit1} and {fruit2}, boss."
# If n is greater than 1, it repeats the message for n times, each on a new line.

class Blender:
    def blend(self, fruit1: str = None, fruit2: str = None, n: int = 1):
        if fruit1 == None and fruit2 == None:
            print("There's nothing to blend here, boss.")
        else:
            if n > 1:
                print(f"Blending {fruit1} and {fruit2}, boss.\n" * n)
            else:
                print(f"Blending {fruit1} and {fruit2}, boss.")