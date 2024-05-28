from passwordInputElement import PasswordInputElement

class CustomPasswordInputElement(PasswordInputElement):
    DEFAULT_ALLOWED_CHARACTERS = ['J', 'r', 'v', 'D']
    def __init__(self, max_length):
        super().__init__(max_length, self.DEFAULT_ALLOWED_CHARACTERS)