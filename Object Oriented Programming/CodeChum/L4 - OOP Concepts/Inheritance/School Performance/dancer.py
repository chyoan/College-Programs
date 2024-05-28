from performer import Performer

class Dancer(Performer):
    def __init__(self, name, age, dance_style):
        super().__init__(name, age)
        self.dance_style = dance_style

    def get_dance_style(self):
        return self.dance_style

    def dance(self):
        print(f"{self.name} is performing {self.dance_style} dance.")