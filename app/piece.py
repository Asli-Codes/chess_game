class Piece:

    def __init__(self, is_white):
        self.is_white = is_white

    @property
    def symbol(self):
        raise NotImplemented

    def moves(self, board, row, col):
        return []

    def is_enemy(self,other):
        return  other is not None and self.is_white != other.is_white

