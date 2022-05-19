import random

class Player:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_move(self, board):
        return self.strategy(board)


def random_strat(board):
    move = random.randrange(0, 7)
    return move
