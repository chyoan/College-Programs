# Cha-ching! - Python
# by CodeChum Admin

# Create a class called Money with the following details:
# Class - Money:
# Public Properties:
# amount (type: int): Represents the monetary amount.
# denomination (type: str): Specifies the denomination or currency type.
# Constructor:
# __init__(self, amount: int = 0, denomination: str = "Unknown"):
# This constructor can be used in three ways:
# When called with no parameters, it initializes amount to 0 and denomination to "Unknown". This constructor is used when no specific monetary details are provided, setting default values.
# When called with only the amount as a parameter, it sets the amount property accordingly and sets denomination to "Unknown". This constructor is useful when only the amount is known, but the denomination is not specified.
# When called with both amount and denomination as parameters, it sets the respective properties to these values. This constructor is used when complete information about the monetary value, including its denomination, is available.

class Money:
    def __init__(self, amount: int = 0, denomination: str = "Unknown"):
        self.amount = amount
        self.denomination = denomination