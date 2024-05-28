from pet import Pet

class Cat(Pet):
    def __init__(self):
        super().__init__("cat", True)

    def make_noise(self):
        print("Meow!")