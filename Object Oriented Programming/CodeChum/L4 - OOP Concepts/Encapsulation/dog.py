# Dog Breeds - Python
# by CodeChum Admin
# 
# Implement the class Dog with the following details:
# Class - Dog:
# Properties:
# breed (type: str): The breed of the dog.
# bark_count (type: int): A counter to keep track of the number of times the dog has barked, initialized to 0.
# Methods:
# Getter and Setter for breed:
# get_breed(self) -> str: Returns the breed of the dog.
# set_breed(self, breed: str) -> None: Sets the breed of the dog to the given breed.
# Getter for barkCount:
# get_bark_count(self) -> int: Returns the bark count.
# has_barked_a_lot(self) -> bool: Returns True if bark_count has reached 100 or more. 
# This method checks whether the dog has barked a significant number of times.
# bark(self, n: int) -> None: Simulates the dog barking n times. It prints "Woof" n times (each on a new line) and adds n to the current bark_count. 
# This method allows the dog to bark multiple times and updates the bark counter accordingly.

class Dog:
    def __init__(self, breed):
        self.breed = breed
        self.bark_count = 0

    def get_breed(self):
        return self.breed

    def set_breed(self, breed):
        self.breed = breed

    def get_bark_count(self):
        return self.bark_count

    def has_barked_a_lot(self):
        if self.bark_count >= 100:
            return True
        else:
            return False

    def bark(self, n):
        for i in range(n):
            print("Woof")
        self.bark_count += n