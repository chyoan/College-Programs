from father import Father

class Son(Father):
    def __init__(self, name="Unknown", age=5):
        super().__init__(name, age)

    def introduce_with_style(self, n):
        for i in range(n):
            print(' ' * (n - i - 1) + "I am your son")