import random

def strat_1(board):
    for row in board:
        if board[3] == 0:
            return 3
    for row in board:
        if board[2] == 0:
            return 2
    for row in board:
        if board[4] == 0:
            return 4
    return random.randrange(0, 7)

    