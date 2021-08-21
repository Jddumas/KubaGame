import copy
import pygame
from .constants import WHITE, BLACK
from Kuba.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    def reset(self):
        self._init()

    # piece to be moved
    def selected(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != "X" and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        return False


    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == "X" and (row, col) in self.valid_moves:
            # only if we selected something and we are trying to
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False

        return True

    def change_turn(self):
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = WHITE

# turn
# piece
# can we move here/there