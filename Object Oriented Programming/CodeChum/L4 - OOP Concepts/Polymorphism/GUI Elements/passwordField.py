from passwordInputElement import PasswordInputElement
from customPasswordInputElement import CustomPasswordInputElement

class PasswordField:
    def validate(self, password, password_input_element):
        for ch in password:
            password_input_element.set_value(ch)
        password_input_element.validated()