# The Beauty of Chess - Python
# by CodeChum Admin
# 
# For this program, we will be implementing the chess pieces.
# Base Class - ChessPiece:
# Constructor:
# def __init__(self, type: str, is_white: bool) -> None: Initializes a ChessPiece object with type (str) and is_white (bool) properties, representing the type of chess piece and whether it's white or not.
# Methods:
# def get_type(self) -> str: Returns the type of the chess piece.
# def get_is_white(self) -> bool: Returns whether the chess piece is white or not.
#  
# Subclass - Pawn (extends ChessPiece):
# Constructor
# def __init__(self, is_white: bool) -> None: Initializes a Pawn object. Calls the constructor of the base class ChessPiece with "Pawn" as the type and the provided is_white value. It also initializes the has_moved property to False.
# Methods:
# def move(self, is_two_moves: bool) -> None: Handles the movement of the pawn. It takes a boolean parameter is_two_moves, indicating whether the pawn should move two steps or one step. It prints the corresponding message based on the move and updates the has_moved property. (Example print message: "White pawn has moved one step")
# def __str__(self) -> str: Returns a string representation of the pawn. It indicates the color ("White" or "Black") and whether the pawn has already moved or not. (Example string: "White pawn has not yet moved")

class ChessPiece:
    def __init__(self, type, is_white,):
        self.type = type
        self.is_white = is_white

    def get_type(self):
        return self.type

    def get_is_white(self):
        return self.is_white