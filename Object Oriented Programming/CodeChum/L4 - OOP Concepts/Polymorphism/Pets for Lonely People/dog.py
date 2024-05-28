from pet import Pet 

class Dog(Pet):
    def __init__(self, breed):
        super().__init__("dog", True)
        self.breed = breed

    def make_noise(self):
        print("Arf!")

    def __str__(self):
        return f"Pet {self.type} {'is friendly' if self.is_friendly else 'is not friendly'} [{self.breed}]"