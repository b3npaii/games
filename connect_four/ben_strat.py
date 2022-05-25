import random

def strat_1(board):
    order = 0
    for row in board:
        order += sum(row)
    if order % 3 == 0:
        return 3
    else:
        return 3