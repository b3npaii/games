import random

def strat_1(board):
    for row in board:
        if board[3] == 0:
            return 3
    return random.randrange(0, 7)

    