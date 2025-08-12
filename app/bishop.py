from board import Board
from piece import Piece

class Bishop(Piece):
    @property
    def symbol(self):
        return '♗' if self.is_white else '♝'

    def moves(self, board, row, col):
        possible_moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for r, c in directions:
            target_row = row + r
            target_column = col + c
            while board.is_inside(target_row, target_column):
                if board.is_empty(target_row, target_column):
                    possible_moves.append((target_row, target_column))
                else:
                    target_piece = board.get_piece(target_row, target_column)
                    if self.is_enemy(target_piece):
                        possible_moves.append((target_row, target_column))
                    break
                target_row += r
                target_column += c
        return possible_moves
