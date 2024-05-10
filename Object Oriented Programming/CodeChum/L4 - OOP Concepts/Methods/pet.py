# Owning a Pet - Python
# by CodeChum Admin
 
# A class called Pet is already defined. Implement the following:
# Class - Pet:
# Public methods:
# move() - prints "The pet has moved."
# give_companionship() - accepts and integer n and prints the message "The pet is giving you companionship." n times (one per line).

class Pet:
    def move(self):
        print("The pet has moved.")
        
    def give_companionship(self, n):
        print("The pet is giving you companionship.\n" * n)