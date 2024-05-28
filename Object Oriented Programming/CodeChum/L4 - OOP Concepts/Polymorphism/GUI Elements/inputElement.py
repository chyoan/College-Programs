# GUI Elements - Python
# by CodeChum Admin
# 
# Graphical User Interface or GUI is a form of user interface that allows users to interact with electronic devices through graphical icons and audio indicator such as primary notation, instead of text-based UIs, typed command labels or text navigation. In this program, we will be implementing some of the different types of input elements.
# 
# Class - InputElement:
# Properties:
# max_length (int): Represents the maximum length allowed for the input.
# value (str): Represents the current value of the input.
# Constructor:
# def __init__(self, max_length: int): Initializes the max_length property with the provided value and sets value to an empty string.
# Methods:
# def get_value(self) -> str: Returns the current value of the input.
# def set_value(self, c: str) -> None: Modifies the input value based on the provided character c. If c is '/', it removes the last character from the value (if not empty), otherwise, it appends c to the value.
# def validate(self) -> bool: Validates the input value length to ensure it falls within the range of 1 to max_length. Returns True if the value is valid, otherwise False. 
# 
# Class - PasswordInputElement (extends InputElement):
# Properties:
# allowed_characters (list of str): Represents the list of allowed characters for the password.
# Constructor:
# def __init__(self, max_length: int, allowed_characters: list of str): Calls the constructor of InputElement with max_length and initializes the allowed_characters property with a copy of the provided list.
# Methods:
# def validate(self) -> bool: Overrides the validate method of InputElement. Checks both the length of the value and the presence of characters from allowed_characters. Returns True if both conditions are met, otherwise False.
#  
# Class - CustomPasswordInputElement (extends PasswordInputElement):
# Properties:
# DEFAULT_ALLOWED_CHARACTERS (list of str): Default allowed characters for custom password input. The list is ['J', 'r', 'v', 'D']
# Constructor:
# def __init__(self, max_length: int): Calls the constructor of PasswordInputElement with max_length and the default allowed characters from DEFAULT_ALLOWED_CHARACTERS.
#  
# Class - PasswordField:
# Methods:
# def validate(self, password: str, password_input_element: PasswordInputElement) -> None: Validates a password by setting each character from the password into the password_input_element using the set_value method. After processing all characters, it calls the validate method of password_input_element to check if the password is valid and prints the result.

class InputElement:
    def __init__(self, max_length):
        self.max_length = max_length
        self.value = ''

    def get_value(self):
        return self.value

    def set_value(self, c):
        if c == '/':
            self.value = self.value[:-1]
        else:
            self.value += c

    def validate(self):
        return 1 <= len(self.value) <= self.max_length