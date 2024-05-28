from inputElement import InputElement

class PasswordInputElement(InputElement):
    def __init__(self, max_length, allowed_characters):
        super().__init__(max_length)
        self.allowed_characters = allowed_characters

    def validate(self):
        return len(self.get_value()) > 0 and all(ch in self.allowed_characters for ch in self.value)