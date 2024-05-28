from chessPiece import ChessPiece

class Pawn(ChessPiece):
    def __init__(self, is_white):
        super().__init__("Pawn", is_white)
        self.has_moved = False

    def move(self, is_two_moves):
        self.has_moved = True
        steps = "two steps" if is_two_moves else "one step"
        color = "White" if self.get_is_white() else "Black"
        print(f"{color} pawn has moved {steps}")
        

    def __str__(self):
        color = "White" if self.get_is_white() else "Black"
        status = "has already moved" if self.has_moved else "has not yet moved"
        return f"{color} pawn {status}"