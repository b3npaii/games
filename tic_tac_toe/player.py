#use 1 dimensional array 9 long for board
from random import randrange

class Player:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_move(self, board):
        return self.strategy(board)


def random_strat(board):
    move = randrange(0, 9)
    while board[move] != 0:
        move = randrange(0, 9)
    return move
