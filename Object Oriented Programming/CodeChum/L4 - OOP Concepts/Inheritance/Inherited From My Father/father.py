from person import Person 

class Father(Person):
    def __init__(self, name, age):
        super().__init__(name, age, "M")

    def introduce_with_style(self, n):
        for i in range(n):
            print(' ' * i + "I am your father")