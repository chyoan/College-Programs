from lion import Lion 
from cat import Cat 
from dog import Dog

class PetHouse:
    def make_noise(self, pets):
        for pet in pets:
            pet.make_noise()