from piece import Piece

class Knight(Piece):
    @property
    def symbol(self):
        return '♘' if self.is_white else '♞'

    def moves(self, board, row, col):
        possible_moves = []
        jumps = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for r,c in jumps:
            target_row = row + r
            target_col = col + c
            if board.is_inside(target_row, target_col):
                target_piece = board.get_piece(target_row, target_col)
                if target_piece is None or self.is_enemy(target_piece):
                    possible_moves.append((target_row, target_col))
        return possible_moves


