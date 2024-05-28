from pet import Pet 

class Lion(Pet):
    def __init__(self):
        super().__init__("lion", False)

    def make_noise(self):
        print("Roar!")