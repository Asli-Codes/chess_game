from board import Board
from piece import Piece

class Pawn(Piece):
    @property
    def symbol(self):
        return '♙' if self.is_white else '♟️'

    def moves(self, board, row, col):
        direction = -1 if self.is_white else 1
        possible_moves = []
        if board.is_inside(row + direction, col):
            if board.is_empty(row + direction, col):
                possible_moves.append((row + direction, col))

        if board.is_inside(row + 2 * direction, col):
            if board.is_empty(row + direction, col):
                if board.is_empty(row + 2 * direction, col):
                    if row == 1 or row == 6:
                        possible_moves.append((row + 2 * direction, col))

        for col_direction in (-1,1):
            target_row = row + direction
            target_col = col + col_direction
            if board.is_inside(target_row, target_col):
                target_piece = board.get_piece(target_row, target_col)
                if not board.is_empty(target_row, target_col) and self.is_enemy(target_piece):
                    possible_moves.append((target_row, target_col))

        return possible_moves