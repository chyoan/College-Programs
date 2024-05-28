from parrot import Parrot
from sparrow import Sparrow

class BirdCage:
    def make_bird_sounds(self, birds):
        for bird in birds:
            bird.make_sound()